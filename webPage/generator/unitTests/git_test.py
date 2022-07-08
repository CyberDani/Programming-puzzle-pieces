import pathlib
import sys
import unittest

sys.path.append('..')
from modules import git
from modules import cmd
from modules import stringUtil
from modules import filerw

class GitUtilTests(unittest.TestCase):

  def test_getRepoRootDirectory(self):
    gitRoot = git.getRepoRootDirectory()
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(gitRoot))
    self.assertTrue(filerw.fileExistsByPath(gitRoot + "/.git/HEAD"))

  def test_getCurrentBranch(self):
    currentBranch = git.getCurrentBranch()
    gitBranchCmd = stringUtil.rTrimNewLines(cmd.getOutputFromCommand("git branch --show-current"))
    self.assertEqual(currentBranch, gitBranchCmd)
