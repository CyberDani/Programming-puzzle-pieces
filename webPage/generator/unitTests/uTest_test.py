import os
import sys
import unittest

sys.path.append('..')

from defTypes import appDecisionType
from defTypes.dirPathType import DirectoryPathType as Dir
from defTypes.filePathType import FilePathType as File

from modules import checks
from modules import filerw
from modules import path
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
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(None, None, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName("", "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('./unitTests/', "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName("", "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('./unitTests/', True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('./unitTests/', "*.patternWithNoFounding", "tempDir", void)
    self.assertFalse(filerw.directoryExists('./unitTests/tempDir'))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('./nonExistingFolder/', "*.py", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(False, "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(False, True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('unitTests', "*.py", "temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('./unitTests/', "*.py", "")

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_examples_noTempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('./unitTests4unitTests/',
                                                                 "pass_*.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('unitTests4unitTests',
                                                                 "*_group2.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('./unitTests4unitTests',
                                                                 "*_group1.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('unitTests4unitTests/',
                                                                 "*_x_*.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_example_tempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('./unitTests4unitTests/',
                                                                 "*_tempDir.py", "tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_example_wrongFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('./unitTests4unitTests/',
                                                                 "*_tempDir.py", "wrongTempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_nonSense(self):
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(None, None, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames("", "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(None, None, ["temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames("", "", ["temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', "", "temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', "", ["temp12"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames("", "*.py", "temp23")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames("", "*.py", ["temp23"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', True, "temp23")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', True, ["temp23"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', "*.patternWithNoFounding", "tmp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', "*.patternWith0Founding", ["tmp"], void)
    self.assertFalse(filerw.directoryExists('./unitTests/tmp'))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./nonExistingFolder/', "*.py", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./nonExistingFolder/', "*.py", ["temp"], void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(False, "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(False, True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(False, "*.py", ["temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(False, True, ["temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('unitTests', "*.py", "temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', "*.py", "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('unitTests', "*.py", ["temp1/temp2"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', "*.py", [""])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests4unitTests/', "*_tempDir.py",
                                                                "tempDir", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests4unitTests/', "*_tempDir.py", [], void)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_examples_noTempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir34"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests4unitTests/',
                                                                 "pass_*.py", ["tempDir", "tempDir34"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir34"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('unitTests4unitTests',
                                                                 "*_group2.py", ["tempDir"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests4unitTests',
                                                                 "*_group1.py", ["tempForTests", "tempDir"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempForTests"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('unitTests4unitTests/',
                                                                 "*_x_*.py", ["tempDir"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_example_tempFoldersUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('unitTests4unitTests',
                                                                 "*_tempDirs.py", ["tempDir1", "tempDir2"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_example_wrongFoldersUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests4unitTests/',
                                                                 "*_tempDir.py", ["wrongTempDir1", "tempDir2"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingSingleTempFolderPath_nonSense(self):
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(None, None, "unitTests/temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath("", "", "unitTests/temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests/', "", "unitTests/temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath("", "*.py", "unitTests/temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests/', True, "unitTests/temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests/', "*.patternWithNoFounding",
                                                             "unitTests/temp12", void)
    self.assertFalse(filerw.directoryExists("unitTests/temp12"))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./nonExistingFolder/', "*.py",
                                                             "unitTests/temp12", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(False, "*.py", "unitTests/temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(False, True, "unitTests/temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests/', "*.py", "")

  def test_runAndEvaluateUnitTestsUsingSingleTempFolderPath_examples_noTempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests4unitTests/', "pass_*.py",
                                                                           "unitTests4unitTests/tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('unitTests4unitTests',
                                                                 "*_group2.py", "unitTests4unitTests/tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests4unitTests',
                                                                 "*_group1.py", "unitTests4unitTests/tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('unitTests4unitTests/',
                                                                 "*_x_*.py", "unitTests4unitTests/tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))

  def test_runAndEvaluateUnitTestsUsingSingleTempFolderPath_example_tempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests4unitTests/',
                                                                 "*_tempDir.py", "unitTests4unitTests/tempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingSingleTempFolderPath_example_wrongFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests4unitTests/',
                                                               "*_tempDir.py", "unitTests4unitTests/wrongTempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPaths_nonSense(self):
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(None, None, "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(None, None, ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths("", "", "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths("", "", ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests/', "", ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths("", "*.py", ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests/', True, ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests/', "*.patternWithNoFounding",
                                                                ["unitTests4unitTests/temp"], void)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/temp"))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./nonExistingFolder/', "*.py",
                                                                ["unitTests4unitTests/temp"], void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(False, "*.py", ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(False, True, ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('unitTests', "*.py", "unitTests4unitTests/temp1")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests/', "*.py", [""])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests4unitTests/', "*_tempDir.py",
                                                                "unitTests4unitTests/tempDir", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests4unitTests/', "*_tempDir.py", [], void)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPaths_examples_noTempFolderUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir34"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests4unitTests/',
                                                                 "pass_*.py", ["unitTests4unitTests/tempDir",
                                                                               "unitTests4unitTests/tempDir34"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir34"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('unitTests4unitTests',
                                                                 "*_group2.py", ["unitTests4unitTests/tempDir"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests4unitTests',
                                                                 "*_group1.py", ["unitTests4unitTests/tempForTests",
                                                                                 "unitTests4unitTests/tempDir"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempForTests"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('unitTests4unitTests/',
                                                                 "*_x_*.py", ["unitTests4unitTests/tempDir"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPaths_example_tempFoldersUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir2"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('unitTests4unitTests',
                                                                 "*_tempDirs.py", ["unitTests4unitTests/tempDir1",
                                                                                 "unitTests4unitTests/tempDir2"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir3"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPaths_example_wrongFoldersUsed(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir2"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/wrongTempDir1"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests4unitTests/',
                                                                 "*_tempDir.py", ["unitTests4unitTests/wrongTempDir1",
                                                                  "unitTests4unitTests/tempDir2"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/wrongTempDir1"))
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir2"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType_nonSense(self):
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(None, None, "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(None, None, ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(None, None,
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "", "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "", ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "",
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType('./unitTests/', "", "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType('./unitTests/', "", ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS, "",
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "*.py", "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "*.py", ["unitTests4unitTests/temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "*.py",
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType('./unitTests/', True, "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS, True,
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS,
                                                                    "*.patternWithNoFounding",
                                                                    [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR], void)
    tempPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR)
    self.assertFalse(filerw.directoryExists(tempPath))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.NON_EXISTING_DIRECTORY, "*.py",
                                                                   [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR], void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(False, "*.py", "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(False, "*.py",
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(False, True, "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(False, True,
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType('unitTests', "*.py",
                                                                      "unitTests4unitTests/temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS, "*.py",
                                                                      Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType('./unitTests/', "*.py", "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS, "*.py", "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                                      "*_tempDir.py",
                                                                      Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR, void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType('./unitTests4unitTests/',
                                                                      "*_tempDir.py", [], void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                                      "*_tempDir.py", [], void)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType_examples_noTempFolderUsed(self):
    tempdirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR)
    tempdir34Path = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34)
    self.assertFalse(filerw.directoryExists(tempdirPath))
    self.assertFalse(filerw.directoryExists(tempdir34Path))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                               "pass_*.py", [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR,
                                                                   Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists(tempdirPath))
    self.assertFalse(filerw.directoryExists(tempdir34Path))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                                    "*_group2.py",
                                                                    [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists(tempdirPath))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                           "*_group1.py", [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34,
                                                                      Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists(tempdirPath))
    self.assertFalse(filerw.directoryExists(tempdir34Path))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                              "*_x_*.py", [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR],
                                                              void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExists(tempdirPath))

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType_example_tempFoldersUsed(self):
    tempdir1Path = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1)
    tempdir2Path = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2)
    self.assertFalse(filerw.directoryExists(tempdir1Path))
    self.assertFalse(filerw.directoryExists(tempdir2Path))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                                  "*_tempDirs.py",
                                                                  [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1,
                                                                    Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists(tempdir1Path))
    self.assertFalse(filerw.directoryExists(tempdir2Path))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType_example_wrongFoldersUsed(self):
    tempdir2Path = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2)
    tempdir34Path = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34)
    self.assertFalse(filerw.directoryExists(tempdir2Path))
    self.assertFalse(filerw.directoryExists(tempdir34Path))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                                    "*_tempDir.py",
                                                                    [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34,
                                                                    Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExists(tempdir34Path))
    self.assertFalse(filerw.directoryExists(tempdir2Path))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
