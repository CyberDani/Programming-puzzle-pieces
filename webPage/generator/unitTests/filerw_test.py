import os
import sys
import unittest

sys.path.append('..')
from modules import filerw

class FileReadWriterTests(unittest.TestCase):

  def test_getLinesByFilePathWithEndingNewLine_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY")
    file.close()
    linesFromFile = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0],"HEY")

  def test_getLinesByFilePathWithEndingNewLine_1line_1emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY\n")
    file.close()
    linesFromFile = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0],"HEY\n")

  def test_getLinesByFilePathWithEndingNewLine_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    linesFromFile = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0],"hello dear\n")
    self.assertEqual(linesFromFile[1],"this is the tester\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeStringsIndentedToFileThenAppendNewLine(file, 2, "asd")
    with self.assertRaises(Exception):
      filerw.writeStringsIndentedToFileThenAppendNewLine(file, -1, ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsIndentedToFileThenAppendNewLine("./unitTests/temp/test.txt", 1, ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsIndentedToFileThenAppendNewLine(None, 3, ["asd"])

  def test_writeStringsIndentedToFileThenAppendNewLine_emptyList(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(1, [])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_oneEmptyString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(2, [""])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_twoEmptyStrings(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["", ""])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_oneNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_twoNewLines(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(5, ["\n", "\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_NewLineAndEmptyString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["\n",""])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_emptyStringAndNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["", "\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\n")
    self.assertEqual(readLines[1], "\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_oneString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(2, ["hey"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\t\they\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_twoStrings(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(1, ["hey","Joe"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\they\tJoe\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_threeStrings(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(1, ["hey", "magnificent", "Joe"])
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "\they\tmagnificent\tJoe\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_oneStringEndingWithNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(3, ["hey\n"])
    self.assertEqual(len(readLines), 2)
    self.assertEqual(readLines[0], "\t\t\they\n")
    self.assertEqual(readLines[1], "\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_twoStringsEndingWithNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(4, ["hey\n", "Joe\n"])
    self.assertEqual(len(readLines), 3)
    self.assertEqual(readLines[0], "\t\t\t\they\n")
    self.assertEqual(readLines[1], "\t\t\t\tJoe\n")
    self.assertEqual(readLines[2], "\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_stringsAndNewLine(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(4, ["hey\n", "Joe\n", "\n"])
    self.assertEqual(len(readLines), 4)
    self.assertEqual(readLines[0], "\t\t\t\they\n")
    self.assertEqual(readLines[1], "\t\t\t\tJoe\n")
    self.assertEqual(readLines[2], "\n")
    self.assertEqual(readLines[3], "\n")

  def test_writeStringsIndentedToFileThenAppendNewLine_stringsAndNewLineAndEmptyString(self):
    readLines = self.helper_writeStringsIndentedToFileThenAppendNewLine(4, ["hey\n", "Joe\n", "\n", ""])
    self.assertEqual(len(readLines), 5)
    self.assertEqual(readLines[0], "\t\t\t\they\n")
    self.assertEqual(readLines[1], "\t\t\t\tJoe\n")
    self.assertEqual(readLines[2], "\n")
    self.assertEqual(readLines[3], "\n")
    self.assertEqual(readLines[4], "\n")

  def helper_writeStringsIndentedToFileThenAppendNewLine(self, indent, lines):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeStringsIndentedToFileThenAppendNewLine(file, indent, lines)
    file.close()
    return filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")

  def test_writeLinesToFileRaisesExceptionWhenAskingNonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToFileThenAppendNewLine(file, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToFileThenAppendNewLine(file, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToFileThenAppendNewLine(file, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToFileThenAppendNewLine("text.txt", ["firstLine"])

  def test_writeLinesToFileThenAppendNewLine_Noline(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, [])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),0)

  def test_writeLinesToFileThenAppendNewLine_emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, [""])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),1)
    self.assertEqual(readLines[0], "\n")

  def test_writeLinesToFileThenAppendNewLine_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["this is me"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),1)
    self.assertEqual(readLines[0],"this is me\n")

  def test_writeLinesToFileThenAppendNewLine_1lineEndingWithNewline(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["this is me\n"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),2)
    self.assertEqual(readLines[0],"this is me\n")
    self.assertEqual(readLines[1],"\n")

  def test_writeLinesToFileThenAppendNewLine_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["this is me:","\tJohn Doe, VIP executor"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),2)
    self.assertEqual(readLines[0],"this is me:\n")
    self.assertEqual(readLines[1],"\tJohn Doe, VIP executor\n")

  def test_writeLinesToFileThenAppendNewLine_3lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["this is me:","\tJohn Doe, VIP executor","tel: 0875432123"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),3)
    self.assertEqual(readLines[0],"this is me:\n")
    self.assertEqual(readLines[1],"\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2],"tel: 0875432123\n")