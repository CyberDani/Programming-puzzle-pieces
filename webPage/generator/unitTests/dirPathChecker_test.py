import pathlib
import sys
import unittest

sys.path.append('..')

from defTypes.dirPathCheckerActionType import DirPathCheckerActionType as dirAction
from defTypes import dirPathChecker

from modules import filerw

class DirPathCheckerTests(unittest.TestCase):

  def test_getGitRepoAbsolutePathEndingWithSlash(self):
    gitRepoPath = dirPathChecker.getGitRepoAbsolutePathEndingWithSlash()
    self.assertEqual(gitRepoPath[-1], "/")
    self.assertTrue(filerw.fileExists(gitRepoPath + ".git/HEAD"))
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(gitRepoPath))

  def test_DirectoryPathChecker_nonSense(self):
    self.dirPatchCheckWithoutAndWithActions(None, ["file.txt"])
    self.dirPatchCheckWithoutAndWithActions("./unitTests", None)
    self.dirPatchCheckWithoutAndWithActions(True, ["file.txt"])
    self.dirPatchCheckWithoutAndWithActions("./webPage/generator/unitTests", False)
    self.dirPatchCheckWithoutAndWithActions("./webPage/generator/unitTests", 34)
    self.dirPatchCheckWithoutAndWithActions(None, ["checks.py"])
    self.dirPatchCheckWithoutAndWithActions(12, ["checks.py"])
    self.dirPatchCheckWithoutAndWithActions(None, None)
    self.dirPatchCheckWithoutAndWithActions(False, True)
    self.dirPatchCheckWithoutAndWithActions(1, 5)
    self.dirPatchCheckWithoutAndWithActions("webPage\\generator\\unitTests\\temp", ["testFile.txt"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", "checks_test.py")
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("checks.py", ["checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("nonExistingFolder", ["checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["nonExistingFile.py"],
                                          dirAction.ENSURE_PATH_EXISTS_ONLY)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/nonExistingDirectory", ["nonExistingFile.py"],
                                          dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["nonExistingFile.py"],
                                          dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["checks_test.py"],
                                          dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
    with self.assertRaises(Exception):
      file = open("./unitTests/temp/testFile1.txt", "w")
      file.close()
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp", ["testFile1.txt"],
                                          dirAction.ENSURE_PATH_EXISTS_ONLY)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests", [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("", ["READMENOT.md"])

  def dirPatchCheckWithoutAndWithActions(self, firstArg, secondArg):
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(firstArg, secondArg)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(firstArg, secondArg, dirAction.ENSURE_PATH_EXISTS_ONLY)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(firstArg, secondArg, dirAction.ENSURE_PATH_AND_FILES_EXIST)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(firstArg, secondArg, dirAction.DO_NOT_CHECK_PATH_EXISTENCE)

  def test_DirectoryPathChecker_validExamples(self):
    file = open("./unitTests/temp/testFile.txt", "w")
    file.close()
    file = open("./unitTests/temp/testFile2.txt", "w")
    file.close()
    file = open("./unitTests/temp/testFile3.txt", "w")
    file.close()
    try:
      dirPathChecker.DirectoryPathChecker("", ["README.md"])
      dirPathChecker.DirectoryPathChecker("", [], dirAction.ENSURE_PATH_EXISTS_ONLY)
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", [], dirAction.ENSURE_PATH_EXISTS_ONLY)
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", [],
                                          dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
      dirPathChecker.DirectoryPathChecker("./webPage/generator/nonExistingDirectory", [],
                                          dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp", ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/temp/", ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/temp", ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["temp/testFile.txt"])
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["/temp/testFile.txt"])
      dirPathChecker.DirectoryPathChecker("webPage/generator", ["unitTests/temp/testFile.txt"])
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", ["testFile.txt", "testFile2.txt"])
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", ["testFile.txt", "testFile2.txt",
                                                                               "testFile3.txt"])
    except Exception:
      self.fail("DirectoryPathChecker() raised Exception unexpectedly!")

  def test_DirectoryPathChecker_getAbsolutePathEndingWithSlash(self):
    gitRepoAbsPath = dirPathChecker.getGitRepoAbsolutePathEndingWithSlash()
    dir = dirPathChecker.DirectoryPathChecker("", ["README.md"])
    self.assertEqual(dir.getAbsoluteDirPathEndingWithSlash(), gitRepoAbsPath)
    dir = dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["/temp/testFile.txt"])
    self.assertEqual(dir.getAbsoluteDirPathEndingWithSlash(), gitRepoAbsPath + "webPage/generator/unitTests/")
    dir = dirPathChecker.DirectoryPathChecker("./././././webPage/generator/unitTests", ["/temp/testFile.txt"])
    self.assertEqual(dir.getAbsoluteDirPathEndingWithSlash(), gitRepoAbsPath + "webPage/generator/unitTests/")
    dir = dirPathChecker.DirectoryPathChecker("./webPage/generator/nonExistingDirectory", [],
                                        dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
    self.assertEqual(dir.getAbsoluteDirPathEndingWithSlash(),
                     gitRepoAbsPath + "webPage/generator/nonExistingDirectory/")
    dir = dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", [],
                                              dirAction.ENSURE_PATH_EXISTS_ONLY)
    self.assertEqual(dir.getAbsoluteDirPathEndingWithSlash(),
                     gitRepoAbsPath + "webPage/generator/unitTests/temp/")
