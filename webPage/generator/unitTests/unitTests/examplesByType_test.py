import sys

sys.path.append('../..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.unitTests.values import examplesByType as ex


class UtExamplesByTypeTests(AutoUnitTest):

  def test_generateValuesByType_checkIfDictWithValues(self):
    self.assertEqual(type(ex.examples), dict)
    self.assertTrue(len(ex.examples) > 0)

  def test_generateValuesByType_checkIfAllValuesAreCorrect(self):
    for key, value in ex.examples.items():
      self.assertEqual(type(value), list, "examples[{}] is not list type, found type: {}".format(str(key), type(value)))
      self.assertTrue(len(value) > 0, "examples[{}] cannot be an empty list!".format(str(key)))
      for val in value:
        self.assertEqual(type(val), key, "examples[{}] contains wrong type value: {}".format(str(key), str(val)))
