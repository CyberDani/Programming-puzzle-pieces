import os
import sys
import unittest

sys.path.append('..')

from modules.unitTests.autoUnitTest import AutoUnitTest

from unitTests4unitTests import autoUt_scenario1 as ut1
from unitTests4unitTests import autoUt_scenario2 as ut2

class AutoUtTests(unittest.TestCase):

  def test_checkIfSubclassOfPythonUt(self):
    self.assertTrue(issubclass(AutoUnitTest, unittest.TestCase))

  def test_checkIfRuns_test1(self):
    suites = unittest.TestSuite()
    runner = unittest.TextTestRunner(stream=open(os.devnull, "w"), verbosity=0)
    suites.addTests(unittest.makeSuite(ut1.Tests1UsingAutoUnitTest))
    result = runner.run(suites)
    self.assertEqual(result.testsRun, 4)
    self.assertEqual(len(result.failures), 1)
    self.assertEqual(len(result.errors), 0)
    self.assertFalse(result.wasSuccessful())

  def test_checkIfRuns_test2(self):
    suites = unittest.TestSuite()
    runner = unittest.TextTestRunner(stream=open(os.devnull, "w"), verbosity=0)
    suites.addTests(unittest.makeSuite(ut2.Tests2UsingAutoUnitTest))
    result = runner.run(suites)
    self.assertEqual(result.testsRun, 2)
    self.assertEqual(len(result.failures), 0)
    self.assertEqual(len(result.errors), 0)
    self.assertTrue(result.wasSuccessful())
