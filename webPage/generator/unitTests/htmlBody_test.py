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

  def test_openHtmlTagThenAppendNewLine_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    body = htmlBody.HtmlBody(file, 3)
    body.openHtmlTagThenAppendNewLine("div")
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine("")
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine("<div")
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine("<div>")
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine("/div")
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine("div\nspan")
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine("ul selected")
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine("", "focused")
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine(12)
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine(2, "option2")
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine(None)
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine(None, "selected")
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine("abc", None)
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine("abc", 12)
    with self.assertRaises(Exception):
      body.openHtmlTagThenAppendNewLine("abc", False)

  def test_openHtmlTagThenAppendNewLine_addOneTag(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 3)
    body.openHtmlTagThenAppendNewLine("div", "class='magicalDiv'")
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t\t\t<div class='magicalDiv'>")

  def test_openHtmlTagThenAppendNewLine_addTwoTag(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("div", "class='magicalDiv'") \
        .openHtmlTagThenAppendNewLine("table")
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t<div class='magicalDiv'>")
    self.assertEqual(lines[3], "\t\t<table>")

  def test_openHtmlTagThenAppendNewLine_addThreeTag(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 2)
    body.openHtmlTagThenAppendNewLine("div", "class='magicalDiv'") \
        .openHtmlTagThenAppendNewLine("table") \
        .openHtmlTagThenAppendNewLine("tr")
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 5)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t\t<div class='magicalDiv'>")
    self.assertEqual(lines[3], "\t\t\t<table>")
    self.assertEqual(lines[4], "\t\t\t\t<tr>")

  def test_openHtmlTagThenAppendNewLine_indentationWith1HtmlTag(self):
    file2 = open("./unitTests/temp/test2.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file2, ["1. include", "2. include"])
    file2.close()
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("div", "class='magicalDiv'") \
        .includeFileThenAppendNewLine("./unitTests/temp/test2.txt")
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 6)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t<div class='magicalDiv'>")
    self.assertEqual(lines[3], "\t\t1. include")
    self.assertEqual(lines[4], "\t\t2. include")
    self.assertEqual(lines[5], "")

  def test_openHtmlTagThenAppendNewLine_indentationWith2HtmlTag(self):
    file2 = open("./unitTests/temp/test2.txt", "w")
    filerw.writeLinesToFile(file2, ["1. include", "2. include"])
    file2.close()
    file3 = open("./unitTests/temp/test3.txt", "w")
    filerw.writeLinesToFile(file3, ["next", "next -> next", "next -> next -> next"])
    file3.close()
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("div", "class='magicalDiv'") \
        .includeFileThenAppendNewLine("./unitTests/temp/test2.txt") \
        .openHtmlTagThenAppendNewLine("div", "class='nestedDiv'") \
        .includeFileThenAppendNewLine("./unitTests/temp/test3.txt")
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 9)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t<div class='magicalDiv'>")
    self.assertEqual(lines[3], "\t\t1. include")
    self.assertEqual(lines[4], "\t\t2. include")
    self.assertEqual(lines[5], "\t\t<div class='nestedDiv'>")
    self.assertEqual(lines[6], "\t\t\tnext")
    self.assertEqual(lines[7], "\t\t\tnext -> next")
    self.assertEqual(lines[8], "\t\t\tnext -> next -> next")

  def test_closeLastOpenedHtmlTag_closeNothing(self):
    file = open("./unitTests/temp/test.txt", "w")
    body = htmlBody.HtmlBody(file, 1)
    with self.assertRaises(Exception):
      body.closeLastOpenedHtmlTag()
    file.close()
    file = open("./unitTests/temp/test.txt", "w")
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("table").closeLastOpenedHtmlTag()
    with self.assertRaises(Exception):
      body.closeLastOpenedHtmlTag()
    file.close()
    file = open("./unitTests/temp/test.txt", "w")
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("table").openHtmlTagThenAppendNewLine("tr") \
        .closeLastOpenedHtmlTag().closeLastOpenedHtmlTag()
    with self.assertRaises(Exception):
      body.closeLastOpenedHtmlTag()
    file.close()
    file = open("./unitTests/temp/test.txt", "w")
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("table").openHtmlTagThenAppendNewLine("tr").openHtmlTagThenAppendNewLine("td") \
        .closeLastOpenedHtmlTag().closeLastOpenedHtmlTag().closeLastOpenedHtmlTag()
    with self.assertRaises(Exception):
      body.closeLastOpenedHtmlTag()

  def test_closeLastOpenedHtmlTag_oneTag(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("a", "href='link.com'").closeLastOpenedHtmlTag()
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t<a href='link.com'>")
    self.assertEqual(lines[3], "\t</a>")

  def test_closeLastOpenedHtmlTag_twoTag(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("h2").openHtmlTagThenAppendNewLine("a", "href='link.com'") \
        .closeLastOpenedHtmlTag().closeLastOpenedHtmlTag()
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 6)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t<h2>")
    self.assertEqual(lines[3], "\t\t<a href='link.com'>")
    self.assertEqual(lines[4], "\t\t</a>")
    self.assertEqual(lines[5], "\t</h2>")

  def test_closeLastOpenedHtmlTag_threeTag(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 3)
    body.openHtmlTagThenAppendNewLine("div").openHtmlTagThenAppendNewLine("div", "class='myDiv'") \
        .openHtmlTagThenAppendNewLine("span") \
        .closeLastOpenedHtmlTag().closeLastOpenedHtmlTag().closeLastOpenedHtmlTag()
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 8)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t\t\t<div>")
    self.assertEqual(lines[3], "\t\t\t\t<div class='myDiv'>")
    self.assertEqual(lines[4], "\t\t\t\t\t<span>")
    self.assertEqual(lines[5], "\t\t\t\t\t</span>")
    self.assertEqual(lines[6], "\t\t\t\t</div>")
    self.assertEqual(lines[7], "\t\t\t</div>")

  def test_closeLastOpenedHtmlTag_indentation(self):
    file2 = open("./unitTests/temp/test2.txt", "w")
    filerw.writeLinesToFile(file2, ["1. include", "2. include"])
    file2.close()
    file3 = open("./unitTests/temp/test3.txt", "w")
    filerw.writeLinesToFile(file3, ["next", "next -> next", "next -> next -> next"])
    file3.close()
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 2)
    body.openHtmlTagThenAppendNewLine("table").includeFileThenAppendNewLine("./unitTests/temp/test2.txt")
    body.openHtmlTagThenAppendNewLine("tr").includeFileThenAppendNewLine("./unitTests/temp/test3.txt")
    body.closeLastOpenedHtmlTag().includeFileThenAppendNewLine("./unitTests/temp/test2.txt")
    body.closeLastOpenedHtmlTag().includeFileThenAppendNewLine("./unitTests/temp/test2.txt")
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 15)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t\t<table>")
    self.assertEqual(lines[3], "\t\t\t1. include")
    self.assertEqual(lines[4], "\t\t\t2. include")
    self.assertEqual(lines[5], "\t\t\t<tr>")
    self.assertEqual(lines[6], "\t\t\t\tnext")
    self.assertEqual(lines[7], "\t\t\t\tnext -> next")
    self.assertEqual(lines[8], "\t\t\t\tnext -> next -> next")
    self.assertEqual(lines[9], "\t\t\t</tr>")
    self.assertEqual(lines[10], "\t\t\t1. include")
    self.assertEqual(lines[11], "\t\t\t2. include")
    self.assertEqual(lines[12], "\t\t</table>")
    self.assertEqual(lines[13], "\t\t1. include")
    self.assertEqual(lines[14], "\t\t2. include")
