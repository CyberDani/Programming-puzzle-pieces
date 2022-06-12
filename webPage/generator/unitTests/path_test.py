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
    fileAbsolutePath = path.getAbsoluteFilePath(fileType)
    self.assertTrue(fileAbsolutePath.startswith(gitRepoAbsPath))
    self.assertTrue(fileAbsolutePath.endswith(fileType.value.getFileName()))
    self.assertEqual(fileAbsolutePath, gitRepoAbsPath + fileType.value.getRelativeFilePathToGitRepo())
    self.assertEqual(fileAbsolutePath, fileType.value.getAbsoluteFilePath())

  def test_getRelativeDirPathToGitRepoEndingWithSlash_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(".")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash("")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash("webPage/generator")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(False)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(None)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(0)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(["webPage/generator"])
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash([])
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(filePathType.FilePathType.HTML_INCLUDE_SIDENAV)

  def test_getRelativeDirPathToGitRepoEndingWithSlash_examples(self):
    gitRepoAbsPath = path.getGitRepoAbsolutePathEndingWithSlash()
    self.assertRelDirPathToGit(gitRepoAbsPath, dirPathType.DirectoryPathType.GIT_REPOSITORY)
    self.assertRelDirPathToGit(gitRepoAbsPath, dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertRelDirPathToGit(gitRepoAbsPath, dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES)
    self.assertRelDirPathToGit(gitRepoAbsPath, dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR)

  def assertRelDirPathToGit(self, gitRepoAbsPath, directoryPathType):
    relDirPath = path.getRelativeDirPathToGitRepoEndingWithSlash(directoryPathType)
    self.assertFalse(relDirPath.startswith(gitRepoAbsPath))
    self.assertTrue(len(relDirPath) == 0 or relDirPath[-1] == "/")
    self.assertEqual(relDirPath, directoryPathType.value.getRelativeDirPathToGitRepoEndingWithSlash())
    self.assertEqual(gitRepoAbsPath + relDirPath, directoryPathType.value.getAbsoluteDirPathEndingWithSlash())

  def test_getRelativeFilePathToGitRepo_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo(".")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo("")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo("webPage/generator")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo(False)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo(None)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo(0)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo(["webPage/generator"])
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo([])
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo(dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES)

  def test_getRelativeFilePathToGitRepo_examples(self):
    gitRepoAbsPath = path.getGitRepoAbsolutePathEndingWithSlash()
    self.assertRelFilePathToGit(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_FOOTER)
    self.assertRelFilePathToGit(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_TOPNAV)
    self.assertRelFilePathToGit(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_TOPQUOTE)
    self.assertRelFilePathToGit(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_INLINEJS)
    self.assertRelFilePathToGit(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_SIDENAV)

  def assertRelFilePathToGit(self, gitRepoAbsPath, fileType):
    fileRelPathToGit = path.getRelativeFilePathToGitRepo(fileType)
    self.assertFalse(fileRelPathToGit.startswith(gitRepoAbsPath))
    self.assertTrue(fileRelPathToGit.endswith(fileType.value.getFileName()))
    self.assertEqual(gitRepoAbsPath + fileRelPathToGit, fileType.value.getAbsoluteFilePath())
    self.assertEqual(fileRelPathToGit, fileType.value.getRelativeFilePathToGitRepo())
