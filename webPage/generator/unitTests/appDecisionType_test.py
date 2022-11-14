import sys

sys.path.append('..')

from defTypes import appDecisionType
from modules.unitTests.autoUnitTest import AutoUnitTest

class AppDecisionTypeTests(AutoUnitTest):

  def test_values(self):
    appDecisionType.AppDecisionType.STOP_APP
    appDecisionType.AppDecisionType.CONTINUE_RUNNING

  def test_validateLength(self):
    self.assertEqual(len(appDecisionType.AppDecisionType), 2)
