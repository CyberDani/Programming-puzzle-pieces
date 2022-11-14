import sys

sys.path.append('..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.paths.dirPathCheckerActionType import DirPathCheckerActionType as dirAction
from modules.paths import dirPathChecker
from modules.paths import projectRootDetector as projRoot
from defTypes import pppConfig as config

from modules import filerw

class DirPathCheckerTests(AutoUnitTest):

  def test_DirectoryPathChecker_nonSense(self):
    self.dirPatchCheckWithoutAndWithActions(None, ["file.txt"])
    self.dirPatchCheckWithoutAndWithActions(config.PATH_FROM_GENERATOR_TO_UNIT_TESTS, None)
    self.dirPatchCheckWithoutAndWithActions(True, ["file.txt"])
    self.dirPatchCheckWithoutAndWithActions(config.PATH_FROM_ROOT_TO_UNIT_TESTS, False)
    self.dirPatchCheckWithoutAndWithActions(config.PATH_FROM_ROOT_TO_UNIT_TESTS, 34)
    self.dirPatchCheckWithoutAndWithActions(None, ["checks.py"])
    self.dirPatchCheckWithoutAndWithActions(12, ["checks.py"])
    self.dirPatchCheckWithoutAndWithActions(None, None)
    self.dirPatchCheckWithoutAndWithActions(False, True)
    self.dirPatchCheckWithoutAndWithActions(1, 5)
    pathWithAlteredSlash = config.PATH_FROM_ROOT_TO_UNIT_TESTS.replace("/", "\\")
    self.dirPatchCheckWithoutAndWithActions(pathWithAlteredSlash, ["testFile.txt"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, "checks_test.py")
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("checks.py", ["checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("nonExistingFolder", ["checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["nonExistingFile.py"],
                                          dirAction.ENSURE_DIR_EXISTS_ONLY)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + "nonExistingDirectory",
                                          ["nonExistingFile.py"], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["nonExistingFile.py"],
                                          dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["checks_test.py"],
                                          dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
    with self.assertRaises(Exception):
      filePath = config.PATH_FROM_GENERATOR_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME + "/testFile1.txt"
      file = open(filePath, "w")
      file.close()
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME,
                                          ["testFile1.txt"], dirAction.ENSURE_DIR_EXISTS_ONLY)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS, ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("", ["READMENOT.md"])

  def dirPatchCheckWithoutAndWithActions(self, firstArg, secondArg):
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(firstArg, secondArg)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(firstArg, secondArg, dirAction.ENSURE_DIR_EXISTS_ONLY)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(firstArg, secondArg, dirAction.ENSURE_PATH_AND_FILES_EXIST)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(firstArg, secondArg, dirAction.DO_NOT_CHECK_DIR_EXISTENCE)

  def test_DirectoryPathChecker_validExamples(self):
    found, projRootAbsPath = projRoot.getProjectRootPath()
    if not found:
      return
    filePath = config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME + "/testFile.txt"
    filePath2 = config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME + "/testFile2.txt"
    filePath3 = config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME + "/testFile3.txt"
    file = open(projRootAbsPath + filePath, "w")
    file.close()
    file = open(projRootAbsPath + filePath2, "w")
    file.close()
    file = open(projRootAbsPath + filePath3, "w")
    file.close()
    try:
      dirPathChecker.DirectoryPathChecker("", ["README.md"])
      dirPathChecker.DirectoryPathChecker("", [], dirAction.ENSURE_DIR_EXISTS_ONLY)
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME,
                                          ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME, [],
                                          dirAction.ENSURE_DIR_EXISTS_ONLY)
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME, [],
                                          dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + "nonExistingDirectory", [],
                                          dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
      dirPathChecker.DirectoryPathChecker("./" + config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME,
                                          ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME,
                                          ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME,
                                          ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS,
                                          [config.UT_TEMP1_FOLDER_NAME + "/testFile.txt"])
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS,
                                          [config.UT_TEMP1_FOLDER_NAME + "/testFile.txt"])
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_PY_GENERATOR,
                                          [config.PATH_FROM_GENERATOR_TO_UNIT_TESTS +
                                           config.UT_TEMP1_FOLDER_NAME + "/testFile.txt"])
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME,
                                          ["testFile.txt", "testFile2.txt"])
      dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME,
                                          ["testFile.txt", "testFile2.txt", "testFile3.txt"])
    except Exception:
      self.fail("DirectoryPathChecker() raised Exception unexpectedly!")

  def test_DirectoryPathChecker_getAbsolutePathEndingWithSlash(self):
    found, projRootAbsPath = projRoot.getProjectRootPath()
    if not found:
      return
    dir = dirPathChecker.DirectoryPathChecker("", ["README.md"])
    self.assertEqual(dir.getAbsoluteDirPathEndingWithSlash(), projRootAbsPath)
    filePath = config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME + "/testFile.txt"
    filerw.createOrOverwriteWithEmptyFileByPath(projRootAbsPath + filePath)
    dir = dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS,
                                              [config.UT_TEMP1_FOLDER_NAME + "/testFile.txt"])
    self.assertEqual(dir.getAbsoluteDirPathEndingWithSlash(), projRootAbsPath + config.PATH_FROM_ROOT_TO_UNIT_TESTS)
    dir = dirPathChecker.DirectoryPathChecker("./././././" + config.PATH_FROM_ROOT_TO_UNIT_TESTS,
                                              [config.UT_TEMP1_FOLDER_NAME + "/testFile.txt"])
    self.assertEqual(dir.getAbsoluteDirPathEndingWithSlash(), projRootAbsPath + config.PATH_FROM_ROOT_TO_UNIT_TESTS)
    dir = dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + "nonExistingDirectory", [],
                                              dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
    self.assertEqual(dir.getAbsoluteDirPathEndingWithSlash(),
                     projRootAbsPath + config.PATH_FROM_ROOT_TO_UNIT_TESTS + "nonExistingDirectory/")
    dir = dirPathChecker.DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME, [],
                                              dirAction.ENSURE_DIR_EXISTS_ONLY)
    self.assertEqual(dir.getAbsoluteDirPathEndingWithSlash(),
                     projRootAbsPath + config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME + "/")
