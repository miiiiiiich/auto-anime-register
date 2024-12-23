from datetime import datetime
from typing import Any, Literal

import mal
from pydantic import BaseModel

Status = Literal["done", "back_log", "todo", "in_progress", "cancel", "paid"]


class Property(BaseModel):
    title: str
    status: Status
    title_japanese: str | None
    genres: list[str] | None
    score: float | None
    scored_by: int | None
    rank: int | None
    premiered: str | None
    my_anime_list_id: int | None
    url: str | None
    studios: list[str] | None
    source: str | None
    type: str | None
    title_english: str | None
    edit_at: datetime

    @classmethod
    def new(cls, properties: dict) -> "Property":
        return cls(
            title=get_title_item(properties),
            status=get_status_item(properties, "status"),
            title_japanese=get_text_item(properties, "title_japanese"),
            genres=get_multi_select_item(properties, "genres"),
            score=get_number_item(properties, "score"),
            scored_by=get_number_item(properties, "scored_by"),
            rank=get_number_item(properties, "rank"),
            premiered=get_select_item(properties, "premiered"),
            my_anime_list_id=get_number_item(properties, "my_anime_list_id"),
            url=get_url_item(properties, "url"),
            studios=get_multi_select_item(properties, "studios"),
            source=get_select_item(properties, "source"),
            type=get_select_item(properties, "type"),
            title_english=get_text_item(properties, "title_english"),
            edit_at=get_default_time_item(properties, "edit_at", "last_edited_time"),
        )

    def update(self, anime: mal.Anime):
        self.title = anime.title
        self.title_japanese = anime.title_japanese
        self.genres = anime.genres
        self.score = anime.score
        self.scored_by = anime.scored_by
        self.rank = anime.rank
        self.premiered = anime.premiered
        self.my_anime_list_id = anime.mal_id
        self.url = anime.url
        self.studios = anime.studios
        self.source = anime.source
        self.type = anime.type
        self.title_english = anime.title_english

    def format_notion_json(self):
        return (
            text_to_json("title_japanese", self.title_japanese)
            | multi_select_to_json("genres", self.genres)
            | number_to_json("score", self.score)
            | number_to_json("scored_by", self.scored_by)
            | number_to_json("rank", self.rank)
            | select_to_json("premiered", self.premiered)
            | number_to_json("my_anime_list_id", self.my_anime_list_id)
            | url_to_json("url", self.url)
            | multi_select_to_json("studios", self.studios)
            | select_to_json("source", self.source)
            | select_to_json("type", self.type)
            | text_to_json("title_english", self.title_english)
        )


class Page(BaseModel):
    id: str
    properties: Property

    @classmethod
    def new(cls, page: dict) -> "Page":
        return cls(
            id=page["id"],
            properties=Property.new(page["properties"]),
        )


def get_select_item(properties: dict[str, dict[str, Any]], key: str) -> str | None:
    items = properties.get(key, {}).get("select", {})
    return items["name"] if items else None


def get_multi_select_item(
    properties: dict[str, dict[str, Any]], key: str
) -> list[str] | None:
    items = properties.get(key, {}).get("multi_select", [])
    return [item["name"] for item in items] if items else None


def get_text_item(properties: dict[str, dict[str, Any]], key: str) -> str | None:
    items = properties.get(key, {}).get("rich_text", [])
    return items[0]["plain_text"] if items else None


def get_number_item(properties: dict[str, dict[str, Any]], key: str) -> int | None:
    items = properties.get(key, {}).get("number", None)
    return items if items else None


def get_status_item(properties: dict[str, dict[str, Any]], key: str) -> Status:
    return properties[key]["status"]["name"]


def get_title_item(properties: dict[str, dict[str, Any]]) -> str:
    return properties["title"]["title"][0]["plain_text"]


def get_url_item(properties: dict[str, dict[str, Any]], key: str) -> str:
    return properties[key]["url"]


def get_default_time_item(
    properties: dict[str, dict[str, Any]],
    key: str,
    default_name: Literal["last_edited_time", "created_time"],
) -> datetime:
    s = properties[key][default_name]
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")


# edit_at = properties_d["edit_at"]["last_edited_time"]
# edit_at = datetime.strptime(edit_at, "%Y-%m-%dT%H:%M:%S.%fZ")


def title_to_json(title: str):
    return {"title": {"title": [{"text": {"content": title}}]}}


def number_to_json(key: str, number: int | float | None):
    return {key: {"number": number}}


def text_to_json(key: str, text: str | None):
    if text is None:
        return {}
    return {key: {"rich_text": [{"text": {"content": text}}]}}


def select_to_json(key: str, name: str | None):
    if name is None:
        return {}
    return {key: {"select": {"name": name}}}


def multi_select_to_json(
    key: str, names: list[str] | None
) -> dict[str, dict[str, list[dict[str, str]]]]:
    if names is None:
        return {}
    return {key: {"multi_select": [{"name": name} for name in names]}}


def url_to_json(key: str, url: str | None):
    if url is None:
        return {}
    return {key: {"url": url}}
