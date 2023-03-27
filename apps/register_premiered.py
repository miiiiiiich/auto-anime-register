import os
import sys
from os.path import dirname

import fire
from notion_client import Client

sys.path.append(dirname(dirname(__file__)))
from functions.anime import request_seasonal_mal_id


def register(year: int, season: str) -> None:
    """
    I have registered all the upcoming anime and have commented out for now
    because I haven't found a way to filter only what I need
    Args:
        year:
        season:

    Returns:

    """
    notion = Client(auth=os.getenv("NOTION_API_TOKEN", ""))
    database_id = os.getenv("NOTION_DATABASE_ID", "")
    mal_ids = request_seasonal_mal_id(os.getenv("MAL_CLIENT_ID", ""), year, season)
    # mal_list = request_anime_list(mal_ids)
    # create_page_by_mal(notion, database_id, mal_list)


if __name__ == "__main__":
    fire.Fire(register)
