from defTypes import dirPathType
from defTypes import possibleDirPathTypes

from defTypes.filePathCheckerActionType import FilePathCheckerActionType as fileAction

from modules import checks

class FilePathChecker:
  def __init__(self, directoryPathType, fileName, actionType = fileAction.ENSURE_FILE_EXISTS):
    checks.checkIfStringDoesNotContainAnySubstringFromList(fileName, 1, 300, ["/", "\\"])
    checks.checkIfAnyType(directoryPathType, possibleDirPathTypes.dirPathTypes)
    self.fileName = fileName
    self.absolutePath = directoryPathType.value.getAbsoluteDirPathEndingWithSlash() + fileName
    if actionType == fileAction.ENSURE_FILE_EXISTS:
      checks.checkIfFilePathExists(self.absolutePath)

  def getAbsoluteFilePath(self):
    return self.absolutePath

  def getFileName(self):
    return self.fileName
