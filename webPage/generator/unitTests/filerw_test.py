import os
import sys
import unittest

sys.path.append('..')

from modules.paths.definitions.dirPathTypeForUT import DirectoryPathTypeForUT as Dir
from modules.paths.definitions.filePathTypeForUT import FilePathTypeForUT as File

from modules import checks
from modules import filerw
from modules import htmlBuilder
from modules.paths import path


class FileReadWriterTests(unittest.TestCase):

  def test_getFileWithWritePerm_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      filerw.getFileWithWritePerm(filePath)
    with self.assertRaises(Exception):
      filerw.getFileWithWritePerm("")
    with self.assertRaises(Exception):
      filerw.getFileWithWritePerm(12)

  def test_getFileWithWritePerm_example(self):
    filerw.deleteFileIfExistsByType(File.FOR_TEST_TEXTFILE1)
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    checks.checkIfFile(file)
    file.write("Hello test!\n")
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 1)
    self.assertEqual(lines[0], "Hello test!")

  def test_createOrOverwriteWithEmptyFileByType_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByType(file)
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByType("")
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByType()
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByType(None)
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByType(23)
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByType(False)
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByType(Dir.HTML_PAGES_MAIN)
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByType(filePath)

  def test_createOrOverwriteWithEmptyFileByType_example_fileNotExists(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    if filerw.fileExistsByPath(filePath):
      os.remove(filePath)
    self.assertFalse(filerw.fileExistsByPath(filePath))
    filerw.createOrOverwriteWithEmptyFileByType(File.FOR_TEST_TEXTFILE1)
    self.assertTrue(filerw.fileExistsByPath(filePath))
    lines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(lines), 0)

  def test_createOrOverwriteWithEmptyFileByType_example_fileExists(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath,
                                                                                 ["first line", "second line", "hi"])
    self.assertTrue(filerw.fileExistsByPath(filePath))
    lines = filerw.getLinesByPath(filePath)
    self.assertEqual(len(lines), 3)
    filerw.createOrOverwriteWithEmptyFileByType(File.FOR_TEST_TEXTFILE1)
    self.assertTrue(filerw.fileExistsByPath(filePath))
    lines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(lines), 0)

  def test_createOrOverwriteWithEmptyFileByPath_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByPath(file)
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByPath("")
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByPath()
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByPath(None)
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByPath(23)
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByPath(False)
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByPath(Dir.HTML_PAGES_MAIN)
    with self.assertRaises(Exception):
      filerw.createOrOverwriteWithEmptyFileByPath(File.FOR_TEST_TEXTFILE1)

  def test_createOrOverwriteWithEmptyFileByPath_example_fileNotExists(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    if filerw.fileExistsByPath(filePath):
      os.remove(filePath)
    self.assertFalse(filerw.fileExistsByPath(filePath))
    filerw.createOrOverwriteWithEmptyFileByPath(filePath)
    self.assertTrue(filerw.fileExistsByPath(filePath))
    lines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(lines), 0)

  def test_createOrOverwriteWithEmptyFileByPath_example_fileExists(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath,
                                                                                 ["first line", "second line", "hi"])
    self.assertTrue(filerw.fileExistsByPath(filePath))
    lines = filerw.getLinesByPath(filePath)
    self.assertEqual(len(lines), 3)
    filerw.createOrOverwriteWithEmptyFileByPath(filePath)
    self.assertTrue(filerw.fileExistsByPath(filePath))
    lines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(lines), 0)

  # TODO rework test case
  #def test_createOrOverwriteWithEmptyFileByPath_relPath(self):
  #  filePath = path.getRelativeFilePathToDirectory(File.FOR_TEST_TEXTFILE1, Dir.PYTHON_MAIN_GENERATOR)
  #  filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath,
  #                                                                               ["first line", "second line", "hi"])
  #  self.assertTrue(filerw.fileExistsByPath(filePath))
  #  lines = filerw.getLinesByPath(filePath)
  #  self.assertEqual(len(lines), 3)
  #  filerw.createOrOverwriteWithEmptyFileByPath(filePath)
  #  self.assertTrue(filerw.fileExistsByPath(filePath))
  #  lines = filerw.getLinesByPathWithEndingNewLine(filePath)
  #  self.assertEqual(len(lines), 0)

  def test_fileExists_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.fileExistsByPath(file)
    with self.assertRaises(Exception):
      filerw.fileExistsByPath("")
    with self.assertRaises(Exception):
      filerw.fileExistsByPath()
    with self.assertRaises(Exception):
      filerw.fileExistsByPath(None)
    with self.assertRaises(Exception):
      filerw.fileExistsByPath(23)
    with self.assertRaises(Exception):
      filerw.fileExistsByPath(False)

  def test_fileExists_example(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.close()
    self.assertTrue(filerw.fileExistsByPath(filePath))
    os.remove(filePath)
    self.assertFalse(filerw.fileExistsByPath(filePath))

  # TODO rework test case
  #def test_fileExists_relPath(self):
  #  filePath = path.getRelativeFilePathToDirectory(File.FOR_TEST_TEXTFILE1, Dir.PYTHON_MAIN_GENERATOR)
  #  file = open(filePath, "w")
  #  file.close()
  #  self.assertTrue(filerw.fileExistsByPath(filePath))
  #  os.remove(filePath)
  #  self.assertFalse(filerw.fileExistsByPath(filePath))

  def test_fileExistsByType_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.fileExistsByType(file)
    with self.assertRaises(Exception):
      filerw.fileExistsByType("")
    with self.assertRaises(Exception):
      filerw.fileExistsByType()
    with self.assertRaises(Exception):
      filerw.fileExistsByType(None)
    with self.assertRaises(Exception):
      filerw.fileExistsByType(23)
    with self.assertRaises(Exception):
      filerw.fileExistsByType(False)
    with self.assertRaises(Exception):
      filerw.fileExistsByType(filePath)

  def test_fileExistsByType_example(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.close()
    self.assertTrue(filerw.fileExistsByType(File.FOR_TEST_TEXTFILE1))
    os.remove(filePath)
    self.assertFalse(filerw.fileExistsByType(File.FOR_TEST_TEXTFILE1))

  def test_directoryExists_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.directoryExistsByPath(file)
    with self.assertRaises(Exception):
      filerw.directoryExistsByPath("")
    with self.assertRaises(Exception):
      filerw.directoryExistsByPath()
    with self.assertRaises(Exception):
      filerw.directoryExistsByPath(None)
    with self.assertRaises(Exception):
      filerw.directoryExistsByPath(23)
    with self.assertRaises(Exception):
      filerw.directoryExistsByPath(False)

  def test_directoryExists_example(self):
    existingDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    nonExistingDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.NON_EXISTING_DIRECTORY)
    self.assertTrue(filerw.directoryExistsByPath(existingDirPath))
    self.assertTrue(filerw.directoryExistsByPath(existingDirPath[:-1]))
    self.assertFalse(filerw.directoryExistsByPath(nonExistingDirPath))
    self.assertFalse(filerw.directoryExistsByPath(nonExistingDirPath[:-1]))

  # TODO rework test case
  #def test_directoryExists_relPath(self):
  #  existingDirPath = path.getRelativeDirPathToDirectoryEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1,
  #                                                                      Dir.PYTHON_MAIN_GENERATOR)
  #  nonExistingDirPath = path.getRelativeDirPathToDirectoryEndingWithSlash(Dir.NON_EXISTING_DIRECTORY,
  #                                                                         Dir.PYTHON_MAIN_GENERATOR)
  #  self.assertTrue(filerw.directoryExistsByPath(existingDirPath))
  #  self.assertTrue(filerw.directoryExistsByPath(existingDirPath[:-1]))
  #  self.assertFalse(filerw.directoryExistsByPath(nonExistingDirPath))
  #  self.assertFalse(filerw.directoryExistsByPath(nonExistingDirPath[:-1]))

  def test_directoryExistsByType_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.directoryExistsByType(file)
    with self.assertRaises(Exception):
      filerw.directoryExistsByType("")
    with self.assertRaises(Exception):
      filerw.directoryExistsByType()
    with self.assertRaises(Exception):
      filerw.directoryExistsByType(None)
    with self.assertRaises(Exception):
      filerw.directoryExistsByType(23)
    with self.assertRaises(Exception):
      filerw.directoryExistsByType(False)
    with self.assertRaises(Exception):
      filerw.directoryExistsByType(filePath)
    with self.assertRaises(Exception):
      filerw.directoryExistsByType(path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1))

  def test_directoryExistsByType_example(self):
    self.assertTrue(filerw.directoryExistsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1))
    self.assertFalse(filerw.directoryExistsByType(Dir.NON_EXISTING_DIRECTORY))

  def test_createDirectoryWithParentsIfNotExists_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByPathIfNotExists(file)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByPathIfNotExists("")
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByPathIfNotExists()
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByPathIfNotExists(None)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByPathIfNotExists(23)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByPathIfNotExists(False)

  def test_createDirectoryWithParentsIfNotExists_existingFolder(self):
    dirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    os.mkdir(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    os.rmdir(dirPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))

  # TODO rewrite test case
  # def test_createDirectoryWithParentsIfNotExists_relPath(self):
    #dirPath = path.getRelativeDirPathToDirectoryEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1,
    #                                                            Dir.PYTHON_MAIN_GENERATOR)
    #os.mkdir(dirPath)
    #self.assertTrue(filerw.directoryExistsByPath(dirPath))
    #filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
    #self.assertTrue(filerw.directoryExistsByPath(dirPath))
    #os.rmdir(dirPath)
    #self.assertFalse(filerw.directoryExistsByPath(dirPath))

  def test_createDirectoryWithParentsIfNotExists_nonExistingFolder(self):
    dirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    os.rmdir(dirPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))

  def test_createDirectoryWithParentsIfNotExists_nonExistingNestedFolder(self):
    dirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2)
    dirParentPath = path.getAbsoluteDirParentPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2)
    if filerw.directoryExistsByPath(dirPath):
      os.rmdir(dirPath)
    if filerw.directoryExistsByPath(dirParentPath):
      os.rmdir(dirParentPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertFalse(filerw.directoryExistsByPath(dirParentPath))
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    os.rmdir(dirPath)
    os.rmdir(dirParentPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertFalse(filerw.directoryExistsByPath(dirParentPath))

  def test_createDirectoryWithParentsByTypeIfNotExists_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    dirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByTypeIfNotExists(file)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByTypeIfNotExists(filePath)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByTypeIfNotExists(dirPath)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByTypeIfNotExists("")
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByTypeIfNotExists()
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByTypeIfNotExists(None)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByTypeIfNotExists(23)
    with self.assertRaises(Exception):
      filerw.createDirectoryWithParentsByTypeIfNotExists(False)

  def test_createDirectoryWithParentsByTypeIfNotExists_existingFolder(self):
    dirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    os.mkdir(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    filerw.createDirectoryWithParentsByTypeIfNotExists(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    os.rmdir(dirPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))

  def test_createDirectoryWithParentsByTypeIfNotExists_nonExistingFolder(self):
    dirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    filerw.createDirectoryWithParentsByTypeIfNotExists(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    os.rmdir(dirPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))

  def test_createDirectoryWithParentsByTypeIfNotExists_nonExistingNestedFolder(self):
    dirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2)
    dirParentPath = path.getAbsoluteDirParentPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2)
    if filerw.directoryExistsByPath(dirPath):
      os.rmdir(dirPath)
    if filerw.directoryExistsByPath(dirParentPath):
      os.rmdir(dirParentPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertFalse(filerw.directoryExistsByPath(dirParentPath))
    filerw.createDirectoryWithParentsByTypeIfNotExists(Dir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    os.rmdir(dirPath)
    os.rmdir(dirParentPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertFalse(filerw.directoryExistsByPath(dirParentPath))

  def test_deleteFileIfExistsByType_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByType(file)
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByType([filePath])
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByType()
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByType(None)
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByType(23)
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByType(False)
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByType(filePath)
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByType(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)

  def test_deleteFileIfExistsByType_fileExists(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.createOrOverwriteWithEmptyFileByPath(filePath)
    self.assertTrue(filerw.fileExistsByPath(filePath))
    filerw.deleteFileIfExistsByType(File.FOR_TEST_TEXTFILE1)
    self.assertFalse(filerw.fileExistsByPath(filePath))

  def test_deleteFileIfExistsByType_fileNotExists(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    if filerw.fileExistsByPath(filePath):
      os.remove(filePath)
    self.assertFalse(filerw.fileExistsByPath(filePath))
    filerw.deleteFileIfExistsByType(File.FOR_TEST_TEXTFILE1)
    self.assertFalse(filerw.fileExistsByPath(filePath))

  def test_deleteFileIfExistsByPath_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByPath(file)
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByPath([filePath])
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByPath()
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByPath(None)
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByPath(23)
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByPath(False)
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByPath(File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      filerw.deleteFileIfExistsByPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)

  def test_deleteFileIfExistsByPath_fileExists(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.createOrOverwriteWithEmptyFileByPath(filePath)
    self.assertTrue(filerw.fileExistsByPath(filePath))
    filerw.deleteFileIfExistsByPath(filePath)
    self.assertFalse(filerw.fileExistsByPath(filePath))

  # TODO rework test case
  #def test_deleteFileIfExistsByPath_fileExists_relPath(self):
  #  filePath = path.getRelativeFilePathToDirectory(File.FOR_TEST_TEXTFILE1, Dir.PYTHON_MAIN_GENERATOR)
  #  filerw.createOrOverwriteWithEmptyFileByPath(filePath)
  #  self.assertTrue(filerw.fileExistsByPath(filePath))
  #  filerw.deleteFileIfExistsByPath(filePath)
  #  self.assertFalse(filerw.fileExistsByPath(filePath))

  def test_deleteFileIfExistsByPath_fileNotExists(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    if filerw.fileExistsByPath(filePath):
      os.remove(filePath)
    self.assertFalse(filerw.fileExistsByPath(filePath))
    filerw.deleteFileIfExistsByPath(filePath)
    self.assertFalse(filerw.fileExistsByPath(filePath))

  def test_deleteNonEmptyDirectoryIfExists_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath)
    dirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByPathIfExists(file)
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByPathIfExists([dirPath])
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByPathIfExists()
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByPathIfExists(None)
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByPathIfExists(23)
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByPathIfExists(False)

  def test_deleteNonEmptyDirectoryIfExists_nonExistingDirectory(self):
    pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2
    dirPath = path.getAbsoluteDirPathEndingWithSlash(pathType)
    dirParentPath = path.getAbsoluteDirParentPathEndingWithSlash(pathType)
    dirParentOfParentPath = path.getAbsoluteDirParentX2PathEndingWithSlash(pathType)
    if filerw.directoryExistsByPath(dirPath):
      os.rmdir(dirPath)
    if filerw.directoryExistsByPath(dirParentPath):
      os.rmdir(dirParentPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertFalse(filerw.directoryExistsByPath(dirParentPath))
    self.assertTrue(filerw.directoryExistsByPath(dirParentOfParentPath))
    filerw.deleteNonEmptyDirectoryByPathIfExists(dirPath)
    self.assertFalse(filerw.directoryExistsByPath(dirParentPath))
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertTrue(filerw.directoryExistsByPath(dirParentOfParentPath))

  def test_deleteNonEmptyDirectoryIfExists_nonExistingDirectory_2(self):
    pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1
    dirPath = path.getAbsoluteDirPathEndingWithSlash(pathType)
    dirParentPath = path.getAbsoluteDirParentPathEndingWithSlash(pathType)
    if filerw.directoryExistsByPath(dirPath):
      os.rmdir(dirPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertTrue(filerw.directoryExistsByPath(dirParentPath))
    filerw.deleteNonEmptyDirectoryByPathIfExists(dirPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertTrue(filerw.directoryExistsByPath(dirParentPath))

  def test_deleteNonEmptyDirectoryIfExists_emptyDirectory(self):
    pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1
    dirPath = path.getAbsoluteDirPathEndingWithSlash(pathType)
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    filerw.deleteNonEmptyDirectoryByPathIfExists(dirPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))

  def test_deleteNonEmptyDirectoryIfExists_directoryWithFiles(self):
    pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1
    dirPath = path.getAbsoluteDirPathEndingWithSlash(pathType)
    filePath1 = dirPath + "test1.txt"
    filePath2 = dirPath + "test2.txt"
    filePath3 = dirPath + "test3.txt"
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    file = open(filePath1, "w")
    file.close()
    file = open(filePath2, "w")
    file.close()
    file = open(filePath3, "w")
    file.close()
    filerw.deleteNonEmptyDirectoryByPathIfExists(dirPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))

  # TODO rework test case
  #def test_deleteNonEmptyDirectoryIfExists_directoryWithFiles_relPath(self):
  #  pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1
  #  dirPath = path.getRelativeDirPathToDirectoryEndingWithSlash(pathType, Dir.PYTHON_MAIN_GENERATOR)
  #  filePath1 = dirPath + "test1.txt"
  #  filePath2 = dirPath + "test2.txt"
  #  filePath3 = dirPath + "test3.txt"
  #  filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
  #  self.assertTrue(filerw.directoryExistsByPath(dirPath))
  #  file = open(filePath1, "w")
  #  file.close()
  #  file = open(filePath2, "w")
  #  file.close()
  #  file = open(filePath3, "w")
  #  file.close()
  #  filerw.deleteNonEmptyDirectoryByPathIfExists(dirPath)
  #  self.assertFalse(filerw.directoryExistsByPath(dirPath))

  def test_deleteNonEmptyDirectoryIfExists_directoryWithFilesAndDirs(self):
    pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2
    dirPath = path.getAbsoluteDirPathEndingWithSlash(pathType)
    dirParentPath = path.getAbsoluteDirParentPathEndingWithSlash(pathType)
    filePath1 = dirParentPath + "test1.txt"
    filePath2 = dirParentPath + "test2.txt"
    filePath3 = dirParentPath + "test3.txt"
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    file = open(filePath1, "w")
    file.close()
    file = open(filePath2, "w")
    file.close()
    file = open(filePath3, "w")
    file.close()
    filerw.deleteNonEmptyDirectoryByPathIfExists(dirParentPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertFalse(filerw.directoryExistsByPath(dirParentPath))

  def test_deleteNonEmptyDirectoryByTypeIfExists_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath)
    dirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByTypeIfExists(file)
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByTypeIfExists([dirPath])
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByTypeIfExists([Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1])
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByTypeIfExists()
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByTypeIfExists(None)
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByTypeIfExists(23)
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByTypeIfExists(False)
    with self.assertRaises(Exception):
      filerw.deleteNonEmptyDirectoryByTypeIfExists(dirPath)

  def test_deleteNonEmptyDirectoryByTypeIfExists_nonExistingDirectory(self):
    pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2
    dirPath = path.getAbsoluteDirPathEndingWithSlash(pathType)
    dirParentPath = path.getAbsoluteDirParentPathEndingWithSlash(pathType)
    dirParentOfParentPath = path.getAbsoluteDirParentX2PathEndingWithSlash(pathType)
    if filerw.directoryExistsByPath(dirPath):
      os.rmdir(dirPath)
    if filerw.directoryExistsByPath(dirParentPath):
      os.rmdir(dirParentPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertFalse(filerw.directoryExistsByPath(dirParentPath))
    self.assertTrue(filerw.directoryExistsByPath(dirParentOfParentPath))
    filerw.deleteNonEmptyDirectoryByTypeIfExists(pathType)
    self.assertFalse(filerw.directoryExistsByPath(dirParentPath))
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertTrue(filerw.directoryExistsByPath(dirParentOfParentPath))

  def test_deleteNonEmptyDirectoryByTypeIfExists_nonExistingDirectory_2(self):
    pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1
    dirPath = path.getAbsoluteDirPathEndingWithSlash(pathType)
    dirParentPath = path.getAbsoluteDirParentPathEndingWithSlash(pathType)
    if filerw.directoryExistsByPath(dirPath):
      os.rmdir(dirPath)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertTrue(filerw.directoryExistsByPath(dirParentPath))
    filerw.deleteNonEmptyDirectoryByTypeIfExists(pathType)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))
    self.assertTrue(filerw.directoryExistsByPath(dirParentPath))

  def test_deleteNonEmptyDirectoryByTypeIfExists_emptyDirectory(self):
    pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1
    dirPath = path.getAbsoluteDirPathEndingWithSlash(pathType)
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    filerw.deleteNonEmptyDirectoryByTypeIfExists(pathType)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))

  def test_deleteNonEmptyDirectoryByTypeIfExists_directoryWithFiles(self):
    pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1
    dirPath = path.getAbsoluteDirPathEndingWithSlash(pathType)
    filePath1 = dirPath + "test1.txt"
    filePath2 = dirPath + "test2.txt"
    filePath3 = dirPath + "test3.txt"
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    file = open(filePath1, "w")
    file.close()
    file = open(filePath2, "w")
    file.close()
    file = open(filePath3, "w")
    file.close()
    filerw.deleteNonEmptyDirectoryByTypeIfExists(pathType)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))

  def test_deleteNonEmptyDirectoryByTypeIfExists_directoryWithFilesAndDirs(self):
    pathType = Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1
    dirPath = path.getAbsoluteDirPathEndingWithSlash(pathType)
    filePath1 = dirPath + "test1.txt"
    filePath2 = dirPath + "test2.txt"
    filePath3 = dirPath + "test3.txt"
    dirPath1 = dirPath + "tempDir1"
    dirPath2 = dirPath + "tempDir2"
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath)
    self.assertTrue(filerw.directoryExistsByPath(dirPath))
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath1)
    filerw.createDirectoryWithParentsByPathIfNotExists(dirPath2)
    self.assertTrue(filerw.directoryExistsByPath(dirPath1))
    self.assertTrue(filerw.directoryExistsByPath(dirPath2))
    file = open(filePath1, "w")
    file.close()
    file = open(filePath2, "w")
    file.close()
    file = open(filePath3, "w")
    file.close()
    filerw.deleteNonEmptyDirectoryByTypeIfExists(pathType)
    self.assertFalse(filerw.directoryExistsByPath(dirPath))

  def test_getLinesByFilePathWithEndingNewLine_1line(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY")
    file.close()
    linesFromFile = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByFilePathWithEndingNewLine_1line_1emptyLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY\n")
    file.close()
    linesFromFile = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY\n")

  def test_getLinesByFilePathWithEndingNewLine_2lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    linesFromFile = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear\n")
    self.assertEqual(linesFromFile[1], "this is the tester\n")

  # TODO rework test case
  #def test_getLinesByFilePathWithEndingNewLine_2lines_relPath(self):
  #  filePath = path.getRelativeFilePathToDirectory(File.FOR_TEST_TEXTFILE1, Dir.PYTHON_MAIN_GENERATOR)
  #  file = open(filePath, "w")
  #  file.write("hello dear\n")
  #  file.write("this is the tester\n")
  #  file.close()
  #  linesFromFile = filerw.getLinesByPathWithEndingNewLine(filePath)
  #  self.assertEqual(len(linesFromFile), 2)
  #  self.assertEqual(linesFromFile[0], "hello dear\n")
  #  self.assertEqual(linesFromFile[1], "this is the tester\n")

  def test_getLinesByTypeWithEndingNewLine_1line(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY")
    file.close()
    linesFromFile = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByTypeWithEndingNewLine_1line_1emptyLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY\n")
    file.close()
    linesFromFile = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY\n")

  def test_getLinesByTypeWithEndingNewLine_2lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    linesFromFile = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear\n")
    self.assertEqual(linesFromFile[1], "this is the tester\n")

  def test_getLinesByFilePath_1line(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY")
    file.close()
    linesFromFile = filerw.getLinesByPath(filePath)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByFilePath_1line_1emptyLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY\n")
    file.close()
    linesFromFile = filerw.getLinesByPath(filePath)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByFilePath_2lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    linesFromFile = filerw.getLinesByPath(filePath)
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear")
    self.assertEqual(linesFromFile[1], "this is the tester")

  # TODO rework test case
  #def test_getLinesByFilePath_2lines_relPath(self):
  #  filePath = path.getRelativeFilePathToDirectory(File.FOR_TEST_TEXTFILE1, Dir.PYTHON_MAIN_GENERATOR)
  #  file = open(filePath, "w")
  #  file.write("hello dear\n")
  #  file.write("this is the tester\n")
  #  file.close()
  #  linesFromFile = filerw.getLinesByPath(filePath)
  #  self.assertEqual(len(linesFromFile), 2)
  #  self.assertEqual(linesFromFile[0], "hello dear")
  #  self.assertEqual(linesFromFile[1], "this is the tester")

  def test_getLinesByType_1line(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY")
    file.close()
    linesFromFile = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByType_1line_1emptyLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY\n")
    file.close()
    linesFromFile = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByType_2lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    linesFromFile = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear")
    self.assertEqual(linesFromFile[1], "this is the tester")

  def test_getLinesWithEndingNewLine_1line(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY")
    file.close()
    file = open(filePath, "r")
    linesFromFile = filerw.getLinesByFileWithEndingNewLine(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesWithEndingNewLine_1line_1emptyLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY\n")
    file.close()
    file = open(filePath, "r")
    linesFromFile = filerw.getLinesByFileWithEndingNewLine(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY\n")

  def test_getLinesWithEndingNewLine_2lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    file = open(filePath, "r")
    linesFromFile = filerw.getLinesByFileWithEndingNewLine(file)
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear\n")
    self.assertEqual(linesFromFile[1], "this is the tester\n")

  def test_getLines_1line(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY")
    file.close()
    file = open(filePath, "r")
    linesFromFile = filerw.getLinesByFile(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLines_1line_1emptyLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("HEY\n")
    file.close()
    file = open(filePath, "r")
    linesFromFile = filerw.getLinesByFile(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLines_2lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    file = open(filePath, "r")
    linesFromFile = filerw.getLinesByFile(file)
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear")
    self.assertEqual(linesFromFile[1], "this is the tester")

  def test_writeLinesPrefixedToFile_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(file, "prefix", "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(file, "prefix", None)
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(file, 1, ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(file, ["prefix"], ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(filePath, "prefix", ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFile(None, "prefix", ["asd"])

  def test_writeLinesPrefixedToFile_emptyList(self):
    readLines = self.helper_writeLinesPrefixedToFile("== prefix ==", [])
    self.assertEqual(len(readLines), 0)

  def test_writeLinesPrefixedToFile_oneEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFile("== prefix ==", [""])
    self.assertEqual(len(readLines), 1)
    # empty line
    self.assertEqual(readLines[0], "")

  def test_writeLinesPrefixedToFile_twoEmptyStrings(self):
    readLines = self.helper_writeLinesPrefixedToFile("== prefix ==", ["", ""])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFile_oneNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFile("[-]", ["\n"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "")

  def test_writeLinesPrefixedToFile_twoNewLines(self):
    readLines = self.helper_writeLinesPrefixedToFile("-=-", ["\n", "\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFile_NewLineAndEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFile("line: ", ["\n", ""])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFile_emptyStringAndNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFile("text: ", ["", "\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFile_oneString(self):
    readLines = self.helper_writeLinesPrefixedToFile("Greetings: ", ["hey"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "Greetings: hey")

  def test_writeLinesPrefixedToFile_twoStrings(self):
    readLines = self.helper_writeLinesPrefixedToFile("[text] ", ["hey", "Joe"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "[text] hey")
    self.assertEqual(readLines[1], "[text] Joe")

  def test_writeLinesPrefixedToFile_threeStrings(self):
    readLines = self.helper_writeLinesPrefixedToFile("", ["hey", "magnificent", "Joe"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "hey")
    self.assertEqual(readLines[1], "magnificent")
    self.assertEqual(readLines[2], "Joe")

  def test_writeLinesPrefixedToFile_oneStringEndingWithNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFile(".", ["hey\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], ".hey")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFile_twoStringsEndingWithNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFile("# ", ["hey\n", "Joe\n"])
    self.assertEqual(len(readLines), 4)
    self.assertEqual(readLines[0], "# hey")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "# Joe")
    self.assertEqual(readLines[3], "")

  def test_writeLinesPrefixedToFile_stringsAndNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFile(">", ["hey\n", "Joe\n", "\n"])
    self.assertEqual(len(readLines), 5)
    self.assertEqual(readLines[0], ">hey")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], ">Joe")
    self.assertEqual(readLines[3], "")
    self.assertEqual(readLines[4], "")

  def test_writeLinesPrefixedToFile_stringsAndNewLineAndEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFile("\t\t", ["hey\n", "Joe\n", "\n", ""])
    self.assertEqual(len(readLines), 6)
    self.assertEqual(readLines[0], "\t\they")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "\t\tJoe")
    self.assertEqual(readLines[3], "")
    self.assertEqual(readLines[4], "")
    self.assertEqual(readLines[5], "")

  def helper_writeLinesPrefixedToFile(self, prefix, lines):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesPrefixedToFile(file, prefix, lines)
    file.close()
    return filerw.getLinesByPath(filePath)

  def test_writeLinesPrefixedToFileThenAppendNewLine_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(file, "prefix", "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(file, "prefix", None)
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(file, 1, ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(file, ["prefix"], ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(filePath, "prefix", ["asd"])
    with self.assertRaises(Exception):
      filerw.writeLinesPrefixedToFileThenAppendNewLine(None, "prefix", ["asd"])

  def test_writeLinesPrefixedToFileThenAppendNewLine_emptyList(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("== prefix ==", [])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "")  # empty line

  def test_writeLinesPrefixedToFileThenAppendNewLine_oneEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("== prefix ==", [""])
    self.assertEqual(len(readLines), 2)
    # empty lines
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_twoEmptyStrings(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("== prefix ==", ["", ""])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_oneNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("[-]", ["\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_twoNewLines(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("-=-", ["\n", "\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_NewLineAndEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("line: ", ["\n", ""])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_emptyStringAndNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("text: ", ["", "\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_oneString(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("Greetings: ", ["hey"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "Greetings: hey")
    self.assertEqual(readLines[1], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_twoStrings(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("[text] ", ["hey", "Joe"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "[text] hey")
    self.assertEqual(readLines[1], "[text] Joe")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_threeStrings(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("", ["hey", "magnificent", "Joe"])
    self.assertEqual(len(readLines), 4)
    self.assertEqual(readLines[0], "hey")
    self.assertEqual(readLines[1], "magnificent")
    self.assertEqual(readLines[2], "Joe")
    self.assertEqual(readLines[3], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_oneStringEndingWithNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine(".", ["hey\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], ".hey")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_twoStringsEndingWithNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("# ", ["hey\n", "Joe\n"])
    self.assertEqual(len(readLines), 5)
    self.assertEqual(readLines[0], "# hey")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "# Joe")
    self.assertEqual(readLines[3], "")
    self.assertEqual(readLines[4], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_stringsAndNewLine(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine(">", ["hey\n", "Joe\n", "\n"])
    self.assertEqual(len(readLines), 6)
    self.assertEqual(readLines[0], ">hey")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], ">Joe")
    self.assertEqual(readLines[3], "")
    self.assertEqual(readLines[4], "")
    self.assertEqual(readLines[5], "")

  def test_writeLinesPrefixedToFileThenAppendNewLine_stringsAndNewLineAndEmptyString(self):
    readLines = self.helper_writeLinesPrefixedToFileThenAppendNewLine("\t\t", ["hey\n", "Joe\n", "\n", ""])
    self.assertEqual(len(readLines), 7)
    self.assertEqual(readLines[0], "\t\they")
    self.assertEqual(readLines[1], "")
    self.assertEqual(readLines[2], "\t\tJoe")
    self.assertEqual(readLines[3], "")
    self.assertEqual(readLines[4], "")
    self.assertEqual(readLines[5], "")
    self.assertEqual(readLines[6], "")

  def helper_writeLinesPrefixedToFileThenAppendNewLine(self, prefix, lines):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesPrefixedToFileThenAppendNewLine(file, prefix, lines)
    file.close()
    return filerw.getLinesByPath(filePath)

  def test_writeStringsPrefixedToFileThenAppendNewLine_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, "prefix", "asd")
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, "prefix", None)
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, 1, ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, ["prefix"], ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(filePath, "prefix", ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(None, "prefix", ["asd"])

  def test_writeStringsPrefixedToFileThenAppendNewLine_emptyList(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(1, [])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_oneEmptyString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(2, [""])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_twoEmptyStrings(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["", ""])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_oneNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_twoNewLines(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(5, ["\n", "\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_NewLineAndEmptyString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["\n", ""])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_emptyStringAndNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["", "\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_oneString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(2, ["hey"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\t\they\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_twoStrings(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(1, ["hey", "Joe"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\they\tJoe\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_threeStrings(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(1, ["hey", "magnificent", "Joe"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\they\tmagnificent\tJoe\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_oneStringEndingWithNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["hey\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "\t\t\they\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_twoStringsEndingWithNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(4, ["hey\n", "Joe\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\t\t\t\they\n")
    self.assertEqual(readLines[1], "\t\t\t\tJoe\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_stringsAndNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(4, ["hey\n", "Joe\n", "\n"])
    self.assertEqual(len(readLines), 4)
    self.assertEqual(readLines[0], "\t\t\t\they\n")
    self.assertEqual(readLines[1], "\t\t\t\tJoe\n")
    self.assertEqual(readLines[2], "\n")
    self.assertEqual(readLines[3], "\n")

  def test_writeStringsPrefixedToFileThenAppendNewLine_stringsAndNewLineAndEmptyString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(4, ["hey\n", "Joe\n", "\n", ""])
    self.assertEqual(len(readLines), 5)
    self.assertEqual(readLines[0], "\t\t\t\they\n")
    self.assertEqual(readLines[1], "\t\t\t\tJoe\n")
    self.assertEqual(readLines[2], "\n")
    self.assertEqual(readLines[3], "\n")
    self.assertEqual(readLines[4], "\n")

  def helper_writeStringsIndentedToFileThenAppendNewLine(self, indent, lines):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    tabs = htmlBuilder.getEscapedTabs(indent)
    filerw.writeStringsPrefixedToFileThenAppendNewLine(file, tabs, lines)
    file.close()
    return filerw.getLinesByPathWithEndingNewLine(filePath)

  def test_writeLinesToFileThenAppendNewLine_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingFileThenAppendNewLine(file, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingFileThenAppendNewLine(file, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingFileThenAppendNewLine(file, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingFileThenAppendNewLine(filePath, ["firstLine"])

  def test_writeLinesToFileThenAppendNewLine_noLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, [])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFileThenAppendNewLine_emptyLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, [""])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  def test_writeLinesToFileThenAppendNewLine_1line(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["this is me"])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToFileThenAppendNewLine_1lineEndingWithNewline(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["this is me\n"])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeLinesToFileThenAppendNewLine_2lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["this is me:", "\tJohn Doe, VIP executor"])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")

  def test_writeLinesToFileThenAppendNewLine_3lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2], "tel: 0875432123\n")

  def test_writeLinesToFileByFilePathThenAppendNewLine_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(file, ["firstLine"])

  def test_writeLinesToFileByFilePathThenAppendNewLine_emptyList(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath, [])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFileByFilePathThenAppendNewLine_emptyLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath, [""])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  def test_writeLinesToFileByFilePathThenAppendNewLine_emptyLine_afterSomethingElse(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath,
                                                                                 ["first", "second", "third", "fourth"])
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath, [""])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  # TODO rework test case
  #def test_writeLinesToFileByFilePathThenAppendNewLine_emptyLine_relPath(self):
  #  filePath = path.getRelativeFilePathToDirectory(File.FOR_TEST_TEXTFILE1, Dir.PYTHON_MAIN_GENERATOR)
  #  filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath,
  #                                                                               ["first", "second", "third", "fourth"])
  #  filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath, [""])
  #  readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
  #  self.assertEqual(len(readLines), 1)
  #  self.assertEqual(readLines[0], "\n")

  def test_writeLinesToFileByFilePathThenAppendNewLine_1line(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath, ["this is me"])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToFileByFilePathThenAppendNewLine_1lineEndingWithNewline(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath, ["this is me\n"])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeLinesToFileByFilePathThenAppendNewLine_2lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath,
                                                                           ["this is me:", "\tJohn Doe, VIP executor"])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")

  def test_wwriteLinesToFileByFilePathThenAppendNewLine_3lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath,
                                                         ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2], "tel: 0875432123\n")

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(filePath, ["firstLine"])
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(file, ["firstLine"])

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose_emptyList(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1, [])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose_emptyLine(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1, [""])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose_emptyLine_afterSomethingElse(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1,
                                                                                 ["first", "second", "third", "fourth"])
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1, [""])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose_1line(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1, ["this is me"])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose_1lineEndingWithNewline(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1,
                                                                                 ["this is me\n"])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose_2lines(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1,
                                                                           ["this is me:", "\tJohn Doe, VIP executor"])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose_3lines(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE1,
                                                         ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2], "tel: 0875432123\n")

  def test_writeLinesToFile_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToFile(file, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToFile(file, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToFile(file, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToFile(filePath, ["firstLine"])

  def test_writeLinesToFile_noLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToFile(file, [])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFile_emptyLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToFile(file, [""])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFile_1line(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToFile(file, ["this is me"])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me")

  def test_writeLinesToFile_1lineEndingWithNewline(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToFile(file, ["this is me\n"])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToFile_2lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToFile(file, ["this is me:", "\tJohn Doe, VIP executor"])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor")

  def test_writeLinesToFile_3lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToFile(file, ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    file.close()
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2], "tel: 0875432123")

  def test_writeLinesToFileByFilePath_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(file, ["firstLine"])

  def test_writeLinesToFileByFilePath_noLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, [])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFileByFilePath_noLine_afterSomeLines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["hey", "little", "man"])
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, [])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFileByFilePath_emptyLine(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, [""])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFileByFilePath_1line(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["this is me"])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me")

  def test_writeLinesToFileByFilePath_1lineEndingWithNewline(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["this is me\n"])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToFileByFilePath_2lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath,
                                                                ["this is me:", "\tJohn Doe, VIP executor"])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor")

  def test_writeLinesToFileByFilePath_3lines(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath,
                                                        ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2], "tel: 0875432123")

  # TODO rework test case
  #def test_writeLinesToFileByFilePath_3lines_relPath(self):
    #filePath = path.getRelativeFilePathToDirectory(File.FOR_TEST_TEXTFILE1, Dir.PYTHON_MAIN_GENERATOR)
    #filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath,
    #                                                    ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    #readLines = filerw.getLinesByPathWithEndingNewLine(filePath)
    #self.assertEqual(len(readLines), 3)
    #self.assertEqual(readLines[0], "this is me:\n")
    #self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    #self.assertEqual(readLines[2], "tel: 0875432123")

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeAndClose_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(filePath, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(filePath, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(filePath, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(filePath, ["firstLine"])
    with self.assertRaises(Exception):
      filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(file, ["firstLine"])

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeAndClose_noLine(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1, [])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeAndClose_noLine_afterSomeLines(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1, ["hey", "little", "man"])
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1, [])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeAndClose_emptyLine(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1, [""])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeAndClose_1line(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1, ["this is me"])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me")

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeAndClose_1lineEndingWithNewline(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1, ["this is me\n"])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeAndClose_2lines(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1,
                                                                ["this is me:", "\tJohn Doe, VIP executor"])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor")

  def test_writeLinesToExistingOrNewlyCreatedFileByTypeAndClose_3lines(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(File.FOR_TEST_TEXTFILE1,
                                                        ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "this is me:\n")
    self.assertEqual(readLines[1], "\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2], "tel: 0875432123")

  def test_rTrimNewLines_nonSense(self):
    with self.assertRaises(Exception):
      filerw.rTrimNewLines()
    with self.assertRaises(Exception):
      filerw.rTrimNewLines("hello")
    with self.assertRaises(Exception):
      filerw.rTrimNewLines(None)
    with self.assertRaises(Exception):
      filerw.rTrimNewLines("hey\n")
    with self.assertRaises(Exception):
      filerw.rTrimNewLines(False)
    with self.assertRaises(Exception):
      filerw.rTrimNewLines(["one", None, "three"])

  def test_rTrimNewLines_emptyList(self):
    result = filerw.rTrimNewLines([])
    self.assertEqual(len(result), 0)

  def test_rTrimNewLines_oneElement(self):
    result = filerw.rTrimNewLines(["Hello!"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "Hello!")
    result = filerw.rTrimNewLines(["\n\tHello!"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "\n\tHello!")
    result = filerw.rTrimNewLines(["\n\tHello!\n"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "\n\tHello!")
    result = filerw.rTrimNewLines(["Hello\n\n"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "Hello")
    result = filerw.rTrimNewLines(["Hello\n\n\n\n\n\n\n"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "Hello")

  def test_rTrimNewLines_twoElements(self):
    result = filerw.rTrimNewLines(["Hello", "hey\n"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "hey")
    result = filerw.rTrimNewLines(["hey\n", "Hello\n"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[1], "Hello")
    self.assertEqual(result[0], "hey")
    result = filerw.rTrimNewLines(["Hello", "hey"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "hey")
    result = filerw.rTrimNewLines(["Hello", "\n\n"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "")

  def test_rTrimNewLines_threeElements(self):
    result = filerw.rTrimNewLines(["Hello\n", "hey", "hi\n\n"])
    self.assertEqual(len(result), 3)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "hey")
    self.assertEqual(result[2], "hi")

  def test_moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory_nonSense(self):
    dirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP,
                                                                        File.FOR_TEST_TEXTFILE3)
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP,
                                                                          Dir.HTML_BACKUP)
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(File.FOR_TEST_TEXTFILE2,
                                                                          File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory("Readme.md",
                                                                        Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP)
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(File.HTML_INCLUDE_TOPNAV, dirPath)
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(dirPath, "Readme.md")
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory("Readme.md", dirPath)
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(None, None)
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(12, 32)
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(["Readme.md"], False)
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(23, [dirPath])
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory([], [])
    with self.assertRaises(Exception):
      filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory("", "")

  def test_moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory_example1(self):
    testFilePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    fileName = path.getFileName(File.FOR_TEST_TEXTFILE1)
    destTempDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(testFilePath, ["hello", "world", "smile"])
    self.assertTrue(filerw.fileExistsByPath(testFilePath))
    self.assertTrue(filerw.directoryExistsByPath(destTempDirPath))
    expectedDestFilePath = destTempDirPath + fileName
    self.assertFalse(filerw.fileExistsByPath(expectedDestFilePath))
    filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(File.FOR_TEST_TEXTFILE1,
                                                                      Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    self.assertFalse(filerw.fileExistsByPath(testFilePath))
    self.assertTrue(filerw.fileExistsByPath(expectedDestFilePath))
    lines = filerw.getLinesByPath(expectedDestFilePath)
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "hello")
    self.assertEqual(lines[1], "world")
    self.assertEqual(lines[2], "smile")

  def test_moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory_example2(self):
    testFilePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    fileName = path.getFileName(File.FOR_TEST_TEXTFILE2)
    destTempDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(testFilePath,
                                                        ["this is me:", "\tJohn Doe, VIP executor", "tel: 0875432123"])
    self.assertTrue(filerw.fileExistsByPath(testFilePath))
    self.assertTrue(filerw.directoryExistsByPath(destTempDirPath))
    expectedDestFilePath = destTempDirPath + fileName
    if filerw.fileExistsByPath(expectedDestFilePath):
      os.remove(expectedDestFilePath)
    self.assertFalse(filerw.fileExistsByPath(expectedDestFilePath))
    filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(File.FOR_TEST_TEXTFILE2,
                                                                      Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    self.assertFalse(filerw.fileExistsByPath(testFilePath))
    self.assertTrue(filerw.fileExistsByPath(expectedDestFilePath))
    lines = filerw.getLinesByPath(expectedDestFilePath)
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "this is me:")
    self.assertEqual(lines[1], "\tJohn Doe, VIP executor")
    self.assertEqual(lines[2], "tel: 0875432123")

  def test_moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory_srcFileNotExists(self):
    testFilePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE3)
    fileName = path.getFileName(File.FOR_TEST_TEXTFILE3)
    destTempDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    if filerw.fileExistsByPath(testFilePath):
      os.remove(testFilePath)
    self.assertFalse(filerw.fileExistsByPath(testFilePath))
    self.assertTrue(filerw.directoryExistsByPath(destTempDirPath))
    expectedDestFilePath = destTempDirPath + fileName
    if filerw.fileExistsByPath(expectedDestFilePath):
      os.remove(expectedDestFilePath)
    self.assertFalse(filerw.fileExistsByPath(expectedDestFilePath))
    filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(File.FOR_TEST_TEXTFILE2,
                                                                      Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    self.assertTrue(filerw.directoryExistsByPath(destTempDirPath))
    self.assertFalse(filerw.fileExistsByPath(testFilePath))
    self.assertFalse(filerw.fileExistsByPath(expectedDestFilePath))

  def test_moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory_destDirNotExists(self):
    testFilePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE3)
    fileName = path.getFileName(File.FOR_TEST_TEXTFILE3)
    destTempDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(testFilePath, ["hello", "world", "smile"])
    filerw.deleteNonEmptyDirectoryByPathIfExists(destTempDirPath)
    self.assertFalse(filerw.directoryExistsByPath(destTempDirPath))
    self.assertTrue(filerw.fileExistsByPath(testFilePath))
    expectedDestFilePath = destTempDirPath + fileName
    if filerw.fileExistsByPath(expectedDestFilePath):
      os.remove(expectedDestFilePath)
    self.assertFalse(filerw.fileExistsByPath(expectedDestFilePath))
    filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(File.FOR_TEST_TEXTFILE3,
                                                                      Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    self.assertTrue(filerw.directoryExistsByPath(destTempDirPath))
    self.assertFalse(filerw.fileExistsByPath(testFilePath))
    self.assertTrue(filerw.fileExistsByPath(expectedDestFilePath))
    lines = filerw.getLinesByPath(expectedDestFilePath)
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "hello")
    self.assertEqual(lines[1], "world")
    self.assertEqual(lines[2], "smile")

  def test_moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory_srcAndDestDirNotExists(self):
    testFilePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE3)
    fileName = path.getFileName(File.FOR_TEST_TEXTFILE3)
    destTempDirPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    if filerw.fileExistsByPath(testFilePath):
      os.remove(testFilePath)
    filerw.deleteNonEmptyDirectoryByPathIfExists(destTempDirPath)
    self.assertFalse(filerw.directoryExistsByPath(destTempDirPath))
    self.assertFalse(filerw.fileExistsByPath(testFilePath))
    expectedDestFilePath = destTempDirPath + fileName
    if filerw.fileExistsByPath(expectedDestFilePath):
      os.remove(expectedDestFilePath)
    self.assertFalse(filerw.fileExistsByPath(expectedDestFilePath))
    filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(File.FOR_TEST_TEXTFILE3,
                                                                      Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertFalse(filerw.directoryExistsByPath(destTempDirPath))
    self.assertFalse(filerw.fileExistsByPath(testFilePath))
    self.assertFalse(filerw.fileExistsByPath(expectedDestFilePath))
