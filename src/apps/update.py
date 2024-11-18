from prompt_toolkit.contrib.telnet.log import logger

from modules.notion_api import request_pages, update_page
from modules.notion_x_anime import req_anime_list_by_pages


def update():
    logger.info("update")
    pages = request_pages()
    logger.info(f"target pages: {len(pages)}")
    results = req_anime_list_by_pages(pages)
    updated_pages = []
    for d in results:
        page = d["notion"]
        anime = d["anime"]
        page.properties.update(anime)
        updated_pages.append(page)
    for page in updated_pages:
        try:
            _ = update_page(page)
        except Exception as e:
            logger.exception(f"Error: {e} at {page.properties.title}")
            continue
