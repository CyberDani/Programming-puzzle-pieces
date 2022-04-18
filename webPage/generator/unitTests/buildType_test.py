import unittest
import sys

sys.path.append('..')

from modules import buildType

class BuildTypeTests(unittest.TestCase):

  def test_values(self):
    buildType.buildType.DO_NOT_BUILD
    buildType.buildType.BUILD
    buildType.buildType.REBUILD