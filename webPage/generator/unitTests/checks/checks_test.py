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
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(0, 1, 4)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(-20, 10, 55)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(20, -55, -15)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(-30, -15, -45)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(10, 2, 9)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(-120, 20, 90)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(100, 120, 90)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(100, 30, "hundred")
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(100, [0], 1200)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween("one", 0, 1200)

  def test_checkIntIsBetween_notRaiseException(self):
    try:
      checks.checkIntIsBetween(0, 0, 1200)
      checks.checkIntIsBetween(0, 0, 0)
      checks.checkIntIsBetween(-2, -5, -1)
      checks.checkIntIsBetween(20, 5, 103)
      checks.checkIntIsBetween(20, 5, 20)
      checks.checkIntIsBetween(5, 5, 20)
      checks.checkIntIsBetween(15, 5, 20)
    except Exception:
      self.fail("checkIntIsBetween() raised Exception unexpectedly!")

  def test_checkIfStringIsAlphaNumerical_invalid(self):
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical("!")
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical([])
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical(23)
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical(None)
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical("ha-ha-ha")
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical("[something]")
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical("2+4")
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical("4's street")
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical("hey!")
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical("my text")
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical("nickname_12")
    with self.assertRaises(Exception):
      checks.checkIfStringIsAlphaNumerical("professional?")

  def test_checkIfStringIsAlphaNumerical_valid(self):
    try:
      checks.checkIfStringIsAlphaNumerical("text")
      checks.checkIfStringIsAlphaNumerical("simpleText")
      checks.checkIfStringIsAlphaNumerical("2022")
      checks.checkIfStringIsAlphaNumerical("2errors2fails")
      checks.checkIfStringIsAlphaNumerical("good2go")
      checks.checkIfStringIsAlphaNumerical("number1")
      checks.checkIfStringIsAlphaNumerical("1dev4all100")
    except Exception:
      self.fail("checkIfStringIsAlphaNumerical() raised Exception unexpectedly!")

  def test_checkIfFile_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfFile(0)
    with self.assertRaises(Exception):
      checks.checkIfFile(None)
    nonExistingFilePath = path.getAbsoluteFilePath(File.FOR_TEST_NON_EXISTING_TEXTFILE1)
    with self.assertRaises(Exception):
      checks.checkIfFile(nonExistingFilePath)
    with self.assertRaises(Exception):
      checks.checkIfFile([2, 3, 4])
    with self.assertRaises(Exception):
      checks.checkIfFile(True)

  def test_checkIfFile_notRaiseException(self):
    try:
      fileWrite = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
      checks.checkIfFile(fileWrite)
      fileWrite.close()
      fileRead = open(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1), "r")
      fileRead.close()
    except Exception:
      self.fail("checkIfFile() raised Exception unexpectedly!")

  def test_checkIfList_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfList(0)
    with self.assertRaises(Exception):
      checks.checkIfList(None)
    with self.assertRaises(Exception):
      checks.checkIfList(False)
    with self.assertRaises(Exception):
      checks.checkIfList("hey")

  def test_checkIfList_notRaiseException(self):
    try:
      checks.checkIfList([0, 2, 4, 1, 0])
      checks.checkIfList([0])
      checks.checkIfList([])
      checks.checkIfList(["hello", "world"])
      checks.checkIfList([0, "world", False])
      checks.checkIfList(["hey", None])
    except Exception:
      self.fail("checkIfList() raised Exception unexpectedly!")

  def test_checkIfEmptyList_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfEmptyList(0)
    with self.assertRaises(Exception):
      checks.checkIfEmptyList(None)
    with self.assertRaises(Exception):
      checks.checkIfEmptyList(False)
    with self.assertRaises(Exception):
      checks.checkIfEmptyList("hey")
    with self.assertRaises(Exception):
      checks.checkIfEmptyList(["hello", "world"])
    with self.assertRaises(Exception):
      checks.checkIfEmptyList([0, "world", False])
    with self.assertRaises(Exception):
      checks.checkIfEmptyList(["hey", None])
    with self.assertRaises(Exception):
      checks.checkIfEmptyList([0, 2, 4, 1, 0])
    with self.assertRaises(Exception):
      checks.checkIfEmptyList([0])

  def test_checkIfEmptyList_notRaiseException(self):
    try:
      checks.checkIfEmptyList([])
    except Exception:
      self.fail("checkIfList() raised Exception unexpectedly!")

  def test_checkIfNonEmptyList_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyList(0)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyList(None)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyList(False)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyList("hey")
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyList([])

  def test_checkIfNonEmptyList_validExample(self):
    try:
      checks.checkIfNonEmptyList([1, 2, 3])
      checks.checkIfNonEmptyList(["hello"])
      checks.checkIfNonEmptyList([True, "hello", 32])
    except Exception:
      self.fail("checkIfNonEmptyList() raised Exception unexpectedly!")

  def test_checkIfNonEmptyPureListOfType_invalidExamples(self):
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType(12, int)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType("Hello", int)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType(12, 23)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType(12, 12)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType(True, False)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([1, 2, 3], False)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([False, False, False], False)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([False, False, False], int)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([False, False, False], list)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([2, None, 3], int)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([2, 32, 123, 35, 33, 67, 23, 13, [44, 11], 0, 12, 44, 566, 1256, 335], int)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([None, 3, 4], int)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType(["NaN", 3, 4, 5, 6, 7, 1, 2, 3, 4, 1, 2, 2, 5, 6, 1, 3, 5, 6, 3], int)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([2, 3, 4, 5, None], int)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([2, 3, 4, 5, 2, 2, 4, 4, 2, 2, 1, 2, 3, 5, 6, 6, 3, 1, 3, 33, False], int)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([], int)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([], list)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([], None)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([2, 3, 4, 5], bool)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType([2, 3, 4, 5], list)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfType(int, [2, 3, 4, 5])

  def test_checkIfNonEmptyPureListOfType_validExamples(self):
    try:
      checks.checkIfNonEmptyPureListOfType([1, 2, 3], int)
      checks.checkIfNonEmptyPureListOfType([1], int)
      checks.checkIfNonEmptyPureListOfType([1, 2, 3, 4, 5, 6, 7, 8, 9, 12323, 213123, 1234, 41, 53], int)
      checks.checkIfNonEmptyPureListOfType(["hello"], str)
      checks.checkIfNonEmptyPureListOfType([""], str)
      checks.checkIfNonEmptyPureListOfType(["", "bye", "hi"], str)
      checks.checkIfNonEmptyPureListOfType([True, False, True], bool)
    except Exception:
      self.fail("checkIfNonEmptyPureListOfType() raised Exception unexpectedly!")

  def test_checkIfPureListOfNonEmptyStrings_nonSense(self):
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings(0)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings(None)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings(False)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings("hey")
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings(["hello", "my", "world", 12])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings([True, "hello", "my", "world"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings(["hello", "my", ["one", "two"], "world"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings([True])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings([0, 1, 2, 3, 4, 5, 6])

  def test_checkIfPureListOfNonEmptyStrings_invalid(self):
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings([""])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings(["", "HEY"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings(["HEY", ""])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings(["hello", "", "be happy"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStrings(["don't worry", "be happy", ""])

  def test_checkIfPureListOfNonEmptyStrings_valid(self):
    try:
      checks.checkIfPureListOfNonEmptyStrings([])
      checks.checkIfPureListOfNonEmptyStrings(["one"])
      checks.checkIfPureListOfNonEmptyStrings(["1"])
      checks.checkIfPureListOfNonEmptyStrings(["1", "two"])
      checks.checkIfPureListOfNonEmptyStrings(["1", "two", "3", "4", "5"])
    except Exception:
      self.fail("checkIfPureListOfNonEmptyStrings() raised Exception unexpectedly!")

  def test_checkIfPureListOfStringsDoesNotContainWhitespaceCharacter_nonSense(self):
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(0)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(None)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(False)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter("hey")
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["hello", "my", "world", 12])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter([True, "hello", "my", "world"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["hello", "my", ["one", "two"], "world"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter([True])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter([0, 1, 2, 3, 4, 5, 6])

  def test_checkIfPureListOfStringsDoesNotContainWhitespaceCharacter_invalid(self):
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter([" "])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["       "])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["\t       \t"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["\t"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["\r"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["\n"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["apple", "Hey you!"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["firstLine\nsecondLine", "banana"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["cat", "monkey", "python", "\t\tbird"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["cat", "monkey", "python", "bird\t"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["cat", "monkey", "python", "my\tbird"])

  def test_checkIfPureListOfStringsDoesNotContainWhitespaceCharacter_valid(self):
    try:
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter([])
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter([""])
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["1"])
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["1", "two"])
      checks.checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(["1", "two", "3_das!wfoewffasS", "4", "5", "//"])
    except Exception:
      self.fail("checkIfPureListOfNonEmptyStrings() raised Exception unexpectedly!")

  def test_checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter_nonSense(self):
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(0)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(None)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(False)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter("hey")
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["hello", "my", "world", 12])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter([True, "hello", "my", "world"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["hello", "my", ["one", "two"], "world"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter([True])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter([0, 1, 2, 3, 4, 5, 6])

  def test_checkIfPureListOfStringsDoesNotContainWhitespaceCharacter_invalid2(self):
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter([""])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter([" "])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["       "])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["\t       \t"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["\t"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["\r"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["\n"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["apple", "Hey you!"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["apple", "pear", ""])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["apple", "", "ananas"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["", "detail", "question"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["firstLine\nsecondLine", "banana"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["cat", "monkey", "python", "\t\tbird"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["cat", "monkey", "python", "bird\t"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["cat", "monkey", "python", "my\tbird"])

  def test_checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter_valid(self):
    try:
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter([])
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["1"])
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["1", "two"])
      checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(["1", "two", "3_das!wfoewffasS",
                                                                                "4", "5", "//"])
    except Exception:
      self.fail("checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter() raised Exception unexpectedly!")

  def test_checkIfTwoNonEmptyStringsAreDifferent_nonSense(self):
    with self.assertRaises(Exception):
      checks.checkIfTwoNonEmptyStringsAreDifferent(False, True)
    with self.assertRaises(Exception):
      checks.checkIfTwoNonEmptyStringsAreDifferent(45, 2)
    with self.assertRaises(Exception):
      checks.checkIfTwoNonEmptyStringsAreDifferent(None, [])
    with self.assertRaises(Exception):
      checks.checkIfTwoNonEmptyStringsAreDifferent("test", "")
    with self.assertRaises(Exception):
      checks.checkIfTwoNonEmptyStringsAreDifferent("", "test")
    with self.assertRaises(Exception):
      checks.checkIfTwoNonEmptyStringsAreDifferent("", "")

  def test_checkIfTwoNonEmptyStringsAreDifferent_invalid(self):
    with self.assertRaises(Exception):
      checks.checkIfTwoNonEmptyStringsAreDifferent("test", "test")
    with self.assertRaises(Exception):
      checks.checkIfTwoNonEmptyStringsAreDifferent("123_abc_!@#", "123_abc_!@#")

  def test_checkIfTwoNonEmptyStringsAreDifferent_valid(self):
    try:
      checks.checkIfTwoNonEmptyStringsAreDifferent("test1", "test2")
      checks.checkIfTwoNonEmptyStringsAreDifferent("1. line", "2. line")
      checks.checkIfTwoNonEmptyStringsAreDifferent("apple", "mushroom")
    except Exception:
      self.fail("checkIfTwoNonEmptyStringsAreDifferent() raised Exception unexpectedly!")

  def test_checkIfPureListOfStrings_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings(0)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings(None)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings(False)
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings("hey")
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings(["hello", "my", "world", 12])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings([True, "hello", "my", "world"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings(["hello", "my", ["one", "two"], "world"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings([True])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings([0, 1, 2, 3, 4, 5, 6])

  def test_checkIfPureListOfStrings_notRaiseException(self):
    try:
      checks.checkIfPureListOfStrings([])
      checks.checkIfPureListOfStrings([""])
      checks.checkIfPureListOfStrings(["\t"])
      checks.checkIfPureListOfStrings(["X"])
      checks.checkIfPureListOfStrings(["\tHELLO\n"])
      checks.checkIfPureListOfStrings(["one"])
      checks.checkIfPureListOfStrings(["one", "two"])
      checks.checkIfPureListOfStrings(["one", "two", "three"])
      checks.checkIfPureListOfStrings(["one", "\t", "two", "three", "four", "five", "six", "seven", "\n"])
    except Exception:
      self.fail("checkIfPureListOfStrings() raised Exception unexpectedly!")

  def test_checkIfNonEmptyPureListOfStrings_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfStrings(0)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfStrings(None)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfStrings(False)
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfStrings("hey")
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfStrings(["hello", "my", "world", 12])
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfStrings([True, "hello", "my", "world"])
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfStrings(["hello", "my", ["one", "two"], "world"])
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfStrings([True])
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfStrings([0, 1, 2, 3, 4, 5, 6])
    with self.assertRaises(Exception):
      checks.checkIfNonEmptyPureListOfStrings([])

  def test_checkIfNonEmptyPureListOfStrings_notRaiseException(self):
    try:
      checks.checkIfNonEmptyPureListOfStrings([""])
      checks.checkIfNonEmptyPureListOfStrings(["\t"])
      checks.checkIfNonEmptyPureListOfStrings(["X"])
      checks.checkIfNonEmptyPureListOfStrings(["\tHELLO\n"])
      checks.checkIfNonEmptyPureListOfStrings(["one"])
      checks.checkIfNonEmptyPureListOfStrings(["one", "two"])
      checks.checkIfNonEmptyPureListOfStrings(["one", "two", "three"])
      checks.checkIfNonEmptyPureListOfStrings(["one", "\t", "two", "three", "four", "five", "six", "seven", "\n"])
    except Exception:
      self.fail("checkIfPureListOfStrings() raised Exception unexpectedly!")

  def test_checkIfFilePathExists_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    file.close()
    with self.assertRaises(Exception):
      checks.checkIfFilePathExists(file)
    with self.assertRaises(Exception):
      checks.checkIfFilePathExists("")
    with self.assertRaises(Exception):
      checks.checkIfFilePathExists(None)
    with self.assertRaises(Exception):
      checks.checkIfFilePathExists(23)
    with self.assertRaises(Exception):
      checks.checkIfFilePathExists(False)
    nonExistingFilePath = path.getAbsoluteFilePath(File.FOR_TEST_NON_EXISTING_TEXTFILE1)
    with self.assertRaises(Exception):
      checks.checkIfFilePathExists(nonExistingFilePath)
    dirPath = path.getAbsoluteDirPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEST1)
    with self.assertRaises(Exception):
      checks.checkIfFilePathExists(dirPath)
    with self.assertRaises(Exception):
      checks.checkIfFilePathExists(dirPath[:-1])
    with self.assertRaises(Exception):
      checks.checkIfFilePathExists("./" + dirPath)

  def test_checkIfFilePathExists_absolutePath(self):
    try:
      file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
      file.close()
      file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
      file.close()
      filePath1abs = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
      filePath2abs = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
      checks.checkIfFilePathExists(filePath1abs)
      checks.checkIfFilePathExists(filePath2abs)
    except Exception:
      self.fail("checkIfFilePathExists() raised Exception unexpectedly!")

  def test_checkIfFilePathExists_relativePath(self):
    try:
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
    except Exception:
      self.fail("checkIfFilePathExists() raised Exception unexpectedly!")

  def test_checkIfDirectoryPathExists_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    file.close()
    with self.assertRaises(Exception):
      checks.checkIfDirectoryPathExists(file)
    with self.assertRaises(Exception):
      checks.checkIfDirectoryPathExists("")
    with self.assertRaises(Exception):
      checks.checkIfDirectoryPathExists(None)
    with self.assertRaises(Exception):
      checks.checkIfDirectoryPathExists(23)
    with self.assertRaises(Exception):
      checks.checkIfDirectoryPathExists(False)
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    nonExistingFilePath = path.getAbsoluteFilePath(File.FOR_TEST_NON_EXISTING_TEXTFILE1)
    nonExistingDirPath = path.getAbsoluteDirPath(Dir.NON_EXISTING_DIRECTORY)
    with self.assertRaises(Exception):
      checks.checkIfDirectoryPathExists(filePath)
    with self.assertRaises(Exception):
      checks.checkIfDirectoryPathExists(nonExistingFilePath)
    with self.assertRaises(Exception):
      checks.checkIfDirectoryPathExists(nonExistingDirPath)

  def test_checkIfDirectoryPathExists_absolutePath(self):
    try:
      absDirPath = path.getAbsoluteDirPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
      checks.checkIfDirectoryPathExists(absDirPath)
      checks.checkIfDirectoryPathExists(absDirPath[:-1])
      absDirPath = path.getAbsoluteDirPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2)
      checks.checkIfDirectoryPathExists(absDirPath)
      checks.checkIfDirectoryPathExists(absDirPath[:-1])
    except Exception:
      self.fail("checkIfDirectoryPathExists() raised Exception unexpectedly!")

  def test_checkIfDirectoryPathExists_relativePath(self):
    try:
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
    except Exception:
      self.fail("checkIfDirectoryPathExists() raised Exception unexpectedly!")

  def test_checkIfChar_invalid(self):
    with self.assertRaises(Exception):
      checks.checkIfChar(123)
    with self.assertRaises(Exception):
      checks.checkIfChar(False)
    with self.assertRaises(Exception):
      checks.checkIfChar(None)
    with self.assertRaises(Exception):
      checks.checkIfChar("String")
    with self.assertRaises(Exception):
      checks.checkIfChar("")
    with self.assertRaises(Exception):
      checks.checkIfChar("AB")

  def test_checkIfChar_valid(self):
    try:
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
    except Exception:
      self.fail("checkIfChar() raised Exception unexpectedly!")

  def test_checkIfCallable_invalid(self):
    self.assertRaises(Exception, checks.checkIfCallable, 1)
    self.assertRaises(Exception, checks.checkIfCallable, {})
    self.assertRaises(Exception, checks.checkIfCallable, [1, 2, 3])
    self.assertRaises(Exception, checks.checkIfCallable, "string")

  def test_checkIfCallable_valid(self):
    try:
      checks.checkIfCallable(print)
      checks.checkIfCallable(type)
      checks.checkIfCallable(self.test_checkIfCallable_invalid)
      checks.checkIfCallable(self.assertEqual)
      checks.checkIfCallable(checks.checkIfList)
      checks.checkIfCallable(checks.checkIfString)
    except Exception:
      self.fail("checkIfCallable() raised Exception unexpectedly!")

  def test_checkIfTuple_invalid(self):
    self.assertRaises(Exception, checks.checkIfTuple, True)
    self.assertRaises(Exception, checks.checkIfTuple, None)
    self.assertRaises(Exception, checks.checkIfTuple, "string")
    self.assertRaises(Exception, checks.checkIfTuple, [1, 2, 3])
    self.assertRaises(Exception, checks.checkIfTuple, [None, 2, True])
    self.assertRaises(Exception, checks.checkIfTuple, {})
    self.assertRaises(Exception, checks.checkIfTuple, {"key": "value"})

  def test_checkIfTuple_valid(self):
    try:
      checks.checkIfTuple((1, 2))
      checks.checkIfTuple((0, True, False, "string", [], {}, None))
      checks.checkIfTuple((-1, False))
      checks.checkIfTuple((None, None))
      checks.checkIfTuple(([], ""))
      checks.checkIfTuple(([1, 2, 3], {"nr": 1}, (True, False)))
    except Exception:
      self.fail("checkIfTuple() raised Exception unexpectedly!")

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
    try:
      checks.checkIfDict({})
      checks.checkIfDict({1: "one"})
      checks.checkIfDict({"one": 1})
      checks.checkIfDict({"zero": None, "one": 1, "two": "zwei"})
      checks.checkIfDict({None: None, "one": 1, 2: "zwei", True: False})
    except Exception:
      self.fail("checkIfDict() raised Exception unexpectedly!")

  def test_checkIfString_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfString(123, 3, 10)
    with self.assertRaises(Exception):
      checks.checkIfString("hello", "empty", 10)
    with self.assertRaises(Exception):
      checks.checkIfString("hey", 1, None)
    with self.assertRaises(Exception):
      checks.checkIfString("hey", -3, 10)
    with self.assertRaises(Exception):
      checks.checkIfString("", -3, 10)
    with self.assertRaises(Exception):
      checks.checkIfString("hey", 20, 2)
    with self.assertRaises(Exception):
      checks.checkIfString("hey", -2, -1)
    with self.assertRaises(Exception):
      checks.checkIfString("hey", 5, 1500)
    with self.assertRaises(Exception):
      checks.checkIfString("", 1, 21)
    with self.assertRaises(Exception):
      checks.checkIfString("this string is intended to represent a longer one", 5, 15)

  def test_checkIfString_notRaiseException(self):
    try:
      checks.checkIfString("hey", 3, 10)
      checks.checkIfString("hey", 0, 3)
      checks.checkIfString("", 0, 23)
      checks.checkIfString("hello", 0, 12)
      checks.checkIfString("hello", 3, 20)
      checks.checkIfString("hello", 5, 5)
    except Exception:
      self.fail("checkIfString() raised Exception unexpectedly!")

  def test_checkIfStringDoesNotContainAnySubstringFromList_nonSense(self):
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList(123, 3, 10, ["/"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 1, 15, "el")
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 1, 15, "abc")
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 1, 15, None)
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 1, 15, False)
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 1, 15, 2)
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("hello", "empty", 10, ["notMatch"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("hey", 1, None, ["notMatch"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("hey", -3, 10, ["notMatch"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("", -3, 10, ["notMatch"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("hey", 20, 2, ["notMatch"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("hey", -2, -1, ["notMatch"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("hey", 5, 1500, ["notMatch"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("", 1, 21, ["notMatch"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("this string is intended to represent a longer one", 5, 15,
                                                             ["^_^"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 3, 21, ["notMatch", 2])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 3, 21, [None])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 3, 21, [True, "notMatch"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 3, 21, ["notMatch", 2, "bye"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 3, 21, [None, "notMatch", 2])

  def test_checkIfStringDoesNotContainAnySubstringFromList_containsString(self):
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 3, 21, ["H"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 2, 21, ["./", "H"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 3, 8, ["y", "H", "x"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 1, 121, ["hey", "hell", "H", "bye"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 1, 11, ["hey", "Hell", "bye"])
    with self.assertRaises(Exception):
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 0, 21, ["ell", "Hell", "H", "He"])

  def test_checkIfStringDoesNotContainAnySubstringFromList_valid(self):
    try:
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 5, 5, [])
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 5, 5, ["hello"])
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 5, 5, ["hell", "elo", "L", "LO", "hello"])
      checks.checkIfStringDoesNotContainAnySubstringFromList("Hello", 5, 5, ["abcd", "\n", "\t", "bye"])
    except Exception:
      self.fail("checkIfStringDoesNotContainAnySubstringFromList() raised Exception unexpectedly!")

  def test_checkIfAllNoneOrString_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString("not a list", 3, 10)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString([], 0, 10)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString(["hello", "hey", "hi"], 3, 10)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString(["", "hello"], 0, 2)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString(["heyho", "hello"], 0, 4)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString(["heyho", "hello"], 10, 22)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString(["hello"], 6, 6)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString(["hello", "bye", None], 0, 16)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString(["hello", None, "bye"], 0, 16)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString([None, "hello", "bye"], 0, 16)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString([None, "im a lonely string :(", None], 0, 16)

  def test_checkIfAllNoneOrString_notRaiseException(self):
    try:
      checks.checkIfAllNoneOrString([None], 3, 10)
      checks.checkIfAllNoneOrString([None, None], 0, 10)
      checks.checkIfAllNoneOrString([None, None, None], 10, 100)
      checks.checkIfAllNoneOrString([""], 0, 0)
      checks.checkIfAllNoneOrString([""], 0, 10)
      checks.checkIfAllNoneOrString(["hello"], 0, 10)
      checks.checkIfAllNoneOrString(["hello", ""], 0, 10)
      checks.checkIfAllNoneOrString(["hello", "hey"], 3, 5)
      checks.checkIfAllNoneOrString(["hello", "hey", "hi", "k", ""], 0, 15)
    except Exception:
      self.fail("checkIfAllNoneOrString() raised Exception unexpectedly!")

  def test_checkIfValidJsonFile_nonSense(self):
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFile("test.json")
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFile(None)
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFile("{}")
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFile(False)

  def test_checkIfValidJsonFile_invalid(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, [""])
    file = open(filePath, "r")
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFile(file)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["hello internet"])
    file = open(filePath, "r")
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFile(file)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "true", "}"])
    file = open(filePath, "r")
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFile(file)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["1", "2", "3", "4"])
    file = open(filePath, "r")
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFile(file)

  def test_checkIfValidJsonFile_valid(self):
    try:
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
    except Exception:
      self.fail("checkIfValidJsonFile() raised Exception unexpectedly!")

  def test_checkIfValidJsonFileByFilePath_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "r")
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFileByFilePath(file)
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFileByFilePath("notExistingFile.extension")
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFileByFilePath(None)
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFileByFilePath(12)
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFileByFilePath(False)

  def test_checkIfValidJsonFileByFilePath_invalid(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, [""])
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFileByFilePath(filePath)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["hello internet"])
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFileByFilePath(filePath)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath,
                                                                ["{", "true", "}"])
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFileByFilePath(filePath)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath,
                                                                ["1", "2", "3", "4"])
    with self.assertRaises(Exception):
      checks.checkIfValidJsonFileByFilePath(filePath)

  def test_checkIfValidJsonFileByFilePath_valid(self):
    try:
      filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "}"])
      checks.checkIfValidJsonFileByFilePath(filePath)
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "\"numbers\": ", "[1,2,3,4,5]", "}"])
      checks.checkIfValidJsonFileByFilePath(filePath)
      filerw.writeLinesToExistingOrNewlyCreatedFileByPathAndClose(filePath, ["{", "\"boolValue\": ", "true", "}"])
      checks.checkIfValidJsonFileByFilePath(filePath)
    except Exception:
      self.fail("checkIfValidJsonFileByFilePath() raised Exception unexpectedly!")

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
    with self.assertRaises(Exception):
      checks.checkIfType(file, 12)
    with self.assertRaises(Exception):
      checks.checkIfType(12, "notExistingFile.extension")
    with self.assertRaises(Exception):
      checks.checkIfType(None, None)
    with self.assertRaises(Exception):
      checks.checkIfType(True, False)
    with self.assertRaises(Exception):
      checks.checkIfType(False, Exception)

  def test_checkIfType_wrongType(self):
    filerw.createOrOverwriteWithEmptyFileByType(File.FOR_TEST_TEXTFILE1)
    file = open(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1), "r")
    with self.assertRaises(Exception):
      checks.checkIfType(file, int)
    with self.assertRaises(Exception):
      checks.checkIfType(12, str)
    with self.assertRaises(Exception):
      checks.checkIfType(None, list)
    with self.assertRaises(Exception):
      checks.checkIfType(True, bytearray)
    with self.assertRaises(Exception):
      checks.checkIfType(False, io.TextIOWrapper)

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
    with self.assertRaises(Exception):
      checks.checkIfAnyType(2, 3)
    with self.assertRaises(Exception):
      checks.checkIfAnyType(2, int)
    with self.assertRaises(Exception):
      checks.checkIfAnyType(2, None)
    with self.assertRaises(Exception):
      checks.checkIfAnyType(2, [1, 2, 3])
    with self.assertRaises(Exception):
      checks.checkIfAnyType(2, [True, 2, None])

  def test_checkIfAnyType_notMatch(self):
    with self.assertRaises(Exception):
      checks.checkIfAnyType(2, [])
    with self.assertRaises(Exception):
      checks.checkIfAnyType(2, [bool])
    with self.assertRaises(Exception):
      checks.checkIfAnyType(2, [list])
    with self.assertRaises(Exception):
      checks.checkIfAnyType(2, [str])
    with self.assertRaises(Exception):
      checks.checkIfAnyType(2, [list, bool])
    with self.assertRaises(Exception):
      checks.checkIfAnyType("string", [list, bool])
    with self.assertRaises(Exception):
      checks.checkIfAnyType("string", [list, bool, int])
    with self.assertRaises(Exception):
      checks.checkIfAnyType(23, [list, bool, str])
    with self.assertRaises(Exception):
      checks.checkIfAnyType({}, [list, bool, str, int])

  def test_checkIfAnyType_match(self):
    try:
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
    except Exception:
      self.fail("checkIfAnyType() raised Exception unexpectedly!")
