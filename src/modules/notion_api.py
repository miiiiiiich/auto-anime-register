from typing import Any, cast

from utils.env import Env
from modules.notion import Page
from utils.system import log_fn


@log_fn
def request_notion_db(filter_mal_id=True) -> list[dict[str, Any]]:
    env = Env.get()
    q = {
        "database_id": env.notion_db_id,
    }
    if filter_mal_id:
        q["filter"] = {
            "property": "my_anime_list_id",
            "number": {"is_empty": True},
        }
    result = []
    while True:
        res_json = env.notion_client().databases.query(**q)
        res_json = cast(dict[str, Any], res_json)
        result += res_json["results"]
        next_cursor = res_json.get("next_cursor", "")
        q["start_cursor"] = next_cursor
        if not next_cursor or res_json["has_more"] is False:
            break

    return result


def update_page(page: Page):
    env = Env.get()
    response = env.notion_client().pages.update(
        **{
            "page_id": page.id,
            "properties": page.properties.format_notion_json(),
        }
    )
    return response


if __name__ == "__main__":
    from pprint import pprint

    res = request_notion_db()
    pprint(res[1])
