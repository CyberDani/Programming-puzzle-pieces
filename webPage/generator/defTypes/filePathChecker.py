import os

from defTypes import dirPathType

from modules import checks

class FilePathChecker:
  def __init__(self, directoryPathType, fileName):
    checks.checkIfStringDoesNotContainAnySubstringFromList(fileName, 1, 300, "/")
    checks.checkIfType(directoryPathType, dirPathType.DirectoryPathType)
    self.fileName = fileName
    self.absolutePath = directoryPathType.value.getAbsoluteDirPathEndingWithSlash() + fileName
    self.relativePathToGitRepo = directoryPathType.value.getRelativeDirPathToGitRepoEndingWithSlash() + fileName
    checks.checkIfFilePathExists(self.absolutePath)

  def getRelativeFilePathToGitRepo(self):
    return self.relativePathToGitRepo

  def getAbsoluteFilePath(self):
    return self.absolutePath

  def getFileName(self):
    return self.fileName

  def getPathRelativeToDirectory(self, directoryPathType):
    checks.checkIfType(directoryPathType, dirPathType.DirectoryPathType)
    return os.path.relpath(self.absolutePath, directoryPathType.value.getAbsoluteDirPathEndingWithSlash())
