import sys

sys.path.append('../..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.paths import dirPathChecker
from modules.paths.values import dirPathTypeForProd


class PathTypeTests(AutoUnitTest):

  def test_DirectoryRelPathType_checkPaths(self):
    # this line will run the pathChecker test for all enum values
    dirPathTypeForProd.DirectoryPathTypeForProd

  def test_DirectoryRelPathType_allMemberHasCheckerValueType(self):
    for name, member in dirPathTypeForProd.DirectoryPathTypeForProd.__members__.items():
      self.assertTrue(type(member.value) == dirPathChecker.DirectoryPathChecker)
