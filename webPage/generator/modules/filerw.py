import os
import pathlib
import shutil

from modules import checks
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
  linesWithNewEndingline = getLinesByFilePathWithEndingNewLine(filePath)
  return rTrimNewLines(linesWithNewEndingline)

def getLines(file):
  linesWithNewEndingline = getLinesWithEndingNewLine(file)
  return rTrimNewLines(linesWithNewEndingline)

###### Deletes ######

def deleteNonEmptyDirectoryIfExists(dirPath):
  if not directoryExists(dirPath):
    return
  shutil.rmtree(dirPath)

###### Writes ######

def createDirectoryWithParentsIfNotExists(dirPath):
  if directoryExists(dirPath):
    return
  pathlib.Path(dirPath).mkdir(parents=True, exist_ok=True)

def writeLinesToFile(file, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  n = len(lines)
  for i in range(n):
    file.write(lines[i])
    if (i < n - 1):
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
    if (line and line != "\n" and line != "\r\n"):
      file.write(prefix + line)
    else:
      file.write("\n")
  file.write("\n")

def writeLinesPrefixedToFileThenAppendNewLine(file, prefix, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  checks.checkIfString(prefix, 0, 300)
  for line in lines:
    if (line and line != "\n" and line != "\r\n"):
      file.write(prefix + line + "\n")
    else:
      file.write("\n")
  file.write("\n")

def writeLinesPrefixedToFile(file, prefix, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  checks.checkIfString(prefix, 0, 300)
  for line in lines:
    if (line and line != "\n" and line != "\r\n"):
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