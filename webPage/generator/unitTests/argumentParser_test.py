import unittest
import sys

sys.path.append('..')

from modules import argumentParser
from modules import buildType

class ArgumentParserTests(unittest.TestCase):

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
    invalidUsage, runUnitTests, buildOption = argumentParser.parseArguments(args)
    self.assertTrue(invalidUsage)
    self.assertFalse(runUnitTests)
    self.assertEqual(buildOption, buildType.BuildType.DO_NOT_BUILD)

  def test_unitTestSingleArgument(self):
    args = ['-u']
    invalidUsage, runUnitTests, buildOption = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertEqual(buildOption, buildType.BuildType.DO_NOT_BUILD)

  def test_build(self):
    args = ['-b']
    invalidUsage, runUnitTests, buildOption = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertEqual(buildOption, buildType.BuildType.BUILD)

  def test_rebuild(self):
    args = ['-rb']
    invalidUsage, runUnitTests, buildOption = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertEqual(buildOption, buildType.BuildType.REBUILD)

  def invalidArgumentCheck(self, args):
    invalidUsage, runUnitTests, buildOption = argumentParser.parseArguments(args)
    self.assertTrue(invalidUsage)
    self.assertFalse(runUnitTests)
    self.assertEqual(buildOption, buildType.BuildType.DO_NOT_BUILD)

  def test_invalidArguments(self):
    self.invalidArgumentCheck(['-A'])
    self.invalidArgumentCheck(['-B'])
    self.invalidArgumentCheck(['-U'])
    self.invalidArgumentCheck(['b'])
    self.invalidArgumentCheck(['a'])
    self.invalidArgumentCheck(['-a'])
    self.invalidArgumentCheck(['u'])
    self.invalidArgumentCheck(['au'])
    self.invalidArgumentCheck(['ua'])
    self.invalidArgumentCheck(['-ua'])
    self.invalidArgumentCheck(['-au'])
    self.invalidArgumentCheck(['-a','-u'])
    self.invalidArgumentCheck(['-b','-u'])
    self.invalidArgumentCheck(['-a','-x'])
    self.invalidArgumentCheck(['-b','-x'])
    self.invalidArgumentCheck(['-u','-a'])
    self.invalidArgumentCheck(['-u','-b'])
    self.invalidArgumentCheck(['-u','-x'])
    self.invalidArgumentCheck(['-u','file'])
    self.invalidArgumentCheck(['-','file'])
    self.invalidArgumentCheck(['-','-idk'])
    self.invalidArgumentCheck(['-a','-idk'])
    self.invalidArgumentCheck(['-b','-idk'])
    self.invalidArgumentCheck(['-u','-idk'])
    self.invalidArgumentCheck(['x'])
    self.invalidArgumentCheck(['-x'])
    self.invalidArgumentCheck(['-x','file.yaml'])
    self.invalidArgumentCheck(['-x','-y'])
    self.invalidArgumentCheck(['-x','-y','file.txt'])
    self.invalidArgumentCheck(['text','-y','-file'])
    self.invalidArgumentCheck(['-x','-y','-z','-alpha','-beta','-gamma'])