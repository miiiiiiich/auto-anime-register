from concurrent.futures import Future, ThreadPoolExecutor

import mal
from loguru import logger


def req(mal_id: int) -> mal.Anime | None:
    try:
        return mal.Anime(mal_id)
    except Exception as e:
        logger.exception(e)
        return None


def search_anime(title: str, limit=5) -> list[mal.Anime]:
    search = mal.AnimeSearch(title).results
    if len(search) < limit:
        limit = len(search)
    search = search[:limit]
    with ThreadPoolExecutor(max_workers=5) as executor:
        features: list[Future[mal.Anime | None]] = [
            executor.submit(req, mal_id=s.mal_id) for s in search
        ]

    anime_list = []
    for feature in features:
        try:
            res = feature.result()
            if not res:
                return anime_list
            anime_list.append(res)
        except Exception as e:
            logger.exception(e)
            return anime_list
    return anime_list


def main():
    res = search_anime("聖者無双")
    print(res)


if __name__ == "__main__":
    main()
