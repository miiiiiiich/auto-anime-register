from typing import TypedDict

import mal

from modules.anime_api import search_anime
from modules.notion import Page
from utils.system import log_fn


class SearchResults(TypedDict):
    notion: Page
    anime_list: list[mal.Anime]


@log_fn
def search_anime_by_pages(pages: list[Page]) -> list[SearchResults]:
    results = []
    for page in pages:
        search_results = search_anime(page.properties.title)
        search_results = [r for r in search_results if r is not None]
        if not search_results:
            # リクエスト制限が出た場合はNoneになるのでそれ以上リクエストしない
            break
        results.append(
            {
                "notion": page,
                "anime_list": search_results,
            }
        )
    return results
