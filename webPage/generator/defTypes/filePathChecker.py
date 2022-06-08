import os

from defTypes import dirPathChecker
from defTypes import dirPathType

from modules import checks
from modules import filerw
from modules import path

class FilePathChecker:
  def __init__(self, directoryPathType, fileName):
    checks.checkIfStringDoesNotContainAnySubstringFromList(fileName, 1, 300, "/")
    checks.checkIfType(directoryPathType, dirPathType.DirectoryRelPathType)
    self.fileName = fileName
    self.absolutePath = directoryPathType.value.getAbsolutePathEndingWithSlash() + fileName
    self.relativePathToGitRepo = directoryPathType.value.getRelativePathEndingWithSlash() + fileName
    checks.checkIfFilePathExists(self.absolutePath)

  def getRelativePathEndingWithSlash(self):
    """The path is relative to the git root repository"""
    return self.relativePathToGitRepo

  def getAbsolutePathEndingWithSlash(self):
    return self.absolutePath

  def getFileName(self):
    return self.fileName

  def getPathRelativeToDirectory(self, directoryPathType):
    checks.checkIfType(directoryPathType, dirPathType.DirectoryRelPathType)
    return os.path.relpath(self.absolutePath, directoryPathType.value.getAbsolutePathEndingWithSlash())
