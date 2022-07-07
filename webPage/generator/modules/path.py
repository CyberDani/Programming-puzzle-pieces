import os

from defTypes import dirPathType
from defTypes import filePathType

from modules import checks

def getGitRepoAbsolutePathEndingWithSlash():
  return dirPathType.DirectoryPathType.GIT_REPOSITORY.value.getAbsoluteDirPathEndingWithSlash()

def getFileName(fPathType):
  checks.checkIfType(fPathType, filePathType.FilePathType)
  return fPathType.value.getFileName()

def getAbsoluteDirPathEndingWithSlash(directoryPathType):
  checks.checkIfType(directoryPathType, dirPathType.DirectoryPathType)
  return directoryPathType.value.getAbsoluteDirPathEndingWithSlash()

def getAbsoluteDirParentPathEndingWithSlash(directoryPathType):
  absolutePath = getAbsoluteDirPathEndingWithSlash(directoryPathType)
  absolutePath = absolutePath[:-1]
  idx = absolutePath.rfind("/")
  return absolutePath[:idx + 1]

def getAbsoluteDirParentX2PathEndingWithSlash(directoryPathType):
  absoluteParentPath = getAbsoluteDirParentPathEndingWithSlash(directoryPathType)
  absoluteParentPath = absoluteParentPath[:-1]
  idx = absoluteParentPath.rfind("/")
  return absoluteParentPath[:idx + 1]

def getAbsoluteFilePath(fPathType):
  checks.checkIfType(fPathType, filePathType.FilePathType)
  return fPathType.value.getAbsoluteFilePath()

def getRelativeFilePathToDirectory(fPathType, directoryPathType):
  checks.checkIfType(fPathType, filePathType.FilePathType)
  checks.checkIfType(directoryPathType, dirPathType.DirectoryPathType)
  relPath = os.path.relpath(fPathType.value.getAbsoluteFilePath(),
                            directoryPathType.value.getAbsoluteDirPathEndingWithSlash())
  relPath = relPath.replace("\\", "/")
  return relPath

def getRelativeDirPathToDirectoryEndingWithSlash(dirPathTypeToResolve, dirPathTypeForComparison):
  checks.checkIfType(dirPathTypeToResolve, dirPathType.DirectoryPathType)
  checks.checkIfType(dirPathTypeForComparison, dirPathType.DirectoryPathType)
  relPath = os.path.relpath(dirPathTypeToResolve.value.getAbsoluteDirPathEndingWithSlash(),
                            dirPathTypeForComparison.value.getAbsoluteDirPathEndingWithSlash())
  relPath = relPath.replace("\\", "/")
  if len(relPath) > 0 and relPath[-1] != '/':
    relPath += '/'
  return relPath

def getRelativeDirPathToGitRepoEndingWithSlash(directoryPathType):
  return getRelativeDirPathToDirectoryEndingWithSlash(directoryPathType, dirPathType.DirectoryPathType.GIT_REPOSITORY)

def getRelativeFilePathToGitRepo(fPathType):
  return getRelativeFilePathToDirectory(fPathType, dirPathType.DirectoryPathType.GIT_REPOSITORY)

def getRelativeFilePathToIndexHtml(fPathType):
  return getRelativeFilePathToDirectory(fPathType, dirPathType.DirectoryPathType.INDEX_HTML_LOCATION)

def getRelativeDirPathToIndexHtmlEndingWithSlash(directoryPathType):
  return getRelativeDirPathToDirectoryEndingWithSlash(directoryPathType,
                                                      dirPathType.DirectoryPathType.INDEX_HTML_LOCATION)
