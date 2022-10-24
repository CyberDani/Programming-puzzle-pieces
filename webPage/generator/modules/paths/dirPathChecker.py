from modules import checks
from modules.paths import projectRootDetector as projRoot
from modules.paths.dirPathCheckerActionType import DirPathCheckerActionType as dirAction


class DirectoryPathChecker:

  projRootDetected, projRootAbsolutePath = projRoot.getProjectRootPath()

  def __init__(self, dirPathRelativeToGitRepo, filesToCheck, actionType = dirAction.ENSURE_DIR_AND_FILES_EXIST):
    """The associated path must be relative to the git root repository"""
    checks.checkIfStringDoesNotContainAnySubstringFromList(dirPathRelativeToGitRepo, 0, 300, ["\\"])
    if not self.projRootDetected:
      raise Exception("Could not detect the the project root path!")
    if actionType == dirAction.ENSURE_DIR_AND_FILES_EXIST:
      checks.checkIfNonEmptyPureListOfStrings(filesToCheck)
    elif actionType == dirAction.ENSURE_DIR_EXISTS_ONLY \
            or actionType == dirAction.DO_NOT_CHECK_DIR_EXISTENCE:
      checks.checkIfEmptyList(filesToCheck)
    if len(dirPathRelativeToGitRepo) > 1 and dirPathRelativeToGitRepo[-1] != "/":
      dirPathRelativeToGitRepo += "/"
    while len(dirPathRelativeToGitRepo) > 1 and dirPathRelativeToGitRepo.startswith("./"):
      dirPathRelativeToGitRepo = dirPathRelativeToGitRepo[2:]
    self.absoluteDirPath = self.projRootAbsolutePath + dirPathRelativeToGitRepo
    if actionType != dirAction.DO_NOT_CHECK_DIR_EXISTENCE:
      checks.checkIfDirectoryPathExists(self.absoluteDirPath)
    for file in filesToCheck:
      absPath = self.absoluteDirPath + file
      checks.checkIfFilePathExists(absPath)

  def getAbsoluteDirPathEndingWithSlash(self):
    return self.absoluteDirPath
