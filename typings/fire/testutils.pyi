"""
This type stub file was generated by pyright.
"""

import contextlib
import unittest

"""
This type stub file was generated by pyright.
"""
class BaseTestCase(unittest.TestCase):
  """Shared tests case for Python Fire tests."""
  @contextlib.contextmanager
  def assertOutputMatches(self, stdout=..., stderr=..., capture=...):
    """Asserts that the context generates stdout and stderr matching regexps.

    Note: If wrapped code raises an exception, stdout and stderr will not be
      checked.

    Args:
      stdout: (str) regexp to match against stdout (None will check no stdout)
      stderr: (str) regexp to match against stderr (None will check no stderr)
      capture: (bool, default True) do not bubble up stdout or stderr

    Yields:
      Yields to the wrapped context.
    """
    ...
  
  def assertRaisesRegex(self, *args, **kwargs):
    ...
  
  @contextlib.contextmanager
  def assertRaisesFireExit(self, code, regexp=...):
    """Asserts that a FireExit error is raised in the context.

    Allows tests to check that Fire's wrapper around SystemExit is raised
    and that a regexp is matched in the output.

    Args:
      code: The status code that the FireExit should contain.
      regexp: stdout must match this regex.

    Yields:
      Yields to the wrapped context.
    """
    ...
  


@contextlib.contextmanager
def ChangeDirectory(directory):
  """Context manager to mock a directory change and revert on exit."""
  ...

main = unittest.main
skip = ...
skipIf = ...
