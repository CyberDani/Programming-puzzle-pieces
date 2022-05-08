import pathlib
import sys
import unittest

sys.path.append('..')

from defTypes import pathType
from defTypes import pathChecker

from modules import filerw
from modules import path

class PathTypeTests(unittest.TestCase):

  def test_DirectoryRelPathType_checkPaths(self):
    # this line will run the pathChecker test for all enum values
    pathType.DirectoryRelPathType

