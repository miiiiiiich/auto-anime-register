"""
This type stub file was generated by pyright.
"""

import enum
import six

"""
This type stub file was generated by pyright.
"""
if six.PY3:
  ...
def identity(arg1, arg2, arg3=..., arg4=..., *arg5, **arg6):
  ...

def multiplier_with_docstring(num, rate=...):
  """Multiplies num by rate.

  Args:
    num (int): the num you want to multiply
    rate (int): the rate for multiplication
  Returns:
    Multiplication of num by rate
  """
  ...

def function_with_help(help=...):
  ...

class Empty:
  ...


class OldStyleEmpty:
  ...


class WithInit:
  def __init__(self) -> None:
    ...
  


class ErrorInConstructor:
  def __init__(self, value=...) -> None:
    ...
  


class WithHelpArg:
  """Test class for testing when class has a help= arg."""
  def __init__(self, help=...) -> None:
    ...
  


class NoDefaults:
  def double(self, count):
    ...
  
  def triple(self, count):
    ...
  


class WithDefaults:
  """Class with functions that have default arguments."""
  def double(self, count=...):
    """Returns the input multiplied by 2.

    Args:
      count: Input number that you want to double.

    Returns:
      A number that is the double of count.
    """
    ...
  
  def triple(self, count=...):
    ...
  
  def text(self, string=...):
    ...
  


class OldStyleWithDefaults:
  def double(self, count=...):
    ...
  
  def triple(self, count=...):
    ...
  


class MixedDefaults:
  def ten(self):
    ...
  
  def sum(self, alpha=..., beta=...):
    ...
  
  def identity(self, alpha, beta=...):
    ...
  


class SimilarArgNames:
  def identity(self, bool_one=..., bool_two=...):
    ...
  
  def identity2(self, a=..., alpha=...):
    ...
  


class CapitalizedArgNames:
  def sum(self, Delta=..., Gamma=...):
    ...
  


class Annotations:
  def double(self, count=...):
    ...
  
  def triple(self, count=...):
    ...
  


class TypedProperties:
  """Test class for testing Python Fire with properties of various types."""
  def __init__(self) -> None:
    ...
  


class VarArgs:
  """Test class for testing Python Fire with a property with varargs."""
  def cumsums(self, *items):
    ...
  
  def varchars(self, alpha=..., beta=..., *chars):
    ...
  


class Underscores:
  def __init__(self) -> None:
    ...
  
  def underscore_function(self, underscore_arg):
    ...
  


class BoolConverter:
  def as_bool(self, arg=...):
    ...
  


class ReturnsObj:
  def get_obj(self, *items):
    ...
  


class NumberDefaults:
  def reciprocal(self, divisor=...):
    ...
  
  def integer_reciprocal(self, divisor=...):
    ...
  


class InstanceVars:
  def __init__(self, arg1, arg2) -> None:
    ...
  
  def run(self, arg1, arg2):
    ...
  


class Kwargs:
  def props(self, **kwargs):
    ...
  
  def upper(self, **kwargs):
    ...
  
  def run(self, positional, named=..., **kwargs):
    ...
  


class ErrorRaiser:
  def fail(self):
    ...
  


class NonComparable:
  def __eq__(self, other) -> bool:
    ...
  
  def __ne__(self, other) -> bool:
    ...
  


class EmptyDictOutput:
  def totally_empty(self):
    ...
  
  def nothing_printable(self):
    ...
  


class CircularReference:
  def create(self):
    ...
  


class OrderedDictionary:
  def empty(self):
    ...
  
  def non_empty(self):
    ...
  


class NamedTuple:
  """Functions returning named tuples used for testing."""
  def point(self):
    """Point example straight from Python docs."""
    ...
  
  def matching_names(self):
    """Field name equals value."""
    ...
  


class CallableWithPositionalArgs:
  """Test class for supporting callable."""
  TEST = ...
  def __call__(self, x, y):
    ...
  
  def fn(self, x):
    ...
  


NamedTuplePoint = ...
class SubPoint(NamedTuplePoint):
  """Used for verifying subclasses of namedtuples behave as intended."""
  def coordinate_sum(self):
    ...
  


class CallableWithKeywordArgument:
  """Test class for supporting callable."""
  def __call__(self, **kwargs):
    ...
  
  def print_msg(self, msg):
    ...
  


CALLABLE_WITH_KEYWORD_ARGUMENT = ...
class ClassWithDocstring:
  """Test class for testing help text output.

  This is some detail description of this test class.
  """
  def __init__(self, message=...) -> None:
    """Constructor of the test class.

    Constructs a new ClassWithDocstring object.

    Args:
      message: The default message to print.
    """
    ...
  
  def print_msg(self, msg=...):
    """Prints a message."""
    ...
  


class ClassWithMultilineDocstring:
  """Test class for testing help text output with multiline docstring.

  This is a test class that has a long docstring description that spans across
  multiple lines for testing line breaking in help text.
  """
  @staticmethod
  def example_generator(n):
    """Generators have a ``Yields`` section instead of a ``Returns`` section.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    ...
  


def simple_set():
  ...

def simple_frozenset():
  ...

class Subdict(dict):
  """A subclass of dict, for testing purposes."""
  ...


SUBDICT = ...
class Color(enum.Enum):
  RED = ...
  GREEN = ...
  BLUE = ...


class HasStaticAndClassMethods:
  """A class with a static method and a class method."""
  CLASS_STATE = ...
  def __init__(self, instance_state) -> None:
    ...
  
  @staticmethod
  def static_fn(args):
    ...
  
  @classmethod
  def class_fn(cls, args):
    ...
  


def function_with_varargs(arg1, arg2, arg3=..., *varargs):
  """Function with varargs.

  Args:
    arg1: Position arg docstring.
    arg2: Position arg docstring.
    arg3: Flags docstring.
    *varargs: Accepts unlimited positional args.
  Returns:
    The unlimited positional args.
  """
  ...

def function_with_keyword_arguments(arg1, arg2=..., **kwargs):
  ...

def fn_with_code_in_docstring():
  """This has code in the docstring.



  Example:
    x = fn_with_code_in_docstring()
    indentation_matters = True



  Returns:
    True.
  """
  ...

class BinaryCanvas:
  """A canvas with which to make binary art, one bit at a time."""
  def __init__(self, size=...) -> None:
    ...
  
  def __str__(self) -> str:
    ...
  
  def show(self):
    ...
  
  def move(self, row, col):
    ...
  
  def on(self):
    ...
  
  def off(self):
    ...
  
  def set(self, value):
    ...
  


class DefaultMethod:
  def double(self, number):
    ...
  
  def __getattr__(self, name):
    ...
  


class InvalidProperty:
  def double(self, number):
    ...
  
  @property
  def prop(self):
    ...
  


def simple_decorator(f):
  ...

@simple_decorator
def decorated_method(name=...):
  ...

def fn_with_kwarg(arg1, arg2, **kwargs):
  """Function with kwarg.

  :param arg1: Description of arg1.
  :param arg2: Description of arg2.
  :key arg3: Description of arg3.
  """
  ...

def fn_with_kwarg_and_defaults(arg1, arg2, opt=..., **kwargs):
  """Function with kwarg and defaults.

  :param arg1: Description of arg1.
  :param arg2: Description of arg2.
  :key arg3: Description of arg3.
  """
  ...

def fn_with_multiple_defaults(first=..., last=..., late=...):
  """Function with kwarg and defaults.

  :key first: Description of first.
  :key last: Description of last.
  :key late: Description of late.
  """
  ...

