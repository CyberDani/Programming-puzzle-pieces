import sys

sys.path.append('..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules import stringUtil


class StringUtilTests(AutoUnitTest):

  def test_getNextChar_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.getNextChar("Chuck Norris", None)
    with self.assertRaises(Exception):
      stringUtil.getNextChar(False, True)
    with self.assertRaises(Exception):
      stringUtil.getNextChar(None, 0)
    with self.assertRaises(Exception):
      stringUtil.getNextChar("Dynamic", -1)
    with self.assertRaises(Exception):
      stringUtil.getNextChar("Generation", 56)
    with self.assertRaises(Exception):
      stringUtil.getNextChar("012345", 6)

  def test_getNextChar_emptyString(self):
    with self.assertRaises(Exception):
      stringUtil.getNextChar("", 0)

  def test_getNextChar_noNextChar(self):
    found, char = stringUtil.getNextChar("012345", 5)
    self.assertFalse(found)
    self.assertEqual(char, "")
    found, char = stringUtil.getNextChar("Q", 0)
    self.assertFalse(found)
    self.assertEqual(char, "")
    found, char = stringUtil.getNextChar("oO", 1)
    self.assertFalse(found)
    self.assertEqual(char, "")

  def test_getNextChar_examples(self):
    found, char = stringUtil.getNextChar("Ex", 0)
    self.assertTrue(found)
    self.assertEqual(char, "x")
    found, char = stringUtil.getNextChar("Explore", 0)
    self.assertTrue(found)
    self.assertEqual(char, "x")
    found, char = stringUtil.getNextChar("ABC", 1)
    self.assertTrue(found)
    self.assertEqual(char, "C")
    found, char = stringUtil.getNextChar("Generator", 1)
    self.assertTrue(found)
    self.assertEqual(char, "n")
    found, char = stringUtil.getNextChar("0123456789", 8)
    self.assertTrue(found)
    self.assertEqual(char, "9")
    found, char = stringUtil.getNextChar("0123456789", 4)
    self.assertTrue(found)
    self.assertEqual(char, "5")

  def test_getPreviousChar_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.getPreviousChar("Chuck Norris", None)
    with self.assertRaises(Exception):
      stringUtil.getPreviousChar(False, True)
    with self.assertRaises(Exception):
      stringUtil.getPreviousChar(None, 0)
    with self.assertRaises(Exception):
      stringUtil.getPreviousChar("Dynamic", -1)
    with self.assertRaises(Exception):
      stringUtil.getPreviousChar("Generation", 56)
    with self.assertRaises(Exception):
      stringUtil.getPreviousChar("012345", 6)

  def test_getPreviousChar_emptyString(self):
    with self.assertRaises(Exception):
      stringUtil.getPreviousChar("", 0)

  def test_getPreviousChar_noPrevChar(self):
    found, char = stringUtil.getPreviousChar("tomato sauce", 0)
    self.assertFalse(found)
    self.assertEqual(char, "")
    found, char = stringUtil.getPreviousChar("Q", 0)
    self.assertFalse(found)
    self.assertEqual(char, "")
    found, char = stringUtil.getPreviousChar("oO", 0)
    self.assertFalse(found)
    self.assertEqual(char, "")

  def test_getPreviousChar_examples(self):
    found, char = stringUtil.getPreviousChar("Ex", 1)
    self.assertTrue(found)
    self.assertEqual(char, "E")
    found, char = stringUtil.getPreviousChar("Explore", 1)
    self.assertTrue(found)
    self.assertEqual(char, "E")
    found, char = stringUtil.getPreviousChar("ABC", 2)
    self.assertTrue(found)
    self.assertEqual(char, "B")
    found, char = stringUtil.getPreviousChar("0123456789", 9)
    self.assertTrue(found)
    self.assertEqual(char, "8")
    found, char = stringUtil.getPreviousChar("0123456789", 4)
    self.assertTrue(found)
    self.assertEqual(char, "3")

  def test_getStringStartsWithEndsWith_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap(None, None, None)
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap("", "Mozart", "Bach")
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap("X", "Mozart", "Bach")
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap("", "", "")
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap("", "", "endStr")
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap("", "beginStr", "")
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap("Small test string", "", "test")
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap("Small test string", "", "asd")
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap("Small test string", "Small", "")
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap("Small test string", "asd", "")
    with self.assertRaises(Exception):
      stringUtil.getStringStartsWithEndsWithNoOverlap("Small test string", "", "")

  def test_getStringStartsWithEndsWith_stringNotFound(self):
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "test", "end")
    self.assertEqual(len(ans), 0)
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "begin", "string")
    self.assertEqual(len(ans), 0)
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "begin", "end")
    self.assertEqual(len(ans), 0)
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "x", "y")
    self.assertEqual(len(ans), 0)
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "tesu", "string")
    self.assertEqual(len(ans), 0)
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "tests", "string")
    self.assertEqual(len(ans), 0)
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "test", "strings")
    self.assertEqual(len(ans), 0)
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "test", "strinh")
    self.assertEqual(len(ans), 0)
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("abcabcQWE", "ca", "ab")
    self.assertEqual(len(ans), 0)

  def test_getStringStartsWithEndsWith_stringFound(self):
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "test", "string")
    self.assertEqual(ans, "test string")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "test", "g")
    self.assertEqual(ans, "test string")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "t", "g")
    self.assertEqual(ans, "test string")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "te", "st")
    self.assertEqual(ans, "test")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "st", "st")
    self.assertEqual(ans, "st st")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "s", "s")
    self.assertEqual(ans, "st s")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("test string", "s", "t")
    self.assertEqual(ans, "st")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("abcabcQWEabcabc", "ca", "ab")
    self.assertEqual(ans, "cabcQWEab")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("abcabcQWEabcabc", "bca", "bca")
    self.assertEqual(ans, "bcabcQWEabca")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("abcabcQWEabcabc", "bca", "ca")
    self.assertEqual(ans, "bcabcQWEabca")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("abcabcQWAEabcabc", "bca", "a")
    self.assertEqual(ans, "bcabcQWAEa")
    ans = stringUtil.getStringStartsWithEndsWithNoOverlap("abcabcQWAEabcabc", "abc", "abc")
    self.assertEqual(ans, "abcabc")

  def test_stringListToString_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.stringListToString(["element1", "element2"], "[", "]", 2)
    with self.assertRaises(Exception):
      stringUtil.stringListToString(["element1", "element2"], "[", None, "-")
    with self.assertRaises(Exception):
      stringUtil.stringListToString(["element1", "element2"], False, "]", "-")
    with self.assertRaises(Exception):
      stringUtil.stringListToString("this is just a simple string", "[", "]", "-")
    with self.assertRaises(Exception):
      stringUtil.stringListToString([True, False], "[", "]", "-")
    with self.assertRaises(Exception):
      stringUtil.stringListToString([1, 2, 3, 4, 5, 6], "[", "]", "-")
    with self.assertRaises(Exception):
      stringUtil.stringListToString(["one", "two", "three", []], "[", "]", "-")

  def test_stringListToString_examples(self):
    res = stringUtil.stringListToString([], "-<(", ")>-", "|")
    self.assertEqual(res, "-<()>-")
    res = stringUtil.stringListToString([], "", "", "|")
    self.assertEqual(res, "")
    res = stringUtil.stringListToString([], "", "", "")
    self.assertEqual(res, "")
    res = stringUtil.stringListToString(["one", "two", "three"], "", "", "")
    self.assertEqual(res, "onetwothree")
    res = stringUtil.stringListToString(["one", "two", "three"], "", "", "|")
    self.assertEqual(res, "one|two|three")
    res = stringUtil.stringListToString(["hey", "bye", "hello"], "(", ")", "|")
    self.assertEqual(res, "(hey|bye|hello)")
    res = stringUtil.stringListToString(["hey", "bye", "hello"], "(", ")", "")
    self.assertEqual(res, "(heybyehello)")
    res = stringUtil.stringListToString(["hey", "bye", "hello"], "-<(", ")>-", "|")
    self.assertEqual(res, "-<(hey|bye|hello)>-")
    res = stringUtil.stringListToString(["hey", "bye", "hello"], "-<(", ")>-", ", ")
    self.assertEqual(res, "-<(hey, bye, hello)>-")
    res = stringUtil.stringListToString(["hey", "bye", "hello"], "", "", ", ")
    self.assertEqual(res, "hey, bye, hello")
    res = stringUtil.stringListToString(["hey", "bye", "hello"], "", "", " --> ")
    self.assertEqual(res, "hey --> bye --> hello")
    res = stringUtil.stringListToString(["hey", "bye", "hello"], "<<<== ", " ==>>>", " --> ")
    self.assertEqual(res, "<<<== hey --> bye --> hello ==>>>")

  def test_doubleSplit_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.doubleSplit("test", "|", "|")
    with self.assertRaises(Exception):
      stringUtil.doubleSplit("test string", "", "_")
    with self.assertRaises(Exception):
      stringUtil.doubleSplit("test string", "_", "")
    with self.assertRaises(Exception):
      stringUtil.doubleSplit("test string", 12, "_")
    with self.assertRaises(Exception):
      stringUtil.doubleSplit("test string", "_", True)
    with self.assertRaises(Exception):
      stringUtil.doubleSplit(["test string", "HEY"], "[]", "_")

  def test_doubleSplit_examples(self):
    parts1, parts2 = stringUtil.doubleSplit("", "_", "|")
    self.assertEqual(parts1, [""])
    self.assertEqual(parts2, [])
    parts1, parts2 = stringUtil.doubleSplit("random test string", "$", "@")
    self.assertEqual(parts1, ["random test string"])
    self.assertEqual(parts2, [])
    parts1, parts2 = stringUtil.doubleSplit("random test string@username", "$", "@")
    self.assertEqual(parts1, ["random test string"])
    self.assertEqual(parts2, ["username"])
    parts1, parts2 = stringUtil.doubleSplit("random test string@username$100", "$", "@")
    self.assertEqual(parts1, ["random test string", "100"])
    self.assertEqual(parts2, ["username"])
    parts1, parts2 = stringUtil.doubleSplit("$100@random", "$", "@")
    self.assertEqual(parts1, ["", "100"])
    self.assertEqual(parts2, ["random"])
    parts1, parts2 = stringUtil.doubleSplit("@random$100", "$", "@")
    self.assertEqual(parts1, ["", "100"])
    self.assertEqual(parts2, ["random"])
    parts1, parts2 = stringUtil.doubleSplit("key:value_db_something", ":", "_")
    self.assertEqual(parts1, ["key", "value"])
    self.assertEqual(parts2, ["db", "something"])
    parts1, parts2 = stringUtil.doubleSplit("key:value_db_something:default_numeric", ":", "_")
    self.assertEqual(parts1, ["key", "value", "default"])
    self.assertEqual(parts2, ["db", "something", "numeric"])
    parts1, parts2 = stringUtil.doubleSplit("key:value_db_something:default_numeric", ":", "//")
    self.assertEqual(parts1, ["key", "value_db_something", "default_numeric"])
    self.assertEqual(parts2, [])

  def test_getFirstNewLineCharIdx_nonSense(self):
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, "example test string", None, None)
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, "another test string", 2, True)
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, "again a string", "0", 3)
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, "let me use this example", -1, 3)
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, "let me use this example", 3, 61)
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, "let me use this example", 8, 5)
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, "let me use this example", 11, 10)
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, 123, 3, 61)
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, ["let me use this example"], 3, 61)
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, None, 3, 61)

  def test_getFirstNewLineCharIdx_emptyString(self):
    self.assertRaises(Exception, stringUtil.getFirstNewLineCharIdx, "", 0, 0)

  def helper_getFirstNewLineCharIdx_checkIfNotFound(self, string, startIdx, endIdx):
    found, idx = stringUtil.getFirstNewLineCharIdx(string, startIdx, endIdx)
    self.assertEqual((found, idx), (False, -1))

  def test_getFirstNewLineCharIdx_notFound(self):
    self.helper_getFirstNewLineCharIdx_checkIfNotFound(".", 0, 0)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("_Q", 0, 1)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("not a single newline", 0, 19)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("not a single newline", 0, 10)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("not a single newline", 9, 19)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("not a single newline", 5, 15)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\nnewLine not in range", 1, 20)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\nnewLine not in range", 1, 10)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\nnewLine not in range", 10, 16)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\nnewLine not in range", 10, 20)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\nnewLine not in range\n", 1, 20)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\nnewLine\nnot\nin\nrange\n", 1, 7)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\nnewLine\nnot\nin\nrange\n", 9, 11)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\nnewLine\nnot\nin\nrange\n", 13, 14)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\nnewLine\nnot\nin\nrange\n", 16, 20)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\n\nanother\n\n\nexample\n\n", 2, 8)
    self.helper_getFirstNewLineCharIdx_checkIfNotFound("\n\nanother\n\n\nexample\n\n", 12, 18)

  def helper_getFirstNewLineCharIdx_checkIfFound(self, string, startIdx, endIdx, foundAt):
    found, idx = stringUtil.getFirstNewLineCharIdx(string, startIdx, endIdx)
    self.assertEqual((found, idx), (True, foundAt))

  def test_getFirstNewLineCharIdx_found(self):
    self.helper_getFirstNewLineCharIdx_checkIfFound("\n", 0, 0, foundAt=0)
    self.helper_getFirstNewLineCharIdx_checkIfFound("\n\n", 0, 0, foundAt=0)
    self.helper_getFirstNewLineCharIdx_checkIfFound("\n\n", 0, 1, foundAt=0)
    self.helper_getFirstNewLineCharIdx_checkIfFound("\n\n", 1, 1, foundAt=1)
    self.helper_getFirstNewLineCharIdx_checkIfFound("\n\n\n", 0, 1, foundAt=0)
    self.helper_getFirstNewLineCharIdx_checkIfFound("\n\n\n", 0, 2, foundAt=0)
    self.helper_getFirstNewLineCharIdx_checkIfFound("\n\n\n", 1, 2, foundAt=1)
    self.helper_getFirstNewLineCharIdx_checkIfFound("first line\nsecond line", 0, 21, foundAt=10)
    self.helper_getFirstNewLineCharIdx_checkIfFound("first line\nsecond line", 9, 11, foundAt=10)
    self.helper_getFirstNewLineCharIdx_checkIfFound("first line\nsecond line", 10, 10, foundAt=10)
    self.helper_getFirstNewLineCharIdx_checkIfFound("\nmultiple\nnewlines\n", 0, 18, foundAt=0)
    self.helper_getFirstNewLineCharIdx_checkIfFound("\nmultiple\nnewlines\n", 1, 18, foundAt=9)
    self.helper_getFirstNewLineCharIdx_checkIfFound("\n\nmore\n\n\nnewlines\n\n\n\n", 2, 20, foundAt=6)
    self.helper_getFirstNewLineCharIdx_checkIfFound("\n\nmore\n\n\nnewlines\n\n\n\n", 8, 18, foundAt=8)

  def test_getLastNewLineCharIdx_nonSense(self):
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, "example test string", None, None)
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, "another test string", 2, True)
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, "again a string", "0", 3)
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, "let me use this example", -1, 3)
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, "let me use this example", 3, 61)
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, "let me use this example", 8, 5)
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, "let me use this example", 11, 10)
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, 123, 3, 61)
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, ["let me use this example"], 3, 61)
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, None, 3, 61)

  def test_getLastNewLineCharIdx_emptyString(self):
    self.assertRaises(Exception, stringUtil.getLastNewLineCharIdx, "", 0, 0)

  def helper_getLastNewLineCharIdx_checkIfNotFound(self, string, startIdx, endIdx):
    found, idx = stringUtil.getLastNewLineCharIdx(string, startIdx, endIdx)
    self.assertEqual((found, idx), (False, -1))

  def test_getLastNewLineCharIdx_notFound(self):
    self.helper_getLastNewLineCharIdx_checkIfNotFound(".", 0, 0)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("_Q", 0, 1)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("not a single newline", 0, 19)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("not a single newline", 0, 10)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("not a single newline", 9, 19)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("not a single newline", 5, 15)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\nnewLine not in range", 1, 20)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\nnewLine not in range", 1, 10)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\nnewLine not in range", 10, 16)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\nnewLine not in range", 10, 20)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\nnewLine not in range\n", 1, 20)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\nnewLine\nnot\nin\nrange\n", 1, 7)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\nnewLine\nnot\nin\nrange\n", 9, 11)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\nnewLine\nnot\nin\nrange\n", 13, 14)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\nnewLine\nnot\nin\nrange\n", 16, 20)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\n\nanother\n\n\nexample\n\n", 2, 8)
    self.helper_getLastNewLineCharIdx_checkIfNotFound("\n\nanother\n\n\nexample\n\n", 12, 18)

  def helper_getLastNewLineCharIdx_checkIfFound(self, string, startIdx, endIdx, foundAt):
    found, idx = stringUtil.getLastNewLineCharIdx(string, startIdx, endIdx)
    self.assertEqual((found, idx), (True, foundAt))

  def test_getLastNewLineCharIdx_found(self):
    self.helper_getLastNewLineCharIdx_checkIfFound("\n", 0, 0, foundAt=0)
    self.helper_getLastNewLineCharIdx_checkIfFound("\n\n", 0, 0, foundAt=0)
    self.helper_getLastNewLineCharIdx_checkIfFound("\n\n", 0, 1, foundAt=1)
    self.helper_getLastNewLineCharIdx_checkIfFound("\n\n", 1, 1, foundAt=1)
    self.helper_getLastNewLineCharIdx_checkIfFound("\n\n\n", 0, 1, foundAt=1)
    self.helper_getLastNewLineCharIdx_checkIfFound("\n\n\n", 0, 2, foundAt=2)
    self.helper_getLastNewLineCharIdx_checkIfFound("\n\n\n", 1, 2, foundAt=2)
    self.helper_getLastNewLineCharIdx_checkIfFound("first line\nsecond line", 0, 21, foundAt=10)
    self.helper_getLastNewLineCharIdx_checkIfFound("first line\nsecond line", 9, 11, foundAt=10)
    self.helper_getLastNewLineCharIdx_checkIfFound("first line\nsecond line", 10, 10, foundAt=10)
    self.helper_getLastNewLineCharIdx_checkIfFound("\nmultiple\nnewlines\n", 0, 18, foundAt=18)
    self.helper_getLastNewLineCharIdx_checkIfFound("\nmultiple\nnewlines\n", 0, 17, foundAt=9)
    self.helper_getLastNewLineCharIdx_checkIfFound("\n\nmore\n\n\nnewlines\n\n\n\n", 0, 20, foundAt=20)
    self.helper_getLastNewLineCharIdx_checkIfFound("\n\nmore\n\n\nnewlines\n\n\n\n", 0, 8, foundAt=8)

  def helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised(self, string, startIdx, endIdx):
    with self.assertRaises(Exception):
      stringUtil.getFirstNonWhiteSpaceCharIdx(string, startIdx, endIdx)

  def helper_getFirstNonWhiteSpaceCharIdx_checkIfNotFound(self, string, startIdx, endIdx):
    found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(string, startIdx, endIdx)
    self.assertFalse(found)
    self.assertEqual(idx, -1)

  def helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(self, string, startIdx, endIdx, foundAt):
    found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(string, startIdx, endIdx)
    self.assertTrue(found)
    self.assertEqual(idx, foundAt)

  def test_getFirstNonWhiteSpaceCharIdx_nonSense(self):
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised("example test string", None, None)
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised("another test string", 2, True)
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised("again a string", "0", 3)
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised("let me use this example", -1, 3)
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised("let me use this example", 3, 61)
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised("let me use this example", 8, 5)
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised("let me use this example", 11, 10)
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised(123, 3, 61)
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised(["let me use this example"], 3, 61)
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised(None, 3, 61)

  def test_getFirstNonWhiteSpaceCharIdx_emptyString(self):
    self.helper_getFirstNonWhiteSpaceCharIdx_exceptionRaised("", 0, 0)

  def test_getFirstNonWhiteSpaceCharIdx_notFound(self):
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfNotFound(" \t \r\n \t", 0, 6)
    string = "here comes some whitespaces: \t\t\t \r\r\n\n    \t      "
    self.assertEqual(string[27], ':')
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfNotFound(string, 28, len(string) - 1)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfNotFound(string, 28, len(string) - 5)
    string = " \t\t\t \r\r\n\n    \t      : these are my whitespaces"
    colonIdx = string.find(':')
    self.assertEqual(string[colonIdx], ':')
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfNotFound(string, 0, colonIdx - 1)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfNotFound(string, 0, 0)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfNotFound(string, colonIdx - 1, colonIdx - 1)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfNotFound(string, 6, colonIdx - 5)
    string = "look at these whitespaces: \t\t\t \r\r\n\n    \t      => beautiful"
    self.assertEqual(string[25], ':')
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfNotFound(string, 26, string.find("=>") - 1)

  def test_getFirstNonWhiteSpaceCharIdx_found(self):
    string = "\ta\r\nb \r\n \t \n cwer\nd\nd"
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, 0, len(string)-1, foundAt=1)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, 2, len(string)-1, foundAt=4)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, 5, len(string)-1, foundAt=string.find("c"))
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound("a\tb\tc\nd\nd", 0, 8, foundAt=0)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound("a\tb\tc\nd\nd", 4, 8, foundAt=4)
    string = " \t  asad\tbrev\tcSasd\ndbrt\ndqwY      \r\n\r\n X"
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, 0, len(string)-1, foundAt=4)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, 0, 12, foundAt=4)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, 2, 7, foundAt=4)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, 4, 4, foundAt=4)
    startIdx = string.find('Y')
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, startIdx + 1, len(string) - 1, foundAt=len(string) - 1)
    string = "[log-info]In_this_${string}_there_are_(no|0)_whitespaces!"
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, 0, len(string) -1, foundAt=0)
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, 0, len(string) - 13, foundAt=0)
    randomIndex = string.find("$")
    self.helper_getFirstNonWhiteSpaceCharIdx_checkIfFound(string, randomIndex, len(string) - 13, foundAt=randomIndex)

  def helper_getLastNonWhiteSpaceCharIdx_exceptionRaised(self, string, startIdx, endIdx):
    with self.assertRaises(Exception):
      stringUtil.getLastNonWhiteSpaceCharIdx(string, startIdx, endIdx)

  def helper_getLastNonWhiteSpaceCharIdx_checkIfNotFound(self, string, startIdx, endIdx):
    found, idx = stringUtil.getLastNonWhiteSpaceCharIdx(string, startIdx, endIdx)
    self.assertFalse(found)
    self.assertEqual(idx, -1)

  def helper_getLastNonWhiteSpaceCharIdx_checkIfFound(self, string, startIdx, endIdx, foundAt):
    found, idx = stringUtil.getLastNonWhiteSpaceCharIdx(string, startIdx, endIdx)
    self.assertTrue(found)
    self.assertEqual(idx, foundAt)

  def test_getLastNonWhiteSpaceCharIdx_nonSense(self):
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised("example test string", None, None)
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised("another test string", 2, True)
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised("again a string", "0", 3)
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised("let me use this example", -1, 3)
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised("let me use this example", 3, 61)
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised("let me use this example", 8, 5)
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised("let me use this example", 11, 10)
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised(123, 3, 61)
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised(["let me use this example"], 3, 61)
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised(None, 3, 61)

  def test_getLastNonWhiteSpaceCharIdx_emptyString(self):
    self.helper_getLastNonWhiteSpaceCharIdx_exceptionRaised("", 0, 0)

  def test_getLastNonWhiteSpaceCharIdx_notFound(self):
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfNotFound(" \t \r\n \t", 0, 6)
    string = "here comes some whitespaces: \t\t\t \r\r\n\n    \t      "
    self.assertEqual(string[27], ':')
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfNotFound(string, 28, len(string) - 1)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfNotFound(string, 28, len(string) - 5)
    string = " \t\t\t \r\r\n\n    \t      : these are my whitespaces"
    colonIdx = string.find(':')
    self.assertEqual(string[colonIdx], ':')
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfNotFound(string, 0, colonIdx - 1)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfNotFound(string, 0, 0)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfNotFound(string, colonIdx - 1, colonIdx - 1)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfNotFound(string, 6, colonIdx - 5)
    string = "look at these whitespaces: \t\t\t \r\r\n\n    \t      => beautiful"
    self.assertEqual(string[25], ':')
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfNotFound(string, 26, string.find("=>") - 1)

  def test_getLastNonWhiteSpaceCharIdx_found(self):
    string = "\ta\r\nb \r\n \t \n cwer\nd\nd"
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfFound(string, 0, len(string) - 1, foundAt=len(string) - 1)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfFound(string, 5, len(string) - 1, foundAt=len(string) - 1)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfFound(string, 1, 13, foundAt=13)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfFound(string, 2, 12, foundAt=4)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfFound(string, 4, 12, foundAt=4)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfFound("a\tb\tc\nd\nd", 0, 8, foundAt=8)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfFound("a\tb\tc\nd\nd", 4, 7, foundAt=6)
    string = " \t  asad\tbrev\tcSasd\ndbrt\ndqwY      \r\n\r\n X"
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfFound(string, 2, 7, foundAt=7)
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfFound(string, 4, 4, foundAt=4)
    string = "[log-info]In_this_${string}_there_are_(no|0)_whitespaces!"
    self.helper_getLastNonWhiteSpaceCharIdx_checkIfFound(string, 7, len(string) - 13, foundAt=len(string)-13)

  def test_beforeWhitespaceDelimitedFind_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind(True, "word", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind(None, "word", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind(415, "word", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind(["hello", "world"], "word", 0, 1)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", True, 0, 1)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", None, 0, 1)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", 312, 0, 1)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", [], 0, 1)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", "string", -1, 5)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", "string", 2, 95)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", "string", 10, 4)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", "string", 3, 2)

  def test_beforeWhitespaceDelimitedFind_emptyStrings(self):
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", "", 0, len("sample string") - 1)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", "", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("sample string", "", 0, 1)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("", "apple", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.beforeWhitespaceDelimitedFind("", ".", 0, 0)

  def test_beforeWhitespaceDelimitedFind_notFound(self):
    string = "Soft kitty,\twarm kitty,\nlittle ball\tof fur!"
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "putty", 0, len(string) - 1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, ",", 0, len(string) - 1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "soft", 0, len(string) - 1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "itty", 0, len(string) - 1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "oft", 0, len(string) - 1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "!", 0, len(string) - 1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "Soft", 1, len(string) - 1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "fur!", string.find("fur") + 1, len(string) - 1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "fur!", string.find("fur!"), len(string) - 2)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "Soft", string.find("warm"), string.find("ball") - 1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "fur!", string.find("warm"), string.find("ball") - 1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)

  def test_beforeWhitespaceDelimitedFind_found(self):
    string = "Soft kitty,\twarm kitty,\nlittle ball\tof fur!"
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "Soft", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertEqual(idx, 0)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "So", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertEqual(idx, 0)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "S", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertEqual(idx, 0)
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "fur", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("fur"))
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "fur!", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("fur"))
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "little", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("little"))
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "warm", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("warm"))
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "warm", string.find("\twarm"), len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("warm"))
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "ball", string.find("\twarm"),
                                                          string.find("\tof fur") - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("ball"))
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "kitty", string.find("\twarm"),
                                                          string.find("\tof fur") - 1)
    self.assertTrue(found)
    self.assertEqual(string[17], 'k')
    self.assertTrue(idx != string.find("kitty"))
    self.assertEqual(idx, 17)
    string = "Bill is feeling ill."
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "ill", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertEqual(string[16], 'i')
    self.assertEqual(idx, string.find("ill."))
    self.assertEqual(idx, 16)
    string = "Bill on the hill is feeling ill."
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "ill", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("ill."))
    string = "Bill on the hill is feeling ill while doing sth illegal."
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "ill", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("ill while doing sth"))
    string = "Kill Bill on the hill is feeling ill while doing sth illegally illegitimate."
    found, idx = stringUtil.beforeWhitespaceDelimitedFind(string, "ill", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("ill while doing sth"))

  def test_whitespaceDelimitedFind_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind(True, "word", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind(None, "word", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind(415, "word", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind(["hello", "world"], "word", 0, 1)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", True, 0, 1)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", None, 0, 1)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", 312, 0, 1)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", [], 0, 1)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", "string", -1, 5)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", "string", 2, 95)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", "string", 10, 4)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", "string", 3, 2)

  def test_whitespaceDelimitedFind_emptyStrings(self):
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", "", 0, len("sample string") - 1)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", "", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("sample string", "", 0, 1)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("", "apple", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.whitespaceDelimitedFind("", ".", 0, 0)

  def test_whitespaceDelimitedFind_notFound(self):
    string = "Soft kitty,\twarm kitty,\nlittle ball\tof fur!"
    found, idx = stringUtil.whitespaceDelimitedFind(string, "putty", 0, len(string) - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, ",", 0, len(string) - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "soft", 0, len(string) - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "itty", 0, len(string) - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "kitt", 0, len(string) - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "itt", 0, len(string) - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "oft", 0, len(string) - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "!", 0, len(string) - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "Soft", 1, len(string) - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "fur!", string.find("fur") + 1, len(string) - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "fur!", string.find("fur!"), len(string) - 2)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "Soft", string.find("warm"), string.find("ball") - 1)
    self.assertEqual((found, idx), (False, -1))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "fur!", string.find("warm"), string.find("ball") - 1)
    self.assertEqual((found, idx), (False, -1))

  def test_whitespaceDelimitedFind_found(self):
    string = "Soft kitty,\twarm kitty,\nlittle ball\tof fur!"
    found, idx = stringUtil.whitespaceDelimitedFind(string, "Soft", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertEqual(idx, 0)
    found, idx = stringUtil.whitespaceDelimitedFind(string, "fur!", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("fur"))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "little", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("little"))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "warm", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("warm"))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "warm", string.find("\twarm"), len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("warm"))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "ball", string.find("\twarm"),
                                                          string.find("\tof fur") - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("ball"))
    found, idx = stringUtil.whitespaceDelimitedFind(string, "kitty,", string.find("\twarm"),
                                                          string.find("\tof fur") - 1)
    self.assertTrue(found)
    self.assertEqual(string[17], 'k')
    self.assertTrue(idx != string.find("kitty"))
    self.assertEqual(idx, 17)
    string = "Bill is feeling ill ."
    found, idx = stringUtil.whitespaceDelimitedFind(string, "ill", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertEqual(string[16], 'i')
    self.assertEqual(idx, string.find("ill ."))
    self.assertEqual(idx, 16)
    string = "Bill the illager on the hill is feeling ill ."
    found, idx = stringUtil.whitespaceDelimitedFind(string, "ill", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("ill ."))
    string = "Bill on the hill is feeling ill while doing sth illegally ill ."
    found, idx = stringUtil.whitespaceDelimitedFind(string, "ill", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("ill while doing sth"))
    string = "Kill Bill on the hill is feeling ill while doing sth illegally illegitimate."
    found, idx = stringUtil.whitespaceDelimitedFind(string, "ill", 0, len(string) - 1)
    self.assertTrue(found)
    self.assertTrue(idx > -1)
    self.assertEqual(idx, string.find("ill while doing sth"))

  def test_rTrimNewLines_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.rTrimNewLines()
    with self.assertRaises(Exception):
      stringUtil.rTrimNewLines(["hello"])
    with self.assertRaises(Exception):
      stringUtil.rTrimNewLines(True)
    with self.assertRaises(Exception):
      stringUtil.rTrimNewLines(None)

  def test_rTrimNewLines_examples(self):
    ans = stringUtil.rTrimNewLines("")
    self.assertEqual(ans, "")
    ans = stringUtil.rTrimNewLines("X")
    self.assertEqual(ans, "X")
    ans = stringUtil.rTrimNewLines("heLLo")
    self.assertEqual(ans, "heLLo")
    ans = stringUtil.rTrimNewLines("\n")
    self.assertEqual(ans, "")
    ans = stringUtil.rTrimNewLines("\r\n")
    self.assertEqual(ans, "")
    ans = stringUtil.rTrimNewLines("\n\n")
    self.assertEqual(ans, "")
    ans = stringUtil.rTrimNewLines("\r\n\r\n")
    self.assertEqual(ans, "")
    ans = stringUtil.rTrimNewLines("\r\r\r")
    self.assertEqual(ans, "")
    ans = stringUtil.rTrimNewLines("hey!\n")
    self.assertEqual(ans, "hey!")
    ans = stringUtil.rTrimNewLines("\r\nwinLine\r\n")
    self.assertEqual(ans, "\r\nwinLine")
    ans = stringUtil.rTrimNewLines("winLine\r\n")
    self.assertEqual(ans, "winLine")
    ans = stringUtil.rTrimNewLines("firstRow\r\nsecondRow\r\n")
    self.assertEqual(ans, "firstRow\r\nsecondRow")
    ans = stringUtil.rTrimNewLines("\nfirstRow\n\r\nsecondRow\r\n")
    self.assertEqual(ans, "\nfirstRow\n\r\nsecondRow")
    ans = stringUtil.rTrimNewLines("\nfirstRow\n\r\nsecondRow\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n")
    self.assertEqual(ans, "\nfirstRow\n\r\nsecondRow")
    ans = stringUtil.rTrimNewLines("\n\nfirstRow\n\r\n\nsecondRow\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n")
    self.assertEqual(ans, "\n\nfirstRow\n\r\n\nsecondRow")

  def test_find_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.find("string", "substring", 1, 3, None)
    with self.assertRaises(Exception):
      stringUtil.find("string", "substring", -1, 3, -1)
    with self.assertRaises(Exception):
      stringUtil.find("string", "substring", 4, 2, -1)
    with self.assertRaises(Exception):
      stringUtil.find("string", "substring", 0, 26, -1)
    with self.assertRaises(Exception):
      stringUtil.find("string", "substring", 0, 6, -1)
    with self.assertRaises(Exception):
      stringUtil.find("string", "substring", 0, None, -1)
    with self.assertRaises(Exception):
      stringUtil.find("string", "substring", None, 2, -1)
    with self.assertRaises(Exception):
      stringUtil.find("string", None, 2, 2, -1)

  def test_find_emptyString(self):
    with self.assertRaises(Exception):
      stringUtil.find("", "substring", 1, 4, 3)
    with self.assertRaises(Exception):
      stringUtil.find("string", "", 1, 4, 3)

  def test_find_notFound(self):
    found, idx = stringUtil.find("string", "substring", 1, 5, 3)
    self.assertFalse(found)
    self.assertEqual(idx, 3)
    found, idx = stringUtil.find("string", "substring", 1, 5, 12)
    self.assertFalse(found)
    self.assertEqual(idx, 12)
    found, idx = stringUtil.find("string", "substring", 1, 5, -1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.find("this is a longer string", "substring", 1, 5, -2)
    self.assertFalse(found)
    self.assertEqual(idx, -2)
    found, idx = stringUtil.find("this is a longer string", "'", 1, 5, -2)
    self.assertFalse(found)
    self.assertEqual(idx, -2)

  def test_find_found(self):
    found, idx = stringUtil.find("string", "string", 0, 5, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 0)
    found, idx = stringUtil.find("this is my string here", "string", 0, 21, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 11)
    found, idx = stringUtil.find("'field' = 'value'", "'", 0, 6, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 0)
    found, idx = stringUtil.find("'field' = 'value'", "'", 0, 16, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 0)
    found, idx = stringUtil.find("'field' = 'value'", "'", 8, 16, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 10)
    found, idx = stringUtil.find("'field' = 'value'", "'", 11, 16, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 16)

  def test_rfind_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.rfind("string", "substring", 1, 3, None)
    with self.assertRaises(Exception):
      stringUtil.rfind("string", "substring", -1, 3, -1)
    with self.assertRaises(Exception):
      stringUtil.rfind("string", "substring", 4, 2, -1)
    with self.assertRaises(Exception):
      stringUtil.rfind("string", "substring", 0, 26, -1)
    with self.assertRaises(Exception):
      stringUtil.rfind("string", "substring", 0, 6, -1)
    with self.assertRaises(Exception):
      stringUtil.rfind("string", "substring", 0, None, -1)
    with self.assertRaises(Exception):
      stringUtil.rfind("string", "substring", None, 2, -1)
    with self.assertRaises(Exception):
      stringUtil.rfind("string", None, 2, 2, -1)

  def test_rfind_emptyString(self):
    with self.assertRaises(Exception):
      stringUtil.rfind("", "substring", 1, 4, 3)
    with self.assertRaises(Exception):
      stringUtil.rfind("string", "", 1, 4, 3)

  def test_rfind_notFound(self):
    found, idx = stringUtil.rfind("string", "substring", 1, 5, 3)
    self.assertFalse(found)
    self.assertEqual(idx, 3)
    found, idx = stringUtil.rfind("string", "substring", 1, 5, 12)
    self.assertFalse(found)
    self.assertEqual(idx, 12)
    found, idx = stringUtil.rfind("string", "substring", 1, 5, -1)
    self.assertFalse(found)
    self.assertEqual(idx, -1)
    found, idx = stringUtil.rfind("this is a longer string", "substring", 1, 5, -2)
    self.assertFalse(found)
    self.assertEqual(idx, -2)
    found, idx = stringUtil.rfind("this is a longer string", "'", 1, 5, -2)
    self.assertFalse(found)
    self.assertEqual(idx, -2)

  def test_rfind_found(self):
    found, idx = stringUtil.rfind("string", "string", 0, 5, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 0)
    found, idx = stringUtil.rfind("this is my string here", "string", 0, 21, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 11)
    found, idx = stringUtil.rfind("'field' = 'value'", "'", 0, 6, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 6)
    found, idx = stringUtil.rfind("'field' = 'value'", "'", 0, 16, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 16)
    found, idx = stringUtil.rfind("'field' = 'value' // comment", "'", 8, 27, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 16)
    found, idx = stringUtil.rfind("'field' = 'value'", "'", 10, 16, -1)
    self.assertTrue(found)
    self.assertEqual(idx, 16)

  def test_findAll_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.findAll("text", "e", 0, True)
    with self.assertRaises(Exception):
      stringUtil.findAll("text", "e", 0, -1)
    with self.assertRaises(Exception):
      stringUtil.findAll("text", "e", 3, 2)
    with self.assertRaises(Exception):
      stringUtil.findAll("text", "e", 1, 25)
    with self.assertRaises(Exception):
      stringUtil.findAll("text", "e", 1, 4)
    with self.assertRaises(Exception):
      stringUtil.findAll("text", "e", -1, 4)
    with self.assertRaises(Exception):
      stringUtil.findAll("text", "e", None, None)
    with self.assertRaises(Exception):
      stringUtil.findAll("text", "e", False, 2)
    with self.assertRaises(Exception):
      stringUtil.findAll("text", [], 0, 2)
    with self.assertRaises(Exception):
      stringUtil.findAll("text", None, 0, 2)
    with self.assertRaises(Exception):
      stringUtil.findAll(None, "x", 0, 2)
    with self.assertRaises(Exception):
      stringUtil.findAll(None, None, 0, 2)
    with self.assertRaises(Exception):
      stringUtil.findAll(None, None, None, None)
    with self.assertRaises(Exception):
      stringUtil.findAll(1, 2, 3, 4)
    with self.assertRaises(Exception):
      stringUtil.findAll(True, False, False, True)

  def test_findAll_emptyStrings(self):
    with self.assertRaises(Exception):
      stringUtil.findAll("text", "", 0, 0)
    with self.assertRaises(Exception):
      stringUtil.findAll("", "x", 0, 0)

  def test_findAll_notFound(self):
    idxs = stringUtil.findAll("a", "Q", 0, 0)
    self.assertEqual(idxs, [])
    idxs = stringUtil.findAll("a", "longer text", 0, 0)
    self.assertEqual(idxs, [])
    idxs = stringUtil.findAll("this a string", "square", 0, 0)
    self.assertEqual(idxs, [])
    idxs = stringUtil.findAll("this a string", "square", 0, 12)
    self.assertEqual(idxs, [])
    idxs = stringUtil.findAll("this a string", "square", 12, 12)
    self.assertEqual(idxs, [])
    idxs = stringUtil.findAll("this a string", "this is a longer text than the previous one", 0, 12)
    self.assertEqual(idxs, [])
    idxs = stringUtil.findAll("quantum entanglement", "quantum", 0, 4)
    self.assertEqual(idxs, [])
    idxs = stringUtil.findAll("quantum entanglement", "entanglement", 0, 18)
    self.assertEqual(idxs, [])

  def test_findAll_found(self):
    idxs = stringUtil.findAll("Q", "Q", 0, 0)
    self.assertEqual(idxs, [0])
    idxs = stringUtil.findAll("QQ", "Q", 0, 1)
    self.assertEqual(idxs, [0, 1])
    idxs = stringUtil.findAll("QQ", "Q", 0, 0)
    self.assertEqual(idxs, [0])
    idxs = stringUtil.findAll("QQ", "Q", 1, 1)
    self.assertEqual(idxs, [1])
    idxs = stringUtil.findAll("QQQQQQ", "Q", 0, 1)
    self.assertEqual(idxs, [0, 1])
    idxs = stringUtil.findAll("QQQQQQ", "Q", 2, 2)
    self.assertEqual(idxs, [2])
    idxs = stringUtil.findAll("QQQQQQ", "Q", 2, 4)
    self.assertEqual(idxs, [2, 3, 4])
    idxs = stringUtil.findAll("QQQQQQ", "Q", 4, 5)
    self.assertEqual(idxs, [4, 5])
    idxs = stringUtil.findAll("ababa", "aba", 0, 4)
    self.assertEqual(idxs, [0, 2])
    idxs = stringUtil.findAll("this is my special string", "string", 0, 24)
    self.assertEqual(idxs, [19])
    idxs = stringUtil.findAll("this is my special string written in python", "string", 11, 32)
    self.assertEqual(idxs, [19])
    idxs = stringUtil.findAll("this is my special string written in python", "string", 19, 42)
    self.assertEqual(idxs, [19])
    idxs = stringUtil.findAll("this is my special string written in python", "string", 0, 24)
    self.assertEqual(idxs, [19])
    idxs = stringUtil.findAll("this is my special string written in python", "string", 19, 24)
    self.assertEqual(idxs, [19])

  def test_findNthOccurrence_nonSense(self):
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", 1, 0, True)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", 1, 0, -1)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", 1, 3, 2)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", 1, 1, 25)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", 1, 1, 4)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", 1, -1, 4)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", 1, None, None)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", 1, False, 2)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", 0, 0, 4)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", -1, 0, 4)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "e", None, 0, 4)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", [], 1, 0, 2)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", None, 1, 0, 2)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence(None, "x", 1, 0, 2)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence(None, None, 1, 0, 2)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence(None, None, None, None, None)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence(1, 2, 1, 3, 4)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence(True, False, True, False, True)

  def test_findNthOccurrence_emptyStrings(self):
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("text", "", 1, 0, 0)
    with self.assertRaises(Exception):
      stringUtil.findNthOccurrence("", "x", 1, 0, 0)

  def test_findNthOccurrence_notFound_noOccurrence(self):
    idxs = stringUtil.findNthOccurrence("a", "Q", 1, 0, 0)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("a", "longer text", 1, 0, 0)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("this a string", "square", 1, 0, 0)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("this a string", "square", 1, 0, 12)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("this a string", "square", 1, 12, 12)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("this a string", "this is a longer text than the previous one", 1, 0, 12)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("quantum entanglement", "quantum", 1, 0, 4)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("quantum entanglement", "entanglement", 1, 0, 18)
    self.assertEqual(idxs, (False, -1))

  def test_findNthOccurrence_notFound_thereIsOccurrence(self):
    idxs = stringUtil.findNthOccurrence("a", "a", 2, 0, 0)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("_aQa_", "a", 3, 0, 4)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("a-a+a=a", "a", 2, 1, 3)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("a-a+a=a", "a", 5, 0, 5)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("this is a string", "is", 3, 0, 15)
    self.assertEqual(idxs, (False, -1))
    idxs = stringUtil.findNthOccurrence("quantum entanglement", "quantum", 2, 0, 19)
    self.assertEqual(idxs, (False, -1))

  def test_findNthOccurrence_found(self):
    ans = stringUtil.findNthOccurrence("Q", "Q", 1, 0, 0)
    self.assertEqual(ans, (True, 0))
    ans = stringUtil.findNthOccurrence("O_O", "O", 2, 0, 2)
    self.assertEqual(ans, (True, 2))
    ans = stringUtil.findNthOccurrence("This is his string", "is", 1, 0, 17)
    self.assertEqual(ans, (True, 2))
    ans = stringUtil.findNthOccurrence("This is his string", "is", 2, 0, 17)
    self.assertEqual(ans, (True, 5))
    ans = stringUtil.findNthOccurrence("This is his string", "is", 3, 0, 17)
    self.assertEqual(ans, (True, 9))
    ans = stringUtil.findNthOccurrence("This is his string", "is", 2, 4, 17)
    self.assertEqual(ans, (True, 9))
    ans = stringUtil.findNthOccurrence("This is his string", "is", 1, 6, 17)
    self.assertEqual(ans, (True, 9))
