from defTypes import dirPathType

from modules import checks

class FilePathChecker:
  def __init__(self, directoryPathType, fileName):
    checks.checkIfStringDoesNotContainAnySubstringFromList(fileName, 1, 300, ["/", "\\"])
    checks.checkIfType(directoryPathType, dirPathType.DirectoryPathType)
    self.fileName = fileName
    self.absolutePath = directoryPathType.value.getAbsoluteDirPathEndingWithSlash() + fileName
    checks.checkIfFilePathExists(self.absolutePath)

  def getAbsoluteFilePath(self):
    return self.absolutePath

  def getFileName(self):
    return self.fileName
