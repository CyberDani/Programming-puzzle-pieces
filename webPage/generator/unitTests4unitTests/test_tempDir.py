import unittest

from modules import filerw

class TempDirTests(unittest.TestCase):

  def test_quickPass1(self):
    self.assertTrue(filerw.directoryExistsByPath("unitTests4unitTests/tempDir"))
    self.assertFalse(filerw.directoryExistsByPath("unitTests4unitTests/tempDir1"))
    self.assertFalse(filerw.directoryExistsByPath("unitTests4unitTests/tempDir2"))
