from typing import Optional

from mal import AnimeCharacterResult, AnimeStaffResult, _base

class Anime:
    def __init__(self, id: int) -> "Anime":
        ...

    @property
    def mal_id(self) -> int:
        ...

    @property
    def title(self) -> str:
        ...

    @property
    def title_english(self) -> str:
        ...

    @property
    def title_japanese(self) -> str:
        ...

    @property
    def title_synonyms(self) -> list[str]:
        ...

    @property
    def url(self) -> str:
        ...

    @property
    def image_url(self) -> str:
        ...

    @property
    def type(self) -> Optional[str]:
        ...

    @property
    def status(self) -> Optional[str]:
        ...

    @property
    def genres(self) -> list[str]:
        ...

    @property
    def themes(self) -> list[str]:
        ...

    @property
    def external_links(self) -> list[tuple[str, str]]:
        """Return list of Tuples containing name and url"""
        ...

    @property
    def score(self) -> Optional[float]:
        ...

    @property
    def scored_by(self) -> Optional[int]:
        ...

    @property
    def rank(self) -> Optional[int]:
        ...

    @property
    def popularity(self) -> Optional[int]:
        ...

    @property
    def members(self) -> Optional[int]:
        ...

    @property
    def favorites(self) -> Optional[int]:
        ...

    """
    Duplicate properties for AutoAPI ends here
    """

    @property
    @_base.property
    def episodes(self) -> Optional[int]:
        ...

    @property
    @_base.property
    def aired(self) -> Optional[str]:
        ...

    @property
    @_base.property
    def premiered(self) -> Optional[str]:
        ...

    @property
    @_base.property
    def broadcast(self) -> Optional[str]:
        ...

    @property
    @_base.property_list
    def producers(self) -> list[str]:
        ...

    @property
    @_base.property_list
    def licensors(self) -> list[str]:
        ...

    @property
    @_base.property_list
    def studios(self) -> list[str]:
        ...

    @property
    @_base.property
    def source(self) -> Optional[str]:
        ...

    @property
    @_base.property
    def duration(self) -> Optional[str]:
        ...

    @property
    @_base.property
    def rating(self) -> Optional[str]:
        ...

    @property
    @_base.property_dict
    def related_anime(self) -> dict[str, list[str]]:
        ...

    @property
    @_base.property_list
    def opening_themes(self) -> list[str]:
        ...

    @property
    @_base.property_list
    def ending_themes(self) -> list[str]:
        ...

    @property
    @_base.property_list
    def characters(self) -> list[AnimeCharacterResult]:
        ...

    @property
    @_base.property_list
    def staff(self) -> list[AnimeStaffResult]:
        ...

    @property
    @_base.property
    def synopsis(self) -> Optional[str]:
        ...

    @property
    @_base.property
    def background(self) -> Optional[str]:
        ...
