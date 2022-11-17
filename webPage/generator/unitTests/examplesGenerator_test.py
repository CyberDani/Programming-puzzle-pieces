import sys

sys.path.append('..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.unitTests import examplesGenerator as exGen

class UtExamplesGeneratorTests(AutoUnitTest):

  examplesDict = {
    type(None): [None],
    bool: [True, False],
    int: [-5, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    str: ["", "Q", "    ", "\r", "\r\n", "oneWord", "two words", "\t\t {[(1,0\\2,0) + 10] + 2}\r\n<= 12.5;\t"],
    list: [[], [None], [1, 2, 3], [False, -1], [0, "", [], True], [[1, 2, [3, 4]]]],
    dict: [{}, {"key": "value"}, {1: "one", 2: "two"}, {0: None, 1: [], 2: False, "two": 2}],
    tuple: [(1,), (False, -1), ("string", (2,), None), ([], {}, (), ""), ((1, (2,)),)]
  }

  def test_getAllExamplesByTypes_nonSense(self):
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, None)
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, True)
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, 12)
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, "text")
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, [])
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, [1, 2])
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, {})
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, {1: 2})

  def test_getAllExamplesByTypes_typeNotFound(self):
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, (None,))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, (float,))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, (bool, float))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, (float, str, int))

  def test_getAllExamplesByTypes_noneType(self):
    values = exGen.getAllExamplesByTypes(self.examplesDict, (type(None),))
    self.assertEqual(len(values), 1)
    self.assertEqual(len(values[0]), 1)
    self.assertEqual(values[0], [None])

  def test_getAllExamplesByTypes_intType(self):
    values = exGen.getAllExamplesByTypes(self.examplesDict, (int,))
    self.assertEqual(len(values), 1)
    self.assertEqual(len(values[0]), len(self.examplesDict[int]))
    self.assertEqual(values[0], self.examplesDict[int])

  def test_getAllExamplesByTypes_twoTypes(self):
    values = exGen.getAllExamplesByTypes(self.examplesDict, (str, bool))
    self.assertEqual(len(values), 2)
    self.assertEqual(len(values[0]), len(self.examplesDict[str]))
    self.assertEqual(len(values[1]), len(self.examplesDict[bool]))
    self.assertEqual(values[0], self.examplesDict[str])
    self.assertEqual(values[1], self.examplesDict[bool])

  def test_getAllExamplesByTypes_threeTypes(self):
    values = exGen.getAllExamplesByTypes(self.examplesDict, (dict, tuple, list))
    self.assertEqual(len(values), 3)
    self.assertEqual(len(values[0]), len(self.examplesDict[dict]))
    self.assertEqual(len(values[1]), len(self.examplesDict[tuple]))
    self.assertEqual(len(values[2]), len(self.examplesDict[list]))
    self.assertEqual(values[0], self.examplesDict[dict])
    self.assertEqual(values[1], self.examplesDict[tuple])
    self.assertEqual(values[2], self.examplesDict[list])

  def test_getRandomTupleByType_nonSense(self):
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, None)
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, True)
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, 12)
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, "text")
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, [])
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, [1, 2])
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, {})
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, {1: 2})

  def test_getRandomTupleByType_typeNotFound(self):
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, (float,))
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, (str, float))
    self.assertRaises(Exception, exGen.getRandomTupleByType, self.examplesDict, (int, list, float, dict))

  def test_getRandomTupleByType_noneType(self):
    noneTuple = exGen.getRandomTupleByType(self.examplesDict, (type(None),))
    self.assertEqual(noneTuple, (None,))

  def test_getRandomTupleByType_intType(self):
    intTuple = exGen.getRandomTupleByType(self.examplesDict, (int,))
    self.assertEqual(len(intTuple), 1)
    val, = intTuple
    self.assertTrue(val in self.examplesDict[int])

  def test_getRandomTupleByType_tryToGetDifferentTuples(self):
    tuple1 = exGen.getRandomTupleByType(self.examplesDict, (int,))
    tuple2 = exGen.getRandomTupleByType(self.examplesDict, (int,))
    tuple3 = exGen.getRandomTupleByType(self.examplesDict, (int,))
    tuple4 = exGen.getRandomTupleByType(self.examplesDict, (int,))
    tuple5 = exGen.getRandomTupleByType(self.examplesDict, (int,))
    val1, = tuple1
    val2, = tuple2
    val3, = tuple3
    val4, = tuple4
    val5, = tuple5
    self.assertTrue(val1 != val2 or val1 != val3 or val1 != val4 or val1 != val5 or val2 != val3 or val2 != val4 or
                    val2 != val5 or val3 != val4 or val4 != val5)

  def test_getRandomTupleByType_tryToGetDifferentIntsWithinTheSameTuple(self):
    intTuple = exGen.getRandomTupleByType(self.examplesDict, (int, int, int, int, int))
    val1, val2, val3, val4, val5 = intTuple
    self.assertTrue(val1 != val2 or val1 != val3 or val1 != val4 or val1 != val5 or val2 != val3 or val2 != val4 or
                    val2 != val5 or val3 != val4 or val4 != val5)

  def test_getRandomTupleByType_twoTypes(self):
    tupl = exGen.getRandomTupleByType(self.examplesDict, (list, dict))
    self.assertEqual(len(tupl), 2)
    listVal, dictVal = tupl
    self.assertTrue(listVal in self.examplesDict[list])
    self.assertTrue(dictVal in self.examplesDict[dict])

  def test_getRandomTupleByType_threeTypes(self):
    tupl = exGen.getRandomTupleByType(self.examplesDict, (str, dict, bool))
    self.assertEqual(len(tupl), 3)
    strVal, dictVal, boolVal = tupl
    self.assertTrue(strVal in self.examplesDict[str])
    self.assertTrue(dictVal in self.examplesDict[dict])
    self.assertTrue(boolVal in self.examplesDict[bool])
