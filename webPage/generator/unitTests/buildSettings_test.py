import unittest
import sys

sys.path.append('..')

from defTypes import buildSettings
from defTypes import buildType
from defTypes import dbBranchType

from modules import counter

class BuildSettingsTests(unittest.TestCase):

  def test_validateDataMembers_oneExample(self):
    file = open("./unitTests/temp/test.txt", "w")
    ctr = counter.SimpleCounter(1)
    settings = buildSettings.BuildSettings(dbBranch=dbBranchType.DbBranchType.DEVEL,
                                           htmlOutputFile=file,
                                           buildOption=buildType.BuildType.REBUILD,
                                           indentDepth=2,
                                           stepsCounter=ctr)
    self.assertEqual(settings.buildOption, buildType.BuildType.REBUILD)
    self.assertEqual(settings.dbBranch, dbBranchType.DbBranchType.DEVEL)
    self.assertEqual(settings.indentDepth, 2)
    self.assertTrue(settings.htmlOutputFile.writable())
    self.assertEqual(settings.stepsCounter.getNextInt(), 1)

  def test_validateDataMembers_anotherExample(self):
    file = open("./unitTests/temp/test.txt", "w")
    ctr = counter.SimpleCounter(11)
    settings = buildSettings.BuildSettings(dbBranch=dbBranchType.DbBranchType.MASTER,
                                           htmlOutputFile=file,
                                           buildOption=buildType.BuildType.DO_NOT_BUILD,
                                           indentDepth=12,
                                           stepsCounter=ctr)
    self.assertEqual(settings.buildOption, buildType.BuildType.DO_NOT_BUILD)
    self.assertEqual(settings.dbBranch, dbBranchType.DbBranchType.MASTER)
    self.assertEqual(settings.indentDepth, 12)
    self.assertTrue(settings.htmlOutputFile.writable())
    self.assertEqual(settings.stepsCounter.getNextInt(), 11)

  def test_setDataMembers_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    ctr = counter.SimpleCounter(11)
    with self.assertRaises(Exception):
      buildSettings.BuildSettings(dbBranch="master",
                                   htmlOutputFile=file,
                                   buildOption=buildType.BuildType.DO_NOT_BUILD,
                                   indentDepth=12,
                                   stepsCounter=ctr)
    with self.assertRaises(Exception):
      buildSettings.BuildSettings(dbBranch=dbBranchType.DbBranchType.MASTER,
                                  htmlOutputFile=file,
                                  buildOption="build",
                                  indentDepth=12,
                                  stepsCounter=ctr)
    with self.assertRaises(Exception):
      buildSettings.BuildSettings(dbBranch=dbBranchType.DbBranchType.MASTER,
                                  htmlOutputFile="index.html",
                                  buildOption=buildType.BuildType.DO_NOT_BUILD,
                                  indentDepth=12,
                                  stepsCounter=ctr)
    with self.assertRaises(Exception):
      buildSettings.BuildSettings(dbBranch=dbBranchType.DbBranchType.MASTER,
                                  htmlOutputFile=file,
                                  buildOption=buildType.BuildType.DO_NOT_BUILD,
                                  indentDepth="zero",
                                  stepsCounter=ctr)
    with self.assertRaises(Exception):
      buildSettings.BuildSettings(dbBranch=dbBranchType.DbBranchType.MASTER,
                                  htmlOutputFile=file,
                                  buildOption=buildType.BuildType.DO_NOT_BUILD,
                                  indentDepth=2,
                                  stepsCounter=1)