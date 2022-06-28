import os
import pathlib
import shutil

from defTypes.dirPathType import DirectoryPathType as Dir
from defTypes.filePathType import FilePathType as File

from modules import checks
from modules import path
from modules import stringUtil

###### Reads ######

def fileExists(filePath):
  checks.checkIfString(filePath, 2, 300)
  return os.path.isfile(filePath)

def directoryExists(dirPath):
  checks.checkIfString(dirPath, 1, 300)
  return os.path.isdir(dirPath)

def getLinesByFilePathWithEndingNewLine(filePath):
  checks.checkIfString(filePath, 2, 300)
  f = open(filePath, "r")
  return f.readlines()

def getLinesWithEndingNewLine(file):
  checks.checkIfFile(file)
  return file.readlines()

def getLinesByFilePath(filePath):
  linesWithNewEndingLine = getLinesByFilePathWithEndingNewLine(filePath)
  return rTrimNewLines(linesWithNewEndingLine)

def getLines(file):
  linesWithNewEndingLine = getLinesWithEndingNewLine(file)
  return rTrimNewLines(linesWithNewEndingLine)

###### Deletes ######

def deleteNonEmptyDirectoryIfExists(dirPath):
  if not directoryExists(dirPath):
    return
  shutil.rmtree(dirPath)

###### Move & Copy ######

def moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(filePathType, dirPathType):
  checks.checkIfType(filePathType, File)
  checks.checkIfType(dirPathType, Dir)
  filePath = path.getAbsoluteFilePath(filePathType)
  if not fileExists(filePath):
    return
  fileName = path.getFileName(filePathType)
  folderPath = path.getAbsoluteDirPathEndingWithSlash(dirPathType)
  createDirectoryWithParentsIfNotExists(folderPath)
  os.replace(filePath, folderPath + fileName)

###### Create ######

def createDirectoryWithParentsIfNotExists(dirPath):
  if directoryExists(dirPath):
    return
  pathlib.Path(dirPath).mkdir(parents=True, exist_ok=True)

###### Writes ######

def writeLinesToFile(file, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  n = len(lines)
  for i in range(n):
    file.write(lines[i])
    if i < n - 1:
      file.write("\n")

def writeLinesToFileByFilePathAndCloseFile(filePath, lines):
  checks.checkIfString(filePath, 2, 300)
  file = open(filePath, "w")
  writeLinesToFile(file, lines)
  file.close()

def writeLinesToFileThenAppendNewLine(file, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  for line in lines:
    file.write(line)
    file.write("\n")

def writeLinesToFileByFilePathThenAppendNewLineAndCloseFile(filePath, lines):
  checks.checkIfString(filePath, 2, 300)
  file = open(filePath, "w")
  writeLinesToFileThenAppendNewLine(file, lines)
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
