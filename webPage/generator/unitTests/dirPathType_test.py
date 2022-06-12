import sys
import unittest

sys.path.append('..')

from defTypes import dirPathType
from defTypes import dirPathChecker

class PathTypeTests(unittest.TestCase):

  def test_DirectoryRelPathType_checkPaths(self):
    # this line will run the pathChecker test for all enum values
    dirPathType.DirectoryPathType

  def test_DirectoryRelPathType_allMemberHasCheckerValueType(self):
    for name, member in dirPathType.DirectoryPathType.__members__.items():
      self.assertTrue(type(member.value) == dirPathChecker.DirectoryPathChecker)

