import sys
import unittest

sys.path.append('..')

from defTypes import dirPathChecker
from defTypes import dirPathType
from defTypes import filePathChecker

from modules import path

class FilePathCheckerTests(unittest.TestCase):

  def test_FilePathChecker_nonSense(self):
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(None, "file.txt")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR, None)
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR, "")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR, ["file.txt"])
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR, [])
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
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR, "bubbleGenerator.py")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.GIT_REPOSITORY, "notMyRepo.git")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_GENERATOR_UNIT_TESTS, "asdasdsda.py")

  def test_FilePathChecker_existingFiles(self):
    try:
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR, "generator.py")
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.GIT_REPOSITORY, "README.md")
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_GENERATOR_UNIT_TESTS, "checks_test.py")
    except Exception:
      self.fail("FilePathChecker raised Exception unexpectedly!")

  def test_FilePathChecker_existingFilesButContainsSlash(self):
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR, "./generator.py")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.GIT_REPOSITORY, ".git/HEAD")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.GIT_REPOSITORY, "./.git/HEAD")

  def test_FilePathChecker_existingDirectoryInsteadOfExistingFile(self):
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR, "unitTests")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.GIT_REPOSITORY, ".git")
    with self.assertRaises(Exception):
      filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.GIT_REPOSITORY, ".git/refs")

  def test_FilePathChecker_getRelativePathEndingWithSlash(self):
    filePath = filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR, "generator.py")
    self.assertEqual(filePath.getRelativePathEndingWithSlash(),
                     dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR.value.getRelativePathEndingWithSlash()
                          + "generator.py")
    filePath = filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.GIT_REPOSITORY, "README.md")
    self.assertEqual(filePath.getRelativePathEndingWithSlash(),
                     dirPathType.DirectoryRelPathType.GIT_REPOSITORY.value.getRelativePathEndingWithSlash()
                     + "README.md")
    filePath = filePathChecker.FilePathChecker(
                              dirPathType.DirectoryRelPathType.PYTHON_GENERATOR_UNIT_TESTS, "checks_test.py")
    self.assertEqual(filePath.getRelativePathEndingWithSlash(),
                     dirPathType.DirectoryRelPathType.PYTHON_GENERATOR_UNIT_TESTS.value.getRelativePathEndingWithSlash()
                     + "checks_test.py")

  def test_FilePathChecker_getAbsolutePathEndingWithSlash(self):
    filePath = filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR, "generator.py")
    self.assertEqual(filePath.getAbsolutePathEndingWithSlash(),
                     dirPathType.DirectoryRelPathType.PYTHON_MAIN_GENERATOR.value.getAbsolutePathEndingWithSlash()
                          + "generator.py")
    filePath = filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.GIT_REPOSITORY, "README.md")
    self.assertEqual(filePath.getAbsolutePathEndingWithSlash(),
                     dirPathType.DirectoryRelPathType.GIT_REPOSITORY.value.getAbsolutePathEndingWithSlash()
                     + "README.md")
    filePath = filePathChecker.FilePathChecker(
                              dirPathType.DirectoryRelPathType.PYTHON_GENERATOR_UNIT_TESTS, "checks_test.py")
    self.assertEqual(filePath.getAbsolutePathEndingWithSlash(),
                     dirPathType.DirectoryRelPathType.PYTHON_GENERATOR_UNIT_TESTS.value.getAbsolutePathEndingWithSlash()
                     + "checks_test.py")
