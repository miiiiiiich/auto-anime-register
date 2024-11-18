from loguru import logger
from tqdm import tqdm

from modules.cui import select_anime_in_terminal
from modules.notion_api import request_none_my_anime_list_id, update_page
from modules.notion_x_anime import search_anime_by_pages


def give():
    logger.info("start give")
    items = request_none_my_anime_list_id()
    logger.info(f"target items: {len(items)}")
    search_results = search_anime_by_pages(items)
    updated_pages = []
    for d in search_results:
        page = d["notion"]
        anime = select_anime_in_terminal(page.properties.title, d["anime_list"])
        page.properties.update(anime)
        updated_pages.append(page)
    for page in tqdm(updated_pages, desc="Updating Notion"):
        try:
            _ = update_page(page)
        except Exception as e:
            logger.exception(f"Error: {e} at {page.properties.title}")
            continue
