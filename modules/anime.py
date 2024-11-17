import time
from concurrent.futures import Future, ThreadPoolExecutor
from pprint import pprint
from typing import cast

import mal
import requests
from simple_term_menu import TerminalMenu


def request_anime(mal_id: int) -> mal.Anime:
    try:
        return mal.Anime(mal_id)
    except requests.exceptions.ConnectionError:
        # NOTE: max retries exceeded with url
        print("Max retries exceeded with url")
        print("wait 3 minutes...")
        time.sleep(180)
        return request_anime(mal_id)


def anime_future_result(future: list[Future[mal.Anime]]) -> list[mal.Anime]:
    """
    Get the result of the Future object
    Args:
        future:

    Returns:

    """
    anime_list = []
    for feature in future:
        try:
            anime_list.append(feature.result())
        except Exception as e:
            print("Complete the process halfway through")
            return anime_list

    return anime_list


def search_anime(title, limit_items=5) -> list[mal.Anime]:
    """
    Search for anime on my-anime-list
    mal.Anime() is slow, so this does parallel processing
        title:
        limit_items:

    Returns:

    """
    search_results = mal.AnimeSearch(title).results
    limit_items = (
        limit_items if len(search_results) > limit_items else len(search_results)
    )
    search_results = search_results[:limit_items]
    with ThreadPoolExecutor(max_workers=5) as executor:
        features: list[Future[mal.Anime]] = [
            executor.submit(request_anime, mal_id=searched.mal_id)
            for searched in search_results
        ]

    return anime_future_result(features)


def search_anime_all(titles: list[str]) -> list[list[mal.Anime]]:
    """
    error handling: temporarily blocked by my-anime-list
    Args:
        titles:

    Returns:

    """
    anime_list_in_list = []
    for title in titles:
        try:
            anime_list_in_list.append(search_anime(title))
        except ValueError as e:
            print(e, title)
            continue
        except Exception as e:
            print(e, title, type(e))
            print("Complete the process halfway through")
            return anime_list_in_list
    return anime_list_in_list


def select_anime(
        title: str, anime_list: list[mal.Anime], show_num: int = 3
) -> mal.Anime:
    """
    Select a match for the searched title
    Show more search results by selecting "More..." if none match your choices
    Args:
        title: input anime title
        anime_list: list of my-anime-list.Anime objects
        show_num: number of search results to show

    Returns:

    """
    animations: list[mal.Anime] = [anime for anime in anime_list if anime is not None]
    if len(animations) > show_num:
        show_anime_list = [
                              f"{ma.title_japanese}: {ma.title}" for ma in animations[:show_num]
                          ] + ["More..."]
        more = True
    else:
        show_anime_list = [f"{ma.title_japanese}: {ma.title}" for ma in animations]
        more = False
    menu = TerminalMenu(
        show_anime_list,
        title=f"search words: {title}",
        cycle_cursor=True,
        clear_screen=True,
    )
    choice_index = cast(int, menu.show())
    if more and choice_index == show_num:
        return select_anime(title, animations, show_num * 2)
    # NOTE: For some reason, a None Type error appeared, so it was processed
    choice_index = choice_index if choice_index is not None else 0
    return animations[choice_index]


def select_anime_list(
        titles: list[str], searched_list_anime_list: list[list[mal.Anime]]
) -> list[mal.Anime]:
    """
    If you send a request after making a selection,
    the process will be frozen,
    so you can eliminate the stress of making a selection
    by making all requests in advance.

    Args:
        titles:
        searched_list_anime_list:

    Returns:

    """

    mal_list: list[mal.Anime] = []
    for title, list_anime in zip(titles, searched_list_anime_list):
        try:
            mal_list.append(select_anime(title, list_anime))
        except Exception as e:
            print(e)
            continue
    return mal_list


def request_anime_list(id_list: list[int]) -> list[mal.Anime]:
    """
    mal.Anime() is slow, so this does parallel processing
    Args:
        id_list:

    Returns:

    """

    # with ThreadPoolExecutor(max_workers=10) as executor:
    #     features: list[Future[mal.Anime]] = [
    #         executor.submit(request_anime, mal_id=mal_id) for mal_id in id_list
    #     ]
    # return anime_future_result(features)
    anime_list = []
    i = -1
    try:
        for i in id_list:
            anime = request_anime(i)
            anime_list.append(anime)
    except Exception as e:
        print(f"Error: {e}. mal_id: {i}")
        print("Complete the process halfway through")
        return anime_list
    return anime_list


def request_seasonal_mal_id(client_id: str, year: int, season: str) -> list[int]:
    """
    Args:
        client_id:
        year:
        season:

    Returns:

    """
    url = f"https://api.myanimelist.net/v2/anime/season/{year}/{season}"
    header = {
        "X-MAL-CLIENT-ID": client_id,
    }
    data_list: list[dict] = []
    while True:
        response = requests.get(url, headers=header).json()
        data_list += response["data"]
        pprint(response["data"])
        url = response["paging"].get("next", None)
        if url is None:
            break
    return [data["node"]["id"] for data in data_list]
