"""
This type stub file was generated by pyright.
"""

from fire import decorators, testutils

"""
This type stub file was generated by pyright.
"""
class NoDefaults:
  """A class for testing decorated functions without default values."""
  @decorators.SetParseFns(count=int)
  def double(self, count):
    ...
  
  @decorators.SetParseFns(count=float)
  def triple(self, count):
    ...
  
  @decorators.SetParseFns(int)
  def quadruple(self, count):
    ...
  


@decorators.SetParseFns(int)
def double(count):
  ...

class WithDefaults:
  @decorators.SetParseFns(float)
  def example1(self, arg1=...):
    ...
  
  @decorators.SetParseFns(arg1=float)
  def example2(self, arg1=...):
    ...
  


class MixedArguments:
  @decorators.SetParseFns(float, arg2=str)
  def example3(self, arg1, arg2):
    ...
  


class PartialParseFn:
  @decorators.SetParseFns(arg1=str)
  def example4(self, arg1, arg2):
    ...
  
  @decorators.SetParseFns(arg2=str)
  def example5(self, arg1, arg2):
    ...
  


class WithKwargs:
  @decorators.SetParseFns(mode=str, count=int)
  def example6(self, **kwargs):
    ...
  


class WithVarArgs:
  @decorators.SetParseFn(str)
  def example7(self, arg1, arg2=..., *varargs, **kwargs):
    ...
  


class FireDecoratorsTest(testutils.BaseTestCase):
  def testSetParseFnsNamedArgs(self):
    ...
  
  def testSetParseFnsPositionalArgs(self):
    ...
  
  def testSetParseFnsFnWithPositionalArgs(self):
    ...
  
  def testSetParseFnsDefaultsFromPython(self):
    ...
  
  def testSetParseFnsDefaultsFromFire(self):
    ...
  
  def testSetParseFnsNamedDefaultsFromPython(self):
    ...
  
  def testSetParseFnsNamedDefaultsFromFire(self):
    ...
  
  def testSetParseFnsPositionalAndNamed(self):
    ...
  
  def testSetParseFnsOnlySomeTypes(self):
    ...
  
  def testSetParseFnsForKeywordArgs(self):
    ...
  
  def testSetParseFn(self):
    ...
  


if __name__ == '__main__':
  ...
