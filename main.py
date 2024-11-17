import fire

from apps.give_mal_info import give_in_local
from apps.update_mal_info import update_in_local
from modules.models import Status


def input_line(*status_args) -> list[Status]:
    if len(status_args) == 0:
        return [
            Status.BACK_LOG,
            Status.TODO,
            Status.IN_PROGRESS,
            Status.DONE,
            Status.CANCEL,
            Status.PAID,
        ]

    return [Status(status) for status in status_args]


def update(*status_args):
    status_list = input_line(*status_args)
    update_in_local(status_list)


def give(*status_args):
    status_list = input_line(*status_args)
    give_in_local(status_list)


if __name__ == "__main__":
    fire.Fire({"update": update, "give": give})
