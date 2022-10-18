import os

from defTypes import dirPathTypeForProd
from defTypes import possibleDirPathTypes
from defTypes import possibleFilePathTypes

from modules import checks

def getGitRepoAbsolutePathEndingWithSlash():
  return dirPathTypeForProd.DirectoryPathTypeForProd.GIT_REPOSITORY.value.getAbsoluteDirPathEndingWithSlash()

def getFileName(fPathType):
  checks.checkIfAnyType(fPathType, possibleFilePathTypes.filePathTypes)
  return fPathType.value.getFileName()

def getAbsoluteDirPathEndingWithSlash(directoryPathType):
  checks.checkIfAnyType(directoryPathType, possibleDirPathTypes.dirPathTypes)
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
  checks.checkIfAnyType(fPathType, possibleFilePathTypes.filePathTypes)
  return fPathType.value.getAbsoluteFilePath()

def getRelativeFilePathToDirectory(fPathType, directoryPathType):
  checks.checkIfAnyType(fPathType, possibleFilePathTypes.filePathTypes)
  checks.checkIfAnyType(directoryPathType, possibleDirPathTypes.dirPathTypes)
  relPath = os.path.relpath(fPathType.value.getAbsoluteFilePath(),
                            directoryPathType.value.getAbsoluteDirPathEndingWithSlash())
  relPath = relPath.replace("\\", "/")
  return relPath

def getRelativeDirPathToDirectoryEndingWithSlash(dirPathTypeToResolve, dirPathTypeForComparison):
  checks.checkIfAnyType(dirPathTypeToResolve, possibleDirPathTypes.dirPathTypes)
  checks.checkIfAnyType(dirPathTypeForComparison, possibleDirPathTypes.dirPathTypes)
  relPath = os.path.relpath(dirPathTypeToResolve.value.getAbsoluteDirPathEndingWithSlash(),
                            dirPathTypeForComparison.value.getAbsoluteDirPathEndingWithSlash())
  relPath = relPath.replace("\\", "/")
  if len(relPath) > 0 and relPath[-1] != '/':
    relPath += '/'
  return relPath

def getRelativeDirPathToGitRepoEndingWithSlash(directoryPathType):
  return getRelativeDirPathToDirectoryEndingWithSlash(directoryPathType,
                                                      dirPathTypeForProd.DirectoryPathTypeForProd.GIT_REPOSITORY)

def getRelativeFilePathToGitRepo(fPathType):
  return getRelativeFilePathToDirectory(fPathType, dirPathTypeForProd.DirectoryPathTypeForProd.GIT_REPOSITORY)

def getRelativeFilePathToIndexHtml(fPathType):
  return getRelativeFilePathToDirectory(fPathType, dirPathTypeForProd.DirectoryPathTypeForProd.INDEX_HTML_LOCATION)

def getRelativeDirPathToIndexHtmlEndingWithSlash(directoryPathType):
  return getRelativeDirPathToDirectoryEndingWithSlash(directoryPathType,
                                                      dirPathTypeForProd.DirectoryPathTypeForProd.INDEX_HTML_LOCATION)
