import pathlib

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

def getProjectRootAbsolutePath():
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
