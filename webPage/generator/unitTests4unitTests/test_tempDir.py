import unittest

from modules.paths.definitions.dirPathTypeForUT import DirectoryPathTypeForUT as Dir

from modules import filerw
from modules.paths import path


class TempDirTests(unittest.TestCase):

  def test_quickPass1(self):
    utPath = path.getAbsoluteDirPathEndingWithSlash(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    self.assertTrue(filerw.directoryExistsByPath(utPath + "tempDir"))
    self.assertFalse(filerw.directoryExistsByPath(utPath + "tempDir1"))
    self.assertFalse(filerw.directoryExistsByPath(utPath + "tempDir2"))
