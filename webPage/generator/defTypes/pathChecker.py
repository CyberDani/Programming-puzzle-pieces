from modules import checks
from modules import filerw
from modules import path

class DirectoryPathChecker:
  def __init__(self, dirPathRelativeToGitRepo, filesToCheck):
    checks.checkIfString(dirPathRelativeToGitRepo, 0, 300)
    checks.checkIfNonEmptyPureListOfStrings(filesToCheck)
    if len(dirPathRelativeToGitRepo) > 1 and dirPathRelativeToGitRepo[-1] != "/":
      dirPathRelativeToGitRepo += "/"
    self.dirPathRelativeToGitRepo = dirPathRelativeToGitRepo
    self.absoluteDirPath = path.getGitRepoAbsolutePathEndingWithSlash() + dirPathRelativeToGitRepo
    checks.checkIfDirectoryPathExists(self.absoluteDirPath)
    for file in filesToCheck:
      absPath = self.absoluteDirPath + file
      checks.checkIfFilePathExists(absPath)

  def getRelativePath(self):
    """The associated path is relative to the git root repository"""
    return self.dirPathRelativeToGitRepo

  def getAbsolutePath(self):
    return self.absoluteDirPath
