from functools import lru_cache
from pathlib import Path

import notion_client
from pydantic_settings import BaseSettings, SettingsConfigDict


def root_path() -> Path:
    return Path(__file__).parent.parent.parent


class Env(BaseSettings):
    model_config = SettingsConfigDict(env_file=root_path() / ".env")
    notion_api_token: str
    notion_db_id: str

    @classmethod
    @lru_cache
    def get(cls) -> "Env":
        return cls()  # type: ignore

    def notion_client(self) -> "notion_client.Client":
        return notion_client.Client(auth=self.notion_api_token)
