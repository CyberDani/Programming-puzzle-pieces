import os
import pathlib
import shutil

from defTypes.dirPathType import DirectoryPathType as Dir
from defTypes.filePathType import FilePathType as File

from modules import checks
from modules import path
from modules import stringUtil

# TODO every function should have a byPath + byType alternative

###### Existence ######

def fileExistsByPath(filePath):
  checks.checkIfString(filePath, 2, 300)
  return os.path.isfile(filePath)

def fileExistsByType(filePathType):
  filePathType = path.getAbsoluteFilePath(filePathType)
  return fileExistsByPath(filePathType)

def directoryExistsByPath(dirPath):
  checks.checkIfString(dirPath, 1, 300)
  return os.path.isdir(dirPath)

def directoryExistsByType(dirPath):
  dirPath = path.getAbsoluteDirPathEndingWithSlash(dirPath)
  return directoryExistsByPath(dirPath)

###### Reads ######

def getLinesByPathWithEndingNewLine(filePath):
  checks.checkIfString(filePath, 2, 300)
  f = open(filePath, "r")
  return f.readlines()

def getLinesByTypeWithEndingNewLine(filePathType):
  filePath = path.getAbsoluteFilePath(filePathType)
  return getLinesByPathWithEndingNewLine(filePath)

def getLinesByFileWithEndingNewLine(file):
  checks.checkIfFile(file)
  return file.readlines()

def getLinesByPath(filePath):
  linesWithNewEndingLine = getLinesByPathWithEndingNewLine(filePath)
  return rTrimNewLines(linesWithNewEndingLine)

def getLinesByType(filePathType):
  filePath = path.getAbsoluteFilePath(filePathType)
  return getLinesByPath(filePath)

def getLinesByFile(file):
  linesWithNewEndingLine = getLinesByFileWithEndingNewLine(file)
  return rTrimNewLines(linesWithNewEndingLine)

###### Deletes ######

def deleteNonEmptyDirectoryIfExists(dirPath):
  if not directoryExistsByPath(dirPath):
    return
  shutil.rmtree(dirPath)

def deleteFileIfExistsByPath(filePath):
  if not fileExistsByPath(filePath):
    return
  os.remove(filePath)

def deleteFileIfExistsByType(fileType):
  fileType = path.getAbsoluteFilePath(fileType)
  deleteFileIfExistsByPath(fileType)

###### Move & Copy ######

def moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(filePathType, dirPathType):
  checks.checkIfType(filePathType, File)
  checks.checkIfType(dirPathType, Dir)
  filePath = path.getAbsoluteFilePath(filePathType)
  if not fileExistsByPath(filePath):
    return
  fileName = path.getFileName(filePathType)
  folderPath = path.getAbsoluteDirPathEndingWithSlash(dirPathType)
  createDirectoryWithParentsIfNotExists(folderPath)
  os.replace(filePath, folderPath + fileName)

###### Create ######

def createDirectoryWithParentsIfNotExists(dirPath):
  if directoryExistsByPath(dirPath):
    return
  pathlib.Path(dirPath).mkdir(parents=True, exist_ok=True)

def createOrOverwriteWithEmptyFileByPath(filePath):
  checks.checkIfString(filePath, 1, 300)
  file = open(filePath, "w")
  file.close()

def createOrOverwriteWithEmptyFileByType(fileType):
  filePath = path.getAbsoluteFilePath(fileType)
  file = open(filePath, "w")
  file.close()

###### Writes ######

def writeLinesToFile(file, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  n = len(lines)
  for i in range(n):
    file.write(lines[i])
    if i < n - 1:
      file.write("\n")

def writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, lines):
  checks.checkIfString(filePath, 2, 300)
  file = open(filePath, "w")
  writeLinesToFile(file, lines)
  file.close()

def writeLinesToExistingFileThenAppendNewLine(file, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  for line in lines:
    file.write(line)
    file.write("\n")

def writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(filePath, lines):
  checks.checkIfString(filePath, 2, 300)
  file = open(filePath, "w")
  writeLinesToExistingFileThenAppendNewLine(file, lines)
  file.close()

def writeStringsPrefixedToFileThenAppendNewLine(file, prefix, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  checks.checkIfString(prefix, 0, 300)
  for line in lines:
    if line and line != "\n" and line != "\r\n":
      file.write(prefix + line)
    else:
      file.write("\n")
  file.write("\n")

def writeLinesPrefixedToFileThenAppendNewLine(file, prefix, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  checks.checkIfString(prefix, 0, 300)
  for line in lines:
    if line and line != "\n" and line != "\r\n":
      file.write(prefix + line + "\n")
    else:
      file.write("\n")
  file.write("\n")

def writeLinesPrefixedToFile(file, prefix, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  checks.checkIfString(prefix, 0, 300)
  for line in lines:
    if line and line != "\n" and line != "\r\n":
      file.write(prefix + line + "\n")
    else:
      file.write("\n")

###### Helper functions ######

def rTrimNewLines(stringsArr):
  checks.checkIfPureListOfStrings(stringsArr)
  result = []
  for string in stringsArr:
    result.append(stringUtil.rTrimNewLines(string))
  return result
