import os
import sys
import unittest

sys.path.append('..')

from modules.unitTests.autoUnitTest import AutoUnitTest

from unitTests4unitTests.autoUt_scenario1 import Tests1UsingAutoUnitTest as Tests1

class AutoUtTests(unittest.TestCase):

  def test_checkIfSubclassOfPythonUt(self):
    self.assertTrue(issubclass(AutoUnitTest, unittest.TestCase))

  def test_checkIfRuns_test1(self):
    suites = unittest.TestSuite()
    runner = unittest.TextTestRunner(stream=open(os.devnull, "w"), verbosity=0)
    suites.addTests(unittest.makeSuite(Tests1))
    result = runner.run(suites)
    self.assertEqual(result.testsRun, 4)
    self.assertEqual(len(result.failures), 1)
    self.assertEqual(len(result.errors), 0)
    self.assertFalse(result.wasSuccessful())
