from typing import TypedDict

from loguru import logger

from modules.anime_api import Anime, MalFatalError, req, search_anime
from modules.notion import Page
from utils.system import log_fn


class SearchResults(TypedDict):
    notion: Page
    anime_list: list[Anime]


class RequestResults(TypedDict):
    notion: Page
    anime: Anime


@log_fn
def search_anime_by_pages(pages: list[Page]) -> list[SearchResults]:
    results = []
    for page in pages:
        try:
            search_results = search_anime(page.properties.title)
        except MalFatalError as e:
            logger.error(f"Stop requesting MAL: {e}")
            break
        except Exception as e:
            logger.warning(f"MAL search failed for {page.properties.title}: {e}")
            continue
        if not search_results:
            logger.warning(f"No anime found for {page.properties.title}")
            continue
        results.append(
            {
                "notion": page,
                "anime_list": search_results,
            }
        )
    return results


@log_fn
def req_anime_list_by_pages(pages: list[Page]) -> list[RequestResults]:
    results = []
    for i, page in enumerate(pages):
        if page.properties.my_anime_list_id is None:
            continue
        try:
            anime = req(page.properties.my_anime_list_id)
        except MalFatalError as e:
            logger.error(f"Stop requesting MAL: {e}. Requested: {i + 1}")
            break
        except Exception as e:
            logger.warning(f"MAL request failed for {page.properties.title}: {e}")
            continue
        results.append(
            {
                "notion": page,
                "anime": anime,
            }
        )
    return results
