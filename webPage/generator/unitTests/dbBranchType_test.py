import sys

sys.path.append('..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from defTypes import dbBranchType

class DbBranchTypeTests(AutoUnitTest):

  def test_values(self):
    dbBranchType.DbBranchType.MASTER
    dbBranchType.DbBranchType.DEVEL

  def test_validateLength(self):
    self.assertEqual(len(dbBranchType.DbBranchType), 2)
