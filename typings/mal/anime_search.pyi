from mal import AnimeSearchResult, _base, config

class AnimeSearch:
    def __init__(self, query: str, timeout: int = config.TIMEOUT):
        ...

    @property
    @_base.property_list
    def results(self) -> list[AnimeSearchResult]:
        ...
