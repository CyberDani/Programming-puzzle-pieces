import os

from defTypes import dirPathType
from defTypes import filePathType

from modules import checks

def getGitRepoAbsolutePathEndingWithSlash():
  return dirPathType.DirectoryPathType.GIT_REPOSITORY.value.getAbsoluteDirPathEndingWithSlash()

def getAbsoluteDirPathEndingWithSlash(directoryPathType):
  checks.checkIfType(directoryPathType, dirPathType.DirectoryPathType)
  return directoryPathType.value.getAbsoluteDirPathEndingWithSlash()

def getAbsoluteFilePath(fPathType):
  checks.checkIfType(fPathType, filePathType.FilePathType)
  return fPathType.value.getAbsoluteFilePath()

def getRelativeDirPathToGitRepoEndingWithSlash(directoryPathType):
  checks.checkIfType(directoryPathType, dirPathType.DirectoryPathType)
  return directoryPathType.value.getRelativeDirPathToGitRepoEndingWithSlash()

def getRelativeFilePathToGitRepo(fPathType):
  checks.checkIfType(fPathType, filePathType.FilePathType)
  return fPathType.value.getRelativeFilePathToGitRepo()

def getRelativeFilePathToDirectory(fPathType, directoryPathType):
  checks.checkIfType(fPathType, filePathType.FilePathType)
  checks.checkIfType(directoryPathType, dirPathType.DirectoryPathType)
  relPath = os.path.relpath(fPathType.value.getAbsoluteFilePath(),
                            directoryPathType.value.getAbsoluteDirPathEndingWithSlash())
  relPath = relPath.replace("\\", "/")
  return relPath
