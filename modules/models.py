from datetime import datetime
from enum import Enum
from typing import Any

import mal
from pydantic import BaseModel


class Status(Enum):
    """
    Status of anime
    """

    DONE = "done"
    BACK_LOG = "back_log"
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    CANCEL = "cancel"


class NotionProperty(BaseModel):
    title: str
    status: Status
    title_japanese: str | None
    # comment: str | None
    genres: list[str] | None
    # start_date: str | None
    # end_date: str | None
    score: float | None
    scored_by: int | None
    rank: int | None
    premiered: str | None
    mal_id: int | None
    url: str | None
    studios: list[str] | None
    source: str | None
    type: str | None
    title_english: str | None
    edit_at: datetime

    @classmethod
    def new_from_notion_properties(cls, properties_d: dict) -> "NotionProperty":
        genres: list[dict[str, str]] = properties_d.get("genres", {}).get(
            "multi_select", []
        )
        studios: list[dict[str, str]] = properties_d.get("studios", {}).get(
            "multi_select", []
        )
        # NOTE: select item
        premiered_selected = properties_d.get("premiered", {}).get("select", None)
        premiered = premiered_selected["name"] if premiered_selected else None
        source_selected = properties_d.get("source", {}).get("select", None)
        source = source_selected["name"] if source_selected else None
        type_selected = properties_d.get("type", {}).get("select", None)
        type_ = type_selected["name"] if type_selected else None
        # NOTE: text item
        title_japanese_content = properties_d.get("title_japanese", {}).get(
            "rich_text", []
        )
        title_japanese = (
            title_japanese_content[0]["plain_text"] if title_japanese_content else None
        )
        title_english_content = properties_d.get("title_english", {}).get(
            "rich_text", []
        )

        title_english = (
            title_english_content[0]["plain_text"] if title_english_content else None
        )

        # NOTE: default value
        edit_at = properties_d["edit_at"]["last_edited_time"]
        edit_at = datetime.strptime(edit_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        return cls.model_validate(
            {
                "title": properties_d["title"]["title"][0]["plain_text"],
                "status": properties_d["status"]["status"]["name"],
                "genres": [g["name"] for g in genres],
                "score": properties_d.get("score", {}).get("number", None),
                "scored_by": properties_d.get("scored_by", {}).get("number", None),
                "rank": properties_d.get("rank", {}).get("number", None),
                "premiered": premiered,
                "mal_id": properties_d.get("my_anime_list_id", {}).get("number", None),
                "url": properties_d.get("url", {}).get("url", None),
                "studios": [s["name"] for s in studios],
                "source": source,
                "type": type_,
                "title_japanese": title_japanese,
                "title_english": title_english,
                "edit_at": edit_at,
            }
        )

    @classmethod
    def new_from_anime(cls, anime: mal.Anime, status: Status) -> "NotionProperty":
        return cls.model_validate(
            {
                "title": anime.title_japanese,
                "status": status.value,
                "genres": anime.genres,
                "score": anime.score,
                "scored_by": anime.scored_by,
                "rank": anime.rank,
                "premiered": anime.premiered,
                "my_anime_list_id": anime.mal_id,
                "url": anime.url,
                "studios": anime.studios,
                "source": anime.source,
                "title_japanese": anime.title_japanese,
            }
        )

    def update_from_mal(self, anime: mal.Anime) -> None:
        self.genres = anime.genres
        self.score = anime.score
        self.scored_by = anime.scored_by
        self.rank = anime.rank
        self.mal_id = anime.mal_id
        self.url = anime.url
        self.studios = anime.studios
        self.source = anime.source
        self.premiered = anime.premiered
        self.title_japanese = anime.title_japanese
        self.title_english = anime.title
        self.type = anime.type

    def to_notion(
        self,
    ) -> dict:
        properties_d = {
            "title": {"title": [{"text": {"content": self.title}}]},
            "score": {"number": self.score},
            "scored_by": {"number": self.scored_by},
            "rank": {"number": self.rank},
            "my_anime_list_id": {"number": self.mal_id},
            "url": {"url": self.url},
            "title_japanese": {
                "rich_text": [{"text": {"content": self.title_japanese}}]
            },
            "title_english": {"rich_text": [{"text": {"content": self.title_english}}]},
        }

        if self.premiered:
            properties_d["premiered"] = {"select": {"name": self.premiered}}
        if self.source:
            properties_d["source"] = {"select": {"name": self.source}}
        if self.type:
            properties_d["type"] = {"select": {"name": self.type}}
        if self.genres:
            properties_d["genres"] = {
                "multi_select": [{"name": g} for g in self.genres]
            }
        if self.studios:
            properties_d["studios"] = {
                "multi_select": [{"name": s} for s in self.studios]
            }
        return properties_d


class NotionAnimeItem(BaseModel):
    id: str
    prop: NotionProperty

    @classmethod
    def new_from_notion(cls, result_d: dict[str, Any]) -> "NotionAnimeItem":
        properties_d = result_d.get("properties", {})
        prop = NotionProperty.new_from_notion_properties(properties_d)

        return cls.model_validate({"id": result_d["id"], "prop": prop})

    def update_from_mal(self, anime: mal.Anime) -> "NotionAnimeItem":
        self.prop.update_from_mal(anime)
        return self

    def to_notion(self) -> dict[str, Any]:
        # TODO: テキストのアップデートとnotionデータベースに列がない場合の処理：関数化して列のexistsをチェックする。設定ファイルでも可能にしたい
        # TODO: リクエスト系やserde系はテストしたい

        return {
            "page_id": self.id,
            "properties": self.prop.to_notion(),
        }
