import os
import sys
import unittest

sys.path.append('..')

from modules import htmlBuilder
from modules import filerw
from modules import htmlBody
from modules import webLibs

class HtmlBodyTests(unittest.TestCase):

  def test_constructor_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(file, -2)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(file, None)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(file, "")
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(file, True)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody("./unitTests/temp/test.txt", 2)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(None, 2)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(False, 2)

  def test_includeFileThenAppendNewLine_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["line 1", "line 2"])
    body = htmlBody.HtmlBody(file, 2)
    with self.assertRaises(Exception):
      body.includeFileThenAppendNewLine(file)
    with self.assertRaises(Exception):
      body.includeFileThenAppendNewLine(["line3", "line4"])
    with self.assertRaises(Exception):
      body.includeFileThenAppendNewLine(None)
    with self.assertRaises(Exception):
      body.includeFileThenAppendNewLine(True)
    with self.assertRaises(Exception):
      body.includeFileThenAppendNewLine("heyho")

  def test_includeFileThenAppendNewLine_includeEmptyFile(self):
    file2 = open("./unitTests/temp/test2.txt", "w")
    file2.close()
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["line 1", "line 2"])
    body = htmlBody.HtmlBody(file, 2)
    body.includeFileThenAppendNewLine("./unitTests/temp/test2.txt")
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "")

  def test_includeFileThenAppendNewLine_includeNonEmptyFile(self):
    file2 = open("./unitTests/temp/test2.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file2, ["include 1", "include 2"])
    file2.close()
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["line 1", "line 2"])
    body = htmlBody.HtmlBody(file, 3)
    body.includeFileThenAppendNewLine("./unitTests/temp/test2.txt")
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 5)
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "\t\t\tinclude 1")
    self.assertEqual(lines[3], "\t\t\tinclude 2")
    self.assertEqual(lines[4], "")

  def test_includeFileThenAppendNewLine_chaining(self):
    file2 = open("./unitTests/temp/test2.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file2, ["include 1", "include 2"])
    file2.close()
    file3 = open("./unitTests/temp/test3.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file3, ["include 3", "include 4"])
    file3.close()
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["line 1", "line 2"])
    body = htmlBody.HtmlBody(file, 3)
    body.includeFileThenAppendNewLine("./unitTests/temp/test2.txt") \
        .includeFileThenAppendNewLine("./unitTests/temp/test3.txt")
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 8)
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "\t\t\tinclude 1")
    self.assertEqual(lines[3], "\t\t\tinclude 2")
    self.assertEqual(lines[4], "")
    self.assertEqual(lines[5], "\t\t\tinclude 3")
    self.assertEqual(lines[6], "\t\t\tinclude 4")
    self.assertEqual(lines[7], "")
