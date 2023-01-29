import os
import sys
from os.path import dirname

import fire
from notion_client import Client
from tqdm import tqdm

sys.path.append(dirname(dirname(__file__)))
from functions.models import NotionAnimeItem, Status
from functions.notion_database import request_notion_db
from functions.anime import search_anime_all, select_anime_list, request_anime_list


def give_in_local(status: str) -> None:
    status = Status(status)
    notion = Client(auth=os.getenv("NOTION_API_TOKEN"))
    items = request_notion_db(notion, os.getenv("NOTION_DATABASE_ID"))
    notion_items = [NotionAnimeItem.new_from_notion(item) for item in items]
    notion_to_search: list[NotionAnimeItem] = []
    notion_to_update: list[NotionAnimeItem] = []
    for notion_item in notion_items:
        if notion_item.prop.status != status:
            continue
        if notion_item.prop.mal_id is None:
            notion_to_search.append(notion_item)
        else:
            notion_to_update.append(notion_item)

    searched_titles = [item.prop.title for item in notion_to_search]
    print("searching all items")
    searched_d = search_anime_all(searched_titles)
    selected_d = select_anime_list(searched_titles, searched_d)
    notion_to_search = [
        notion_item.update_from_mal(anime)
        for notion_item, anime in zip(notion_to_search, selected_d)
    ]

    print("requesting all items")
    update_anime_list = request_anime_list([item.prop.mal_id for item in notion_to_update])
    notion_to_update = [
        to_update.update_from_mal(anime)
        for to_update, anime in zip(notion_to_update, update_anime_list)
    ]
    for notion_item in tqdm(notion_to_search + notion_to_update, desc="Updating Notion"):
        try:
            notion.pages.update(**notion_item.to_notion())
        except Exception as e:
            print(e)
            print(notion_item.to_notion())
            continue


if __name__ == '__main__':
    fire.Fire(give_in_local)
