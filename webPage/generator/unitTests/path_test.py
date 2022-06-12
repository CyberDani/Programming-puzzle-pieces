import pathlib
import sys
import unittest

sys.path.append('..')

from defTypes import dirPathType
from defTypes import filePathType

from modules import filerw
from modules import path

class StringUtilTests(unittest.TestCase):

  def test_getGitRepoAbsolutePathEndingWithSlash(self):
    gitRepoPath = path.getGitRepoAbsolutePathEndingWithSlash()
    self.assertTrue(len(gitRepoPath) > 0)
    self.assertEqual(gitRepoPath[-1], "/")
    self.assertTrue(filerw.fileExists(gitRepoPath + ".git/HEAD"))
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(gitRepoPath))

  def test_getAbsoluteDirPathEndingWithSlash_nonSense(self):
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(".")
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash("")
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash("webPage/generator")
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(False)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(None)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(0)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(["webPage/generator"])
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash([])
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(filePathType.FilePathType.HTML_INCLUDE_SIDENAV)

  def test_getAbsoluteDirPathEndingWithSlash_examples(self):
    gitRepoAbsPath = path.getGitRepoAbsolutePathEndingWithSlash()
    self.assertAbsoluteDirPath(gitRepoAbsPath, dirPathType.DirectoryPathType.GIT_REPOSITORY)
    self.assertAbsoluteDirPath(gitRepoAbsPath, dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertAbsoluteDirPath(gitRepoAbsPath, dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES)
    self.assertAbsoluteDirPath(gitRepoAbsPath, dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR)

  def assertAbsoluteDirPath(self, gitRepoAbsPath, dirType):
    absPath = path.getAbsoluteDirPathEndingWithSlash(dirType)
    self.assertTrue(absPath.startswith(gitRepoAbsPath))
    self.assertEqual(absPath, gitRepoAbsPath + dirType.value.getRelativeDirPathToGitRepoEndingWithSlash())
    self.assertEqual(absPath, dirType.value.getAbsoluteDirPathEndingWithSlash())
    self.assertTrue(absPath[-1] == "/")

  def test_getAbsoluteFilePath_nonSense(self):
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(".")
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath("")
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath("webPage/generator")
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(False)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(None)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(0)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(["webPage/generator"])
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath([])
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES)

  def test_getAbsoluteFilePath_examples(self):
    gitRepoAbsPath = path.getGitRepoAbsolutePathEndingWithSlash()
    self.assertAbsoluteFilePath(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_FOOTER)
    self.assertAbsoluteFilePath(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_TOPNAV)
    self.assertAbsoluteFilePath(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_TOPQUOTE)
    self.assertAbsoluteFilePath(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_INLINEJS)
    self.assertAbsoluteFilePath(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_SIDENAV)

  def assertAbsoluteFilePath(self, gitRepoAbsPath, fileType):
    fileAbsolutePath = fileType.value.getAbsoluteFilePath()
    self.assertTrue(fileAbsolutePath.startswith(gitRepoAbsPath))
    self.assertTrue(fileAbsolutePath.endswith(fileType.value.getFileName()))
    self.assertEqual(fileAbsolutePath, gitRepoAbsPath + fileType.value.getRelativeFilePathToGitRepo())
    self.assertEqual(fileAbsolutePath, fileType.value.getAbsoluteFilePath())
