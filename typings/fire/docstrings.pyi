"""
This type stub file was generated by pyright.
"""

import collections
import enum

"""
This type stub file was generated by pyright.
"""
class DocstringInfo(collections.namedtuple('DocstringInfo', ('summary', 'description', 'args', 'returns', 'yields', 'raises'))):
  ...


class ArgInfo(collections.namedtuple('ArgInfo', ('name', 'type', 'description'))):
  ...


class KwargInfo(ArgInfo):
  ...


class Namespace(dict):
  """A dict with attribute (dot-notation) access enabled."""
  def __getattr__(self, key):
    ...
  
  def __setattr__(self, key, value):
    ...
  
  def __delattr__(self, key):
    ...
  


class Sections(enum.Enum):
  ARGS = ...
  RETURNS = ...
  YIELDS = ...
  RAISES = ...
  TYPE = ...


class Formats(enum.Enum):
  GOOGLE = ...
  NUMPY = ...
  RST = ...


SECTION_TITLES = ...
def parse(docstring):
  """Returns DocstringInfo about the given docstring.

  This parser aims to parse Google, numpy, and rst formatted docstrings. These
  are the three most common docstring styles at the time of this writing.

  This parser aims to be permissive, working even when the docstring deviates
  from the strict recommendations of these styles.

  This parser does not aim to fully extract all structured information from a
  docstring, since there are simply too many ways to structure information in a
  docstring. Sometimes content will remain as unstructured text and simply gets
  included in the description.

  The Google docstring style guide is available at:
  https://github.com/google/styleguide/blob/gh-pages/pyguide.md

  The numpy docstring style guide is available at:
  https://numpydoc.readthedocs.io/en/latest/format.html

  Information about the rST docstring format is available at:
  https://www.python.org/dev/peps/pep-0287/
  The full set of directives such as param and type for rST docstrings are at:
  http://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html

  Note: This function does not claim to handle all docstrings well. A list of
  limitations is available at the top of the file. It does aim to run without
  crashing in O(n) time on all strings on length n. If you find a string that
  causes this to crash or run unacceptably slowly, please consider submitting
  a pull request.

  Args:
    docstring: The docstring to parse.

  Returns:
    A DocstringInfo containing information about the docstring.
  """
  ...

