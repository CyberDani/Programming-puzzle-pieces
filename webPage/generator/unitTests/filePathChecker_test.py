import sys
import unittest

sys.path.append('..')

from defTypes import dirPathType
from defTypes.filePathCheckerActionType import FilePathCheckerActionType as fileAction
from defTypes import filePathChecker

from modules import filerw

class FilePathCheckerTests(unittest.TestCase):

  def test_FilePathChecker_nonSense(self):
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(None, "file.txt")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, None)
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, "")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, ["file.txt"])
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, [])
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(True, ["file.txt"])
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker("./webPage/generator/unitTests", False)
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker("./webPage/generator/unitTests", 34)
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker("./webPage/generator/unitTests", "checks_test.py")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(12, ["checks.py"])
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker("checks.py", ["checks_test.py"])
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(None, None)
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(False, True)
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(1, 5)
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker("", ["README.md"])

  def test_FilePathChecker_nonExistingFiles(self):
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, "bubbleGenerator.py")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.GIT_REPOSITORY, "notMyRepo.git")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS, "asdasdsda.py")

  def test_FilePathChecker_existingFiles(self):
    try:
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, "generator.py")
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.GIT_REPOSITORY, "README.md")
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS, "checks_test.py")
    except Exception:
      self.fail("FilePathChecker raised Exception unexpectedly!")

  def test_FilePathChecker_nonExistingFiles_doNotCheckExistence(self):
    try:
      generatorDirPath = dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR.value.getAbsoluteDirPathEndingWithSlash()
      nonExistingFileName1 = "asdddawcvw.das"
      self.assertFalse(filerw.fileExists(generatorDirPath + nonExistingFileName1))
      ch = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, nonExistingFileName1,
                                      fileAction.DONT_CHECK_FILE_EXISTENCE)
      self.assertEqual(ch.getFileName(), nonExistingFileName1)
      self.assertEqual(ch.getAbsoluteFilePath(), generatorDirPath + nonExistingFileName1)
    except Exception:
      self.fail("FilePathChecker raised Exception unexpectedly!")

  def test_FilePathChecker_existingFilesButContainsSlash(self):
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, "./generator.py")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.GIT_REPOSITORY, ".git/HEAD")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.GIT_REPOSITORY, "./.git/HEAD")

  def test_FilePathChecker_existingDirectoryInsteadOfExistingFile(self):
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, "unitTests")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.GIT_REPOSITORY, ".git")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.GIT_REPOSITORY, ".git/refs")

  def test_FilePathChecker_getAbsolutePathEndingWithSlash(self):
    filePath = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, "generator.py")
    self.assertEqual(filePath.getAbsoluteFilePath(),
                     dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR.value.getAbsoluteDirPathEndingWithSlash()
                     + "generator.py")
    filePath = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.GIT_REPOSITORY, "README.md")
    self.assertEqual(filePath.getAbsoluteFilePath(),
                     dirPathType.DirectoryPathType.GIT_REPOSITORY.value.getAbsoluteDirPathEndingWithSlash()
                     + "README.md")
    filePath = filePathChecker.FilePathChecker(
                              dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS, "checks_test.py")
    self.assertEqual(filePath.getAbsoluteFilePath(),
                     dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS.value.getAbsoluteDirPathEndingWithSlash()
                     + "checks_test.py")

  def test_FilePathChecker_getFileName(self):
    filePath = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR, "generator.py")
    self.assertEqual(filePath.getFileName(), "generator.py")
    filePath = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.GIT_REPOSITORY, "README.md")
    self.assertEqual(filePath.getFileName(), "README.md")
    filePath = filePathChecker.FilePathChecker(
                              dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS, "checks_test.py")
    self.assertEqual(filePath.getFileName(), "checks_test.py")
