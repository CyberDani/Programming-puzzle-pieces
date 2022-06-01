from modules import checks
from modules import filerw
from modules import path

class DirectoryPathChecker:
  def __init__(self, dirPathRelativeToGitRepo, filesToCheck):
    checks.checkIfString(dirPathRelativeToGitRepo, 0, 300)
    checks.checkIfNonEmptyPureListOfStrings(filesToCheck)
    if len(dirPathRelativeToGitRepo) > 1 and dirPathRelativeToGitRepo[-1] != "/":
      dirPathRelativeToGitRepo += "/"
    while len(dirPathRelativeToGitRepo) > 1 and dirPathRelativeToGitRepo.startswith("./"):
      dirPathRelativeToGitRepo = dirPathRelativeToGitRepo[2:]
    self.dirPathRelativeToGitRepo = dirPathRelativeToGitRepo
    self.absoluteDirPath = path.getGitRepoAbsolutePathEndingWithSlash() + dirPathRelativeToGitRepo
    checks.checkIfDirectoryPathExists(self.absoluteDirPath)
    for file in filesToCheck:
      absPath = self.absoluteDirPath + file
      checks.checkIfFilePathExists(absPath)

  def getRelativePathEndingWithSlash(self):
    """The path is relative to the git root repository"""
    return self.dirPathRelativeToGitRepo

  def getAbsolutePathEndingWithSlash(self):
    return self.absoluteDirPath