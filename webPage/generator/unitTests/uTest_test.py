import os
import sys
import unittest

sys.path.append('..')

from modules import uTest

class UnitTestTests(unittest.TestCase):

  def test_collectAndRunUnitTestsByFilePattern_nonSense(self):
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(None, None)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern("", "")
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern('./unitTests/', "")
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern("", "*.py")
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern('./unitTests/', True)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern('./unitTests/', True)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern('./nonExistingFolder/', "*.py")
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(False, "*.py")
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(False, True)

  def test_collectAndRunUnitTestsByFilePattern_examples(self):
    void = open(os.devnull, "w")
    result = uTest.collectAndRunUnitTestsByFilePattern('./unitTests4unitTests/', "pass_*.py", void)
    self.assertEqual(result.testsRun, 6)
    self.assertTrue(result.wasSuccessful())
    result = uTest.collectAndRunUnitTestsByFilePattern('./unitTests4unitTests/', "*_group1.py", void)
    self.assertEqual(result.testsRun, 7)
    self.assertFalse(result.wasSuccessful())
