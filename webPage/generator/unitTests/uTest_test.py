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

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_nonSense(self):
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder(None, None, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder("", "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('./unitTests/', "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder("", "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('./unitTests/', True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('./unitTests/', "*.patternWithNoFounding", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('./nonExistingFolder/', "*.py", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder(False, "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder(False, True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('unitTests', "*.py", "temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('./unitTests/', "*.py", "")

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_examples_noTempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('./unitTests4unitTests/',
                                                                 "pass_*.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('unitTests4unitTests',
                                                                 "*_group2.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('./unitTests4unitTests',
                                                                 "*_group1.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('unitTests4unitTests/',
                                                                 "*_x_*.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_example_tempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('./unitTests4unitTests/',
                                                                 "*_tempDir.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_example_wrongFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolder('./unitTests4unitTests/',
                                                                 "*_tempDir.py", "wrongTempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_nonSense(self):
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders(None, None, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders("", "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('./unitTests/', "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders("", "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('./unitTests/', True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('./unitTests/', "*.patternWithNoFounding", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('./nonExistingFolder/', "*.py", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders(False, "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders(False, True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('unitTests', "*.py", "temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('./unitTests/', "*.py", "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('./unitTests4unitTests/', "*_tempDir.py", "tempDir", void)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_examples_noTempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir34"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('./unitTests4unitTests/',
                                                                 "pass_*.py", ["tempDir", "tempDir34"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir34"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('unitTests4unitTests',
                                                                 "*_group2.py", ["tempDir"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('./unitTests4unitTests',
                                                                 "*_group1.py", ["tempForTests", "tempDir"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempForTests"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('unitTests4unitTests/',
                                                                 "*_x_*.py", ["tempDir"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_example_tempFoldersUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('unitTests4unitTests',
                                                                 "*_tempDirs.py", ["tempDir1", "tempDir2"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_example_wrongFoldersUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolders('./unitTests4unitTests/',
                                                                 "*_tempDir.py", ["wrongTempDir1", "tempDir2"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
