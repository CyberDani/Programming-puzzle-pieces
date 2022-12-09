import sys
import itertools

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

  examplesDict_justInt = {
    int: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  }

  examplesDict_stringAndEmptyList = {
    str: ["Hello", "test string", "None"],
    list: [[]]
  }

  examplesDict_dictTupleList = {
    dict: [{}, {"myKey": "myValue"}, {1: "one", 2: "two"}],
    tuple: [(1,), (False, -1), ("string", (2,), None), ([], {}, (), ""), ((1, (2,)),)],
    list: [[]]
  }

  def setUp(self):
    self.twoElementTuples = list(itertools.product(self.examplesDict, repeat=2))
    self.twoElementTuples_stringAndEmptyList = list(itertools.product(self.examplesDict_stringAndEmptyList, repeat=2))
    self.twoElementTuples_dictTupleList = list(itertools.product(self.examplesDict_dictTupleList, repeat=2))
    self.threeElementTuples = list(itertools.product(self.examplesDict, repeat=3))
    self.threeElementTuples_stringAndEmptyList = list(itertools.product(self.examplesDict_stringAndEmptyList, repeat=3))
    self.threeElementTuples_dictTupleList = list(itertools.product(self.examplesDict_dictTupleList, repeat=3))
    self.fourElementTuples = list(itertools.product(self.examplesDict, repeat=4))
    self.fourElementTuples_stringAndEmptyList = list(itertools.product(self.examplesDict_stringAndEmptyList, repeat=4))
    self.fourElementTuples_dictTupleList = list(itertools.product(self.examplesDict_dictTupleList, repeat=4))
    self.fiveElementTuples = list(itertools.product(self.examplesDict, repeat=5))
    self.fiveElementTuples_stringAndEmptyList = list(itertools.product(self.examplesDict_stringAndEmptyList, repeat=5))
    self.fiveElementTuples_dictTupleList = list(itertools.product(self.examplesDict_dictTupleList, repeat=5))

  def test_getAllExamplesByTypes_nonSense(self):
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, None)
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, True)
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, 12)
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, "text")
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, [])
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, [1, 2])
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, {})
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, self.examplesDict, {1: 2})
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, None, (None,))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, "string test", (None,))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, 0, (None,))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, [], (None,))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, [None], (None,))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, [None, 2, True, False], (True,))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, [None, 2, True, False], (True,))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, (True, False), (True,))

  def test_getAllExamplesByTypes_typeNotFound(self):
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, {}, (None,))
    self.assertRaises(Exception, exGen.getAllExamplesByTypes, {}, (str,))
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

  def test_getOneRandomExampleByType_nonSense(self):
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, None)
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, True)
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, 12)
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, "text")
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, [])
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, [1, 2])
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, {})
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, {1: 2})

  def test_getOneRandomExampleByType_typeNotFound(self):
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, (float,))
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, (str, float))
    self.assertRaises(Exception, exGen.getOneRandomExampleByType, self.examplesDict, (int, list, float, dict))

  def test_getOneRandomExampleByType_noneType(self):
    noneTuple = exGen.getOneRandomExampleByType(self.examplesDict, (type(None),))
    self.assertEqual(noneTuple, (None,))

  def test_getOneRandomExampleByType_intType(self):
    intTuple = exGen.getOneRandomExampleByType(self.examplesDict, (int,))
    self.assertEqual(len(intTuple), 1)
    val, = intTuple
    self.assertTrue(val in self.examplesDict[int])

  def test_getOneRandomExampleByType_tryToGetDifferentTuples(self):
    tuple1 = exGen.getOneRandomExampleByType(self.examplesDict, (int,))
    tuple2 = exGen.getOneRandomExampleByType(self.examplesDict, (int,))
    tuple3 = exGen.getOneRandomExampleByType(self.examplesDict, (int,))
    tuple4 = exGen.getOneRandomExampleByType(self.examplesDict, (int,))
    tuple5 = exGen.getOneRandomExampleByType(self.examplesDict, (int,))
    val1, = tuple1
    val2, = tuple2
    val3, = tuple3
    val4, = tuple4
    val5, = tuple5
    self.assertTrue(val1 != val2 or val1 != val3 or val1 != val4 or val1 != val5 or val2 != val3 or val2 != val4 or
                    val2 != val5 or val3 != val4 or val4 != val5)

  def test_getOneRandomExampleByType_tryToGetDifferentIntsWithinTheSameTuple(self):
    intTuple = exGen.getOneRandomExampleByType(self.examplesDict, (int, int, int, int, int))
    val1, val2, val3, val4, val5 = intTuple
    self.assertTrue(val1 != val2 or val1 != val3 or val1 != val4 or val1 != val5 or val2 != val3 or val2 != val4 or
                    val2 != val5 or val3 != val4 or val4 != val5)

  def test_getOneRandomExampleByType_twoTypes(self):
    tupl = exGen.getOneRandomExampleByType(self.examplesDict, (list, dict))
    self.assertEqual(len(tupl), 2)
    listVal, dictVal = tupl
    self.assertTrue(listVal in self.examplesDict[list])
    self.assertTrue(dictVal in self.examplesDict[dict])

  def test_getOneRandomExampleByType_threeTypes(self):
    tupl = exGen.getOneRandomExampleByType(self.examplesDict, (str, dict, bool))
    self.assertEqual(len(tupl), 3)
    strVal, dictVal, boolVal = tupl
    self.assertTrue(strVal in self.examplesDict[str])
    self.assertTrue(dictVal in self.examplesDict[dict])
    self.assertTrue(boolVal in self.examplesDict[bool])

  def test_getNRandomExamplesByType_wrongArgTypes(self):
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, (int,), None)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, (int,), True)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, (int,), int)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, (int,), [])
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, (int,), "str")
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, 2, 1)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, bool, 2)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, [bool, str], 3)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, True, 4)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, None, 5)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, 1, (int,), 1)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, True, (int, str), 2)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, None, (int, str), 2)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, [], (tuple,), 2)
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, {}, (list, dict), 2)

  def test_getNRandomExamplesByType_zeroExamples(self):
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, (int,), 0)

  def test_getNRandomExamplesByType_typeNotFound(self):
    self.assertRaises(Exception, exGen.getNRandomExamplesByType, self.examplesDict, (float,), 1)

  def test_getNRandomExamplesByType_oneNoneType(self):
    examples = exGen.getNRandomExamplesByType(self.examplesDict, (type(None),), 1)
    self.assertEqual(len(examples), 1)
    self.assertEqual(examples[0], (None,))

  def test_getNRandomExamplesByType_threeNoneType(self):
    examples = exGen.getNRandomExamplesByType(self.examplesDict, (type(None),), 3)
    self.assertEqual(len(examples), 3)
    self.assertEqual(examples, [(None,), (None,), (None,)])

  def test_getNRandomExamplesByType_threeDoubleNoneType(self):
    examples = exGen.getNRandomExamplesByType(self.examplesDict, (type(None), type(None)), 3)
    self.assertEqual(len(examples), 3)
    self.assertEqual(examples, [(None, None), (None, None), (None, None)])

  def test_getNRandomExamplesByType_twoBoolType(self):
    examples = exGen.getNRandomExamplesByType(self.examplesDict, (bool,), 2)
    self.assertEqual(len(examples), 2)
    self.assertNotEqual(examples[0], examples[1])

  def test_getNRandomExamplesByType_fourBoolType(self):
    examples = exGen.getNRandomExamplesByType(self.examplesDict, (bool,), 4)
    self.assertEqual(len(examples), 4)
    self.assertNotEqual(examples[0], examples[1])
    self.assertNotEqual(examples[2], examples[3])

  def test_getNRandomExamplesByType_twoBoolNoneType(self):
    examples = exGen.getNRandomExamplesByType(self.examplesDict, (bool, type(None)), 2)
    self.assertEqual(len(examples), 2)
    self.assertNotEqual(examples[0][0], examples[1][0])
    self.assertEqual(type(examples[0][0]), bool)
    self.assertEqual(type(examples[1][0]), bool)
    self.assertTrue(examples[0][1] is None)
    self.assertTrue(examples[1][1] is None)

  def test_getNRandomExamplesByType_5int(self):
    examples = exGen.getNRandomExamplesByType(self.examplesDict, (int, ), 5)
    self.assertEqual(len(examples), 5)
    self.assertEqual(type(examples[0][0]), int)
    self.assertEqual(type(examples[1][0]), int)
    self.assertEqual(type(examples[2][0]), int)
    self.assertEqual(type(examples[3][0]), int)
    self.assertEqual(type(examples[4][0]), int)
    int1 = examples[0][0]
    int2 = examples[1][0]
    int3 = examples[2][0]
    int4 = examples[3][0]
    int5 = examples[4][0]
    self.assertTrue(int1 in self.examplesDict[int] and int2 in self.examplesDict[int] and int3 in self.examplesDict[int]
                    and int4 in self.examplesDict[int] and int5 in self.examplesDict[int])
    self.assertTrue(int1 != int2 and int1 != int3 and int1 != int4 and int1 != int5 and int2 != int3 and int2 != int4
                    and int2 != int5 and int3 != int4 and int3 != int5 and int4 != int5)

  def test_getNRandomExamplesByType_5doubleInts(self):
    examples = exGen.getNRandomExamplesByType(self.examplesDict, (int, int), 5)
    self.assertEqual(type(examples[0][0]), int)
    self.assertEqual(type(examples[1][0]), int)
    self.assertEqual(type(examples[2][0]), int)
    self.assertEqual(type(examples[3][0]), int)
    self.assertEqual(type(examples[4][0]), int)
    self.assertEqual(type(examples[0][1]), int)
    self.assertEqual(type(examples[1][1]), int)
    self.assertEqual(type(examples[2][1]), int)
    self.assertEqual(type(examples[3][1]), int)
    self.assertEqual(type(examples[4][1]), int)
    int1 = examples[0][0]
    int2 = examples[1][0]
    int3 = examples[2][0]
    int4 = examples[3][0]
    int5 = examples[4][0]
    self.assertTrue(int1 in self.examplesDict[int] and int2 in self.examplesDict[int] and int3 in self.examplesDict[int]
                    and int4 in self.examplesDict[int] and int5 in self.examplesDict[int])
    self.assertTrue(int1 != int2 and int1 != int3 and int1 != int4 and int1 != int5 and int2 != int3 and int2 != int4
                    and int2 != int5 and int3 != int4 and int3 != int5 and int4 != int5)
    int1 = examples[0][1]
    int2 = examples[1][1]
    int3 = examples[2][1]
    int4 = examples[3][1]
    int5 = examples[4][1]
    self.assertTrue(int1 in self.examplesDict[int] and int2 in self.examplesDict[int] and int3 in self.examplesDict[int]
                    and int4 in self.examplesDict[int] and int5 in self.examplesDict[int])
    self.assertTrue(int1 != int2 and int1 != int3 and int1 != int4 and int1 != int5 and int2 != int3 and int2 != int4
                    and int2 != int5 and int3 != int4 and int3 != int5 and int4 != int5)

  def test_getNRandomExamplesByType_5intBoolNone(self):
    examples = exGen.getNRandomExamplesByType(self.examplesDict, (int, bool, type(None)), 5)
    self.assertEqual(len(examples), 5)
    self.assertEqual(type(examples[0][0]), int)
    self.assertEqual(type(examples[1][0]), int)
    self.assertEqual(type(examples[2][0]), int)
    self.assertEqual(type(examples[3][0]), int)
    self.assertEqual(type(examples[4][0]), int)
    self.assertEqual(type(examples[0][1]), bool)
    self.assertEqual(type(examples[1][1]), bool)
    self.assertEqual(type(examples[2][1]), bool)
    self.assertEqual(type(examples[3][1]), bool)
    self.assertEqual(type(examples[4][1]), bool)
    self.assertIsNone(examples[0][2])
    self.assertIsNone(examples[1][2])
    self.assertIsNone(examples[2][2])
    self.assertIsNone(examples[3][2])
    self.assertIsNone(examples[4][2])
    int1 = examples[0][0]
    int2 = examples[1][0]
    int3 = examples[2][0]
    int4 = examples[3][0]
    int5 = examples[4][0]
    self.assertTrue(int1 in self.examplesDict[int] and int2 in self.examplesDict[int] and int3 in self.examplesDict[int]
                    and int4 in self.examplesDict[int] and int5 in self.examplesDict[int])
    self.assertTrue(int1 != int2 and int1 != int3 and int1 != int4 and int1 != int5 and int2 != int3 and int2 != int4
                    and int2 != int5 and int3 != int4 and int3 != int5 and int4 != int5)
    self.assertNotEqual(examples[0][0], examples[1][0])
    self.assertNotEqual(examples[2][0], examples[3][0])

  def test_getNRandomExamplesByType_get2BigTuples(self):
    examples = exGen.getNRandomExamplesByType(self.examplesDict, (str, bool, list, int, tuple, type(None), dict), 2)
    self.assertEqual(len(examples), 2)
    self.assertEqual(type(examples[0][0]), str)
    self.assertTrue(examples[0][0] in self.examplesDict[str])
    self.assertEqual(type(examples[1][0]), str)
    self.assertTrue(examples[1][0] in self.examplesDict[str])
    self.assertNotEqual(examples[0][0], examples[1][0])
    self.assertEqual(type(examples[0][1]), bool)
    self.assertEqual(type(examples[1][1]), bool)
    self.assertTrue(examples[0][1] in self.examplesDict[bool])
    self.assertTrue(examples[1][1] in self.examplesDict[bool])
    self.assertNotEqual(examples[0][1], examples[1][1])
    self.assertEqual(type(examples[0][2]), list)
    self.assertEqual(type(examples[1][2]), list)
    self.assertTrue(examples[0][2] in self.examplesDict[list])
    self.assertTrue(examples[1][2] in self.examplesDict[list])
    self.assertNotEqual(examples[0][2], examples[1][2])
    self.assertEqual(type(examples[0][3]), int)
    self.assertEqual(type(examples[1][3]), int)
    self.assertTrue(examples[0][3] in self.examplesDict[int])
    self.assertTrue(examples[1][3] in self.examplesDict[int])
    self.assertNotEqual(examples[0][3], examples[1][3])
    self.assertEqual(type(examples[0][4]), tuple)
    self.assertEqual(type(examples[1][4]), tuple)
    self.assertTrue(examples[0][4] in self.examplesDict[tuple])
    self.assertTrue(examples[1][4] in self.examplesDict[tuple])
    self.assertNotEqual(examples[0][4], examples[1][4])
    self.assertIsNone(examples[0][5])
    self.assertIsNone(examples[1][5])
    self.assertEqual(type(examples[0][6]), dict)
    self.assertEqual(type(examples[1][6]), dict)
    self.assertTrue(examples[0][6] in self.examplesDict[dict])
    self.assertTrue(examples[1][6] in self.examplesDict[dict])
    self.assertNotEqual(examples[0][6], examples[1][6])

  def test_getNrOfLookalikeTypeTuples_nonSense(self):
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, None)
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, True)
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, 12)
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, "text")
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, [])
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, [1, 2])
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, {})
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, {1: 2})
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, None, (None,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, "string test", (None,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, 0, (None,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, [], (None,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, [None], (None,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, [None, 2, True, False], (True,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, [None, 2, True, False], (True,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, (True, False), (True,))

  def test_getNrOfLookalikeTypeTuples_typeNotFound(self):
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, {}, (None,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, {}, (str,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, (None,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, (float,))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, (bool, float))
    self.assertRaises(Exception, exGen.getNrOfLookalikeTypeTuples, self.examplesDict, (float, str, int))

  def test_getNrOfLookalikeTypeTuples_oneElement(self):
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict, (str,))
    self.assertEqual(n, 0)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict, (tuple,))
    self.assertEqual(n, 0)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_justInt, (int,))
    self.assertEqual(n, 0)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_stringAndEmptyList, (str,))
    self.assertEqual(n, 0)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_stringAndEmptyList, (list,))
    self.assertEqual(n, 0)

  @staticmethod
  def countNrOfFilteredLookalikeTwoTuples(permutatedList, sourceTuple):
    type1 = sourceTuple[0]
    type2 = sourceTuple[1]
    # comment this if you want to debug
    return sum(1 for elem in permutatedList if elem != (type1, type2) and (elem[0] == type1 or elem[1] == type2))
    #answer = [elem for elem in permutatedList if elem != (type1, type2) and (elem[0] == type1 or elem[1] == type2)]
    #return len(answer)

  def test_getNrOfLookalikeTypeTuples_twoElements(self):
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict, (tuple, tuple))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeTwoTuples(self.twoElementTuples, (tuple, tuple))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict, (str, type(None)))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeTwoTuples(self.twoElementTuples, (str, type(None)))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_stringAndEmptyList, (list, str))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeTwoTuples(self.twoElementTuples_stringAndEmptyList, (list, str))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_dictTupleList, (tuple, dict))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeTwoTuples(self.twoElementTuples_dictTupleList, (tuple, dict))
    self.assertEqual(n, nrOfFilteredTuples)

  @staticmethod
  def countNrOfFilteredLookalikeThreeTuples(permutatedList, sourceTuple):
    type1 = sourceTuple[0]
    type2 = sourceTuple[1]
    type3 = sourceTuple[2]
    # comment this if you want to debug
    return sum(1 for elem in permutatedList if elem != (type1, type2, type3) and
               (elem[0] == type1 or elem[1] == type2 or elem[2] == type3))
    #answer = [elem for elem in permutatedList if elem != (type1, type2, type3) and
    #                (elem[0] == type1 or elem[1] == type2 or elem[2] == type3)]
    # return len(answer)

  def test_getNrOfLookalikeTypeTuples_threeElements(self):
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict, (bool, bool, bool))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeThreeTuples(self.threeElementTuples, (bool, bool, bool))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict, (list, dict, type(None)))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeThreeTuples(self.threeElementTuples, (bool, bool, bool))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_stringAndEmptyList, (list, list, str))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeTwoTuples(self.threeElementTuples_stringAndEmptyList,
                                                                  (list, list, str))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_dictTupleList, (list, tuple, dict))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeThreeTuples(self.threeElementTuples_dictTupleList,
                                                                   (list, tuple, dict))
    self.assertEqual(n, nrOfFilteredTuples)

  @staticmethod
  def countNrOfFilteredLookalikeFourTuples(permutatedList, sourceTuple):
    type1 = sourceTuple[0]
    type2 = sourceTuple[1]
    type3 = sourceTuple[2]
    type4 = sourceTuple[3]
    # comment this if you want to debug
    return sum(1 for elem in permutatedList if elem != (type1, type2, type3, type4) and
               (elem[0] == type1 or elem[1] == type2 or elem[2] == type3 or elem[3] == type4))
    # answer = [elem for elem in permutatedList if elem != (type1, type2, type3, type4) and
    #                (elem[0] == type1 or elem[1] == type2 or elem[2] == type3 or elem[3] == type4)]
    # return len(answer)

  def test_getNrOfLookalikeTypeTuples_fourElements(self):
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict, (dict, dict, dict, dict))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeFourTuples(self.fourElementTuples, (dict, dict, dict, dict))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict, (int, tuple, dict, list))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeFourTuples(self.fourElementTuples, (int, tuple, dict, list))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_stringAndEmptyList, (str, str, str, list))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeFourTuples(self.fourElementTuples_stringAndEmptyList,
                                                                  (str, str, str, list))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_dictTupleList, (list, tuple, tuple, dict))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeFourTuples(self.fourElementTuples_dictTupleList,
                                                                  (list, tuple, tuple, dict))
    self.assertEqual(n, nrOfFilteredTuples)

  @staticmethod
  def countNrOfFilteredLookalikeFiveTuples(permutatedList, sourceTuple):
    type1 = sourceTuple[0]
    type2 = sourceTuple[1]
    type3 = sourceTuple[2]
    type4 = sourceTuple[3]
    type5 = sourceTuple[4]
    # comment this if you want to debug
    return sum(1 for elem in permutatedList if elem != (type1, type2, type3, type4, type5) and
               (elem[0] == type1 or elem[1] == type2 or elem[2] == type3 or elem[3] == type4 or elem[4] == type5))

  def test_getNrOfLookalikeTypeTuples_fiveElements(self):
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict, (dict, dict, dict, dict, dict))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeFiveTuples(self.fiveElementTuples,
                                                                   (dict, dict, dict, dict, dict))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict, (int, tuple, dict, bool, list))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeFiveTuples(self.fiveElementTuples,
                                                                   (int, tuple, dict, bool, list))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_stringAndEmptyList, (str, str, str, list, list))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeFiveTuples(self.fiveElementTuples_stringAndEmptyList,
                                                                  (str, str, str, list, list))
    self.assertEqual(n, nrOfFilteredTuples)
    n = exGen.getNrOfLookalikeTypeTuples(self.examplesDict_dictTupleList, (list, tuple, tuple, dict, tuple))
    nrOfFilteredTuples = self.countNrOfFilteredLookalikeFiveTuples(self.fiveElementTuples_dictTupleList,
                                                                  (list, tuple, tuple, dict, tuple))
    self.assertEqual(n, nrOfFilteredTuples)
