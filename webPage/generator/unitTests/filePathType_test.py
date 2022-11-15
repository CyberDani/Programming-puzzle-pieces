import sys

sys.path.append('..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.paths import filePathChecker
from modules.paths.values import filePathTypeForProd


class FileTypeTests(AutoUnitTest):

  def test_FilePathType_checkPaths(self):
    # this line will run the pathChecker test for all enum values
    filePathTypeForProd.FilePathType

  def test_FilePathType_allMemberHasCheckerValueType(self):
    for name, member in filePathTypeForProd.FilePathType.__members__.items():
      self.assertTrue(type(member.value) == filePathChecker.FilePathChecker)
