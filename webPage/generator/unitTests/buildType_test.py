import sys

sys.path.append('..')

from defTypes import buildType

from modules.unitTests.autoUnitTest import AutoUnitTest

class BuildTypeTests(AutoUnitTest):

  def test_values(self):
    buildType.BuildType.DO_NOT_BUILD
    buildType.BuildType.BUILD
    buildType.BuildType.REBUILD

  def test_validateLength(self):
    self.assertEqual(len(buildType.BuildType), 3)
