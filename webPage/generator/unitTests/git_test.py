import sys
import unittest

sys.path.append('..')
from modules import git
from modules import cmd
from modules import stringUtil

class GitUtilTests(unittest.TestCase):

  def test_getCurrentBranch(self):
    currentBranch = git.getCurrentBranch()
    gitBranchCmd = stringUtil.rTrimNewLines(cmd.getOutputFromCommand("git branch --show-current"))
    self.assertEqual(currentBranch, gitBranchCmd)
