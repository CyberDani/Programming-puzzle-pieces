from modules import githubApi

import pathlib

# reuse it to reduce extra HTTP requests and computation
__githubBlobOfCurrentFile = None
__projectRootPath = None

def getGithubBlobOfCurrentFileFromDevel():
  """Once it has a value, it will not recalculate it. \n
Return values: \n
* found: True | False \n
* blob: None if not found"""
  notFoundResult = (False, None)
  global __githubBlobOfCurrentFile
  if __githubBlobOfCurrentFile is None:
    currentFileName = pathlib.Path(__file__).name
    found, blobs = githubApi.getBlobsByFileName(githubApi.RepoBranchType.DEVEL, currentFileName)
    if not found or len(blobs) != 1:
      return notFoundResult
    __githubBlobOfCurrentFile = blobs[0]
  return True, __githubBlobOfCurrentFile

def getGitRepoAbsolutePath():
  """Goes back from the current file until it finds the .git folder. \n
Return values: \n
* repoFound: True | False \n
* posixPathToGitRepo: empty string if not found, if found ends with slash"""
  notFoundResult = False, ""
  filesInGitRepo = [".git/HEAD", ".git/index", ".git/config"]
  currentPath = pathlib.Path(__file__).parent.resolve()
  gitRepoFound = False
  while not gitRepoFound:
    if currentPath.as_posix() == currentPath.parent.as_posix():
      return notFoundResult
    gitRepoFound = True
    for file in filesInGitRepo:
      if not (currentPath / file).is_file():
        gitRepoFound = False
        break
    if gitRepoFound:
      currentPath = currentPath.as_posix()
      if currentPath[-1] != '/':
        currentPath += "/"
      return True, currentPath
    currentPath = currentPath.parent
  return notFoundResult

def getProjectRootAbsolutePathByProjFile():
  """Goes back from the current file until it finds the .projRoot folder. \n
Return values: \n
* rootFound: True | False \n
* posixPathToRoot: empty string if not found, if found ends with slash"""
  notFoundResult = False, ""
  currentPath = pathlib.Path(__file__).parent.resolve()
  rootFound = False
  while not rootFound:
    if currentPath.as_posix() == currentPath.parent.as_posix():
      return notFoundResult
    if (currentPath / ".projRoot").is_dir() and (currentPath / ".projRoot/prog_puzzle_pieces.txt").is_file():
      rootFound = True
      break
    currentPath = currentPath.parent
  if not rootFound:
    return notFoundResult
  currentPath = currentPath.as_posix()
  if currentPath[-1] != '/':
    currentPath += "/"
  return True, currentPath

def getRootAbsolutePathBySpecificFileNames():
  """Goes back from the current file until it finds specific file and directory names. \n
Return values: \n
* rootFound: True | False \n
* posixPathToRoot: empty string if not found, if found ends with slash"""
  notFoundResult = False, ""
  filesInRoot = ["libs.txt"]
  directoriesInRoot = ["webPage"]
  currentPath = pathlib.Path(__file__).parent.resolve()
  rootFound = False
  while not rootFound:
    if currentPath.as_posix() == currentPath.parent.as_posix():
      return notFoundResult
    rootFound = True
    for file in filesInRoot:
      if not (currentPath / file).is_file():
        rootFound = False
        break
    if not rootFound:
      currentPath = currentPath.parent
      continue
    for directory in directoriesInRoot:
      if not (currentPath / directory).is_dir():
        rootFound = False
        break
    if rootFound:
      currentPath = currentPath.as_posix()
      if currentPath[-1] != '/':
        currentPath += "/"
      return True, currentPath
    currentPath = currentPath.parent
  return notFoundResult

def getRootAbsolutePathByNumberOfParentsFromGithub():
  """Goes back from the current file as many times as many times the remote file within the github repo says.
Does not check directory names on the way. \n
Return values: \n
* rootFound: True | False \n
* posixPathToRoot: empty string if not found, if found ends with slash"""
  notFoundResult = (False, "")
  found, blob = getGithubBlobOfCurrentFileFromDevel()
  if not found:
    return notFoundResult
  nrOfParents = blob.relPath.count("/")
  currentPath = pathlib.Path(__file__).parent.resolve()
  while nrOfParents > 0:
    if currentPath.as_posix() == currentPath.parent.as_posix():
      return notFoundResult
    nrOfParents -= 1
    currentPath = currentPath.parent
  currentPath = currentPath.as_posix()
  if currentPath[-1] != '/':
    currentPath += "/"
  return True, currentPath

