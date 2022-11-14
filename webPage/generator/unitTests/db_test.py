import sys

sys.path.append('..')

from modules.unitTests.autoUnitTest import AutoUnitTest

from defTypes import dbBranchType
from modules import db
from modules import git

class DbTests(AutoUnitTest):

  def test_getDbBranchByGitBranch_nonSense(self):
    with self.assertRaises(Exception):
      db.getDbBranchByGitBranch("")
    with self.assertRaises(Exception):
      db.getDbBranchByGitBranch(None)
    with self.assertRaises(Exception):
      db.getDbBranchByGitBranch(12)
    with self.assertRaises(Exception):
      db.getDbBranchByGitBranch(True)
    with self.assertRaises(Exception):
      db.getDbBranchByGitBranch([])
    with self.assertRaises(Exception):
      db.getDbBranchByGitBranch(['master'])

  def test_getDbBranchByGitBranch_examples(self):
    ans = db.getDbBranchByGitBranch("master")
    self.assertEqual(ans, dbBranchType.DbBranchType.MASTER)
    ans = db.getDbBranchByGitBranch("devel")
    self.assertEqual(ans, dbBranchType.DbBranchType.DEVEL)
    ans = db.getDbBranchByGitBranch("feature_xy")
    self.assertEqual(ans, dbBranchType.DbBranchType.DEVEL)

  def test_getCurrentDbBranch_examples(self):
    gitBranch = git.getCurrentBranch()
    expectedDbBranch = db.getDbBranchByGitBranch(gitBranch)
    self.assertEqual(expectedDbBranch, db.getCurrentDbBranch())
