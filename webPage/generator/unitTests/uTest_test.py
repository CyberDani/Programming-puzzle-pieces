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
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName('./unitTests/', "*.patternWithNoFounding", "temp", void)
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
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames("", "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', "*.patternWithNoFounding", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./nonExistingFolder/', "*.py", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(False, "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(False, True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('unitTests', "*.py", "temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames('./unitTests/', "*.py", "")
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
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(None, None, "webPage/generator/unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath("", "", "webPage/generator/unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests/', "", "webPage/generator/unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath("", "*.py", "webPage/generator/unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests/', True, "webPage/generator/unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./unitTests/', "*.patternWithNoFounding",
                                                             "webPage/generator/unitTests/temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath('./nonExistingFolder/', "*.py",
                                                             "webPage/generator/unitTests/temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(False, "*.py", "webPage/generator/unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(False, True, "webPage/generator/unitTests/temp")
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
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths("", "", "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests/', "", "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths("", "*.py", "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests/', True, "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests/', "*.patternWithNoFounding",
                                                                "unitTests4unitTests/temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./nonExistingFolder/', "*.py",
                                                                "unitTests4unitTests/temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(False, "*.py", "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(False, True, "unitTests4unitTests/temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('unitTests', "*.py", "unitTests4unitTests/temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths('./unitTests/', "*.py", "")
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