def getRootAbsolutePathByNameOfParentsFromGithub():
  """Goes back from the current file by following the relative path of the remote file from the github repo.
Checks directory names on the way. \n
Return values: \n
* rootFound: True | False \n
* posixPathToRoot: empty string if not found, if found ends with slash"""
  notFoundResult = (False, "")
  found, blob = getGithubBlobOfCurrentFileFromDevel()
  if not found:
    return notFoundResult
  currentPath = pathlib.Path(__file__).resolve()
  githubPathParts = blob.relPath.split("/")
  nrOfParents = blob.relPath.count("/")
  while nrOfParents >= 0:
    if currentPath.as_posix() == currentPath.parent.as_posix():
      return notFoundResult
    if currentPath.name != githubPathParts[nrOfParents]:
      return notFoundResult
    nrOfParents -= 1
    currentPath = currentPath.parent
  currentPath = currentPath.as_posix()
  if currentPath[-1] != '/':
    currentPath += "/"
  return True, currentPath

def collectAllProjectRootPaths():
  """Return values:\n
* nrOfTotalPaths: nr of founds + notFounds
* paths: dictionary of path - nrOfOccurrence"""
  found1, gitRepoPath = getGitRepoAbsolutePath()
  found2, projFilePath = getProjectRootAbsolutePathByProjFile()
  found3, rootBySpecificFileNames = getRootAbsolutePathBySpecificFileNames()
  found4, rootByGithubNrOfParents = getRootAbsolutePathByNumberOfParentsFromGithub()
  found5, rootByGithubNameOfParents = getRootAbsolutePathByNameOfParentsFromGithub()
  nrOfTotalPaths = 5
  paths = {}
  if found1:
    paths[gitRepoPath] = 1
  if found2:
    if projFilePath not in paths:
      paths[projFilePath] = 1
    else:
      paths[projFilePath] += 1
  if found3:
    if rootBySpecificFileNames not in paths:
      paths[rootBySpecificFileNames] = 1
    else:
      paths[rootBySpecificFileNames] += 1
  if found4:
    if rootByGithubNrOfParents not in paths:
      paths[rootByGithubNrOfParents] = 1
    else:
      paths[rootByGithubNrOfParents] += 1
  if found5:
    if rootByGithubNameOfParents not in paths:
      paths[rootByGithubNameOfParents] = 1
    else:
      paths[rootByGithubNameOfParents] += 1
  return nrOfTotalPaths, paths

def getProjectRootPath():
  """Criteria for selecting the most common root path :\n
* at least 2 methods results in that same path
* or other occurrences are less common (no choosing between 30% and 30%)\n
The path ends with a slash.\n
Return values: \n
* found: True | False
* path: empty string if not found"""
  notFoundResult = (False, "")
  global __projectRootPath
  if __projectRootPath is not None:
    return len(__projectRootPath) > 0, __projectRootPath
  nrOfPaths, paths = collectAllProjectRootPaths()
  if not paths:
    __projectRootPath = ""
    return notFoundResult
  maxNrOfOccurrences = 0
  pathWithMaxNrOfOccurrences = ""
  nrOfPathsWithMaxNrOfOccurrences = 0
  for path, nrOfOccurrences in paths.items():
    if nrOfOccurrences == maxNrOfOccurrences:
      nrOfPathsWithMaxNrOfOccurrences += 1
    if nrOfOccurrences > maxNrOfOccurrences:
      maxNrOfOccurrences = nrOfOccurrences
      pathWithMaxNrOfOccurrences = path
      nrOfPathsWithMaxNrOfOccurrences = 1
  if nrOfPathsWithMaxNrOfOccurrences > 1 or maxNrOfOccurrences < 2:
    __projectRootPath = ""
    return notFoundResult
  __projectRootPath = pathWithMaxNrOfOccurrences
  return True, pathWithMaxNrOfOccurrences
