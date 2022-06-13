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
    gitRepoAbsPath = path.getAbsoluteDirPathEndingWithSlash(dirPathType.DirectoryPathType.GIT_REPOSITORY)
    self.assertRelDirPathToGit(gitRepoAbsPath, dirPathType.DirectoryPathType.GIT_REPOSITORY)
    self.assertRelDirPathToGit(gitRepoAbsPath, dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertRelDirPathToGit(gitRepoAbsPath, dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES)
    self.assertRelDirPathToGit(gitRepoAbsPath, dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR)

  def assertRelDirPathToGit(self, gitRepoAbsPath, directoryPathType):
    relDirPath = path.getRelativeDirPathToGitRepoEndingWithSlash(directoryPathType)
    self.assertTrue(len(relDirPath) > 0)
    self.assertTrue(relDirPath[-1] == "/")
    self.assertEqual(pathlib.Path(gitRepoAbsPath + relDirPath).resolve(),
                     pathlib.Path(directoryPathType.value.getAbsoluteDirPathEndingWithSlash()).resolve())

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
    gitRepoAbsPath = path.getAbsoluteDirPathEndingWithSlash(dirPathType.DirectoryPathType.GIT_REPOSITORY)
    self.assertRelFilePathToGit(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_FOOTER)
    self.assertRelFilePathToGit(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_TOPNAV)
    self.assertRelFilePathToGit(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_TOPQUOTE)
    self.assertRelFilePathToGit(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_INLINEJS)
    self.assertRelFilePathToGit(gitRepoAbsPath, filePathType.FilePathType.HTML_INCLUDE_SIDENAV)

  def assertRelFilePathToGit(self, gitRepoAbsPath, fileType):
    fileRelPathToGit = path.getRelativeFilePathToGitRepo(fileType)
    self.assertTrue(fileRelPathToGit.endswith(fileType.value.getFileName()))
    self.assertEqual(pathlib.Path(gitRepoAbsPath + fileRelPathToGit).resolve(),
                     pathlib.Path(fileType.value.getAbsoluteFilePath()).resolve())

  def test_getRelativeFilePathToDirectory_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory(dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS,
                                          filePathType.FilePathType.HTML_INCLUDE_TOPNAV)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory(filePathType.FilePathType.HTML_INCLUDE_TOPNAV,
                                          "D:/Programming puzzle pieces/webPage")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory("D:/Programming puzzle pieces/webPage/generator/generator.py",
                                          dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory("D:/Programming puzzle pieces/webPage/generator/generator.py",
                                          "D:/Programming puzzle pieces/webPage")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory(None, None)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory(True, "directoryName")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory("file.txt", 12)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory(123, 0)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory(["fileName.txt"], False)

  def test_getRelativeFilePathToDirectory_example(self):
    self.assertRelativeFilePathToDirectory(filePathType.FilePathType.HTML_INCLUDE_TOPNAV,
                                        dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertRelativeFilePathToDirectory(filePathType.FilePathType.HTML_INCLUDE_TOPQUOTE,
                                           dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertRelativeFilePathToDirectory(filePathType.FilePathType.HTML_INCLUDE_TOPNAV,
                                           dirPathType.DirectoryPathType.GIT_REPOSITORY)
    self.assertRelativeFilePathToDirectory(filePathType.FilePathType.HTML_INCLUDE_FOOTER,
                                           dirPathType.DirectoryPathType.INDEX_HTML_LOCATION)
    self.assertRelativeFilePathToDirectory(filePathType.FilePathType.HTML_INCLUDE_INLINEJS,
                                           dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES)

  def assertRelativeFilePathToDirectory(self, fPathType, directoryPathType):
    relPath = path.getRelativeFilePathToDirectory(fPathType, directoryPathType)
    self.assertTrue(relPath.endswith(fPathType.value.getFileName()))
    self.assertEqual(pathlib.Path(directoryPathType.value.getAbsoluteDirPathEndingWithSlash() + relPath).resolve(),
                     pathlib.Path(fPathType.value.getAbsoluteFilePath()).resolve())
    self.assertFalse("\\" in relPath)

  def test_getRelativeDirPathToDirectoryEndingWithSlash_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS,
                                                         filePathType.FilePathType.HTML_INCLUDE_TOPNAV)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(filePathType.FilePathType.HTML_INCLUDE_TOPNAV,
                                                        dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(filePathType.FilePathType.HTML_INCLUDE_TOPNAV,
                                                        filePathType.FilePathType.HTML_INCLUDE_FOOTER)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(dirPathType.DirectoryPathType.GIT_REPOSITORY,
                                                         "D:/Programming puzzle pieces/webPage")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash("D:/Programming puzzle pieces/webPage/generator",
                                                        dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash("D:/Programming puzzle pieces/webPage/generator/",
                                          "D:/Programming puzzle pieces/webPage")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(None, None)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(True, "directoryName")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash("directoryName", 12)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(123, 0)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(["directoryName"], False)

  def test_getRelativeDirPathToDirectoryEndingWithSlash_examples(self):
    self.assertRelativeDirPathToDirectory(dirPathType.DirectoryPathType.GIT_REPOSITORY,
                                          dirPathType.DirectoryPathType.GIT_REPOSITORY)
    self.assertRelativeDirPathToDirectory(dirPathType.DirectoryPathType.GIT_REPOSITORY,
                                          dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR)
    self.assertRelativeDirPathToDirectory(dirPathType.DirectoryPathType.INDEX_HTML_LOCATION,
                                          dirPathType.DirectoryPathType.GIT_REPOSITORY)
    self.assertRelativeDirPathToDirectory(dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES,
                                          dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS)

  def assertRelativeDirPathToDirectory(self, dirPath1, dirPath2):
    relPath = path.getRelativeDirPathToDirectoryEndingWithSlash(dirPath1, dirPath2)
    self.assertTrue(len(relPath) > 0)
    self.assertEqual(pathlib.Path(dirPath2.value.getAbsoluteDirPathEndingWithSlash() + relPath).resolve(),
                     pathlib.Path(dirPath1.value.getAbsoluteDirPathEndingWithSlash()).resolve())
    self.assertFalse("\\" in relPath)
    self.assertTrue(relPath[-1] == "/")

  def test_getRelativeFilePathToIndexHtml_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeFilePathToIndexHtml(dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToIndexHtml("")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToIndexHtml(".")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToIndexHtml("temp")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToIndexHtml("..")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToIndexHtml(0)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToIndexHtml(None)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToIndexHtml(False)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToIndexHtml(["webPage"])

  def test_getRelativeFilePathToIndexHtml_examples(self):
    indexHtmlLocationAbsPath = path.getAbsoluteDirPathEndingWithSlash(dirPathType.DirectoryPathType.INDEX_HTML_LOCATION)
    self.assertRelFilePathToIndexHtml(indexHtmlLocationAbsPath, filePathType.FilePathType.HTML_INCLUDE_FOOTER)
    self.assertRelFilePathToIndexHtml(indexHtmlLocationAbsPath, filePathType.FilePathType.HTML_INCLUDE_TOPNAV)
    self.assertRelFilePathToIndexHtml(indexHtmlLocationAbsPath, filePathType.FilePathType.HTML_INCLUDE_TOPQUOTE)
    self.assertRelFilePathToIndexHtml(indexHtmlLocationAbsPath, filePathType.FilePathType.HTML_INCLUDE_INLINEJS)
    self.assertRelFilePathToIndexHtml(indexHtmlLocationAbsPath, filePathType.FilePathType.HTML_INCLUDE_SIDENAV)

  def assertRelFilePathToIndexHtml(self, indexHtmlLocationAbsPath, fileType):
    fileRelPathToIndexHtml = path.getRelativeFilePathToIndexHtml(fileType)
    self.assertTrue(fileRelPathToIndexHtml.endswith(fileType.value.getFileName()))
    self.assertEqual(pathlib.Path(indexHtmlLocationAbsPath + fileRelPathToIndexHtml).resolve(),
                     pathlib.Path(fileType.value.getAbsoluteFilePath()).resolve())

  def test_getRelativeDirPathToIndexHtmlEndingWithSlash_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeDirPathToIndexHtmlEndingWithSlash(filePathType.FilePathType.HTML_INCLUDE_TOPNAV)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToIndexHtmlEndingWithSlash("")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToIndexHtmlEndingWithSlash(".")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToIndexHtmlEndingWithSlash("temp")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToIndexHtmlEndingWithSlash("..")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToIndexHtmlEndingWithSlash(0)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToIndexHtmlEndingWithSlash(None)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToIndexHtmlEndingWithSlash(False)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToIndexHtmlEndingWithSlash(["webPage"])

  def test_getRelativeDirPathToIndexHtmlEndingWithSlash_examples(self):
    indexHtmlLocationAbsPath = path.getAbsoluteDirPathEndingWithSlash(dirPathType.DirectoryPathType.INDEX_HTML_LOCATION)
    self.assertRelDirPathToIndexHtmlLocation(indexHtmlLocationAbsPath, dirPathType.DirectoryPathType.GIT_REPOSITORY)
    self.assertRelDirPathToIndexHtmlLocation(indexHtmlLocationAbsPath,
                                             dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertRelDirPathToIndexHtmlLocation(indexHtmlLocationAbsPath,
                                             dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES)
    self.assertRelDirPathToIndexHtmlLocation(indexHtmlLocationAbsPath,
                                             dirPathType.DirectoryPathType.PYTHON_MAIN_GENERATOR)

  def assertRelDirPathToIndexHtmlLocation(self, indexHtmlLocationAbsPath, directoryPathType):
    relDirPath = path.getRelativeDirPathToIndexHtmlEndingWithSlash(directoryPathType)
    self.assertTrue(len(relDirPath) > 0)
    self.assertTrue(relDirPath[-1] == "/")
    self.assertEqual(pathlib.Path(indexHtmlLocationAbsPath + relDirPath).resolve(),
                     pathlib.Path(directoryPathType.value.getAbsoluteDirPathEndingWithSlash()).resolve())
