import time
from typing import Any

import requests
from loguru import logger
from pydantic import BaseModel

from utils.env import Env

API_URL = "https://api.myanimelist.net/v2"
FIELDS = ",".join(
    [
        "alternative_titles",
        "genres",
        "mean",
        "num_scoring_users",
        "rank",
        "start_season",
        "studios",
        "source",
        "media_type",
    ]
)
# 公式の制限は非公開。1 req/s 程度なら安全とされている
REQUEST_INTERVAL = 1.0
# この範囲外だと 400 invalid q になる
MIN_QUERY_LENGTH = 3
MAX_QUERY_LENGTH = 64
# v2 の genres はテーマ・対象層も含むので、MAL の「Genres」(Explicit 含む) だけ残す
GENRE_IDS = {
    1,
    2,
    4,
    5,
    7,
    8,
    9,
    10,
    12,
    14,
    22,
    24,
    26,
    28,
    30,
    36,
    37,
    41,
    46,
    47,
    49,
}
MEDIA_TYPES = {
    "tv": "TV",
    "ova": "OVA",
    "ona": "ONA",
    "movie": "Movie",
    "special": "Special",
    "tv_special": "TV Special",
    "music": "Music",
    "pv": "PV",
    "cm": "CM",
}
# mal-api 時代の Notion の表記に合わせる
SOURCES = {
    "original": "Original",
    "manga": "Manga",
    "4_koma_manga": "4-koma manga",
    "web_manga": "Web manga",
    "digital_manga": "Digital manga",
    "novel": "Novel",
    "light_novel": "Light novel",
    "web_novel": "Web novel",
    "visual_novel": "Visual novel",
    "game": "Game",
    "card_game": "Card game",
    "book": "Book",
    "picture_book": "Picture book",
    "radio": "Radio",
    "music": "Music",
    "mixed_media": "Mixed media",
    "other": "Other",
}

_last_request_at = 0.0


class MalFatalError(Exception):
    """認証エラー・レート制限など、リクエストを続けても無駄なエラー"""


class Anime(BaseModel):
    mal_id: int
    title: str
    title_japanese: str | None
    title_english: str | None
    genres: list[str]
    score: float | None
    scored_by: int | None
    rank: int | None
    premiered: str | None
    url: str
    studios: list[str]
    source: str | None
    type: str | None

    @classmethod
    def from_api(cls, node: dict[str, Any]) -> "Anime":
        titles = node.get("alternative_titles", {})
        season = node.get("start_season")
        source = node.get("source")
        if source and source not in SOURCES:
            logger.warning(f"Unknown source: {source} (mal_id={node['id']})")
        return cls(
            mal_id=node["id"],
            title=node["title"],
            title_japanese=titles.get("ja") or None,
            title_english=titles.get("en") or None,
            genres=[g["name"] for g in node.get("genres", []) if g["id"] in GENRE_IDS],
            score=node.get("mean"),
            scored_by=node.get("num_scoring_users"),
            rank=node.get("rank"),
            # mal-api 時代は TV 以外に Premiered が無かったので合わせる
            premiered=f"{season['season'].capitalize()} {season['year']}"
            if season and node.get("media_type") == "tv"
            else None,
            url=f"https://myanimelist.net/anime/{node['id']}",
            studios=[s["name"] for s in node.get("studios", [])],
            source=SOURCES.get(source) if source else None,
            type=MEDIA_TYPES.get(node.get("media_type", "")),
        )


def _get(path: str, params: dict[str, Any]) -> dict[str, Any]:
    global _last_request_at
    wait = _last_request_at + REQUEST_INTERVAL - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    _last_request_at = time.monotonic()
    res = requests.get(
        f"{API_URL}{path}",
        params=params,
        headers={"X-MAL-CLIENT-ID": Env.get().mal_client_id},
        timeout=10,
    )
    if res.status_code in (401, 403, 429):
        raise MalFatalError(f"{res.status_code} {res.text[:200]}")
    res.raise_for_status()
    return res.json()


def req(mal_id: int) -> Anime:
    return Anime.from_api(_get(f"/anime/{mal_id}", {"fields": FIELDS}))


def search_anime(title: str, limit=5) -> list[Anime]:
    if len(title) < MIN_QUERY_LENGTH:
        raise ValueError(f"MAL search needs at least {MIN_QUERY_LENGTH} characters")
    params = {
        "q": title[:MAX_QUERY_LENGTH],
        "limit": limit,
        "fields": FIELDS,
        # 既定では成人向け作品が検索結果から除外される
        "nsfw": "true",
    }
    res = _get("/anime", params)
    return [Anime.from_api(d["node"]) for d in res["data"]]
