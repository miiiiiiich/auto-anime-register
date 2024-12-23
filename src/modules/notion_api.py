from typing import Any, cast

from modules.notion import Page
from utils.env import Env
from utils.system import log_fn


def request_notion_db(query: dict) -> list[Page]:
    env = Env.get()
    result = []
    while True:
        res_json = env.notion_client().databases.query(env.notion_db_id, **query)
        res_json = cast(dict[str, Any], res_json)
        result += res_json["results"]
        next_cursor = res_json.get("next_cursor", "")
        query["start_cursor"] = next_cursor
        if not next_cursor or res_json["has_more"] is False:
            break

    return [Page.new(r) for r in result]


@log_fn
def request_none_my_anime_list_id() -> list[Page]:
    q = {
        "filter": {
            "property": "my_anime_list_id",
            "number": {"is_empty": True},
        }
    }
    return request_notion_db(q)


@log_fn
def request_pages() -> list[Page]:
    query = {
        "filter": {
            "property": "my_anime_list_id",
            "number": {"is_not_empty": True},
        },
        # "sorts": [
        #     {
        #         "property": "edit_at",
        #         "direction": "ascending",
        #     }
        # ]
    }
    results = request_notion_db(query)
    sort_results = sorted(results, key=lambda x: x.properties.edit_at)
    return sort_results


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
    res = request_pages()
    print(res)
