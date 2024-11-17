import asyncio
import sys
from collections.abc import Callable
from functools import wraps
from pathlib import Path
from time import time
from typing import ParamSpec, TypeVar, cast

from loguru import logger

from utils.env import Env

P = ParamSpec("P")
R = TypeVar("R")



def log_fn(fn: Callable[P, R]) -> Callable[P, R]:
    if asyncio.iscoroutinefunction(fn):

        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start_time = time()
            # logger.opt(depth=1).info(f"Calling {fn.__name__} with {args} {kwargs}")
            result = await fn(*args, **kwargs)
            end_time = time()
            txt = f"Called {fn.__name__} with elapsed_time={round(end_time - start_time, 3)} "
            # f"args={args} kwargs={kwargs}",
            logger.opt(depth=1).info(txt)
            return result

        return cast(Callable[P, R], async_wrapper)
    else:

        @wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start_time = time()
            # logger.opt(depth=1).info(f"Calling {fn.__name__} with {args} {kwargs}")
            result = fn(*args, **kwargs)
            end_time = time()
            txt = f"Called {fn.__name__} with elapsed_time={round(end_time - start_time, 3)} "
            # f"args={args} kwargs={kwargs}",
            logger.opt(depth=1).info(txt)
            return result

        return cast(Callable[P, R], wrapper)


def debug_fn(fn: Callable[P, R]) -> Callable[P, R]:
    if asyncio.iscoroutinefunction(fn):

        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start_time = time()
            # logger.opt(depth=1).info(f"Calling {fn.__name__} with {args} {kwargs}")
            result = await fn(*args, **kwargs)
            end_time = time()
            txt = f"Called {fn.__name__} with elapsed_time={round(end_time - start_time, 3)} "
            # f"args={args} kwargs={kwargs}",
            logger.opt(depth=1).debug(txt)
            return result

        return cast(Callable[P, R], async_wrapper)
    else:

        @wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start_time = time()
            # logger.opt(depth=1).info(f"Calling {fn.__name__} with {args} {kwargs}")
            result = fn(*args, **kwargs)
            end_time = time()
            txt = f"Called {fn.__name__} with elapsed_time={round(end_time - start_time, 3)} "
            # f"args={args} kwargs={kwargs}",
            logger.opt(depth=1).debug(txt)
            return result

        return cast(Callable[P, R], wrapper)


def root_dir():
    return Path(__file__).parent.parent.parent