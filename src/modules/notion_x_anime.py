from typing import TypedDict

import mal
from loguru import logger

from modules.anime_api import req, search_anime
from modules.notion import Page
from utils.system import log_fn


class SearchResults(TypedDict):
    notion: Page
    anime_list: list[mal.Anime]


class RequestResults(TypedDict):
    notion: Page
    anime: mal.Anime


@log_fn
def search_anime_by_pages(pages: list[Page]) -> list[SearchResults]:
    results = []
    for page in pages:
        search_results = search_anime(page.properties.title)
        search_results = [r for r in search_results if r is not None]
        if not search_results:
            # リクエスト制限が出た場合はNoneになるのでそれ以上リクエストしない
            logger.warning("Max request limit reached")
            break
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
        anime = req(page.properties.my_anime_list_id)
        if anime is None:
            logger.warning(f"Max request limit reached. Requested: {i + 1}")
            break
        results.append(
            {
                "notion": page,
                "anime": anime,
            }
        )
    return results
