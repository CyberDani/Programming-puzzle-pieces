import os
import sys
import unittest

sys.path.append('..')

from defTypes import appDecisionType
from defTypes.dirPathType import DirectoryPathType as Dir

from modules import checks
from modules import filerw
from modules import path
from modules import uTest

class UnitTestTests(unittest.TestCase):

  def test_collectAndRunUnitTestsByFilePattern_nonSense(self):
    void = open(os.devnull, "w")
    unitTestsDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS)
    nonExistingDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.NON_EXISTING_DIRECTORY)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(None, None, void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern("", "", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(unitTestsDirPath, "", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern("", "*.py", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(unitTestsDirPath, True, void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(unitTestsDirPath, "*.patternWithNoFounding", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(nonExistingDirPath, "*.py", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(False, "*.py", void)
    with self.assertRaises(Exception):
      uTest.collectAndRunUnitTestsByFilePattern(False, True, void)

  def test_collectAndRunUnitTestsByFilePattern_examples(self):
    void = open(os.devnull, "w")
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    result = uTest.collectAndRunUnitTestsByFilePattern(ut4utPath, "pass_*.py", void)
    self.assertEqual(result.testsRun, 6)
    self.assertTrue(result.wasSuccessful())
    result = uTest.collectAndRunUnitTestsByFilePattern(ut4utPath, "*_group1.py", void)
    self.assertEqual(result.testsRun, 7)
    self.assertFalse(result.wasSuccessful())

  def test_runAndEvaluateUnitTests_nonSense(self):
    void = open(os.devnull, "w")
    unitTestsDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS)
    nonExistingDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.NON_EXISTING_DIRECTORY)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(None, None)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests("", "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(unitTestsDirPath, "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests("", "*.py")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(unitTestsDirPath, True)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(unitTestsDirPath, "*.patternWithNoFounding", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(nonExistingDirPath, "*.py", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(unitTestsDirPath, "*.py", "file.txt")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(False, "*.py")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTests(False, True)

  def test_runAndEvaluateUnitTests_examples(self):
    void = open(os.devnull, "w")
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    result, lines = uTest.runAndEvaluateUnitTests(ut4utPath, "pass_*.py", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTests(ut4utPath, "*_group2.py", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTests(ut4utPath, "*_group1.py", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTests(ut4utPath, "*_x_*.py", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_nonSense(self):
    void = open(os.devnull, "w")
    utDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS)
    nonExistingDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.NON_EXISTING_DIRECTORY)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(None, None, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName("", "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(utDirPath, "", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName("", "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(utDirPath, True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(utDirPath, "*.patternWithNoFounding", "tempDir", void)
    self.assertFalse(filerw.directoryExistsByPath(utDirPath + "tempDir"))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(nonExistingDirPath, "*.py", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(False, "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(False, True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(utDirPath, "*.py", "temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(utDirPath, "*.py", "")

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_examples_noTempFolderUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(ut4utPath, "pass_*.py", tempDir, void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(ut4utPath, "*_group2.py", tempDir, void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(ut4utPath, "*_group1.py", tempDir, void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(ut4utPath, "*_x_*.py", tempDir, void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_example_tempFolderUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(ut4utPath, "*_tempDir.py", tempDir, void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingSingleTempFolder_example_wrongFolderUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderName(ut4utPath, "*_tempDir.py",
                                                                           "wrongTempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_nonSense(self):
    nonExistingDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.NON_EXISTING_DIRECTORY)
    utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS)
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
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
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(utPath, "", "temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(utPath, "", ["temp12"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames("", "*.py", "temp23")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames("", "*.py", ["temp23"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(utPath, True, "temp23")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(utPath, True, ["temp23"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(utPath, "*.patternWithNoFounding", "tmp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(utPath, "*.patternWith0Founding", ["tmp"], void)
    self.assertFalse(filerw.directoryExistsByPath(utPath + "tmp"))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(nonExistingDirPath, "*.py", "temp", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(nonExistingDirPath, "*.py", ["temp"], void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(False, "*.py", "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(False, True, "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(False, "*.py", ["temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(False, True, ["temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(utPath, "*.py", "temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(utPath, "*.py", "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(utPath, "*.py", ["temp1/temp2"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(utPath, "*.py", [""])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(ut4utPath, "*_tempDir.py", tempDir, void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(ut4utPath, "*_tempDir.py", [], void)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_examples_noTempFolderUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    tempDir34 = "tempDir34"
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir34))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(ut4utPath,
                                                                              "pass_*.py", [tempDir, tempDir34], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir34))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(ut4utPath, "*_group2.py", [tempDir], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(ut4utPath, "*_group1.py",
                                                                              ["tempForTests", tempDir], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "tempForTests"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(ut4utPath, "*_x_*.py", [tempDir], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_example_tempFoldersUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    tempDir1 = "tempDir1"
    tempDir2 = "tempDir2"
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(ut4utPath, "*_tempDirs.py",
                                                                              [tempDir1, tempDir2], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir1))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir2))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolders_example_wrongFoldersUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderNames(ut4utPath, "*_tempDir.py",
                                                                              ["wrongTempDir1", "tempDir2"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingSingleTempFolderPath_nonSense(self):
    nonExistingDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.NON_EXISTING_DIRECTORY)
    utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS)
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(None, None, utPath + "temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath("", "", utPath + "temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(utPath, "", utPath + "temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath("", "*.py", utPath + "temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(utPath, True, utPath + "temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(utPath, "*.patternWithNoFounding", utPath + "temp12", void)
    self.assertFalse(filerw.directoryExistsByPath(utPath + "temp12"))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(nonExistingDirPath, "*.py", utPath + "temp12", void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(False, "*.py", utPath + "temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(False, True, utPath + "temp12")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(utPath, "*.py", "")

  def test_runAndEvaluateUnitTestsUsingSingleTempFolderPath_examples_noTempFolderUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(ut4utPath, "pass_*.py",
                                                                            ut4utPath + tempDir, void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(ut4utPath, "*_group2.py",
                                                                           ut4utPath + tempDir, void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(ut4utPath, "*_group1.py",
                                                                           ut4utPath + tempDir, void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(ut4utPath, "*_x_*.py",
                                                                           ut4utPath + tempDir, void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))

  def test_runAndEvaluateUnitTestsUsingSingleTempFolderPath_example_tempFolderUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(ut4utPath, "*_tempDir.py",
                                                                           ut4utPath + tempDir, void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingSingleTempFolderPath_example_wrongFolderUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingSingleTempFolderPath(ut4utPath, "*_tempDir.py",
                                                                           ut4utPath + "wrongTempDir", void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPaths_nonSense(self):
    nonExistingDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.NON_EXISTING_DIRECTORY)
    utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS)
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(None, None, ut4utPath + "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(None, None, [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths("", "", ut4utPath + "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths("", "", [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(utPath, "", [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths("", "*.py", [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(utPath, True, [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(utPath, "*.patternWithNoFounding",
                                                                [ut4utPath + "temp"], void)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "temp"))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(nonExistingDirPath, "*.py",
                                                                [ut4utPath + "temp"], void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(False, "*.py", [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(False, True, [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(utPath, "*.py", ut4utPath + "temp1")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(utPath, "*.py", [""])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(ut4utPath, "*_tempDir.py",
                                                                ut4utPath + tempDir, void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(ut4utPath, "*_tempDir.py", [], void)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPaths_examples_noTempFolderUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    tempDir = "tempDir"
    tempDir34 = "tempDir34"
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir34))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(ut4utPath,
                                                                 "pass_*.py", [ut4utPath + tempDir,
                                                                               ut4utPath + tempDir34], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir34))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(ut4utPath, "*_group2.py",
                                                                              [ut4utPath + tempDir], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(ut4utPath, "*_group1.py",
                                                                                [ut4utPath + "tempForTests",
                                                                                 ut4utPath + tempDir], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "tempForTests"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(ut4utPath, "*_x_*.py",
                                                                              [ut4utPath + tempDir], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + tempDir))

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPaths_example_tempFoldersUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "tempDir"))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "tempDir2"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(ut4utPath, "*_tempDirs.py",
                                                                                [ut4utPath + "tempDir1",
                                                                                 ut4utPath + "tempDir2"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "tempDir"))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "tempDir3"))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPaths_example_wrongFoldersUsed(self):
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "tempDir2"))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "wrongTempDir1"))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(ut4utPath, "*_tempDir.py",
                                                                              [ut4utPath + "wrongTempDir1",
                                                                                ut4utPath + "tempDir2"], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "wrongTempDir1"))
    self.assertFalse(filerw.directoryExistsByPath(ut4utPath + "tempDir2"))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType_nonSense(self):
    utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS)
    ut4utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    void = open(os.devnull, "w")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(None, None, ut4utPath + "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(None, None, [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(None, None,
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "", ut4utPath + "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "", [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "",
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(utPath, "", ut4utPath + "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(utPath, "", [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS, "",
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "*.py", ut4utPath + "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "*.py", [ut4utPath + "temp"])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType("", "*.py",
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(utPath, True, ut4utPath + "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS, True,
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS,
                                                                    "*.patternWithNoFounding",
                                                                    [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR], void)
    tempPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR)
    self.assertFalse(filerw.directoryExistsByPath(tempPath))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.NON_EXISTING_DIRECTORY, "*.py",
                                                                   [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR], void)
    self.assertFalse(filerw.directoryExistsByPath(path.getAbsoluteDirPathEndingWithSlash(Dir.NON_EXISTING_DIRECTORY)))
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(False, "*.py", ut4utPath + "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(False, "*.py",
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(False, True, ut4utPath + "temp")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(False, True,
                                                                      [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR])
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(utPath, "*.py", ut4utPath + "temp1/temp2")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS, "*.py",
                                                                      Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(utPath, "*.py", "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS, "*.py", "")
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                                      "*_tempDir.py",
                                                                      Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR, void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(ut4utPath, "*_tempDir.py", [], void)
    with self.assertRaises(Exception):
      uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                                      "*_tempDir.py", [], void)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType_examples_noTempFolderUsed(self):
    tempdirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR)
    tempdir34Path = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34)
    self.assertFalse(filerw.directoryExistsByPath(tempdirPath))
    self.assertFalse(filerw.directoryExistsByPath(tempdir34Path))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                               "pass_*.py", [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR,
                                                                   Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(tempdirPath))
    self.assertFalse(filerw.directoryExistsByPath(tempdir34Path))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                                    "*_group2.py",
                                                                    [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(tempdirPath))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                           "*_group1.py", [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34,
                                                                      Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(tempdirPath))
    self.assertFalse(filerw.directoryExistsByPath(tempdir34Path))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                              "*_x_*.py", [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR],
                                                              void)
    checks.checkIfPureListOfStrings(lines)
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
    self.assertFalse(filerw.directoryExistsByPath(tempdirPath))

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType_example_tempFoldersUsed(self):
    tempdir1Path = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1)
    tempdir2Path = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2)
    self.assertFalse(filerw.directoryExistsByPath(tempdir1Path))
    self.assertFalse(filerw.directoryExistsByPath(tempdir2Path))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                                  "*_tempDirs.py",
                                                                  [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1,
                                                                    Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(tempdir1Path))
    self.assertFalse(filerw.directoryExistsByPath(tempdir2Path))
    self.assertEqual(result, appDecisionType.AppDecisionType.CONTINUE_RUNNING)

  def test_runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType_example_wrongFoldersUsed(self):
    tempdir2Path = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2)
    tempdir34Path = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34)
    self.assertFalse(filerw.directoryExistsByPath(tempdir2Path))
    self.assertFalse(filerw.directoryExistsByPath(tempdir34Path))
    void = open(os.devnull, "w")
    result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS,
                                                                    "*_tempDir.py",
                                                                    [Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34,
                                                                    Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2], void)
    checks.checkIfPureListOfStrings(lines)
    self.assertFalse(filerw.directoryExistsByPath(tempdir34Path))
    self.assertFalse(filerw.directoryExistsByPath(tempdir2Path))
    self.assertEqual(result, appDecisionType.AppDecisionType.STOP_APP)
