import fire

from apps.give import give
from apps.update import update

if __name__ == "__main__":
    fire.Fire({"give": give, "update": update})
