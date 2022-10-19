import pathlib

def getGitRepoAbsolutePathEndingWithSlash():
  """Goes back from the current file until it finds the .git folder. \n
Return values: \n
* repoFound: True | False \n
* posixPathToGitRepo: empty string if not found"""
  notFoundResult = False, ""
  filesInGitRepo = [".git/HEAD", ".git/index", ".git/config"]
  currentPath = pathlib.Path(__file__).parent.resolve()
  gitRepoFound = False
  while not gitRepoFound:
    if currentPath.as_posix() == currentPath.parent.as_posix():
      return notFoundResult
    gitRepo = True
    for file in filesInGitRepo:
      if not (currentPath / file).is_file():
        gitRepo = False
        break
    if gitRepo:
      currentPath = currentPath.as_posix()
      if currentPath[-1] != '/':
        currentPath += "/"
      return True, currentPath
    currentPath = currentPath.parent
  return notFoundResult

def getProjectRootAbsolutePathEndingWithSlash():
  """Goes back from the current file until it finds the .git folder. \n
Return values: \n
* rootFound: True | False \n
* posixPathToRoot: empty string if not found"""
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
