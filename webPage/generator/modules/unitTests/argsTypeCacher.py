import json

from modules import filerw
from modules.checks import checks
from modules.checks import fileTypeCheck

from modules.unitTests import examplesGenerator as exGen

examplesHashJsonKey = "examplesHash"

class ArgsTypeChecker:

  def __init__(self, argsCacheFileType, argTypeExamplesDict):
    fileTypeCheck.checkIfFileType(argsCacheFileType)
    checks.checkIfDict(argTypeExamplesDict)
    self.__examplesCache = exGen.getExamplesDictHash(argTypeExamplesDict)
    self.__argsCacheFileType = argsCacheFileType

  def examplesDictIsCached(self):
    """Tells if the dictionary with the examples given to the ctor is already correctly cached in the file."""
    if not filerw.fileExistsByType(self.__argsCacheFileType):
      return False
    file = filerw.getFileWithReadPerm(self.__argsCacheFileType)
    jsonContent = {}
    try:
      jsonContent = json.load(file)
    except ValueError as e:
      return False
    if examplesHashJsonKey not in jsonContent:
      return False
    exampleHash = jsonContent[examplesHashJsonKey]
    return exampleHash == self.__examplesCache

  def writeExampleHashToFile(self):
    dictionary = {
      examplesHashJsonKey: self.__examplesCache
    }
    jsonContent = json.dumps(dictionary, indent=4)
    file = filerw.getFileWithWritePerm(self.__argsCacheFileType)
    file.write(jsonContent)
    file.close()
