import unittest

from modules import filerw

class TempDirsTests(unittest.TestCase):

  def test_quickPass1(self):
    self.assertFalse(filerw.directoryExists("unitTests4unitTests/tempDir"))
    self.assertTrue(filerw.directoryExists("unitTests4unitTests/tempDir1"))
    self.assertTrue(filerw.directoryExists("unitTests4unitTests/tempDir2"))
