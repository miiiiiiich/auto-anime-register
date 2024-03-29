"""
This type stub file was generated by pyright.
"""

import asyncio
import functools
from typing import Tuple

"""
This type stub file was generated by pyright.
"""
def identity(arg1, arg2: int, arg3=..., arg4: int = ..., *arg5, arg6, arg7: int, arg8=..., arg9: int = ..., **arg10):
  ...

class HelpTextComponent:
  def identity(self, *, alpha, beta=...):
    ...
  


class KeywordOnly:
  def double(self, *, count):
    ...
  
  def triple(self, *, count):
    ...
  
  def with_default(self, *, x=...):
    ...
  


class LruCacheDecoratedMethod:
  @functools.lru_cache()
  def lru_cache_in_class(self, arg1):
    ...
  


@functools.lru_cache()
def lru_cache_decorated(arg1):
  ...

class WithAsyncio:
  @asyncio.coroutine
  def double(self, count=...):
    ...
  


class WithTypes:
  """Class with functions that have default arguments and types."""
  def double(self, count: float) -> float:
    """Returns the input multiplied by 2.

    Args:
      count: Input number that you want to double.

    Returns:
      A number that is the double of count.
    """
    ...
  
  def long_type(self, long_obj: Tuple[Tuple[Tuple[Tuple[Tuple[Tuple[Tuple[Tuple[Tuple[Tuple[Tuple[Tuple[int]]]]]]]]]]]]):
    ...
  


class WithDefaultsAndTypes:
  """Class with functions that have default arguments and types."""
  def double(self, count: float = ...) -> float:
    """Returns the input multiplied by 2.

    Args:
      count: Input number that you want to double.

    Returns:
      A number that is the double of count.
    """
    ...
  
  def get_int(self, value: int = ...):
    ...
  


