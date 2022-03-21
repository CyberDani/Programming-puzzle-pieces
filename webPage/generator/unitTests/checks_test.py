import unittest
import sys

sys.path.append('..')

from modules import checks

class ChecksTests(unittest.TestCase):

  def test_checkIntIsBetween_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(0,1,4)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(-20,10,55)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(20,-55,-15)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(-30,-15,-45)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(10,2,9)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(-120,20,90)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(100,120,90)
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(100,30,"houndred")
    with self.assertRaises(Exception):
      checks.checkIntIsBetween(100,[0],1200)
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

  def test_checkIfFile_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfFile(0)
    with self.assertRaises(Exception):
      checks.checkIfFile(None)
    with self.assertRaises(Exception):
      checks.checkIfFile("file.txt")
    with self.assertRaises(Exception):
      checks.checkIfFile([2,3,4])
    with self.assertRaises(Exception):
      checks.checkIfFile(True)

  def test_checkIfFile_notRaiseException(self):
    try:
      fileWrite = open("unitTests/temp/test.txt", "w")
      checks.checkIfFile(fileWrite)
      fileWrite.close()
      fileRead = open("unitTests/temp/test.txt", "r")
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
      checks.checkIfList([0,2,4,1,0])
      checks.checkIfList([0])
      checks.checkIfList([])
      checks.checkIfList(["hello", "world"])
      checks.checkIfList([0, "world", False])
      checks.checkIfList(["hey", None])
    except Exception:
      self.fail("checkIfList() raised Exception unexpectedly!")

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
      checks.checkIfPureListOfStrings(["hello","my","world",12])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings([True, "hello","my","world"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings(["hello","my", ["one", "two"], "world"])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings([True])
    with self.assertRaises(Exception):
      checks.checkIfPureListOfStrings([0,1,2,3,4,5,6])

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

  def test_checkIfString_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfString(123,3, 10)
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
      checks.checkIfString("this string is intented to represent a longer one", 5, 15)

  def test_checkIfString_notRaiseException(self):
    try:
      checks.checkIfString("hey", 3, 10)
      checks.checkIfString("hey", 0, 3)
      checks.checkIfString("", 0, 23)
      checks.checkIfString("hello", 0, 12)
      checks.checkIfString("hello", 3, 20)
    except Exception:
      self.fail("checkIfString() raised Exception unexpectedly!")

  def test_checkIfAllNoneOrString_raiseException(self):
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString("not a list", 3, 10)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString([], 0, 10)
    with self.assertRaises(Exception):
      checks.checkIfAllNoneOrString(["hello","hey","hi"], 3, 10)
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
      self.fail("checkIfString() raised Exception unexpectedly!")
    