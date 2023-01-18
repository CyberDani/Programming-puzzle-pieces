import random
import sys

sys.path.append('../..')

from modules.checks import fileTypeCheck as fTypeCheck
from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.paths.values import possibleFilePathTypes as fTypes

from modules.paths.values.dirPathTypeForUT import DirectoryPathTypeForUT as UtDir

class ChecksTests(AutoUnitTest):

  def test_checkIfFileType_wrongType(self):
    self.assertRaises(Exception, fTypeCheck.checkIfFileType, 2)
    self.assertRaises(Exception, fTypeCheck.checkIfFileType, "string")
    self.assertRaises(Exception, fTypeCheck.checkIfFileType, True)
    self.assertRaises(Exception, fTypeCheck.checkIfFileType, [])
    self.assertRaises(Exception, fTypeCheck.checkIfFileType, {})
    self.assertRaises(Exception, fTypeCheck.checkIfFileType, (1, "One"))
    self.assertRaises(Exception, fTypeCheck.checkIfFileType, None)
    self.assertRaises(Exception, fTypeCheck.checkIfFileType, UtDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)

  def test_checkIfFileType_rightType(self):
    try:
      for fType in fTypes.filePathTypes:
        enumValue1 = random.choice(list(fType))
        enumValue2 = random.choice(list(fType))
        fTypeCheck.checkIfFileType(enumValue1)
        fTypeCheck.checkIfFileType(enumValue2)
    except Exception:
      self.fail("checkIfFileType() raised Exception unexpectedly!")
