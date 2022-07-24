import sys
import unittest

sys.path.append('..')
from modules import stringUtil

class StringUtilTests(unittest.TestCase):

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
