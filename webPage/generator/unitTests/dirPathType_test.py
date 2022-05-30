import pathlib
import sys
import unittest

sys.path.append('..')

from defTypes import dirPathType
from defTypes import pathChecker

from modules import filerw
from modules import path

class PathTypeTests(unittest.TestCase):

  def test_DirectoryRelPathType_checkPaths(self):
    # this line will run the pathChecker test for all enum values
    dirPathType.DirectoryRelPathType

  def test_DirectoryRelPathType_allMemberHasCheckerValueType(self):
    for name, member in dirPathType.DirectoryRelPathType.__members__.items():
      self.assertTrue(type(member.value) == pathChecker.DirectoryPathChecker)

