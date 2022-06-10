import os
import sys
import unittest

sys.path.append('..')

from defTypes import appDecisionType

from modules import checks
from modules import filerw
from modules import uTest

class UnitTestTests(unittest.TestCase):

  def test_collectAndRunUnitTestsByFilePattern_nonSense(self):
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(None, None, void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern("", "", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern('./unitTests/', "", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern("", "*.py", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern('./unitTests/', True, void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern('./unitTests/', True, void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern('./unitTests/', "*.patternWithNoFounding", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern('./nonExistingFolder/', "*.py", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(False, "*.py", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(False, True, void)

  def test_collectAndRunUnitTestsByFilePattern_examples(self):
    void = open(os.devnull, "w")
    result = uTest.collectAndRunUnitTestsByFilePattern('./unitTests4unitTests/', "pass_*.py", void)
    self.assertEqual(result.testsRun, 6)
    self.assertTrue(result.wasSuccessful())
    result = uTest.collectAndRunUnitTestsByFilePattern('./unitTests4unitTests/', "*_group1.py", void)
    self.assertEqual(result.testsRun, 7)
    self.assertFalse(result.wasSuccessful())

  def test_runAndEvaluateUnitTests_nonSense(self):
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(None, None)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests("", "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests('./unitTests/', "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests("", "*.py")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests('./unitTests/', True)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests('./unitTests/', "*.patternWithNoFounding", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests('./nonExistingFolder/', "*.py", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests('unitTests', "*.py", "file.txt")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(False, "*.py")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(False, True)

  def test_runAndEvaluateUnitTests_examples(self):
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTests('./unitTests4unitTests/', "pass_*.py", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTests('./unitTests4unitTests/', "*_group2.py", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTests('./unitTests4unitTests/', "*_group1.py", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTests('./unitTests4unitTests/', "*_x_*.py", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingTempFolder_nonSense(self):
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder(None, None, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder("", "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder('./unitTests/', "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder("", "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder('./unitTests/', True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder('./unitTests/', "*.patternWithNoFounding", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder('./nonExistingFolder/', "*.py", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder(False, "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder(False, True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder('unitTests', "*.py", "temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingTempFolder('./unitTests/', "*.py", "")

  def test_runAndEvaluateUnitTestsUsingTempFolder_examples_noTempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingTempFolder('./unitTests4unitTests/',
                                                                 "pass_*.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingTempFolder('unitTests4unitTests',
                                                                 "*_group2.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingTempFolder('./unitTests4unitTests',
                                                                 "*_group1.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingTempFolder('unitTests4unitTests/',
                                                                 "*_x_*.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))

  def test_runAndEvaluateUnitTestsUsingTempFolder_example_tempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingTempFolder('./unitTests4unitTests/',
                                                                 "*_tempDir.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingTempFolder_example_wrongFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingTempFolder('./unitTests4unitTests/',
                                                                 "*_tempDir.py", "wrongTempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
