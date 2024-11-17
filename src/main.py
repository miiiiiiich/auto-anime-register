import fire

from apps.give_info import give

if __name__ == "__main__":
    fire.Fire({"give": give})
