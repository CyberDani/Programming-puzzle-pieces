import unittest
import sys

sys.path.append('..')

from modules.paths import path
from modules.paths.definitions.dirPathTypeForProd import DirectoryPathTypeForProd as Dir

from modules import cmd
from modules.paths import path
from modules import stringUtil

class CmdTests(unittest.TestCase):

  def test_getOutputFromCommandNonSense(self):
    with self.assertRaises(Exception):
      cmd.getOutputFromCommand("")
    with self.assertRaises(Exception):
      cmd.getOutputFromCommand(12)
    with self.assertRaises(Exception):
      cmd.getOutputFromCommand()
    with self.assertRaises(Exception):
      cmd.getOutputFromCommand(None)
    with self.assertRaises(Exception):
      cmd.getOutputFromCommand(True)

  def test_getOutputFromCommand_simpleExamples(self):
    ans = cmd.getOutputFromCommand("cd")
    cwd = path.getCwd()[:-1]
    cwd = cwd.replace("/", "\\")
    self.assertTrue(stringUtil.rTrimNewLines(ans) == cwd or stringUtil.rTrimNewLines(ans) == cwd + "\\")
    ans = cmd.getOutputFromCommand("echo hello")
    self.assertEqual(stringUtil.rTrimNewLines(ans), "hello")
    ans = cmd.getOutputFromCommand("git --version")
    self.assertTrue(ans.startswith("git version "))
