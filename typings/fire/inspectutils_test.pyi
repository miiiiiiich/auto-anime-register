"""
This type stub file was generated by pyright.
"""

import unittest

import six
from fire import testutils

"""
This type stub file was generated by pyright.
"""
class InspectUtilsTest(testutils.BaseTestCase):
  def testGetFullArgSpec(self):
    ...
  
  @unittest.skipIf(six.PY2, 'No keyword arguments in python 2')
  def testGetFullArgSpecPy3(self):
    ...
  
  def testGetFullArgSpecFromBuiltin(self):
    ...
  
  def testGetFullArgSpecFromSlotWrapper(self):
    ...
  
  def testGetFullArgSpecFromNamedTuple(self):
    ...
  
  def testGetFullArgSpecFromNamedTupleSubclass(self):
    ...
  
  def testGetFullArgSpecFromClassNoInit(self):
    ...
  
  def testGetFullArgSpecFromMethod(self):
    ...
  
  def testInfoOne(self):
    ...
  
  def testInfoClass(self):
    ...
  
  def testInfoClassNoInit(self):
    ...
  
  def testInfoNoDocstring(self):
    ...
  


if __name__ == '__main__':
  ...
