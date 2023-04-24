"""
This type stub file was generated by pyright.
"""

from typing import Any, AsyncGenerator, Awaitable, Callable, Dict, Generator, List

"""Utility functions for notion-sdk-py."""
def pick(base: Dict[Any, Any], *keys: str) -> Dict[Any, Any]:
    """Return a dict composed of key value pairs for keys passed as args."""
    ...

def get_url(object_id: str) -> str:
    """Return the URL for the object with the given id."""
    ...

def get_id(url: str) -> str:
    """Return the id of the object behind the given URL."""
    ...

def iterate_paginated_api(function: Callable[..., Any], **kwargs: Any) -> Generator[List[Any], None, None]:
    """Return an iterator over the results of any paginated Notion API."""
    ...

def collect_paginated_api(function: Callable[..., Any], **kwargs: Any) -> List[Any]:
    """Collect all the results of paginating an API into a list."""
    ...

async def async_iterate_paginated_api(function: Callable[..., Awaitable[Any]], **kwargs: Any) -> AsyncGenerator[List[Any], None]:
    """Return an async iterator over the results of any paginated Notion API."""
    ...

async def async_collect_paginated_api(function: Callable[..., Awaitable[Any]], **kwargs: Any) -> List[Any]:
    """Collect asynchronously all the results of paginating an API into a list."""
    ...

def is_full_block(response: Dict[Any, Any]) -> bool:
    """Return `true` if response is a full block."""
    ...

def is_full_page(response: Dict[Any, Any]) -> bool:
    """Return `true` if response is a full page."""
    ...

def is_full_database(response: Dict[Any, Any]) -> bool:
    """Return `true` if response is a full database."""
    ...

def is_full_user(response: Dict[Any, Any]) -> bool:
    """Return `true` if response is a full user."""
    ...

def is_full_comment(response: Dict[Any, Any]) -> bool:
    """Return `true` if response is a full comment."""
    ...
