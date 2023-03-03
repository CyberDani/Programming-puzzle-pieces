import io
import sys

sys.path.append('../..')

from modules.paths.values.dirPathTypeForUT import DirectoryPathTypeForUT as Dir
from modules.paths.values.filePathTypeForUT import FilePathTypeForUT as File
from modules.unitTests.autoUnitTest import AutoUnitTest

from modules.checks import checks
from modules import filerw
from modules.paths import path


class ChecksTests(AutoUnitTest):

  def test_checkIntIsBetween_raiseException(self):
    self.assertRaises(Exception, checks.checkIntIsBetween, 0, 1, 4)
    self.assertRaises(Exception, checks.checkIntIsBetween, -20, 10, 55)
    self.assertRaises(Exception, checks.checkIntIsBetween, 20, -55, -15)
    self.assertRaises(Exception, checks.checkIntIsBetween, -30, -15, -45)
    self.assertRaises(Exception, checks.checkIntIsBetween, 10, 2, 9)
    self.assertRaises(Exception, checks.checkIntIsBetween, -120, 20, 90)
    self.assertRaises(Exception, checks.checkIntIsBetween, 100, 120, 90)
    self.assertRaises(Exception, checks.checkIntIsBetween, 100, 30, "hundred")
    self.assertRaises(Exception, checks.checkIntIsBetween, 100, [0], 1200)
    self.assertRaises(Exception, checks.checkIntIsBetween, "one", 0, 1200)

  def test_checkIntIsBetween_notRaiseException(self):
    checks.checkIntIsBetween(0, 0, 1200)
    checks.checkIntIsBetween(0, 0, 0)
    checks.checkIntIsBetween(-2, -5, -1)
    checks.checkIntIsBetween(20, 5, 103)
    checks.checkIntIsBetween(20, 5, 20)
    checks.checkIntIsBetween(5, 5, 20)
    checks.checkIntIsBetween(15, 5, 20)
    checks.checkIntIsBetween(10, -5, 25)
    checks.checkIntIsBetween(0, -1, 30)

  def test_checkIfStringIsAlphaNumerical_invalid(self):
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, "!")
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, [])
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, 23)
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, None)
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, "ha-ha-ha")
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, "[something]")
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, "2+4")
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, "4's street")
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, "hey!")
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, "my text")
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, "nickname_12")
    self.assertRaises(Exception, checks.checkIfStringIsAlphaNumerical, "professional?")

  def test_checkIfStringIsAlphaNumerical_valid(self):
    checks.checkIfStringIsAlphaNumerical("text")
    checks.checkIfStringIsAlphaNumerical("simpleText")
    checks.checkIfStringIsAlphaNumerical("2022")
    checks.checkIfStringIsAlphaNumerical("2errors2fails")
    checks.checkIfStringIsAlphaNumerical("good2go")
    checks.checkIfStringIsAlphaNumerical("number1")
    checks.checkIfStringIsAlphaNumerical("1dev4all100")

  def test_checkIfFile_raiseException(self):
    self.assertRaises(Exception, checks.checkIfFile, 0)
    self.assertRaises(Exception, checks.checkIfFile, None)
    nonExistingFilePath = path.getAbsoluteFilePath(File.FOR_TEST_NON_EXISTING_TEXTFILE1)
    self.assertRaises(Exception, checks.checkIfFile, nonExistingFilePath)
    self.assertRaises(Exception, checks.checkIfFile, [2, 3, 4])
    self.assertRaises(Exception, checks.checkIfFile, True)

  def test_checkIfFile_notRaiseException(self):
    fileWrite = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    checks.checkIfFile(fileWrite)
    fileWrite.close()
    fileRead = open(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1), "r")
    fileRead.close()

  def test_checkIfList_raiseException(self):
    self.assertRaises(Exception, checks.checkIfList, 0)
    self.assertRaises(Exception, checks.checkIfList, None)
    self.assertRaises(Exception, checks.checkIfList, False)
    self.assertRaises(Exception, checks.checkIfList, "hey")

  def test_checkIfList_notRaiseException(self):
    checks.checkIfList([0, 2, 4, 1, 0])
    checks.checkIfList([0])
    checks.checkIfList([])
    checks.checkIfList(["hello", "world"])
    checks.checkIfList([0, "world", False])
    checks.checkIfList(["hey", None])

  def test_checkIfEmptyList_raiseException(self):
    self.assertRaises(Exception, checks.checkIfEmptyList, 0)
    self.assertRaises(Exception, checks.checkIfEmptyList, None)
    self.assertRaises(Exception, checks.checkIfEmptyList, False)
    self.assertRaises(Exception, checks.checkIfEmptyList, "hey")
    self.assertRaises(Exception, checks.checkIfEmptyList, ["hello", "world"])
    self.assertRaises(Exception, checks.checkIfEmptyList, [0, "world", False])
    self.assertRaises(Exception, checks.checkIfEmptyList, ["hey", None])
    self.assertRaises(Exception, checks.checkIfEmptyList, [0, 2, 4, 1, 0])
    self.assertRaises(Exception, checks.checkIfEmptyList, [0])

  def test_checkIfEmptyList_notRaiseException(self):
    checks.checkIfEmptyList([])

  def test_checkIfNonEmptyList_raiseException(self):
    self.assertRaises(Exception, checks.checkIfNonEmptyList, 0)
    self.assertRaises(Exception, checks.checkIfNonEmptyList, None)
    self.assertRaises(Exception, checks.checkIfNonEmptyList, False)
    self.assertRaises(Exception, checks.checkIfNonEmptyList, "hey")
    self.assertRaises(Exception, checks.checkIfNonEmptyList, [])

  def test_checkIfNonEmptyList_validExample(self):
    checks.checkIfNonEmptyList([1, 2, 3])
    checks.checkIfNonEmptyList(["hello"])
    checks.checkIfNonEmptyList([True, "hello", 32])

  def test_checkIfNonEmptyPureListOfType_invalidExamples(self):
    func = checks.checkIfNonEmptyPureListOfType
    self.assertRaises(Exception, func, 12, int)
    self.assertRaises(Exception, func, "Hello", int)
    self.assertRaises(Exception, func, 12, 23)
    self.assertRaises(Exception, func, 12, 12)
    self.assertRaises(Exception, func, True, False)
    self.assertRaises(Exception, func, [1, 2, 3], False)
    self.assertRaises(Exception, func, [False, False, False], False)
    self.assertRaises(Exception, func, [False, False, False], int)
    self.assertRaises(Exception, func, [False, False, False], list)
    self.assertRaises(Exception, func, [2, None, 3], int)
    self.assertRaises(Exception, func, [2, 32, 123, 35, 33, 67, 23, 13, [44, 11], 0, 12, 44, 566, 1256, 335], int)
    self.assertRaises(Exception, func, [None, 3, 4], int)
    self.assertRaises(Exception, func, ["NaN", 3, 4, 5, 6, 7, 1, 2, 3, 4, 1, 2, 2, 5, 6, 1, 3, 5, 6, 3], int)
    self.assertRaises(Exception, func, [2, 3, 4, 5, None], int)
    self.assertRaises(Exception, func, [2, 3, 4, 5, 2, 2, 4, 4, 2, 2, 1, 2, 3, 5, 6, 6, 3, 1, 3, 33, False], int)
    self.assertRaises(Exception, func, [], int)
    self.assertRaises(Exception, func, [], list)
    self.assertRaises(Exception, func, [], None)
    self.assertRaises(Exception, func, [2, 3, 4, 5], bool)
    self.assertRaises(Exception, func, [2, 3, 4, 5], list)
    self.assertRaises(Exception, func, int, [2, 3, 4, 5])

  def test_checkIfNonEmptyPureListOfType_validExamples(self):
    checks.checkIfNonEmptyPureListOfType([1, 2, 3], int)
    checks.checkIfNonEmptyPureListOfType([1], int)
    checks.checkIfNonEmptyPureListOfType([1, 2, 3, 4, 5, 6, 7, 8, 9, 12323, 213123, 1234, 41, 53], int)
    checks.checkIfNonEmptyPureListOfType(["hello"], str)
    checks.checkIfNonEmptyPureListOfType([""], str)
    checks.checkIfNonEmptyPureListOfType(["", "bye", "hi"], str)
    checks.checkIfNonEmptyPureListOfType([True, False, True], bool)

  def test_checkIfPureListOfNonEmptyStrings_nonSense(self):
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, 0)
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, None)
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, False)
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, "hey")
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, ["hello", "my", "world", 12])
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, [True, "hello", "my", "world"])
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, ["hello", "my", ["one", "two"], "world"])
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, [True])
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, [0, 1, 2, 3, 4, 5, 6])

  def test_checkIfPureListOfNonEmptyStrings_invalid(self):
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, [""])
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, ["", "HEY"])
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, ["HEY", ""])
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, ["hello", "", "be happy"])
    self.assertRaises(Exception, checks.checkIfPureListOfNonEmptyStrings, ["don't worry", "be happy", ""])

  def test_checkIfPureListOfNonEmptyStrings_valid(self):
    checks.checkIfPureListOfNonEmptyStrings([])
    checks.checkIfPureListOfNonEmptyStrings(["one"])
    checks.checkIfPureListOfNonEmptyStrings(["1"])
    checks.checkIfPureListOfNonEmptyStrings(["1", "two"])
    checks.checkIfPureListOfNonEmptyStrings(["1", "two", "3", "4", "5"])

  def test_checkIfPureListOfStringsDoesNotContainWhitespaceCharacter_nonSense(self):
    func = checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter
    self.assertRaises(Exception, func, 0)
    self.assertRaises(Exception, func, None)
    self.assertRaises(Exception, func, False)
    self.assertRaises(Exception, func, "hey")
    self.assertRaises(Exception, func, ["hello", "my", "world", 12])
    self.assertRaises(Exception, func, [True, "hello", "my", "world"])
    self.assertRaises(Exception, func, ["hello", "my", ["one", "two"], "world"])
    self.assertRaises(Exception, func, [True])
    self.assertRaises(Exception, func, [0, 1, 2, 3, 4, 5, 6])

  def test_checkIfPureListOfStringsDoesNotContainWhitespaceCharacter_invalid(self):
    func = checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter
    self.assertRaises(Exception, func, [" "])
    self.assertRaises(Exception, func, ["       "])
    self.assertRaises(Exception, func, ["\t       \t"])
    self.assertRaises(Exception, func, ["\t"])
    self.assertRaises(Exception, func, ["\r"])
    self.assertRaises(Exception, func, ["\n"])
    self.assertRaises(Exception, func, ["apple", "Hey you!"])
    self.assertRaises(Exception, func, ["firstLine\nsecondLine", "banana"])
    self.assertRaises(Exception, func, ["cat", "monkey", "python", "\t\tbird"])
    self.assertRaises(Exception, func, ["cat", "monkey", "python", "bird\t"])
    self.assertRaises(Exception, func, ["cat", "monkey", "python", "my\tbird"])

  def test_checkIfPureListOfStringsDoesNotContainWhitespaceCharacter_valid(self):
    checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter([])
    checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter([""])
    checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["1"])
    checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["1", "two"])
    checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["1", "two", "3_das!wfoewffasS", "4", "5", "//"])

  def test_checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter_nonSense(self):
    func = checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter
    self.assertRaises(Exception, func, 0)
    self.assertRaises(Exception, func, None)
    self.assertRaises(Exception, func, False)
    self.assertRaises(Exception, func, "hey")
    self.assertRaises(Exception, func, ["hello", "my", "world", 12])
    self.assertRaises(Exception, func, [True, "hello", "my", "world"])
    self.assertRaises(Exception, func, ["hello", "my", ["one", "two"], "world"])
    self.assertRaises(Exception, func, [True])
    self.assertRaises(Exception, func, [0, 1, 2, 3, 4, 5, 6])

  def test_checkIfPureListOfStringsDoesNotContainWhitespaceCharacter_invalid2(self):
    func = checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter
    self.assertRaises(Exception, func, [""])
    self.assertRaises(Exception, func, [" "])
    self.assertRaises(Exception, func, ["       "])
    self.assertRaises(Exception, func, ["\t       \t"])
    self.assertRaises(Exception, func, ["\t"])
    self.assertRaises(Exception, func, ["\r"])
    self.assertRaises(Exception, func, ["\n"])
    self.assertRaises(Exception, func, ["apple", "Hey you!"])
    self.assertRaises(Exception, func, ["apple", "pear", ""])
    self.assertRaises(Exception, func, ["apple", "", "ananas"])
    self.assertRaises(Exception, func, ["", "detail", "question"])
    self.assertRaises(Exception, func, ["firstLine\nsecondLine", "banana"])
    self.assertRaises(Exception, func, ["cat", "monkey", "python", "\t\tbird"])
    self.assertRaises(Exception, func, ["cat", "monkey", "python", "bird\t"])
    self.assertRaises(Exception, func, ["cat", "monkey", "python", "my\tbird"])

  def test_checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter_valid(self):
    func = checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter
    func([])
    func(["1"])
    func(["1", "two"])
    func(["1", "two", "3_das!wfoewffasS", "4", "5", "//"])

  def test_checkIfTwoNonEmptyStringsAreDifferent_nonSense(self):
    self.assertRaises(Exception, checks.checkIfTwoNonEmptyStringsAreDifferent, False, True)
    self.assertRaises(Exception, checks.checkIfTwoNonEmptyStringsAreDifferent, 45, 2)
    self.assertRaises(Exception, checks.checkIfTwoNonEmptyStringsAreDifferent, None, [])
    self.assertRaises(Exception, checks.checkIfTwoNonEmptyStringsAreDifferent, "test", "")
    self.assertRaises(Exception, checks.checkIfTwoNonEmptyStringsAreDifferent, "", "test")
    self.assertRaises(Exception, checks.checkIfTwoNonEmptyStringsAreDifferent, "", "")

  def test_checkIfTwoNonEmptyStringsAreDifferent_invalid(self):
    self.assertRaises(Exception, checks.checkIfTwoNonEmptyStringsAreDifferent, "test", "test")
    self.assertRaises(Exception, checks.checkIfTwoNonEmptyStringsAreDifferent, "123_abc_!@#", "123_abc_!@#")

  def test_checkIfTwoNonEmptyStringsAreDifferent_valid(self):
    try:
      checks.checkIfTwoNonEmptyStringsAreDifferent("test1", "test2")
      checks.checkIfTwoNonEmptyStringsAreDifferent("1. line", "2. line")
      checks.checkIfTwoNonEmptyStringsAreDifferent("apple", "mushroom")
    except Exception:
      self.fail("checkIfTwoNonEmptyStringsAreDifferent() raised Exception unexpectedly!")

  def test_checkIfPureListOfStrings_raiseException(self):
    self.assertRaises(Exception, checks.checkIfPureListOfStrings, 0)
    self.assertRaises(Exception, checks.checkIfPureListOfStrings, None)
    self.assertRaises(Exception, checks.checkIfPureListOfStrings, False)
    self.assertRaises(Exception, checks.checkIfPureListOfStrings, "hey")
    self.assertRaises(Exception, checks.checkIfPureListOfStrings, ["hello", "my", "world", 12])
    self.assertRaises(Exception, checks.checkIfPureListOfStrings, [True, "hello", "my", "world"])
    self.assertRaises(Exception, checks.checkIfPureListOfStrings, ["hello", "my", ["one", "two"], "world"])
    self.assertRaises(Exception, checks.checkIfPureListOfStrings, [True])
    self.assertRaises(Exception, checks.checkIfPureListOfStrings, [0, 1, 2, 3, 4, 5, 6])

  def test_checkIfPureListOfStrings_notRaiseException(self):
    checks.checkIfPureListOfStrings([])
    checks.checkIfPureListOfStrings([""])
    checks.checkIfPureListOfStrings(["\t"])
    checks.checkIfPureListOfStrings(["X"])
    checks.checkIfPureListOfStrings(["\tHELLO\n"])
    checks.checkIfPureListOfStrings(["one"])
    checks.checkIfPureListOfStrings(["one", "two"])
    checks.checkIfPureListOfStrings(["one", "two", "three"])
    checks.checkIfPureListOfStrings(["one", "\t", "two", "three", "four", "five", "six", "seven", "\n"])

  def test_checkIfNonEmptyPureListOfStrings_raiseException(self):
    self.assertRaises(Exception, checks.checkIfNonEmptyPureListOfStrings, 0)
    self.assertRaises(Exception, checks.checkIfNonEmptyPureListOfStrings, None)
    self.assertRaises(Exception, checks.checkIfNonEmptyPureListOfStrings, False)
    self.assertRaises(Exception, checks.checkIfNonEmptyPureListOfStrings, "hey")
    self.assertRaises(Exception, checks.checkIfNonEmptyPureListOfStrings, ["hello", "my", "world", 12])
    self.assertRaises(Exception, checks.checkIfNonEmptyPureListOfStrings, [True, "hello", "my", "world"])
    self.assertRaises(Exception, checks.checkIfNonEmptyPureListOfStrings, ["hello", "my", ["one", "two"], "world"])
    self.assertRaises(Exception, checks.checkIfNonEmptyPureListOfStrings, [True])
    self.assertRaises(Exception, checks.checkIfNonEmptyPureListOfStrings, [0, 1, 2, 3, 4, 5, 6])
    self.assertRaises(Exception, checks.checkIfNonEmptyPureListOfStrings, [])

  def test_checkIfNonEmptyPureListOfStrings_notRaiseException(self):
    checks.checkIfNonEmptyPureListOfStrings([""])
    checks.checkIfNonEmptyPureListOfStrings(["\t"])
    checks.checkIfNonEmptyPureListOfStrings(["X"])
    checks.checkIfNonEmptyPureListOfStrings(["\tHELLO\n"])
    checks.checkIfNonEmptyPureListOfStrings(["one"])
    checks.checkIfNonEmptyPureListOfStrings(["one", "two"])
    checks.checkIfNonEmptyPureListOfStrings(["one", "two", "three"])
    checks.checkIfNonEmptyPureListOfStrings(["one", "\t", "two", "three", "four", "five", "six", "seven", "\n"])

  def test_checkIfFilePathExists_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    file.close()
    self.assertRaises(Exception, checks.checkIfFilePathExists, file)
    self.assertRaises(Exception, checks.checkIfFilePathExists, "")
    self.assertRaises(Exception, checks.checkIfFilePathExists, None)
    self.assertRaises(Exception, checks.checkIfFilePathExists, 23)
    self.assertRaises(Exception, checks.checkIfFilePathExists, False)
    nonExistingFilePath = path.getAbsoluteFilePath(File.FOR_TEST_NON_EXISTING_TEXTFILE1)
    self.assertRaises(Exception, checks.checkIfFilePathExists, nonExistingFilePath)
    dirPath = path.getAbsoluteDirPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertRaises(Exception, checks.checkIfFilePathExists, dirPath)
    self.assertRaises(Exception, checks.checkIfFilePathExists, dirPath[:-1])
    self.assertRaises(Exception, checks.checkIfFilePathExists, "./" + dirPath)

  def test_checkIfFilePathExists_absolutePath(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    file.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    file.close()
    filePath1abs = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filePath2abs = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    checks.checkIfFilePathExists(filePath1abs)
    checks.checkIfFilePathExists(filePath2abs)

  def test_checkIfFilePathExists_relativePath(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    file.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    file.close()
    found1, relFilePath1 = path.getRelativeFilePathToCurrentWorkingDir(File.FOR_TEST_TEXTFILE1)
    found2, relFilePath2 = path.getRelativeFilePathToCurrentWorkingDir(File.FOR_TEST_TEXTFILE2)
    if found1:
      checks.checkIfFilePathExists(relFilePath1)
    if found2:
      checks.checkIfFilePathExists(relFilePath2)

  def test_checkIfDirectoryPathExists_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    file.close()
    self.assertRaises(Exception, checks.checkIfDirectoryPathExists, file)
    self.assertRaises(Exception, checks.checkIfDirectoryPathExists, "")
    self.assertRaises(Exception, checks.checkIfDirectoryPathExists, None)
    self.assertRaises(Exception, checks.checkIfDirectoryPathExists, 23)
    self.assertRaises(Exception, checks.checkIfDirectoryPathExists, False)
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    nonExistingFilePath = path.getAbsoluteFilePath(File.FOR_TEST_NON_EXISTING_TEXTFILE1)
    nonExistingDirPath = path.getAbsoluteDirPath(Dir.NON_EXISTING_DIRECTORY)
    self.assertRaises(Exception, checks.checkIfDirectoryPathExists, filePath)
    self.assertRaises(Exception, checks.checkIfDirectoryPathExists, nonExistingFilePath)
    self.assertRaises(Exception, checks.checkIfDirectoryPathExists, nonExistingDirPath)

  def test_checkIfDirectoryPathExists_absolutePath(self):
    absDirPath = path.getAbsoluteDirPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    checks.checkIfDirectoryPathExists(absDirPath)
    checks.checkIfDirectoryPathExists(absDirPath[:-1])
    absDirPath = path.getAbsoluteDirPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    checks.checkIfDirectoryPathExists(absDirPath)
    checks.checkIfDirectoryPathExists(absDirPath[:-1])

  def test_checkIfDirectoryPathExists_relativePath(self):
    checks.checkIfDirectoryPathExists(".")
    checks.checkIfDirectoryPathExists("./")
    checks.checkIfDirectoryPathExists("..")
    checks.checkIfDirectoryPathExists("../")
    found, relDirPath = path.getRelativeDirPathToCurrentWorkingDir(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    if not found:
      return
    checks.checkIfDirectoryPathExists(relDirPath)
    checks.checkIfDirectoryPathExists(relDirPath[:-1])
    checks.checkIfDirectoryPathExists("./" + relDirPath)
    found, relDirPath = path.getRelativeDirPathToCurrentWorkingDir(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
    if not found:
      return
    checks.checkIfDirectoryPathExists(relDirPath)
    checks.checkIfDirectoryPathExists(relDirPath[:-1])
    checks.checkIfDirectoryPathExists("./" + relDirPath)

  def test_checkIfChar_invalid(self):
    self.assertRaises(Exception, checks.checkIfChar, 123)
    self.assertRaises(Exception, checks.checkIfChar, False)
    self.assertRaises(Exception, checks.checkIfChar, None)
    self.assertRaises(Exception, checks.checkIfChar, "String")
    self.assertRaises(Exception, checks.checkIfChar, "")
    self.assertRaises(Exception, checks.checkIfChar, "AB")

  def test_checkIfChar_valid(self):
    checks.checkIfChar("\t")
    checks.checkIfChar("X")
    checks.checkIfChar("0")
    checks.checkIfChar("%")
    checks.checkIfChar("*")
    checks.checkIfChar("@")
    checks.checkIfChar("\\")
    checks.checkIfChar("/")
    checks.checkIfChar("\r")
    checks.checkIfChar("\n")
    checks.checkIfChar("h")

  def test_checkIfUserDefinedFunction_invalid(self):
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, 1)
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, {})
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, [1, 2, 3])
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, "string")
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, print)
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, io)
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, sys.path.append)
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, self.assertEqual)
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, type)
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, Dir)
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    self.assertRaises(Exception, checks.checkIfUserDefinedFunction, AutoUnitTest)

  def test_checkIfUserDefinedFunction_valid(self):
    checks.checkIfUserDefinedFunction(checks.checkIfFile)
    checks.checkIfUserDefinedFunction(filerw.getFileWithWritePerm)
    checks.checkIfUserDefinedFunction(path.getRelativeDirPathToCurrentWorkingDir)

  def test_checkIfCallable_invalid(self):
    self.assertRaises(Exception, checks.checkIfCallable, 1)
    self.assertRaises(Exception, checks.checkIfCallable, {})
    self.assertRaises(Exception, checks.checkIfCallable, [1, 2, 3])
    self.assertRaises(Exception, checks.checkIfCallable, "string")

  def test_checkIfCallable_valid(self):
    checks.checkIfCallable(print)
    checks.checkIfCallable(type)
    checks.checkIfCallable(self.test_checkIfCallable_invalid)
    checks.checkIfCallable(self.assertEqual)
    checks.checkIfCallable(checks.checkIfList)
    checks.checkIfCallable(checks.checkIfString)

  def test_checkIfTuple_invalid(self):
    self.assertRaises(Exception, checks.checkIfTuple, True)
    self.assertRaises(Exception, checks.checkIfTuple, None)
    self.assertRaises(Exception, checks.checkIfTuple, "string")
    self.assertRaises(Exception, checks.checkIfTuple, [1, 2, 3])
    self.assertRaises(Exception, checks.checkIfTuple, [None, 2, True])
    self.assertRaises(Exception, checks.checkIfTuple, {})
    self.assertRaises(Exception, checks.checkIfTuple, {"key": "value"})

  def test_checkIfTuple_valid(self):
    checks.checkIfTuple((1, 2))
    checks.checkIfTuple((0, True, False, "string", [], {}, None))
    checks.checkIfTuple((-1, False))
    checks.checkIfTuple((None, None))
    checks.checkIfTuple(([], ""))
    checks.checkIfTuple(([1, 2, 3], {"nr": 1}, (True, False)))

  def test_checkIfDict_invalid(self):
    self.assertRaises(Exception, checks.checkIfDict, True)
    self.assertRaises(Exception, checks.checkIfDict, None)
    self.assertRaises(Exception, checks.checkIfDict, "string")
    self.assertRaises(Exception, checks.checkIfDict, [])
    self.assertRaises(Exception, checks.checkIfDict, [1, 2, 3])
    self.assertRaises(Exception, checks.checkIfDict, [None, 2, True])
    self.assertRaises(Exception, checks.checkIfDict, (None,))
    self.assertRaises(Exception, checks.checkIfDict, (1, 2))
    self.assertRaises(Exception, checks.checkIfDict, (0, True, False, "string", [], {}, None))

  def test_checkIfDict_valid(self):
    checks.checkIfDict({})
    checks.checkIfDict({1: "one"})
    checks.checkIfDict({"one": 1})
    checks.checkIfDict({"zero": None, "one": 1, "two": "zwei"})
    checks.checkIfDict({None: None, "one": 1, 2: "zwei", True: False})

  def test_checkIfString_raiseException(self):
    self.assertRaises(Exception, checks.checkIfString, 123, 3, 10)
    self.assertRaises(Exception, checks.checkIfString, "hello", "empty", 10)
    self.assertRaises(Exception, checks.checkIfString, "hey", 1, None)
    self.assertRaises(Exception, checks.checkIfString, "hey", -3, 10)
    self.assertRaises(Exception, checks.checkIfString, "", -3, 10)
    self.assertRaises(Exception, checks.checkIfString, "hey", 20, 2)
    self.assertRaises(Exception, checks.checkIfString, "hey", -2, -1)
    self.assertRaises(Exception, checks.checkIfString, "hey", 5, 1500)
    self.assertRaises(Exception, checks.checkIfString, "", 1, 21)
    self.assertRaises(Exception, checks.checkIfString, "this string is intended to represent a longer one", 5, 15)

  def test_checkIfString_notRaiseException(self):
    checks.checkIfString("hey", 3, 10)
    checks.checkIfString("hey", 0, 3)
    checks.checkIfString("", 0, 23)
    checks.checkIfString("hello", 0, 12)
    checks.checkIfString("hello", 3, 20)
    checks.checkIfString("hello", 5, 5)

  def test_checkIfStringDoesNotContainAnySubstringFromList_nonSense(self):
    func = checks.checkIfStringDoesNotContainAnySubstringFromList
    self.assertRaises(Exception, func, 123, 3, 10, ["/"])
    self.assertRaises(Exception, func, "Hello", 1, 15, "el")
    self.assertRaises(Exception, func, "Hello", 1, 15, "abc")
    self.assertRaises(Exception, func, "Hello", 1, 15, None)
    self.assertRaises(Exception, func, "Hello", 1, 15, False)
    self.assertRaises(Exception, func, "Hello", 1, 15, 2)
    self.assertRaises(Exception, func, "hello", "empty", 10, ["notMatch"])
    self.assertRaises(Exception, func, "hey", 1, None, ["notMatch"])
    self.assertRaises(Exception, func, "hey", -3, 10, ["notMatch"])
    self.assertRaises(Exception, func, "", -3, 10, ["notMatch"])
    self.assertRaises(Exception, func, "hey", 20, 2, ["notMatch"])
    self.assertRaises(Exception, func, "hey", -2, -1, ["notMatch"])
    self.assertRaises(Exception, func, "hey", 5, 1500, ["notMatch"])
    self.assertRaises(Exception, func, "", 1, 21, ["notMatch"])
    self.assertRaises(Exception, func, "this string is intended to represent a longer one", 5, 15, ["^_^"])
    self.assertRaises(Exception, func, "Hello", 3, 21, ["notMatch", 2])
    self.assertRaises(Exception, func, "Hello", 3, 21, [None])
    self.assertRaises(Exception, func, "Hello", 3, 21, [True, "notMatch"])
    self.assertRaises(Exception, func, "Hello", 3, 21, ["notMatch", 2, "bye"])
    self.assertRaises(Exception, func, "Hello", 3, 21, [None, "notMatch", 2])

  def test_checkIfStringDoesNotContainAnySubstringFromList_containsString(self):
    self.assertRaises(Exception, checks.checkIfStringDoesNotContainAnySubstringFromList, "Hello", 3, 21, ["H"])
    self.assertRaises(Exception, checks.checkIfStringDoesNotContainAnySubstringFromList, "Hello", 2, 21, ["./", "H"])
    self.assertRaises(Exception, checks.checkIfStringDoesNotContainAnySubstringFromList, "Hello", 3, 8, ["y", "H", "x"])
    self.assertRaises(Exception, checks.checkIfStringDoesNotContainAnySubstringFromList, "Hello", 1, 121, ["hey", "hell", "H", "bye"])
    self.assertRaises(Exception, checks.checkIfStringDoesNotContainAnySubstringFromList, "Hello", 1, 11, ["hey", "Hell", "bye"])
    self.assertRaises(Exception, checks.checkIfStringDoesNotContainAnySubstringFromList, "Hello", 0, 21, ["ell", "Hell", "H", "He"])

  def test_checkIfStringDoesNotContainAnySubstringFromList_valid(self):
    checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 5, 5, [])
    checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 5, 5, ["hello"])
    checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 5, 5, ["hell", "elo", "L", "LO", "hello"])
    checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 5, 5, ["abcd", "\n", "\t", "bye"])

  def test_checkIfAllNoneOrString_raiseException(self):
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, "not a list", 3, 10)
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, [], 0, 10)
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, ["hello", "hey", "hi"], 3, 10)
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, ["", "hello"], 0, 2)
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, ["heyho", "hello"], 0, 4)
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, ["heyho", "hello"], 10, 22)
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, ["hello"], 6, 6)
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, ["hello", "bye", None], 0, 16)
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, ["hello", None, "bye"], 0, 16)
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, [None, "hello", "bye"], 0, 16)
    self.assertRaises(Exception, checks.checkIfAllNoneOrString, [None, "im a lonely string :(", None], 0, 16)

  def test_checkIfAllNoneOrString_notRaiseException(self):
    checks.checkIfAllNoneOrString([None], 3, 10)
    checks.checkIfAllNoneOrString([None, None], 0, 10)
    checks.checkIfAllNoneOrString([None, None, None], 10, 100)
    checks.checkIfAllNoneOrString([""], 0, 0)
    checks.checkIfAllNoneOrString([""], 0, 10)
    checks.checkIfAllNoneOrString(["hello"], 0, 10)
    checks.checkIfAllNoneOrString(["hello", ""], 0, 10)
    checks.checkIfAllNoneOrString(["hello", "hey"], 3, 5)
    checks.checkIfAllNoneOrString(["hello", "hey", "hi", "k", ""], 0, 15)

  def test_checkIfValidJsonFile_nonSense(self):
    self.assertRaises(Exception, checks.checkIfValidJsonFile, "test.json")
    self.assertRaises(Exception, checks.checkIfValidJsonFile, None)
    self.assertRaises(Exception, checks.checkIfValidJsonFile, "{}")
    self.assertRaises(Exception, checks.checkIfValidJsonFile, False)

  def test_checkIfValidJsonFile_invalid(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, [""])
    file = open(filePath, "r")
    self.assertRaises(Exception, checks.checkIfValidJsonFile, file)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["hello internet"])
    file = open(filePath, "r")
    self.assertRaises(Exception, checks.checkIfValidJsonFile, file)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "true", "}"])
    file = open(filePath, "r")
    self.assertRaises(Exception, checks.checkIfValidJsonFile, file)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["1", "2", "3", "4"])
    file = open(filePath, "r")
    self.assertRaises(Exception, checks.checkIfValidJsonFile, file)

  def test_checkIfValidJsonFile_valid(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "}"])
    file = open(filePath, "r")
    checks.checkIfValidJsonFile(file)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "\"numbers\": ", "[1,2,3,4,5]", "}"])
    file = open(filePath, "r")
    checks.checkIfValidJsonFile(file)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "\"boolValue\": ", "true", "}"])
    file = open(filePath, "r")
    checks.checkIfValidJsonFile(file)

  def test_checkIfValidJsonFileByFilePath_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "r")
    self.assertRaises(Exception, checks.checkIfValidJsonFileByFilePath, file)
    self.assertRaises(Exception, checks.checkIfValidJsonFileByFilePath, "notExistingFile.extension")
    self.assertRaises(Exception, checks.checkIfValidJsonFileByFilePath, None)
    self.assertRaises(Exception, checks.checkIfValidJsonFileByFilePath, 12)
    self.assertRaises(Exception, checks.checkIfValidJsonFileByFilePath, False)

  def test_checkIfValidJsonFileByFilePath_invalid(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, [""])
    self.assertRaises(Exception, checks.checkIfValidJsonFileByFilePath, filePath)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["hello internet"])
    self.assertRaises(Exception, checks.checkIfValidJsonFileByFilePath, filePath)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath,
                                                                ["{", "true", "}"])
    self.assertRaises(Exception, checks.checkIfValidJsonFileByFilePath, filePath)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath,
                                                                ["1", "2", "3", "4"])
    self.assertRaises(Exception, checks.checkIfValidJsonFileByFilePath, filePath)

  def test_checkIfValidJsonFileByFilePath_valid(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "}"])
    checks.checkIfValidJsonFileByFilePath(filePath)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "\"numbers\": ", "[1,2,3,4,5]", "}"])
    checks.checkIfValidJsonFileByFilePath(filePath)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "\"boolValue\": ", "true", "}"])
    checks.checkIfValidJsonFileByFilePath(filePath)

  def test_checkIfValidJsonFileByFilePath_returnedJson(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "\"boolValue\": ", "true", "}"])
    jsonVals = checks.checkIfValidJsonFileByFilePath(filePath)
    self.assertEqual(jsonVals["boolValue"], True)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "\"intValue\": ", "23", "}"])
    jsonVals = checks.checkIfValidJsonFileByFilePath(filePath)
    self.assertEqual(jsonVals["intValue"], 23)

  def test_checkIfValidJsonFile_returnedJson(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "\"boolValue\": ", "true", "}"])
    file = open(filePath, "r")
    jsonVals = checks.checkIfValidJsonFile(file)
    self.assertEqual(jsonVals["boolValue"], True)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "\"intValue\": ", "23", "}"])
    file = open(filePath, "r")
    jsonVals = checks.checkIfValidJsonFile(file)
    self.assertEqual(jsonVals["intValue"], 23)

  def test_checkIfType_invalid(self):
    filerw.createOrOverwriteWithEmptyFileByType(File.FOR_TEST_TEXTFILE1)
    file = open(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1), "r")
    self.assertRaises(Exception, checks.checkIfType, file, 12)
    self.assertRaises(Exception, checks.checkIfType, 12, "notExistingFile.extension")
    self.assertRaises(Exception, checks.checkIfType, None, None)
    self.assertRaises(Exception, checks.checkIfType, True, False)
    self.assertRaises(Exception, checks.checkIfType, False, Exception)

  def test_checkIfType_wrongType(self):
    filerw.createOrOverwriteWithEmptyFileByType(File.FOR_TEST_TEXTFILE1)
    file = open(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1), "r")
    self.assertRaises(Exception, checks.checkIfType, file, int)
    self.assertRaises(Exception, checks.checkIfType, 12, str)
    self.assertRaises(Exception, checks.checkIfType, None, list)
    self.assertRaises(Exception, checks.checkIfType, True, bytearray)
    self.assertRaises(Exception, checks.checkIfType, False, io.TextIOWrapper)

  def test_checkIfType_correctType(self):
    filerw.createOrOverwriteWithEmptyFileByType(File.FOR_TEST_TEXTFILE1)
    file = open(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1), "r")
    checks.checkIfType(file, io.TextIOWrapper)
    checks.checkIfType(12, int)
    checks.checkIfType("", str)
    checks.checkIfType(True, bool)
    checks.checkIfType([], list)
    checks.checkIfType([12], list)
    checks.checkIfType([12, "array"], list)

  def test_checkIfAnyType_nonSense(self):
    self.assertRaises(Exception, checks.checkIfAnyType, 2, 3)
    self.assertRaises(Exception, checks.checkIfAnyType, 2, int)
    self.assertRaises(Exception, checks.checkIfAnyType, 2, None)
    self.assertRaises(Exception, checks.checkIfAnyType, 2, [1, 2, 3])
    self.assertRaises(Exception, checks.checkIfAnyType, 2, [True, 2, None])

  def test_checkIfAnyType_notMatch(self):
    self.assertRaises(Exception, checks.checkIfAnyType, 2, [])
    self.assertRaises(Exception, checks.checkIfAnyType, 2, [bool])
    self.assertRaises(Exception, checks.checkIfAnyType, 2, [list])
    self.assertRaises(Exception, checks.checkIfAnyType, 2, [str])
    self.assertRaises(Exception, checks.checkIfAnyType, 2, [list, bool])
    self.assertRaises(Exception, checks.checkIfAnyType, "string", [list, bool])
    self.assertRaises(Exception, checks.checkIfAnyType, "string", [list, bool, int])
    self.assertRaises(Exception, checks.checkIfAnyType, 23, [list, bool, str])
    self.assertRaises(Exception, checks.checkIfAnyType, {}, [list, bool, str, int])

  def test_checkIfAnyType_match(self):
    checks.checkIfAnyType({}, [dict])
    checks.checkIfAnyType({}, [int, dict])
    checks.checkIfAnyType({}, [dict, int])
    checks.checkIfAnyType(23, [dict, int])
    checks.checkIfAnyType(23, [int])
    checks.checkIfAnyType(["one", "two", "three"], [list])
    checks.checkIfAnyType([1, 2, 3], [list])
    checks.checkIfAnyType(True, [bool])
    checks.checkIfAnyType(False, [bool])
    checks.checkIfAnyType("string", [str])
    checks.checkIfAnyType("string", [int, str, list, dict])
    checks.checkIfAnyType("string", [int, list, dict, bool, str])
    checks.checkIfAnyType("string", [int, list, dict, str, bool])

  def test_checkIfBoolean_wrongType(self):
    self.assertRaises(Exception, checks.checkIfBoolean, 2)
    self.assertRaises(Exception, checks.checkIfBoolean, 2.2)
    self.assertRaises(Exception, checks.checkIfBoolean, None)
    self.assertRaises(Exception, checks.checkIfBoolean, "")
    self.assertRaises(Exception, checks.checkIfBoolean, "0")
    self.assertRaises(Exception, checks.checkIfBoolean, [])

  def test_checkIfBoolean_valid(self):
    checks.checkIfBoolean(True)
    checks.checkIfBoolean(False)

  def test_checkIfTrue_wrongType(self):
    self.assertRaises(Exception, checks.checkIfTrue, 2, "This is not two!")
    self.assertRaises(Exception, checks.checkIfTrue, 2 == 3, 2)
    self.assertRaises(Exception, checks.checkIfTrue, True, False)

  def test_checkIfTrue_emptyOrVeryShortString(self):
    self.assertRaises(Exception, checks.checkIfTrue, 2 == 2, "")
    self.assertRaises(Exception, checks.checkIfTrue, 2 == 2, "A")
    self.assertRaises(Exception, checks.checkIfTrue, 2 == 2, "AB")

  def test_checkIfTrue_false(self):
    with self.assertRaises(Exception) as exc:
      checks.checkIfTrue(2 > 20, "two is not greater than twenty")
    self.assertEqual(exc.exception.args[0], "two is not greater than twenty")
    with self.assertRaises(Exception) as exc:
      checks.checkIfTrue(5 != 5, "five is equal with five")
    self.assertEqual(exc.exception.args[0], "five is equal with five")

  def test_checkIfTrue_true(self):
    checks.checkIfTrue(2 < 20, "two is not greater than twenty!")
    checks.checkIfTrue(-4 == -4, "-4 is equal to -4")
