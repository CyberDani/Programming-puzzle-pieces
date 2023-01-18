import random
import sys
import json

sys.path.append('../..')

from modules import filerw
from modules.paths.values.dirPathTypeForUT import DirectoryPathTypeForUT as UtDir
from modules.paths.values.filePathTypeForUT import FilePathTypeForUT as UtFile

from modules.paths.values import possibleFilePathTypes as fTypes

from modules.unitTests import argsTypeCacher as args
from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.unitTests import examplesGenerator as exGen
from modules.unitTests.values import examplesByType as ex

class ArgsTypeCacherTests(AutoUnitTest):

  exHashJsonKey = "examplesHash"

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

  examplesDict_stringAndEmptyList_2 = {
    str: ["Hello", "test string", "None"],
    list: [[]]
  }

  examplesDict_dictTupleList = {
    dict: [{}, {"myKey": "myValue"}, {1: "one", 2: "two"}],
    tuple: [(1,), (False, -1), ("string", (2,), None), ([], {}, (), ""), ((1, (2,)),)],
    list: [[]]
  }

  examplesDict_dictTupleList_2 = {
    dict: [{}, {"myKey": "myValue"}, {1: "one", 2: "two"}],
    tuple: [(1,), (False, -1), ("string", (2,), None), ([], {}, (), ""), ((1, (2,)),)],
    list: [[]]
  }

  def test_ctor_wrongType(self):
    self.assertRaises(Exception, args.ArgsTypeChecker, UtDir.PYTHON_GENERATOR_UNIT_TESTS_TEST1, ex.examples)
    self.assertRaises(Exception, args.ArgsTypeChecker, 0, ex.examples)
    self.assertRaises(Exception, args.ArgsTypeChecker, "", ex.examples)
    self.assertRaises(Exception, args.ArgsTypeChecker, [], ex.examples)
    self.assertRaises(Exception, args.ArgsTypeChecker, True, ex.examples)
    self.assertRaises(Exception, args.ArgsTypeChecker, None, ex.examples)
    self.assertRaises(Exception, args.ArgsTypeChecker, None, None)
    self.assertRaises(Exception, args.ArgsTypeChecker, UtFile.FOR_TEST_TEXTFILE1, None)
    self.assertRaises(Exception, args.ArgsTypeChecker, UtFile.FOR_TEST_TEXTFILE1, 0)
    self.assertRaises(Exception, args.ArgsTypeChecker, UtFile.FOR_TEST_TEXTFILE1, "")
    self.assertRaises(Exception, args.ArgsTypeChecker, UtFile.FOR_TEST_TEXTFILE1, True)
    self.assertRaises(Exception, args.ArgsTypeChecker, UtFile.FOR_TEST_TEXTFILE1, [])

  def test_ctor_rightType(self):
    try:
      for fType in fTypes.filePathTypes:
        enumValue1 = random.choice(list(fType))
        enumValue2 = random.choice(list(fType))
        args.ArgsTypeChecker(enumValue1, ex.examples)
        args.ArgsTypeChecker(enumValue2, ex.examples)
    except Exception:
      self.fail("ArgsTypeChecker raised Exception unexpectedly!")

  def test_examplesDictIsCached_fileNotExists(self):
    filerw.deleteFileIfExistsByType(UtFile.FOR_TEST_TEXTFILE1)
    arg = args.ArgsTypeChecker(UtFile.FOR_TEST_TEXTFILE1, self.examplesDict)
    self.assertFalse(arg.examplesDictIsCached())

  def test_examplesDictIsCached_emptyFile(self):
    filerw.createOrOverwriteWithEmptyFileByType(UtFile.FOR_TEST_TEXTFILE3)
    arg = args.ArgsTypeChecker(UtFile.FOR_TEST_TEXTFILE3, self.examplesDict)
    self.assertFalse(arg.examplesDictIsCached())

  def test_examplesDictIsCached_notJsonTextFile(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(UtFile.FOR_TEST_TEXTFILE2,
                                                                ["first line", "second line", "third line", "hello"])
    arg = args.ArgsTypeChecker(UtFile.FOR_TEST_TEXTFILE2, self.examplesDict_stringAndEmptyList)
    self.assertFalse(arg.examplesDictIsCached())

  def test_examplesDictIsCached_wrongJsonObject(self):
    examplesHash = exGen.getExamplesDictHash(self.examplesDict_dictTupleList_2)
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(UtFile.FOR_TEST_TEXTFILE1,
                                                            ["{", '"wrongJsonObject":' + '"' + examplesHash + '"', "}"])
    arg = args.ArgsTypeChecker(UtFile.FOR_TEST_TEXTFILE1, self.examplesDict_dictTupleList_2)
    self.assertFalse(arg.examplesDictIsCached())

  def test_examplesDictIsCached_invalidJson(self):
    examplesHash = exGen.getExamplesDictHash(self.examplesDict_stringAndEmptyList)
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(UtFile.FOR_TEST_TEXTFILE1,
                                                      ["{", '"' + self.exHashJsonKey + '":' + '"' + examplesHash + '"'])
    arg = args.ArgsTypeChecker(UtFile.FOR_TEST_TEXTFILE1, self.examplesDict_stringAndEmptyList)
    self.assertFalse(arg.examplesDictIsCached())

  def test_examplesDictIsCached_wrongHash(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(UtFile.FOR_TEST_TEXTFILE1,
                                                                ["{", '"' + self.exHashJsonKey + '":"pineapple"', "}"])
    arg = args.ArgsTypeChecker(UtFile.FOR_TEST_TEXTFILE1, self.examplesDict_justInt)
    self.assertFalse(arg.examplesDictIsCached())

  def test_examplesDictIsCached_validHash(self):
    examplesHash = exGen.getExamplesDictHash(self.examplesDict_dictTupleList)
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(UtFile.FOR_TEST_TEXTFILE1,
                                                                ["{", '"' + self.exHashJsonKey + '":"'
                                                                      + examplesHash + '"', "}"])
    arg = args.ArgsTypeChecker(UtFile.FOR_TEST_TEXTFILE1, self.examplesDict_dictTupleList)
    self.assertTrue(arg.examplesDictIsCached())

  def test_writeExampleHashToFile_fileNotExists(self):
    filerw.deleteFileIfExistsByType(UtFile.FOR_TEST_TEXTFILE1)
    examplesHash = exGen.getExamplesDictHash(self.examplesDict)
    arg = args.ArgsTypeChecker(UtFile.FOR_TEST_TEXTFILE1, self.examplesDict)
    arg.writeExampleHashToFile()
    file = filerw.getFileWithReadPerm(UtFile.FOR_TEST_TEXTFILE1)
    jsonContent = json.load(file)
    self.assertTrue(self.exHashJsonKey in jsonContent)
    self.assertEqual(jsonContent[self.exHashJsonKey], examplesHash)

  def test_writeExampleHashToFile_nonJsonFile(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeAndClose(UtFile.FOR_TEST_TEXTFILE2,
                                                                ["line 1", "second line", "\t\tH E LL O"])
    examplesHash = exGen.getExamplesDictHash(self.examplesDict_stringAndEmptyList)
    arg = args.ArgsTypeChecker(UtFile.FOR_TEST_TEXTFILE2, self.examplesDict_stringAndEmptyList)
    arg.writeExampleHashToFile()
    file = filerw.getFileWithReadPerm(UtFile.FOR_TEST_TEXTFILE2)
    jsonContent = json.load(file)
    self.assertTrue(self.exHashJsonKey in jsonContent)
    self.assertEqual(jsonContent[self.exHashJsonKey], examplesHash)
