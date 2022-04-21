import unittest
import sys

sys.path.append('..')

from defTypes import dbBranchType

class DbBranchTypeTests(unittest.TestCase):

  def test_values(self):
    dbBranchType.DbBranchType.MASTER
    dbBranchType.DbBranchType.DEVEL

  def test_validateLength(self):
    self.assertEqual(len(dbBranchType.DbBranchType), 2)