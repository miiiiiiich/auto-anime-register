import mal
from loguru import logger
from tqdm import tqdm
from typing_extensions import TypedDict

from modules.anime_api import search_anime
from modules.cui import select_anime_in_terminal
from modules.notion import Page
from modules.notion_api import request_notion_db, update_page


class SearchDict(TypedDict):
    notion: Page
    search_results: list[mal.Anime]


def give():
    logger.info("start give")
    items_json = request_notion_db()
    items = [Page.new(item) for item in items_json]
    items = [item for item in items if item.properties.my_anime_list_id is None]
    logger.info(f"target items: {len(items)}")
    item_results: dict[int, SearchDict] = {}
    for i, item in tqdm(enumerate(items), total=len(items), desc="searching all items"):
        search_results = search_anime(item.properties.title)
        search_results = [r for r in search_results if r is not None]
        if not search_results:
            break
        item_results[i] = {
            "notion": item,
            "search_results": search_results,
        }

    update_pages = []
    for d in item_results.values():
        page = d["notion"]
        anime = select_anime_in_terminal(page.properties.title, d["search_results"])
        page.properties.update(anime)
        update_pages.append(page)

    for page in tqdm(update_pages, desc="Updating Notion"):
        try:
            _ = update_page(page)
        except Exception as e:
            logger.exception(f"Error: {e} at {page.properties.title}")
            continue





