import sys
import unittest

sys.path.append('..')
from modules import filerw
from modules import htmlBuilder

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

  def test_getLinesByFilePath_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY")
    file.close()
    linesFromFile = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByFilePath_1line_1emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY\n")
    file.close()
    linesFromFile = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLinesByFilePath_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    linesFromFile = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear")
    self.assertEqual(linesFromFile[1], "this is the tester")

  def test_getLinesWithEndingNewLine_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLinesWithEndingNewLine(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0],"HEY")

  def test_getLinesWithEndingNewLine_1line_1emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY\n")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLinesWithEndingNewLine(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0],"HEY\n")

  def test_getLinesWithEndingNewLine_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLinesWithEndingNewLine(file)
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0],"hello dear\n")
    self.assertEqual(linesFromFile[1],"this is the tester\n")

  def test_getLines_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLines(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLines_1line_1emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY\n")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLines(file)
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0], "HEY")

  def test_getLines_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    file = open("./unitTests/temp/test.txt", "r")
    linesFromFile = filerw.getLines(file)
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0], "hello dear")
    self.assertEqual(linesFromFile[1], "this is the tester")

  def test_writeStringsIndentedToFileThenAppendNewLine_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, "prefix", "asd")
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, "prefix", None)
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, 1, ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(file, ["prefix"], ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine("./unitTests/temp/test.txt", "prefix", ["asd"])
    with self.assertRaises(Exception):
      filerw.writeStringsPrefixedToFileThenAppendNewLine(None, "prefix", ["asd"])

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
    tabs = htmlBuilder.getIndentedTab(indent)
    filerw.writeStringsPrefixedToFileThenAppendNewLine(file, tabs, lines)
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

  def test_writeLinesToFile_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      filerw.writeLinesToFile(file, "asd")
    with self.assertRaises(Exception):
      filerw.writeLinesToFile(file, 1)
    with self.assertRaises(Exception):
      filerw.writeLinesToFile(file, None)
    with self.assertRaises(Exception):
      filerw.writeLinesToFile("text.txt", ["firstLine"])

  def test_writeLinesToFile_Noline(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, [])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),0)

  def test_writeLinesToFile_emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, [""])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 0)

  def test_writeLinesToFile_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, ["this is me"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),1)
    self.assertEqual(readLines[0],"this is me")

  def test_writeLinesToFile_1lineEndingWithNewline(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, ["this is me\n"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), 1)
    self.assertEqual(readLines[0], "this is me\n")

  def test_writeLinesToFile_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, ["this is me:","\tJohn Doe, VIP executor"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),2)
    self.assertEqual(readLines[0],"this is me:\n")
    self.assertEqual(readLines[1],"\tJohn Doe, VIP executor")

  def test_writeLinesToFile_3lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFile(file, ["this is me:","\tJohn Doe, VIP executor","tel: 0875432123"])
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),3)
    self.assertEqual(readLines[0],"this is me:\n")
    self.assertEqual(readLines[1],"\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2],"tel: 0875432123")

  def test_rTrimNewLines_nonSense(self):
    with self.assertRaises(Exception):
      filerw.rTrimNewLines()
    with self.assertRaises(Exception):
      filerw.rTrimNewLines("hello")
    with self.assertRaises(Exception):
      filerw.rTrimNewLines(None)
    with self.assertRaises(Exception):
      filerw.rTrimNewLines("hey\n")
    with self.assertRaises(Exception):
      filerw.rTrimNewLines(False)
    with self.assertRaises(Exception):
      filerw.rTrimNewLines(["one", None, "three"])

  def test_rTrimNewLines_emptyList(self):
    result = filerw.rTrimNewLines([])
    self.assertEqual(len(result), 0)

  def test_rTrimNewLines_oneElement(self):
    result = filerw.rTrimNewLines(["Hello!"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "Hello!")
    result = filerw.rTrimNewLines(["\n\tHello!"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "\n\tHello!")
    result = filerw.rTrimNewLines(["\n\tHello!\n"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "\n\tHello!")
    result = filerw.rTrimNewLines(["Hello\n\n"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "Hello")
    result = filerw.rTrimNewLines(["Hello\n\n\n\n\n\n\n"])
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "Hello")

  def test_rTrimNewLines_twoElements(self):
    result = filerw.rTrimNewLines(["Hello","hey\n"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "hey")
    result = filerw.rTrimNewLines(["hey\n", "Hello\n"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[1], "Hello")
    self.assertEqual(result[0], "hey")
    result = filerw.rTrimNewLines(["Hello","hey"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "hey")
    result = filerw.rTrimNewLines(["Hello","\n\n"])
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "")

  def test_rTrimNewLines_threeElements(self):
    result = filerw.rTrimNewLines(["Hello\n", "hey", "hi\n\n"])
    self.assertEqual(len(result), 3)
    self.assertEqual(result[0], "Hello")
    self.assertEqual(result[1], "hey")
    self.assertEqual(result[2], "hi")