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