import mal
import questionary


def select_anime_in_terminal(
    search_words: str, anime_list: list[mal.Anime]
) -> mal.Anime:
    choices = [
        f"{i + 1}. {anime.title_japanese}: {anime.title}"
        for i, anime in enumerate(anime_list)
    ]
    choice = questionary.select(f"search words: {search_words}", choices=choices).ask()
    if not choice:
        raise ValueError("No anime selected")
    return anime_list[int(choice.split(".")[0]) - 1]
