import pathlib

from defTypes.dirPathCheckerActionType import DirPathCheckerActionType as dirAction

from modules import checks

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

class DirectoryPathChecker:

  gitRepoAbsolutePath = getGitRepoAbsolutePathEndingWithSlash()

  def __init__(self, dirPathRelativeToGitRepo, filesToCheck, actionType = dirAction.ENSURE_PATH_AND_FILES_EXIST):
    """The associated path must be relative to the git root repository"""
    checks.checkIfString(dirPathRelativeToGitRepo, 0, 300)
    if actionType == dirAction.ENSURE_PATH_AND_FILES_EXIST:
      checks.checkIfNonEmptyPureListOfStrings(filesToCheck)
    elif actionType == dirAction.ENSURE_PATH_EXISTS_ONLY:
      checks.checkIfEmptyList(filesToCheck)
    if len(dirPathRelativeToGitRepo) > 1 and dirPathRelativeToGitRepo[-1] != "/":
      dirPathRelativeToGitRepo += "/"
    while len(dirPathRelativeToGitRepo) > 1 and dirPathRelativeToGitRepo.startswith("./"):
      dirPathRelativeToGitRepo = dirPathRelativeToGitRepo[2:]
    self.absoluteDirPath = self.gitRepoAbsolutePath + dirPathRelativeToGitRepo
    checks.checkIfDirectoryPathExists(self.absoluteDirPath)
    for file in filesToCheck:
      absPath = self.absoluteDirPath + file
      checks.checkIfFilePathExists(absPath)

  def getAbsoluteDirPathEndingWithSlash(self):
    return self.absoluteDirPath
