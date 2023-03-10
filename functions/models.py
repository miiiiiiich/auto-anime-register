from enum import Enum
from typing import Optional

from mal import Anime
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
    title_japanese: Optional[str]
    # comment: Optional[str]
    genres: Optional[list[str]]
    # start_date: Optional[str]
    # end_date: Optional[str]
    score: Optional[float]
    scored_by: Optional[int]
    rank: Optional[int]
    premiered: Optional[str]
    mal_id: Optional[int]
    url: Optional[str]
    studios: Optional[list[str]]
    source: Optional[str]

    @classmethod
    def new_from_notion_properties(cls, properties_d: dict):
        genres: list[dict[str, str]] = properties_d.get("genres", {}).get("multi_select", [])
        studios: list[dict[str, str]] = properties_d.get("studios", {}).get("multi_select", [])
        # NOTE: select item
        premiered_selected = properties_d.get("premiered", {}).get("select", None)
        premiered = premiered_selected["name"] if premiered_selected else None
        source_selected = properties_d.get("source", {}).get("select", None)
        source = source_selected["name"] if source_selected else None
        # NOTE: text item
        title_japanese_content = properties_d.get("title_japanese", {}).get("rich_text", [])
        title_japanese = title_japanese_content[0]["plain_text"] if title_japanese_content else None
        return cls.parse_obj({
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
            "title_japanese": title_japanese
        })

    @classmethod
    def new_from_anime(cls, anime: Anime, status: Status):
        return cls.parse_obj({
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
            "title_japanese": anime.title_japanese
        })

    def update_from_mal(self, anime: Anime):
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

    def to_notion(self) -> dict:
        properties_d = {
            "title": {"title": [{"text": {"content": self.title}}]},
            "genres": {"multi_select": [{"name": g} for g in self.genres]},
            "score": {"number": self.score},
            "scored_by": {"number": self.scored_by},
            "rank": {"number": self.rank},
            "my_anime_list_id": {"number": self.mal_id},
            "url": {"url": self.url},
            "studios": {"multi_select": [{"name": s} for s in self.studios]},
            "title_japanese": {"rich_text": [{"text": {"content": self.title_japanese}}]}
        }

        if self.premiered:
            properties_d["premiered"] = {"select": {"name": self.premiered}}
        if self.source:
            properties_d["source"] = {"select": {"name": self.source}}
        return properties_d


class NotionAnimeItem(BaseModel):
    id: str
    prop: NotionProperty

    @classmethod
    def new_from_notion(cls, result_d: dict) -> "NotionAnimeItem":
        properties_d = result_d["properties"]
        prop = NotionProperty.new_from_notion_properties(properties_d)

        return cls.parse_obj({
            "id": result_d["id"],
            "prop": prop
        })

    def update_from_mal(self, anime: Anime) -> "NotionAnimeItem":
        self.prop.update_from_mal(anime)
        return self

    def to_notion(self) -> dict:
        # TODO: ????????????????????????????????????notion????????????????????????????????????????????????????????????????????????exists??????????????????????????????????????????????????????
        # TODO: ?????????????????????serde????????????????????????

        return {
            "page_id": self.id,
            "properties": self.prop.to_notion(),
        }
