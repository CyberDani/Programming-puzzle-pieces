import pathlib

def getGitRepoAbsolutePathEndingWithSlash():
  filesInGitRepo = ["README.md", ".gitignore", ".git/HEAD"]
  currentPath = pathlib.Path(__file__).parent.resolve()
  gitRepoFound = False
  while not gitRepoFound:
    if currentPath.as_posix() == currentPath.parent.as_posix():
      raise Exception("Could not found git repository")
    gitRepo = True
    for file in filesInGitRepo:
      if not (currentPath / file).is_file():
        gitRepo = False
        break
    if gitRepo:
      currentPath = currentPath.as_posix()
      if currentPath[-1] != '/':
        currentPath += "/"
      return currentPath
    currentPath = currentPath.parent
  raise Exception("Could not found git repository")
