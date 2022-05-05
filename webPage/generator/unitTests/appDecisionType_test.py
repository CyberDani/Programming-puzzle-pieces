import unittest
import sys

sys.path.append('..')

from defTypes import appDecisionType

class AppDecisionTypeTests(unittest.TestCase):

  def test_values(self):
    appDecisionType.AppDecisionType.STOP_APP
    appDecisionType.AppDecisionType.CONTINUE_RUNNING

  def test_validateLength(self):
    self.assertEqual(len(appDecisionType.AppDecisionType), 2)
