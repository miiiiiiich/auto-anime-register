from mal import config, _base, AnimeSearchResult


class AnimeSearch:
    def __init__(self, query: str, timeout: int = config.TIMEOUT):
        ...

    @property
    @_base.property_list
    def results(self) -> list[AnimeSearchResult]:
        ...
