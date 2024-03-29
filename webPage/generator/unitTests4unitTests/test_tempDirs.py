import unittest

from modules.paths.definitions.dirPathTypeForUT import DirectoryPathTypeForUT as Dir

from modules import filerw
from modules.paths import path


class TempDirsTests(unittest.TestCase):

  def test_quickPass1(self):
    utPath = path.getAbsoluteDirPath(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS)
    self.assertFalse(filerw.directoryExistsByPath(utPath + "tempDir"))
    self.assertTrue(filerw.directoryExistsByPath(utPath + "tempDir1"))
    self.assertTrue(filerw.directoryExistsByPath(utPath + "tempDir2"))
