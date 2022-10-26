import os
import pathlib
import sys
import unittest

sys.path.append('..')

from modules.paths.definitions.dirPathTypeForUT import DirectoryPathTypeForUT as utDir
from modules.paths.definitions.filePathTypeForUT import FilePathTypeForUT as utFile
from defTypes import pppConfig as config

from modules import filerw
from modules.paths import path


class StringUtilTests(unittest.TestCase):

  def test_getProjectRootAbsolutePath(self):
    gitRepoPath = path.getProjectRootAbsolutePath()
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
      path.getFileName(config.PATH_FROM_ROOT_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getFileName(False)
    with self.assertRaises(Exception):
      path.getFileName(None)
    with self.assertRaises(Exception):
      path.getFileName(0)
    with self.assertRaises(Exception):
      path.getFileName([config.PATH_FROM_ROOT_TO_PY_GENERATOR])
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

  def test_getAbsoluteDirPath_nonSense(self):
    with self.assertRaises(Exception):
      path.getAbsoluteDirPath(".")
    with self.assertRaises(Exception):
      path.getAbsoluteDirPath("")
    with self.assertRaises(Exception):
      path.getAbsoluteDirPath(config.PATH_FROM_ROOT_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPath(False)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPath(None)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPath(0)
    with self.assertRaises(Exception):
      path.getAbsoluteDirPath([config.PATH_FROM_ROOT_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getAbsoluteDirPath([])
    with self.assertRaises(Exception):
      path.getAbsoluteDirPath(utFile.FOR_TEST_TEXTFILE3)

  def test_getAbsoluteDirPathEndingWithSlash_examples(self):
    projRootAbsPath = path.getProjectRootAbsolutePath()
    self.assertAbsoluteDirPath(projRootAbsPath, utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    self.assertAbsoluteDirPath(projRootAbsPath, utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    self.assertAbsoluteDirPath(projRootAbsPath, utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)

  def assertAbsoluteDirPath(self, projRootAbsPath, dirType):
    absPath = path.getAbsoluteDirPath(dirType)
    self.assertTrue(absPath.startswith(projRootAbsPath))
    self.assertEqual(absPath, dirType.value.getAbsoluteDirPathEndingWithSlash())
    self.assertTrue(absPath[-1] == "/")

  def test_getAbsoluteDirParentPath_nonSense(self):
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPath(".")
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPath("")
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPath(config.PATH_FROM_ROOT_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPath(False)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPath(None)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPath(0)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPath([config.PATH_FROM_ROOT_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPath([])
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentPath(utFile.FOR_TEST_TEXTFILE2)

  def test_getAbsoluteDirParentPathEndingWithSlash_examples(self):
    self.assertAbsoluteDirParentPath(utDir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2)
    self.assertAbsoluteDirParentPath(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    self.assertAbsoluteDirParentPath(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertAbsoluteDirParentPath(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    self.assertAbsoluteDirParentPath(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)

  def assertAbsoluteDirParentPath(self, dirType):
    absParentPath = path.getAbsoluteDirParentPath(dirType)
    absPath = path.getAbsoluteDirPath(dirType)
    self.assertTrue(absParentPath[-1] == "/")
    self.assertTrue(absPath[-1] == "/")
    self.assertTrue(absPath.startswith(absParentPath))
    absPathParts = absPath.split("/")
    absParentPathParts = absParentPath.split("/")
    self.assertEqual(len(absPathParts), len(absParentPathParts) + 1)
    self.assertEqual(absParentPathParts[:-1], absPathParts[:-2])

  def test_getAbsoluteDirParentX2Path_nonSense(self):
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2Path(".")
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2Path("")
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2Path(config.PATH_FROM_ROOT_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2Path(False)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2Path(None)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2Path(0)
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2Path([config.PATH_FROM_ROOT_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2Path([])
    with self.assertRaises(Exception):
      path.getAbsoluteDirParentX2Path(utFile.FOR_TEST_TEXTFILE3)

  def test_getAbsoluteDirParentX2PathEndingWithSlash_examples(self):
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1)
    self.assertAbsoluteDirParentX2Path(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2)

  def assertAbsoluteDirParentX2Path(self, dirType):
    absParentPath = path.getAbsoluteDirParentX2Path(dirType)
    absPath = path.getAbsoluteDirPath(dirType)
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
      path.getAbsoluteFilePath(config.PATH_FROM_ROOT_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(False)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(None)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(0)
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath([config.PATH_FROM_ROOT_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath([])
    with self.assertRaises(Exception):
      path.getAbsoluteFilePath(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)

  def test_getAbsoluteFilePath_examples(self):
    gitRepoAbsPath = path.getProjectRootAbsolutePath()
    self.assertAbsoluteFilePath(gitRepoAbsPath, utFile.FOR_TEST_TEXTFILE1)
    self.assertAbsoluteFilePath(gitRepoAbsPath, utFile.FOR_TEST_TEXTFILE2)
    self.assertAbsoluteFilePath(gitRepoAbsPath, utFile.FOR_TEST_TEXTFILE3)
    self.assertAbsoluteFilePath(gitRepoAbsPath, utFile.FOR_TEST_NON_EXISTING_TEXTFILE1)

  def assertAbsoluteFilePath(self, gitRepoAbsPath, fileType):
    fileAbsolutePath = path.getAbsoluteFilePath(fileType)
    self.assertTrue(fileAbsolutePath.startswith(gitRepoAbsPath))
    self.assertTrue(fileAbsolutePath.endswith(fileType.value.getFileName()))
    self.assertEqual(fileAbsolutePath, fileType.value.getAbsoluteFilePath())

  def test_getRelativeDirPathToProjectRoot_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeDirPathToProjectRoot(".")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToProjectRoot("")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToProjectRoot(config.PATH_FROM_ROOT_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToProjectRoot(False)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToProjectRoot(None)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToProjectRoot(0)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToProjectRoot([config.PATH_FROM_ROOT_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getRelativeDirPathToProjectRoot([])
    with self.assertRaises(Exception):
      path.getRelativeDirPathToProjectRoot(utFile.FOR_TEST_TEXTFILE3)

  def test_getRelativeDirPathToProjectRoot_examples(self):
    projRootAbsPath = path.getProjectRootAbsolutePath()
    self.assertRelDirPathToProjectRoot(projRootAbsPath, utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    self.assertRelDirPathToProjectRoot(projRootAbsPath, utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    self.assertRelDirPathToProjectRoot(projRootAbsPath, utDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertRelDirPathToProjectRoot(projRootAbsPath, utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)

  def assertRelDirPathToProjectRoot(self, projRootAbsPath, directoryPathType):
    relDirPath = path.getRelativeDirPathToProjectRoot(directoryPathType)
    self.assertTrue(len(relDirPath) > 0)
    self.assertTrue(relDirPath[-1] == "/")
    self.assertEqual(pathlib.Path(projRootAbsPath + relDirPath).resolve(),
                     pathlib.Path(directoryPathType.value.getAbsoluteDirPathEndingWithSlash()).resolve())

  def test_getRelativeFilePathToProjectRoot_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeFilePathToProjectRoot(".")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToProjectRoot("")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToProjectRoot(config.PATH_FROM_ROOT_TO_PY_GENERATOR)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToProjectRoot(False)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToProjectRoot(None)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToProjectRoot(0)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToProjectRoot([config.PATH_FROM_ROOT_TO_PY_GENERATOR])
    with self.assertRaises(Exception):
      path.getRelativeFilePathToProjectRoot([])
    with self.assertRaises(Exception):
      path.getRelativeFilePathToProjectRoot(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)

  def test_getRelativeFilePathToProjectRoot_examples(self):
    projRootAbsPath = path.getProjectRootAbsolutePath()
    self.assertRelFilePathToProjectRoot(projRootAbsPath, utFile.FOR_TEST_TEXTFILE1)
    self.assertRelFilePathToProjectRoot(projRootAbsPath, utFile.FOR_TEST_TEXTFILE2)
    self.assertRelFilePathToProjectRoot(projRootAbsPath, utFile.FOR_TEST_TEXTFILE3)
    self.assertRelFilePathToProjectRoot(projRootAbsPath, utFile.FOR_TEST_NON_EXISTING_TEXTFILE1)

  def assertRelFilePathToProjectRoot(self, projRootAbsPath, fileType):
    relFilePath = path.getRelativeFilePathToProjectRoot(fileType)
    self.assertTrue(relFilePath.endswith(fileType.value.getFileName()))
    self.assertEqual(pathlib.Path(projRootAbsPath + relFilePath).resolve(),
                     pathlib.Path(fileType.value.getAbsoluteFilePath()).resolve())

  def test_getRelativeFilePathToDirectory_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory(utDir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2,
                                          utFile.FOR_TEST_NON_EXISTING_TEXTFILE1)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory(utFile.FOR_TEST_TEXTFILE1, "D:/Programming puzzle pieces/webPage")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory("D:/Programming puzzle pieces/" + config.PATH_FROM_ROOT_TO_PY_GENERATOR +
                                          "generator.py", utDir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToDirectory("D:/Programming puzzle pieces/" + config.PATH_FROM_ROOT_TO_PY_GENERATOR +
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

  def test_getRelativeFilePathToDirectory_example(self):
    self.assertRelativeFilePathToDirectory(utFile.FOR_TEST_TEXTFILE1, utDir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2)
    self.assertRelativeFilePathToDirectory(utFile.FOR_TEST_TEXTFILE3, utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    self.assertRelativeFilePathToDirectory(utFile.FOR_TEST_NON_EXISTING_TEXTFILE1, utDir.NON_EXISTING_DIRECTORY)
    self.assertRelativeFilePathToDirectory(utFile.FOR_TEST_TEXTFILE2, utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)

  def assertRelativeFilePathToDirectory(self, fPathType, directoryPathType):
    relFilePath = path.getRelativeFilePathToDirectory(fPathType, directoryPathType)
    self.assertTrue(relFilePath.endswith(fPathType.value.getFileName()))
    self.assertEqual(pathlib.Path(directoryPathType.value.getAbsoluteDirPathEndingWithSlash() + relFilePath).resolve(),
                     pathlib.Path(fPathType.value.getAbsoluteFilePath()).resolve())
    self.assertFalse("\\" in relFilePath)

  def test_getRelativeDirPathToDirectory_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectory(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1, utFile.FOR_TEST_TEXTFILE3)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectory(utFile.FOR_TEST_TEXTFILE3, utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectory(utFile.FOR_TEST_TEXTFILE1,
                                         utFile.FOR_TEST_NON_EXISTING_TEXTFILE1)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectory(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1,
                                         "D:/Programming puzzle pieces/webPage")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectory("D:/Programming puzzle pieces/" + config.PATH_FROM_ROOT_TO_PY_GENERATOR,
                                          "D:/Programming puzzle pieces/webPage")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectory(None, None)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectory(True, "directoryName")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectory("directoryName", 12)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectory(123, 0)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToDirectory(["directoryName"], False)

  def test_getRelativeDirPathToDirectoryEndingWithSlash_examples(self):
    self.assertRelativeDirPathToDirectory(utDir.NON_EXISTING_DIRECTORY, utDir.NON_EXISTING_DIRECTORY)
    self.assertRelativeDirPathToDirectory(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1,
                                          utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    self.assertRelativeDirPathToDirectory(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1,
                                          utDir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2)
    self.assertRelativeDirPathToDirectory(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34,
                                          utDir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2)
    self.assertRelativeDirPathToDirectory(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1,
                                          utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    self.assertRelativeDirPathToDirectory(utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2,
                                          utDir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)

  def assertRelativeDirPathToDirectory(self, dirPath1, dirPath2):
    relPath = path.getRelativeDirPathToDirectory(dirPath1, dirPath2)
    self.assertTrue(len(relPath) > 0)
    self.assertEqual(pathlib.Path(dirPath2.value.getAbsoluteDirPathEndingWithSlash() + relPath).resolve(),
                     pathlib.Path(dirPath1.value.getAbsoluteDirPathEndingWithSlash()).resolve())
    self.assertFalse("\\" in relPath)
    self.assertTrue(relPath[-1] == "/")

  def test_getCwd(self):
    cwd = path.getCwd()
    self.assertTrue(len(cwd) > 0)
    self.assertTrue(cwd.endswith("/"))
    self.assertTrue(os.path.isdir(cwd))

  def test_getRelativeDirPathToCurrentWorkingDir_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeDirPathToCurrentWorkingDir(utFile.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      path.getRelativeDirPathToCurrentWorkingDir("file.txt")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToCurrentWorkingDir(".")
    with self.assertRaises(Exception):
      path.getRelativeDirPathToCurrentWorkingDir(None)

  def test_getRelativeDirPathToCurrentWorkingDir_example1(self):
    found, relPath = path.getRelativeDirPathToCurrentWorkingDir(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    if not found:
      return
    self.assertTrue(found)
    cwd = path.getCwd()
    self.assertTrue(os.path.isdir(cwd + relPath))

  def test_getRelativeDirPathToCurrentWorkingDir_example2(self):
    found, relPath = path.getRelativeDirPathToCurrentWorkingDir(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    if not found:
      return
    self.assertTrue(found)
    cwd = path.getCwd()
    self.assertTrue(os.path.isdir(cwd + relPath))

  def test_getRelativeFilePathToCurrentWorkingDir_nonSense(self):
    with self.assertRaises(Exception):
      path.getRelativeFilePathToCurrentWorkingDir(utDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    with self.assertRaises(Exception):
      path.getRelativeFilePathToCurrentWorkingDir("file.txt")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToCurrentWorkingDir(".")
    with self.assertRaises(Exception):
      path.getRelativeFilePathToCurrentWorkingDir(None)

  def test_getRelativeFilePathToCurrentWorkingDir_example1(self):
    found, relPath = path.getRelativeFilePathToCurrentWorkingDir(utFile.FOR_TEST_TEXTFILE1)
    if not found:
      return
    self.assertTrue(found)
    cwd = path.getCwd()
    self.assertTrue(os.path.isfile(cwd + relPath))

  def test_getRelativeFilePathToCurrentWorkingDir_example2(self):
    found, relPath = path.getRelativeFilePathToCurrentWorkingDir(utFile.FOR_TEST_TEXTFILE3)
    if not found:
      return
    self.assertTrue(found)
    cwd = path.getCwd()
    self.assertTrue(os.path.isfile(cwd + relPath))
