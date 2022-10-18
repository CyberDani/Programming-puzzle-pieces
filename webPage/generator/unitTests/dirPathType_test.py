import sys
import unittest

sys.path.append('..')

from defTypes import dirPathTypeForProd
from defTypes import dirPathChecker

class PathTypeTests(unittest.TestCase):

  def test_DirectoryRelPathType_checkPaths(self):
    # this line will run the pathChecker test for all enum values
    dirPathTypeForProd.DirectoryPathTypeForProd

  def test_DirectoryRelPathType_allMemberHasCheckerValueType(self):
    for name, member in dirPathTypeForProd.DirectoryPathTypeForProd.__members__.items():
      self.assertTrue(type(member.value) == dirPathChecker.DirectoryPathChecker)
