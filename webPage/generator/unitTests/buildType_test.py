import unittest
import sys

sys.path.append('..')

from modules import buildType

class BuildTypeTests(unittest.TestCase):

  def test_values(self):
    buildType.BuildType.DO_NOT_BUILD
    buildType.BuildType.BUILD
    buildType.BuildType.REBUILD

  def test_validateLength(self):
    self.assertEqual(len(buildType.BuildType), 3)