import pathlib
import sys
import unittest

sys.path.append('..')

from defTypes.dirPathTypeForUT import DirectoryPathTypeForUT as utDir
from defTypes.filePathTypeForUT import FilePathTypeForUT as utFile
from defTypes import pppConfig as config

from modules import filerw
from modules import path

class StringUtilTests(unittest.TestCase):

  def test_getGitRepoAbsolutePathEndingWithSlash(self):
    gitRepoPath = path.getGitRepoAbsolutePathEndingWithSlash()
    self.assertTrue(len(gitRepoPath) > 0)
    self.assertEqual(gitRepoPath[-1], "/")
    self.assertTrue(filerw.fileExistsByPath(gitRepoPath + ".git/HEAD"))
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(gitRepoPath))

  def test_getFileName_nonSense(self):
    with self.assertRaises(Exception):
      path.getFileName(".")
    with self.assertRaises(Exception):
      path.getFileName("")
    with self.assertRaises(Exception):
      path.getFileName(config.PATH_FROM_REPO_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getFileName(False)
    with self.assertRaises(Exception):
      path.getFileName(None)
    with self.assertRaises(Exception):
      path.getFileName(0)
    with self.assertRaises(Exception):
      path.getFileName([config.PATH_FROM_REPO_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getFileName([])
    with self.assertRaises(Exception):
      path.getFileName(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)

  def test_getFileName_examples(self):
    self.assertGetFileName(utFile.FOR_TEST_TEXTFILE1)
    self.assertGetFileName(utFile.FOR_TEST_TEXTFILE2)
    self.assertGetFileName(utFile.FOR_TEST_TEXTFILE3)
    self.assertGetFileName(utFile.FOR_TEST_NON_EXISTING_TEXTFILE1)

  def assertGetFileName(self, fPathType):
    fileName = path.getFileName(fPathType)
    absolutFilePath = path.getAbsoluteFilePath(fPathType)
    self.assertFalse("/" in fileName)
    self.assertTrue("/" in absolutFilePath)
    self.assertTrue(absolutFilePath.endswith(fileName))
    self.assertEqual(fileName, fPathType.value.getFileName())

  def test_getAbsoluteDirPathEndingWithSlash_nonSense(self):
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(".")
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash("")
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(config.PATH_FROM_REPO_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(False)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(None)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(0)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash([config.PATH_FROM_REPO_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash([])
    with self.assertRaises(Exception):
      path.getAbsoluteDirPathEndingWithSlash(utFile.FOR_TEST_TEXTFILE3)

  def test_getAbsoluteDirPathEndingWithSlash_examples(self):
    gitRepoAbsPath = path.getGitRepoAbsolutePathEndingWithSlash()
    self.assertAbsoluteDirPath(gitRepoAbsPath, utDir.GIT_REPOSITORY)
    self.assertAbsoluteDirPath(gitRepoAbsPath, utDir.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertAbsoluteDirPath(gitRepoAbsPath, utDir.PYTHON_MAIN_GENERATOR)

  def assertAbsoluteDirPath(self, gitRepoAbsPath, dirType):
    absPath = path.getAbsoluteDirPathEndingWithSlash(dirType)
    self.assertTrue(absPath.startswith(gitRepoAbsPath))
    self.assertEqual(absPath, dirType.value.getAbsoluteDirPathEndingWithSlash())
    self.assertTrue(absPath[-1] == "/")

  def test_getAbsoluteDirParentPathEndingWithSlash_nonSense(self):
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPathEndingWithSlash(".")
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPathEndingWithSlash("")
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPathEndingWithSlash(config.PATH_FROM_REPO_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPathEndingWithSlash(False)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPathEndingWithSlash(None)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPathEndingWithSlash(0)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPathEndingWithSlash([config.PATH_FROM_REPO_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPathEndingWithSlash([])
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPathEndingWithSlash(utFile.FOR_TEST_TEXTFILE2)

  def test_getAbsoluteDirParentPathEndingWithSlash_examples(self):
    self.assertAbsoluteDirParentPath(utDir.GIT_REPOSITORY)
    self.assertAbsoluteDirParentPath(utDir.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertAbsoluteDirParentPath(utDir.PYTHON_MAIN_GENERATOR)
    self.assertAbsoluteDirParentPath(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertAbsoluteDirParentPath(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    self.assertAbsoluteDirParentPath(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    self.assertAbsoluteDirParentPath(utDir.HTML_BACKUP)

  def assertAbsoluteDirParentPath(self, dirType):
    absParentPath = path.getAbsoluteDirParentPathEndingWithSlash(dirType)
    absPath = path.getAbsoluteDirPathEndingWithSlash(dirType)
    self.assertTrue(absParentPath[-1] == "/")
    self.assertTrue(absPath[-1] == "/")
    self.assertTrue(absPath.startswith(absParentPath))
    absPathParts = absPath.split("/")
    absParentPathParts = absParentPath.split("/")
    self.assertEqual(len(absPathParts), len(absParentPathParts) + 1)
    self.assertEqual(absParentPathParts[:-1], absPathParts[:-2])

  def test_getAbsoluteDirParentX2PathEndingWithSlash_nonSense(self):
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2PathEndingWithSlash(".")
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2PathEndingWithSlash("")
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2PathEndingWithSlash(config.PATH_FROM_REPO_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2PathEndingWithSlash(False)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2PathEndingWithSlash(None)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2PathEndingWithSlash(0)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2PathEndingWithSlash([config.PATH_FROM_REPO_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2PathEndingWithSlash([])
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2PathEndingWithSlash(utFile.FOR_TEST_TEXTFILE3)

  def test_getAbsoluteDirParentX2PathEndingWithSlash_examples(self):
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_MAIN_GENERATOR)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2)

  def assertAbsoluteDirParentX2Path(self, dirType):
    absParentPath = path.getAbsoluteDirParentX2PathEndingWithSlash(dirType)
    absPath = path.getAbsoluteDirPathEndingWithSlash(dirType)
    self.assertTrue(absParentPath[-1] == "/")
    self.assertTrue(absPath[-1] == "/")
    self.assertTrue(absPath.startswith(absParentPath))
    absPathParts = absPath.split("/")
    absParentPathParts = absParentPath.split("/")
    self.assertEqual(len(absPathParts), len(absParentPathParts) + 2)
    self.assertEqual(absParentPathParts[:-1], absPathParts[:-3])

  def test_getAbsoluteFilePath_nonSense(self):
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(".")
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath("")
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(config.PATH_FROM_REPO_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(False)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(None)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(0)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath([config.PATH_FROM_REPO_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath([])
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)

  def test_getAbsoluteFilePath_examples(self):
    gitRepoAbsPath = path.getGitRepoAbsolutePathEndingWithSlash()
    self.assertAbsoluteFilePath(gitRepoAbsPath, utFile.FOR_TEST_TEXTFILE1)
    self.assertAbsoluteFilePath(gitRepoAbsPath, utFile.FOR_TEST_TEXTFILE2)
    self.assertAbsoluteFilePath(gitRepoAbsPath, utFile.FOR_TEST_TEXTFILE3)
    self.assertAbsoluteFilePath(gitRepoAbsPath, utFile.FOR_TEST_NON_EXISTING_TEXTFILE1)

  def assertAbsoluteFilePath(self, gitRepoAbsPath, fileType):
    fileAbsolutePath = path.getAbsoluteFilePath(fileType)
    self.assertTrue(fileAbsolutePath.startswith(gitRepoAbsPath))
    self.assertTrue(fileAbsolutePath.endswith(fileType.value.getFileName()))
    self.assertEqual(fileAbsolutePath, fileType.value.getAbsoluteFilePath())

  def test_getRelativeDirPathToGitRepoEndingWithSlash_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(".")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash("")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(config.PATH_FROM_REPO_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(False)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(None)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(0)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash([config.PATH_FROM_REPO_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash([])
    with self.assertRaises(Exception):
      path.getRelativeDirPathToGitRepoEndingWithSlash(utFile.FOR_TEST_TEXTFILE3)

  def test_getRelativeDirPathToGitRepoEndingWithSlash_examples(self):
    gitRepoAbsPath = path.getAbsoluteDirPathEndingWithSlash(utDir.GIT_REPOSITORY)
    self.assertRelDirPathToGit(gitRepoAbsPath, utDir.GIT_REPOSITORY)
    self.assertRelDirPathToGit(gitRepoAbsPath, utDir.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertRelDirPathToGit(gitRepoAbsPath, utDir.PYTHON_MAIN_GENERATOR)

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
      path.getRelativeFilePathToGitRepo(config.PATH_FROM_REPO_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo(False)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo(None)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo(0)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo([config.PATH_FROM_REPO_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo([])
    with self.assertRaises(Exception):
      path.getRelativeFilePathToGitRepo(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)

  def test_getRelativeFilePathToGitRepo_examples(self):
    gitRepoAbsPath = path.getAbsoluteDirPathEndingWithSlash(utDir.GIT_REPOSITORY)
    self.assertRelFilePathToGit(gitRepoAbsPath, utFile.FOR_TEST_TEXTFILE1)
    self.assertRelFilePathToGit(gitRepoAbsPath, utFile.FOR_TEST_TEXTFILE2)
    self.assertRelFilePathToGit(gitRepoAbsPath, utFile.FOR_TEST_TEXTFILE3)
    self.assertRelFilePathToGit(gitRepoAbsPath, utFile.FOR_TEST_NON_EXISTING_TEXTFILE1)

  def assertRelFilePathToGit(self, gitRepoAbsPath, fileType):
    fileRelPathToGit = path.getRelativeFilePathToGitRepo(fileType)
    self.assertTrue(fileRelPathToGit.endswith(fileType.value.getFileName()))
    self.assertEqual(pathlib.Path(gitRepoAbsPath + fileRelPathToGit).resolve(),
                     pathlib.Path(fileType.value.getAbsoluteFilePath()).resolve())

  def test_getRelativeFilePathToDirectory_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory(utDir.PYTHON_GENERATOR_UNIT_TESTS, utFile.FOR_TEST_NON_EXISTING_TEXTFILE1)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory(utFile.FOR_TEST_TEXTFILE1, "D:/Programming puzzle pieces/webPage")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory("D:/Programming puzzle pieces/" + config.PATH_FROM_REPO_TO_PY_GENERATOR +
                                          "generator.py", utDir.PYTHON_GENERATOR_UNIT_TESTS)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory("D:/Programming puzzle pieces/" + config.PATH_FROM_REPO_TO_PY_GENERATOR +
                                          "generator.py", "D:/Programming puzzle pieces/webPage")
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

  # TODO implement test case
  #def test_getRelativeFilePathToDirectory_example(self):
    #self.assertRelativeFilePathToDirectory(utFile.HTML_INCLUDE_TOPNAV, utDir.PYTHON_GENERATOR_UNIT_TESTS)
    #self.assertRelativeFilePathToDirectory(utFile.HTML_INCLUDE_TOPQUOTE, utDir.PYTHON_GENERATOR_UNIT_TESTS)
    #self.assertRelativeFilePathToDirectory(utFile.HTML_INCLUDE_TOPNAV, utDir.GIT_REPOSITORY)
    #self.assertRelativeFilePathToDirectory(utFile.HTML_INCLUDE_FOOTER, utDir.INDEX_HTML_LOCATION)

  def assertRelativeFilePathToDirectory(self, fPathType, directoryPathType):
    relPath = path.getRelativeFilePathToDirectory(fPathType, directoryPathType)
    self.assertTrue(relPath.endswith(fPathType.value.getFileName()))
    self.assertEqual(pathlib.Path(directoryPathType.value.getAbsoluteDirPathEndingWithSlash() + relPath).resolve(),
                     pathlib.Path(fPathType.value.getAbsoluteFilePath()).resolve())
    self.assertFalse("\\" in relPath)

  def test_getRelativeDirPathToDirectoryEndingWithSlash_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(utDir.PYTHON_GENERATOR_UNIT_TESTS, utFile.FOR_TEST_TEXTFILE3)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(utFile.FOR_TEST_TEXTFILE3, utDir.PYTHON_GENERATOR_UNIT_TESTS)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(utFile.FOR_TEST_TEXTFILE1,
                                                        utFile.FOR_TEST_NON_EXISTING_TEXTFILE1)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash(utDir.GIT_REPOSITORY,
                                                         "D:/Programming puzzle pieces/webPage")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectoryEndingWithSlash("D:/Programming puzzle pieces/" +
                                                            config.PATH_FROM_REPO_TO_PY_GENERATOR,
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
    self.assertRelativeDirPathToDirectory(utDir.GIT_REPOSITORY, utDir.GIT_REPOSITORY)
    self.assertRelativeDirPathToDirectory(utDir.GIT_REPOSITORY, utDir.PYTHON_MAIN_GENERATOR)
    self.assertRelativeDirPathToDirectory(utDir.INDEX_HTML_LOCATION, utDir.GIT_REPOSITORY)

  def assertRelativeDirPathToDirectory(self, dirPath1, dirPath2):
    relPath = path.getRelativeDirPathToDirectoryEndingWithSlash(dirPath1, dirPath2)
    self.assertTrue(len(relPath) > 0)
    self.assertEqual(pathlib.Path(dirPath2.value.getAbsoluteDirPathEndingWithSlash() + relPath).resolve(),
                     pathlib.Path(dirPath1.value.getAbsoluteDirPathEndingWithSlash()).resolve())
    self.assertFalse("\\" in relPath)
    self.assertTrue(relPath[-1] == "/")

  def test_getRelativeFilePathToIndexHtml_nonSense(self):
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

  # TODO implement test case
  def test_getRelativeFilePathToIndexHtml_examples(self):
    indexHtmlLocationAbsPath = path.getAbsoluteDirPathEndingWithSlash(utDir.INDEX_HTML_LOCATION)

  def assertRelFilePathToIndexHtml(self, indexHtmlLocationAbsPath, fileType):
    fileRelPathToIndexHtml = path.getRelativeFilePathToIndexHtml(fileType)
    self.assertTrue(fileRelPathToIndexHtml.endswith(fileType.value.getFileName()))
    self.assertEqual(pathlib.Path(indexHtmlLocationAbsPath + fileRelPathToIndexHtml).resolve(),
                     pathlib.Path(fileType.value.getAbsoluteFilePath()).resolve())

  def test_getRelativeDirPathToIndexHtmlEndingWithSlash_nonSense(self):
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
    indexHtmlLocationAbsPath = path.getAbsoluteDirPathEndingWithSlash(utDir.INDEX_HTML_LOCATION)
    self.assertRelDirPathToIndexHtmlLocation(indexHtmlLocationAbsPath, utDir.GIT_REPOSITORY)
    self.assertRelDirPathToIndexHtmlLocation(indexHtmlLocationAbsPath, utDir.PYTHON_GENERATOR_UNIT_TESTS)
    self.assertRelDirPathToIndexHtmlLocation(indexHtmlLocationAbsPath, utDir.PYTHON_MAIN_GENERATOR)

  def assertRelDirPathToIndexHtmlLocation(self, indexHtmlLocationAbsPath, directoryPathType):
    relDirPath = path.getRelativeDirPathToIndexHtmlEndingWithSlash(directoryPathType)
    self.assertTrue(len(relDirPath) > 0)
    self.assertTrue(relDirPath[-1] == "/")
    self.assertEqual(pathlib.Path(indexHtmlLocationAbsPath + relDirPath).resolve(),
                     pathlib.Path(directoryPathType.value.getAbsoluteDirPathEndingWithSlash()).resolve())
