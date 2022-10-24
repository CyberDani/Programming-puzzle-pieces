import os
from pathlib import Path

from modules.paths.definitions import dirPathTypeForProd, possibleDirPathTypes, possibleFilePathTypes
from modules.paths import projectRootDetector as projRoot

from modules import checks


currentWorkingDirectory = Path(os.getcwd()).as_posix() + "/"

def getProjectRootAbsolutePath():
  """The path ends with a slash"""
  found, rootPath = projRoot.getProjectRootPath()
  if not found:
    raise Exception("Could not find project root path")
  return rootPath

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

def getRelativeDirPathToProjectRoot(directoryPathType):
  """The path ends with a slash"""
  checks.checkIfAnyType(directoryPathType, possibleDirPathTypes.dirPathTypes)
  dirPath = directoryPathType.value.getAbsoluteDirPathEndingWithSlash()
  projRootPath = getProjectRootAbsolutePath()
  relPath = os.path.relpath(dirPath, projRootPath)
  relPath = relPath.replace("\\", "/")
  if len(relPath) > 0 and relPath[-1] != '/':
    relPath += '/'
  return relPath

def getRelativeFilePathToProjectRoot(fPathType):
  checks.checkIfAnyType(fPathType, possibleFilePathTypes.filePathTypes)
  absFilePath = fPathType.value.getAbsoluteFilePath()
  projRootPath = getProjectRootAbsolutePath()
  relPath = os.path.relpath(absFilePath, projRootPath)
  relPath = relPath.replace("\\", "/")
  return relPath

def getRelativeFilePathToIndexHtml(fPathType):
  return getRelativeFilePathToDirectory(fPathType, dirPathTypeForProd.DirectoryPathTypeForProd.INDEX_HTML_LOCATION)

def getRelativeDirPathToIndexHtmlEndingWithSlash(directoryPathType):
  return getRelativeDirPathToDirectoryEndingWithSlash(directoryPathType,
                                                      dirPathTypeForProd.DirectoryPathTypeForProd.INDEX_HTML_LOCATION)
