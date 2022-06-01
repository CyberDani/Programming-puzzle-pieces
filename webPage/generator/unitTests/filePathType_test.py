import sys
import unittest

sys.path.append('..')

from defTypes import filePathType
from defTypes import filePathChecker

class FileTypeTests(unittest.TestCase):

  def test_FilePathType_checkPaths(self):
    # this line will run the pathChecker test for all enum values
    filePathType.FilePathType

  def test_FilePathType_allMemberHasCheckerValueType(self):
    for name, member in filePathType.FilePathType.__members__.items():
      self.assertTrue(type(member.value) == filePathChecker.FilePathChecker)
