import os
import sys
import unittest

sys.path.append('..')
import htmlBuilder

class HtmlBuilderTests(unittest.TestCase):

  def setUp(self):
    if not os.path.exists('./unitTests/temp'):
      os.makedirs('./unitTests/temp')

  def test_getIndentedTabRaisesExceptionWhenAskingNonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getIndentedTab(0)
    with self.assertRaises(Exception):
      htmlBuilder.getIndentedTab(-1)
    with self.assertRaises(Exception):
      htmlBuilder.getIndentedTab(-10)
    with self.assertRaises(Exception):
      htmlBuilder.getIndentedTab(124)
    with self.assertRaises(Exception):
      htmlBuilder.getIndentedTab('hello')

  def test_getIndentedTabWithNormalValues(self):
    self.assertEqual(htmlBuilder.getIndentedTab(1),'\t')
    self.assertEqual(htmlBuilder.getIndentedTab(2),'\t\t')
    self.assertEqual(htmlBuilder.getIndentedTab(3),'\t\t\t')
    self.assertEqual(htmlBuilder.getIndentedTab(4),'\t\t\t\t')
    self.assertEqual(htmlBuilder.getIndentedTab(5),'\t\t\t\t\t')
    self.assertEqual(htmlBuilder.getIndentedTab(10),'\t\t\t\t\t\t\t\t\t\t')

  def test_getLinesFromFileWithEndingNewLine_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY")
    file.close()
    linesFromFile = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0],"HEY")

  def test_getLinesFromFileWithEndingNewLine_1line_1emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("HEY\n")
    file.close()
    linesFromFile = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 1)
    self.assertEqual(linesFromFile[0],"HEY\n")

  def test_getLinesFromFileWithEndingNewLine_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    file.write("hello dear\n")
    file.write("this is the tester\n")
    file.close()
    linesFromFile = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(linesFromFile), 2)
    self.assertEqual(linesFromFile[0],"hello dear\n")
    self.assertEqual(linesFromFile[1],"this is the tester\n")

  def test_writeLinesToFileRaisesExceptionWhenAskingNonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      htmlBuilder.writeLinesToFile(file, "asd")
    with self.assertRaises(Exception):
      htmlBuilder.writeLinesToFile(file, 1)
    with self.assertRaises(Exception):
      htmlBuilder.writeLinesToFile(file, None)
    with self.assertRaises(Exception):
      htmlBuilder.writeLinesToFile("text.txt", ["firstLine"])

  def test_writeLinesToFileThenAppendNewLine_Noline(self):
    file = open("./unitTests/temp/test.txt", "w")
    htmlBuilder.writeLinesToFileThenAppendNewLine(file, [])
    file.close()
    readLines = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),0)

  def test_writeLinesToFileThenAppendNewLine_emptyLine(self):
    file = open("./unitTests/temp/test.txt", "w")
    htmlBuilder.writeLinesToFileThenAppendNewLine(file, [""])
    file.close()
    readLines = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),1)
    self.assertEqual(readLines[0], "\n")

  def test_writeLinesToFileThenAppendNewLine_1line(self):
    file = open("./unitTests/temp/test.txt", "w")
    htmlBuilder.writeLinesToFileThenAppendNewLine(file, ["this is me"])
    file.close()
    readLines = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),1)
    self.assertEqual(readLines[0],"this is me\n")

  def test_writeLinesToFileThenAppendNewLine_1lineEndingWithNewline(self):
    file = open("./unitTests/temp/test.txt", "w")
    htmlBuilder.writeLinesToFileThenAppendNewLine(file, ["this is me\n"])
    file.close()
    readLines = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),2)
    self.assertEqual(readLines[0],"this is me\n")
    self.assertEqual(readLines[1],"\n")

  def test_writeLinesToFileThenAppendNewLine_2lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    htmlBuilder.writeLinesToFileThenAppendNewLine(file, ["this is me:","\tJohn Doe, VIP executor"])
    file.close()
    readLines = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),2)
    self.assertEqual(readLines[0],"this is me:\n")
    self.assertEqual(readLines[1],"\tJohn Doe, VIP executor\n")

  def test_writeLinesToFileThenAppendNewLine_3lines(self):
    file = open("./unitTests/temp/test.txt", "w")
    htmlBuilder.writeLinesToFileThenAppendNewLine(file, ["this is me:","\tJohn Doe, VIP executor","tel: 0875432123"])
    file.close()
    readLines = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines),3)
    self.assertEqual(readLines[0],"this is me:\n")
    self.assertEqual(readLines[1],"\tJohn Doe, VIP executor\n")
    self.assertEqual(readLines[2],"tel: 0875432123\n")