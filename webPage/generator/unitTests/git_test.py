import sys

sys.path.append('..')

from modules import git
from modules import cmd
from modules import stringUtil

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.paths import path

class GitUtilTests(AutoUnitTest):

  def test_getCurrentBranch(self):
    currentBranch = git.getCurrentBranch()
    cwd = path.getCwd()
    root = path.getProjectRootAbsolutePath()
    if not cwd.startswith(root):
      return
    gitBranchCmd = stringUtil.rTrimNewLines(cmd.getOutputFromCommand("git branch --show-current"))
    self.assertEqual(currentBranch, gitBranchCmd)
