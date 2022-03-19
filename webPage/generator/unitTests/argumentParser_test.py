import unittest
import sys

sys.path.append('..')

from modules import argumentParser

class ArgumentParserTests(unittest.TestCase):

  def test_noArgument(self):
    args = []
    invalidUsage, runUnitTests, backupAndGenerate = argumentParser.parseArguments(args)
    self.assertTrue(invalidUsage)
    self.assertFalse(runUnitTests)
    self.assertFalse(backupAndGenerate)

  def test_unitTestSingleArgument(self):
    args = ['-u']
    invalidUsage, runUnitTests, backupAndGenerate = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertFalse(backupAndGenerate)

  def test_runAllSingleArgument(self):
    args = ['-a']
    invalidUsage, runUnitTests, backupAndGenerate = argumentParser.parseArguments(args)
    self.assertFalse(invalidUsage)
    self.assertTrue(runUnitTests)
    self.assertTrue(backupAndGenerate)

  def invalidArgumentCheck(self, args):
    invalidUsage, runUnitTests, backupAndGenerate = argumentParser.parseArguments(args)
    self.assertTrue(invalidUsage)
    self.assertFalse(runUnitTests)
    self.assertFalse(backupAndGenerate)

  def test_invalidArguments(self):
    self.invalidArgumentCheck(['-A'])
    self.invalidArgumentCheck(['-U'])
    self.invalidArgumentCheck(['a'])
    self.invalidArgumentCheck(['u'])
    self.invalidArgumentCheck(['au'])
    self.invalidArgumentCheck(['ua'])
    self.invalidArgumentCheck(['-ua'])
    self.invalidArgumentCheck(['-au'])
    self.invalidArgumentCheck(['-a','-u'])
    self.invalidArgumentCheck(['-a','-x'])
    self.invalidArgumentCheck(['-u','-a'])
    self.invalidArgumentCheck(['-u','-x'])
    self.invalidArgumentCheck(['-u','file'])
    self.invalidArgumentCheck(['-','file'])
    self.invalidArgumentCheck(['-','-idk'])
    self.invalidArgumentCheck(['-a','-idk'])
    self.invalidArgumentCheck(['-u','-idk'])
    self.invalidArgumentCheck(['x'])
    self.invalidArgumentCheck(['-x'])
    self.invalidArgumentCheck(['-x','file.yaml'])
    self.invalidArgumentCheck(['-x','-y'])
    self.invalidArgumentCheck(['-x','-y','file.txt'])
    self.invalidArgumentCheck(['text','-y','-file'])
    self.invalidArgumentCheck(['-x','-y','-z','-alpha','-beta','-gamma'])