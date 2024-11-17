import os

from notion_client import Client
from tqdm import tqdm

from modules.anime import search_anime_all, select_anime_list
from modules.models import NotionAnimeItem, Status
from modules.notion_database import request_notion_db


def give_in_local(status_list: list[Status]) -> None:
    """
    Give anime in local.
    target notion item is status is one of status_args and my anime list is empty.
    Args:
        status_list:

    Returns:

    """
    notion = Client(auth=os.getenv("NOTION_API_TOKEN", ""))
    items = request_notion_db(notion, os.getenv("NOTION_DATABASE_ID", ""))
    notion_items = [NotionAnimeItem.new_from_notion(item) for item in items]
    notion_to_search: list[NotionAnimeItem] = []
    for notion_item in notion_items:
        if notion_item.prop.status in status_list and notion_item.prop.mal_id is None:
            notion_to_search.append(notion_item)

    print("target items: ", len(notion_to_search))
    searched_titles = [item.prop.title for item in notion_to_search]
    print("searching all items")
    searched_d = search_anime_all(searched_titles)
    selected_d = select_anime_list(searched_titles, searched_d)
    notion_to_search = [
        notion_item.update_from_mal(anime)
        for notion_item, anime in zip(notion_to_search, selected_d)
    ]
    for notion_item in tqdm(notion_to_search, desc="Updating Notion"):
        try:
            notion.pages.update(**notion_item.to_notion())
        except Exception as e:
            print(e)
            print(notion_item.to_notion())
            continue
