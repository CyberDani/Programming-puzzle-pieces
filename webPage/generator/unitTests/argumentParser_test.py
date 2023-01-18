import sys

sys.path.append('..')

from defTypes import dbBranchType
from defTypes import buildType

from modules import argumentParser
from modules.checks import checks
from modules import db
from modules.unitTests.autoUnitTest import AutoUnitTest

class ArgumentParserTests(AutoUnitTest):

  def test_nonSense(self):
    with self.assertRaises(Exception):
      argumentParser.parseArguments(["hello", False])
    with self.assertRaises(Exception):
      argumentParser.parseArguments([False, False])
    with self.assertRaises(Exception):
      argumentParser.parseArguments(["hello", "arg2", None, "arg4"])
    with self.assertRaises(Exception):
      argumentParser.parseArguments([12, "one", "two", "three"])
    with self.assertRaises(Exception):
      argumentParser.parseArguments("-b -a")

  def test_noArgument(self):
    args = []
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertTrue(invalidUsage)
    self.assertFalse(runUnitTests)
    self.assertFalse(backup)
    self.assertEqual(buildOption, buildType.BuildType.DO_NOT_BUILD)
    # not interested in actual value of dbBranch in this case
    self.assertTrue(dbBranch == dbBranchType.DbBranchType.MASTER or dbBranch == dbBranchType.DbBranchType.DEVEL)

  def test_unitTestSingleArgument(self):
    args = ['-u']
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertFalse(backup)
    self.assertEqual(buildOption, buildType.BuildType.DO_NOT_BUILD)
    self.assertEqual(dbBranch, db.getCurrentDbBranch())

  def test_unitTest_dbMaster(self):
    args = ['-u', 'db:master']
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertFalse(backup)
    self.assertEqual(buildOption, buildType.BuildType.DO_NOT_BUILD)
    self.assertEqual(dbBranch, dbBranchType.DbBranchType.MASTER)

  def test_unitTest_dbDevel(self):
    args = ['-u', 'db:devel']
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertFalse(backup)
    self.assertEqual(buildOption, buildType.BuildType.DO_NOT_BUILD)
    self.assertEqual(dbBranch, dbBranchType.DbBranchType.DEVEL)

  def test_build(self):
    args = ['-b']
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertTrue(backup)
    self.assertEqual(buildOption, buildType.BuildType.BUILD)
    self.assertEqual(dbBranch, db.getCurrentDbBranch())

  def test_build_dbMaster(self):
    args = ['-b', 'db:master']
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertTrue(backup)
    self.assertEqual(buildOption, buildType.BuildType.BUILD)
    self.assertEqual(dbBranch, dbBranchType.DbBranchType.MASTER)

  def test_build_dbDevel(self):
    args = ['-b', 'db:devel']
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertTrue(backup)
    self.assertEqual(buildOption, buildType.BuildType.BUILD)
    self.assertEqual(dbBranch, dbBranchType.DbBranchType.DEVEL)

  def test_rebuild(self):
    args = ['-rb']
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertTrue(backup)
    self.assertEqual(buildOption, buildType.BuildType.REBUILD)
    self.assertEqual(dbBranch, db.getCurrentDbBranch())

  def test_rebuild_dbMaster(self):
    args = ['-rb', 'db:master']
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertTrue(backup)
    self.assertEqual(buildOption, buildType.BuildType.REBUILD)
    self.assertEqual(dbBranch, dbBranchType.DbBranchType.MASTER)

  def test_rebuild_dbDevel(self):
    args = ['-rb', 'db:devel']
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertTrue(backup)
    self.assertEqual(buildOption, buildType.BuildType.REBUILD)
    self.assertEqual(dbBranch, dbBranchType.DbBranchType.DEVEL)

  def invalidArgumentCheck(self, args):
    invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
    self.assertTrue(invalidUsage)
    self.assertFalse(runUnitTests)
    self.assertFalse(backup)
    self.assertEqual(buildOption, buildType.BuildType.DO_NOT_BUILD)
    # not interested in actual value of dbBranch in this case
    self.assertTrue(dbBranch == dbBranchType.DbBranchType.MASTER or dbBranch == dbBranchType.DbBranchType.DEVEL)

  def test_invalidArguments(self):
    self.invalidArgumentCheck(['-A'])
    self.invalidArgumentCheck(['-B'])
    self.invalidArgumentCheck(['-U'])
    self.invalidArgumentCheck(['-U', 'db:master'])
    self.invalidArgumentCheck(['b'])
    self.invalidArgumentCheck(['a'])
    self.invalidArgumentCheck(['a', 'db:devel'])
    self.invalidArgumentCheck(['-a'])
    self.invalidArgumentCheck(['u'])
    self.invalidArgumentCheck(['au'])
    self.invalidArgumentCheck(['ua'])
    self.invalidArgumentCheck(['-ua'])
    self.invalidArgumentCheck(['-au'])
    self.invalidArgumentCheck(['-a', '-u'])
    self.invalidArgumentCheck(['-b', '-u'])
    self.invalidArgumentCheck(['-a', '-x'])
    self.invalidArgumentCheck(['-b', '-x'])
    self.invalidArgumentCheck(['-u', '-a'])
    self.invalidArgumentCheck(['-u', '-b'])
    self.invalidArgumentCheck(['-u', '-x'])
    self.invalidArgumentCheck(['-u', 'file'])
    self.invalidArgumentCheck(['-', 'file'])
    self.invalidArgumentCheck(['-', '-idk'])
    self.invalidArgumentCheck(['-a', '-idk'])
    self.invalidArgumentCheck(['-b', '-idk'])
    self.invalidArgumentCheck(['-u', '-idk'])
    self.invalidArgumentCheck(['-u', 'db:nonExistingBranch'])
    self.invalidArgumentCheck(['x'])
    self.invalidArgumentCheck(['-x'])
    self.invalidArgumentCheck(['-x', 'file.yaml'])
    self.invalidArgumentCheck(['-x', '-y'])
    self.invalidArgumentCheck(['-x', '-y', 'file.txt'])
    self.invalidArgumentCheck(['text', '-y', '-file'])
    self.invalidArgumentCheck(['-x', '-y', '-z', '-alpha', '-beta', '-gamma'])
    self.invalidArgumentCheck(['db:master', 'db:devel'])
    self.invalidArgumentCheck(['db:master', '-u'])
    self.invalidArgumentCheck(['db:master'])
    self.invalidArgumentCheck(['db:devel'])

  def test_getScriptUsageLines_returnsPureListOfStrings(self):
    lines = argumentParser.getScriptUsageLines()
    checks.checkIfPureListOfStrings(lines)
    self.assertTrue(len(lines) > 7)
