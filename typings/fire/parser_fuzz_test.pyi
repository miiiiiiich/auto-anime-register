"""
This type stub file was generated by pyright.
"""

from fire import testutils
from hypothesis import example, given, settings
from hypothesis import strategies as st

"""
This type stub file was generated by pyright.
"""
class ParserFuzzTest(testutils.BaseTestCase):
  @settings(max_examples=10000)
  @given(st.text(min_size=1))
  @example('True')
  @example(r'"tests\t\t\a\\a"')
  @example(r' "tests\t\t\a\\a"   ')
  @example('"(1, 2)"')
  @example('(1, 2)')
  @example('(1,                   2)')
  @example('(1,       2) ')
  @example('a,b,c,d')
  @example('(a,b,c,d)')
  @example('[a,b,c,d]')
  @example('{a,b,c,d}')
  @example('tests:(a,b,c,d)')
  @example('{tests:(a,b,c,d)}')
  @example('{tests:a,b,c,d}')
  @example('{tests:a,b:(c,d)}')
  @example('0,')
  @example('#')
  @example('A#00000')
  @example('\x80')
  @example(100 * '[' + '0')
  @example('\r\r\r\r1\r\r')
  def testDefaultParseValueFuzz(self, value):
    ...
  


if __name__ == '__main__':
  ...
