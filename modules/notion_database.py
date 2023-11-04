from typing import Any, cast

import mal
import notion_client

from modules.models import NotionProperty, Status


def request_notion_db(
    client: notion_client.Client, database_id: str
) -> list[dict[str, Any]]:
    """
    Request all items from a notion database
    Args:
        client:
        database_id:

    Returns:

    """
    q = {
        "database_id": database_id,
    }
    result = []
    while True:
        res_json = client.databases.query(**q)
        res_json = cast(dict[str, Any], res_json)
        result += res_json["results"]
        next_cursor = res_json.get("next_cursor", "")
        q["start_cursor"] = next_cursor
        if not next_cursor or res_json["has_more"] is False:
            break

    return result


def create_page_by_mal(
    client: notion_client.Client, database_id: str, mal_list: list[mal.Anime]
) -> None:
    """
    Args:
        client:
        database_id:
        mal_list:

    Returns:

    """
    prop_list = [
        NotionProperty.new_from_anime(anime, Status.BACK_LOG) for anime in mal_list
    ]
    for prop in prop_list:
        client.pages.create(
            **{
                "parent": {"database_id": database_id},
                "properties": prop.to_notion(),
            }
        )
