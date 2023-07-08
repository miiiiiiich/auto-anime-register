import os

import fire
from notion_client import Client
from tqdm import tqdm

from modules.anime import request_anime_list
from modules.models import NotionAnimeItem, Status
from modules.notion_database import request_notion_db


def update_in_local(status_list: list[Status]):
    """
    Update anime in local.
    target notion item is status is one of status_args and my anime list is not empty.
    Args:
        status_list:

    Returns:

    """
    notion = Client(auth=os.getenv("NOTION_API_TOKEN", ""))
    items = request_notion_db(notion, os.getenv("NOTION_DATABASE_ID", ""))
    notion_items = [NotionAnimeItem.new_from_notion(item) for item in items]
    notion_items = sorted(notion_items, key=lambda x: x.prop.edit_at)
    notion_to_update: list[NotionAnimeItem] = []
    for notion_item in notion_items:
        if (
            notion_item.prop.status in status_list
            and notion_item.prop.mal_id is not None
        ):
            notion_to_update.append(notion_item)
    print(f"requests {len(notion_to_update)} items")
    update_anime_list = request_anime_list(
        [item.prop.mal_id for item in notion_to_update]  # type: ignore
    )
    notion_to_update = [
        to_update.update_from_mal(anime)
        for to_update, anime in zip(notion_to_update, update_anime_list)
    ]
    for notion_item in tqdm(notion_to_update, desc="Updating Notion"):
        try:
            notion.pages.update(**notion_item.to_notion())
        except Exception as e:
            print(f"Error: {e} at {notion_item.prop.title}")
            continue


if __name__ == "__main__":
    fire.Fire(update_in_local)
