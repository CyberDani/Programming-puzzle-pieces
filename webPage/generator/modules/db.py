from defTypes import dbBranchType

from modules.checks import checks
from modules import git

# git:master -> MASTER, otherwise DEVEL
def getDbBranchByGitBranch(gitBranch):
  checks.checkIfString(gitBranch, 1, 300)
  if gitBranch == "master":
    return dbBranchType.DbBranchType.MASTER
  return dbBranchType.DbBranchType.DEVEL

# git:master -> MASTER, otherwise DEVEL
def getCurrentDbBranch():
  gitBranch = git.getCurrentBranch()
  return getDbBranchByGitBranch(gitBranch)
