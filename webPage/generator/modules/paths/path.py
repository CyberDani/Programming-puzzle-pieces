import os
from pathlib import Path

from modules.paths.values import dirPathTypeForProd, possibleDirPathTypes, possibleFilePathTypes
from modules.paths import projectRootDetector as projRoot

from modules.checks import checks


__cwd = None
__cwdDrive = Path(os.getcwd()).drive
__projectRootDrive = None

def getCwd():
  """Ends with a slash."""
  global __cwd
  if __cwd is None:
    __cwd = Path(os.getcwd()).as_posix()
    if __cwd[-1] != "/":
      __cwd += "/"
  return __cwd

def getProjectRootAbsolutePath():
  """The path ends with a slash"""
  found, rootPath = projRoot.getProjectRootPath()
  if not found:
    raise Exception("Could not find project root path")
  return rootPath

def getProjectRootDrive():
  root = getProjectRootAbsolutePath()
  global __projectRootDrive
  if __projectRootDrive is None:
    __projectRootDrive = Path(root).drive
  return __projectRootDrive

def getFileName(fPathType):
  checks.checkIfAnyType(fPathType, possibleFilePathTypes.filePathTypes)
  return fPathType.value.getFileName()

def getAbsoluteDirPath(directoryPathType):
  """The path ends with a slash."""
  checks.checkIfAnyType(directoryPathType, possibleDirPathTypes.dirPathTypes)
  return directoryPathType.value.getAbsoluteDirPathEndingWithSlash()

def getAbsoluteDirParentPath(directoryPathType):
  """The path ends with a slash."""
  absolutePath = getAbsoluteDirPath(directoryPathType)
  absolutePath = absolutePath[:-1]
  idx = absolutePath.rfind("/")
  return absolutePath[:idx + 1]

def getAbsoluteDirParentX2Path(directoryPathType):
  """The path ends with a slash."""
  absoluteParentPath = getAbsoluteDirParentPath(directoryPathType)
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

def getRelativeDirPathToDirectory(dirPathTypeToResolve, dirPathTypeForComparison):
  """The path ends with a slash."""
  checks.checkIfAnyType(dirPathTypeToResolve, possibleDirPathTypes.dirPathTypes)
  checks.checkIfAnyType(dirPathTypeForComparison, possibleDirPathTypes.dirPathTypes)
  relPath = os.path.relpath(dirPathTypeToResolve.value.getAbsoluteDirPathEndingWithSlash(),
                            dirPathTypeForComparison.value.getAbsoluteDirPathEndingWithSlash())
  relPath = relPath.replace("\\", "/")
  if len(relPath) > 0 and relPath[-1] != '/':
    relPath += '/'
  return relPath

def getRelativeDirPathToCurrentWorkingDir(directoryPathType):
  """The path ends with a slash \n
Return values:\n
* found: True | False
* relPath: empty string if not found"""
  checks.checkIfAnyType(directoryPathType, possibleDirPathTypes.dirPathTypes)
  dirPath = directoryPathType.value.getAbsoluteDirPathEndingWithSlash()
  global __cwd, __cwdDrive
  currentDrive = getProjectRootDrive()
  if __cwdDrive != currentDrive:
    return False, ""
  relPath = os.path.relpath(dirPath, __cwd)
  relPath = relPath.replace("\\", "/")
  if len(relPath) > 0 and relPath[-1] != '/':
    relPath += '/'
  return True, relPath

def getRelativeFilePathToCurrentWorkingDir(fPathType):
  """Return values:\n
* found: True | False
* relPath: empty string if not found"""
  checks.checkIfAnyType(fPathType, possibleFilePathTypes.filePathTypes)
  absFilePath = fPathType.value.getAbsoluteFilePath()
  global __cwd, __cwdDrive
  currentDrive = getProjectRootDrive()
  if __cwdDrive != currentDrive:
    return False, ""
  relPath = os.path.relpath(absFilePath, __cwd)
  relPath = relPath.replace("\\", "/")
  return True, relPath

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
