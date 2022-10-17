import os
import sys
import unittest

sys.path.append('..')

from defTypes.dirPathTypeForUT import DirectoryPathTypeForUT as Dir
from defTypes.filePathTypeForUT import FilePathTypeForUT as File

from modules import htmlBuilder
from modules import filerw
from modules import htmlBody
from modules import path

class HtmlBodyTests(unittest.TestCase):

  def test_constructor_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(file, -2)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(file, None)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(file, "")
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(file, True)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2), 2)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(None, 2)
    with self.assertRaises(Exception):
      htmlBody.HtmlBody(False, 2)

  def test_includeFileThenAppendNewLine_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2"])
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
    file2 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    file2.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2"])
    body = htmlBody.HtmlBody(file, 2)
    filePathToInclude = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    body.includeFileThenAppendNewLine(filePathToInclude)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "")

  def test_includeFileThenAppendNewLine_includeNonEmptyFile(self):
    file2 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToExistingFileThenAppendNewLine(file2, ["include 1", "include 2"])
    file2.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2"])
    body = htmlBody.HtmlBody(file, 3)
    filePathToInclude = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    body.includeFileThenAppendNewLine(filePathToInclude)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 5)
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "\t\t\tinclude 1")
    self.assertEqual(lines[3], "\t\t\tinclude 2")
    self.assertEqual(lines[4], "")

  def test_includeFileThenAppendNewLine_chaining(self):
    file2 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToExistingFileThenAppendNewLine(file2, ["include 1", "include 2"])
    file2.close()
    file3 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE3)
    filerw.writeLinesToExistingFileThenAppendNewLine(file3, ["include 3", "include 4"])
    file3.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2"])
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    filePath3 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE3)
    body = htmlBody.HtmlBody(file, 3)
    body.includeFileThenAppendNewLine(filePath2) \
        .includeFileThenAppendNewLine(filePath3)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 8)
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "\t\t\tinclude 1")
    self.assertEqual(lines[3], "\t\t\tinclude 2")
    self.assertEqual(lines[4], "")
    self.assertEqual(lines[5], "\t\t\tinclude 3")
    self.assertEqual(lines[6], "\t\t\tinclude 4")
    self.assertEqual(lines[7], "")

  def test_includeFileByTypeThenAppendNewLine_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2"])
    body = htmlBody.HtmlBody(file, 2)
    with self.assertRaises(Exception):
      body.includeFileByTypeThenAppendNewLine(file)
    file.close()
    with self.assertRaises(Exception):
      body.includeFileByTypeThenAppendNewLine(["line3", "line4"])
    with self.assertRaises(Exception):
      body.includeFileByTypeThenAppendNewLine(None)
    with self.assertRaises(Exception):
      body.includeFileByTypeThenAppendNewLine(True)
    with self.assertRaises(Exception):
      body.includeFileByTypeThenAppendNewLine(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2))
    with self.assertRaises(Exception):
      body.includeFileByTypeThenAppendNewLine("heyho")
    with self.assertRaises(Exception):
      body.includeFileByTypeThenAppendNewLine(Dir.PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34)
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    if filerw.fileExistsByPath(filePath):
      os.remove(filePath)

  def test_includeFileByTypeThenAppendNewLine_includeEmptyFile(self):
    testFilePath1 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    filerw.createOrOverwriteWithEmptyFileByType(File.FOR_TEST_TEXTFILE2)
    file = open(testFilePath1, "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2"])
    body = htmlBody.HtmlBody(file, 2)
    body.includeFileByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2)
    file.close()
    lines = filerw.getLinesByPath(testFilePath1)
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "")

  def test_includeFileByTypeThenAppendNewLine_includeNonEmptyFile(self):
    testFilePath1 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    testFilePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(testFilePath2,
                                                                                 ["include 1", "include 2"])
    file = open(testFilePath1, "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2"])
    body = htmlBody.HtmlBody(file, 3)
    body.includeFileByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2)
    file.close()
    lines = filerw.getLinesByPath(testFilePath1)
    self.assertEqual(len(lines), 5)
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "\t\t\tinclude 1")
    self.assertEqual(lines[3], "\t\t\tinclude 2")
    self.assertEqual(lines[4], "")

  def test_includeFileByTypeThenAppendNewLine_chaining(self):
    testFilePath1 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    testFilePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    testFilePath3 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE3)
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(testFilePath2,
                                                                                 ["include 1", "include 2"])
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose(testFilePath3,
                                                                                 ["include 3", "include 4"])
    file = open(testFilePath1, "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2"])
    body = htmlBody.HtmlBody(file, 3)
    body.includeFileByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2) \
        .includeFileByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE3)
    file.close()
    lines = filerw.getLinesByPath(testFilePath1)
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
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
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
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 3)
    body.openHtmlTagThenAppendNewLine("div", "class='magicalDiv'")
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t\t\t<div class=\"magicalDiv\">")

  def test_openHtmlTagThenAppendNewLine_addTwoTag(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("div", "class='magicalDiv'") \
        .openHtmlTagThenAppendNewLine("table")
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t<div class=\"magicalDiv\">")
    self.assertEqual(lines[3], "\t\t<table>")

  def test_openHtmlTagThenAppendNewLine_addThreeTag(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 2)
    body.openHtmlTagThenAppendNewLine("div", "class='magicalDiv'") \
        .openHtmlTagThenAppendNewLine("table") \
        .openHtmlTagThenAppendNewLine("tr")
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 5)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t\t<div class=\"magicalDiv\">")
    self.assertEqual(lines[3], "\t\t\t<table>")
    self.assertEqual(lines[4], "\t\t\t\t<tr>")

  def test_openHtmlTagThenAppendNewLine_indentationWith1HtmlTag(self):
    file2 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToExistingFileThenAppendNewLine(file2, ["1. include", "2. include"])
    file2.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["first line", "second line"])
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("div", "class='magicalDiv'") \
        .includeFileThenAppendNewLine(filePath2)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 6)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t<div class=\"magicalDiv\">")
    self.assertEqual(lines[3], "\t\t1. include")
    self.assertEqual(lines[4], "\t\t2. include")
    self.assertEqual(lines[5], "")

  def test_openHtmlTagThenAppendNewLine_indentationWith2HtmlTag(self):
    file2 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToFile(file2, ["1. include", "2. include"])
    file2.close()
    file3 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE3)
    filerw.writeLinesToFile(file3, ["next", "next -> next", "next -> next -> next"])
    file3.close()
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    filePath3 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE3)
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("div", "class='magicalDiv'") \
        .includeFileThenAppendNewLine(filePath2) \
        .openHtmlTagThenAppendNewLine("div", "class='nestedDiv'") \
        .includeFileThenAppendNewLine(filePath3)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 9)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t<div class=\"magicalDiv\">")
    self.assertEqual(lines[3], "\t\t1. include")
    self.assertEqual(lines[4], "\t\t2. include")
    self.assertEqual(lines[5], "\t\t<div class=\"nestedDiv\">")
    self.assertEqual(lines[6], "\t\t\tnext")
    self.assertEqual(lines[7], "\t\t\tnext -> next")
    self.assertEqual(lines[8], "\t\t\tnext -> next -> next")

  def test_openHtmlTagThenAppendNewLine_jQueryLikeSelectors(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 3)
    body.openHtmlTagThenAppendNewLine("div.cl1#id1#id2.cl2#id3", "class='magicDiv' id='myId' default")
    body.closeLastOpenedHtmlTag()
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t\t\t<div id=\"id1 id2 id3 myId\" class=\"cl1 cl2 magicDiv\" default>")
    self.assertEqual(lines[3], "\t\t\t</div>")

  def test_closeLastOpenedHtmlTag_closeNothing(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    body = htmlBody.HtmlBody(file, 1)
    with self.assertRaises(Exception):
      body.closeLastOpenedHtmlTag()
    file.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("table").closeLastOpenedHtmlTag()
    with self.assertRaises(Exception):
      body.closeLastOpenedHtmlTag()
    file.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("table").openHtmlTagThenAppendNewLine("tr") \
        .closeLastOpenedHtmlTag().closeLastOpenedHtmlTag()
    with self.assertRaises(Exception):
      body.closeLastOpenedHtmlTag()
    file.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("table").openHtmlTagThenAppendNewLine("tr").openHtmlTagThenAppendNewLine("td") \
        .closeLastOpenedHtmlTag().closeLastOpenedHtmlTag().closeLastOpenedHtmlTag()
    with self.assertRaises(Exception):
      body.closeLastOpenedHtmlTag()

  def test_closeLastOpenedHtmlTag_oneTag(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("a", "href='link.com'").closeLastOpenedHtmlTag()
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t<a href=\"link.com\">")
    self.assertEqual(lines[3], "\t</a>")

  def test_closeLastOpenedHtmlTag_twoTag(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 1)
    body.openHtmlTagThenAppendNewLine("h2").openHtmlTagThenAppendNewLine("a", "href='link.com'") \
        .closeLastOpenedHtmlTag().closeLastOpenedHtmlTag()
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 6)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t<h2>")
    self.assertEqual(lines[3], "\t\t<a href=\"link.com\">")
    self.assertEqual(lines[4], "\t\t</a>")
    self.assertEqual(lines[5], "\t</h2>")

  def test_closeLastOpenedHtmlTag_threeTag(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["first line", "second line"])
    body = htmlBody.HtmlBody(file, 3)
    body.openHtmlTagThenAppendNewLine("div").openHtmlTagThenAppendNewLine("div", "class='myDiv'") \
        .openHtmlTagThenAppendNewLine("span") \
        .closeLastOpenedHtmlTag().closeLastOpenedHtmlTag().closeLastOpenedHtmlTag()
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 8)
    self.assertEqual(lines[0], "first line")
    self.assertEqual(lines[1], "second line")
    self.assertEqual(lines[2], "\t\t\t<div>")
    self.assertEqual(lines[3], "\t\t\t\t<div class=\"myDiv\">")
    self.assertEqual(lines[4], "\t\t\t\t\t<span>")
    self.assertEqual(lines[5], "\t\t\t\t\t</span>")
    self.assertEqual(lines[6], "\t\t\t\t</div>")
    self.assertEqual(lines[7], "\t\t\t</div>")

  def test_closeLastOpenedHtmlTag_indentation(self):
    file2 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToFile(file2, ["1. include", "2. include"])
    file2.close()
    file3 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE3)
    filerw.writeLinesToFile(file3, ["next", "next -> next", "next -> next -> next"])
    file3.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["first line", "second line"])
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    filePath3 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE3)
    body = htmlBody.HtmlBody(file, 2)
    body.openHtmlTagThenAppendNewLine("table").includeFileThenAppendNewLine(filePath2)
    body.openHtmlTagThenAppendNewLine("tr").includeFileThenAppendNewLine(filePath3)
    body.closeLastOpenedHtmlTag().includeFileThenAppendNewLine(filePath2)
    body.closeLastOpenedHtmlTag().includeFileThenAppendNewLine(filePath2)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
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

  def test_addHtmlNewLineThenAppendNewLine_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    body = htmlBody.HtmlBody(file, 2)
    with self.assertRaises(Exception):
      body.addHtmlNewLineThenAppendNewLine(None)
    with self.assertRaises(Exception):
      body.addHtmlNewLineThenAppendNewLine(True)
    with self.assertRaises(Exception):
      body.addHtmlNewLineThenAppendNewLine("")
    with self.assertRaises(Exception):
      body.addHtmlNewLineThenAppendNewLine("Zero")
    with self.assertRaises(Exception):
      body.addHtmlNewLineThenAppendNewLine(0)
    with self.assertRaises(Exception):
      body.addHtmlNewLineThenAppendNewLine(-1)

  def test_addHtmlNewLineThenAppendNewLine_1br(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["simple line"])
    body = htmlBody.HtmlBody(file, 1)
    body.addHtmlNewLineThenAppendNewLine(1)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "simple line")
    self.assertEqual(lines[1], htmlBuilder.getHtmlNewLines(1, 1))

  def test_addHtmlNewLineThenAppendNewLine_2br(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["simple line"])
    body = htmlBody.HtmlBody(file, 3)
    body.addHtmlNewLineThenAppendNewLine(2)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "simple line")
    self.assertEqual(lines[1], htmlBuilder.getHtmlNewLines(3, 2))

  def test_addHtmlNewLineThenAppendNewLine_5br(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["simple line"])
    body = htmlBody.HtmlBody(file, 2)
    body.addHtmlNewLineThenAppendNewLine(5)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "simple line")
    self.assertEqual(lines[1], htmlBuilder.getHtmlNewLines(2, 5))

  def test_addHtmlNewLineThenAppendNewLine_2brAnd5br(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["simple line"])
    body = htmlBody.HtmlBody(file, 4)
    body.addHtmlNewLineThenAppendNewLine(2).addHtmlNewLineThenAppendNewLine(5)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "simple line")
    self.assertEqual(lines[1], htmlBuilder.getHtmlNewLines(4, 2))
    self.assertEqual(lines[2], htmlBuilder.getHtmlNewLines(4, 5))

  def test_addJsScriptSrcThenAppendNewLine_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    body = htmlBody.HtmlBody(file, 4)
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine(False, None, None, None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("", None, None, None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("hello", None, None, None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("www.mysite.com/res.js", "sha215-23", None, None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("www.mysite.com/res.js", None, "anonymous", None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("www.mysite.com/res.js", None, None, "no-refferer")
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("www.mysite.com/res.js", None, "anonymous", "no-refferer")
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("www.mysite.com/res.js", "sha512-23", None, "no-refferer")
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("www.mysite.com/res.js", "sha512-23", "anonymous", None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("www.mysite.com/res.js", "a", "x", "z")
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("www.mysite.com/res.js", "abc", "anonymous", "no-refferer")
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("www.mysite.com/res.js", "sha512-asdasdc-xcx", "abc", "no-refferer")
    with self.assertRaises(Exception):
      body.addJsScriptSrcThenAppendNewLine("www.mysite.com/res.js", "sha512-asdasdc-xcx", "anonymous", "ab")

  def test_addJsScriptSrcThenAppendNewLine_justUrl(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["- 1 -", "- 2 -"])
    body = htmlBody.HtmlBody(file, 1)
    body.addJsScriptSrcThenAppendNewLine("myAwesomeSite.com/randomScript.js", None, None, None)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    jsLines = htmlBuilder.getJsScriptSrc(1, "myAwesomeSite.com/randomScript.js", None, None, None)
    self.assertEqual(len(lines), 2 + len(jsLines))
    self.assertEqual(lines[0], "- 1 -")
    self.assertEqual(lines[1], "- 2 -")
    for i in range(0, len(jsLines)):
      self.assertEqual(lines[2 + i], jsLines[i])

  def test_addJsScriptSrcThenAppendNewLine_urlIntegrityCrossoriginReferrerpolicy(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["- 1 -", "- 2 -"])
    body = htmlBody.HtmlBody(file, 6)
    body.addJsScriptSrcThenAppendNewLine("https://lookatthis.com/itsascript.js",
                                        "sha512-wgn28cn12ed02d==", "geekyBoy", "no-refferrer")
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    jsLines = htmlBuilder.getJsScriptSrc(6, "https://lookatthis.com/itsascript.js",
                                         "sha512-wgn28cn12ed02d==", "geekyBoy", "no-refferrer")
    self.assertEqual(len(lines), 2 + len(jsLines))
    self.assertEqual(lines[0], "- 1 -")
    self.assertEqual(lines[1], "- 2 -")
    for i in range(0, len(jsLines)):
      self.assertEqual(lines[2 + i], jsLines[i])

  def test_addJsScriptSrcByTypeThenAppendNewLine_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    body = htmlBody.HtmlBody(file, 4)
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(False, None, None, None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine("", None, None, None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine("hello", None, None, None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, "sha215-23", None, None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, None, "anonymous", None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, None, None, "no-refferer")
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, None, "anonymous", "no-refferer")
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, "sha512-23", None, "no-refferer")
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, "sha512-23", "anonymous", None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, "a", "x", "z")
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, "abc", "anonymous", "no-refferer")
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, "sha512-asdasdc-xcx", "abc", "no-refferer")
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, "sha512-asdasdc-xcx", "anonymous", "ab")
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine("myAwesomeSite.com/randomScript.js", None, None, None)
    with self.assertRaises(Exception):
      body.addJsScriptSrcByTypeThenAppendNewLine("https://lookatthis.com/itsascript.js",
                                               "sha512-wgn28cn12ed02d==", "geekyBoy", "no-refferrer")

  def test_addJsScriptSrcByTypeThenAppendNewLine_justUrl(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["- 1 -", "- 2 -"])
    body = htmlBody.HtmlBody(file, 1)
    body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE2, None, None, None)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    jsFilePath = path.getRelativeFilePathToIndexHtml(File.FOR_TEST_TEXTFILE2)
    jsLines = htmlBuilder.getJsScriptSrc(1, jsFilePath, None, None, None)
    self.assertEqual(len(lines), 2 + len(jsLines))
    self.assertEqual(lines[0], "- 1 -")
    self.assertEqual(lines[1], "- 2 -")
    for i in range(0, len(jsLines)):
      self.assertEqual(lines[2 + i], jsLines[i])

  def test_addJsScriptSrcByTypeThenAppendNewLine_urlIntegrityCrossoriginReferrerpolicy(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["- 1 -", "- 2 -"])
    body = htmlBody.HtmlBody(file, 6)
    body.addJsScriptSrcByTypeThenAppendNewLine(File.FOR_TEST_TEXTFILE3,
                                                "sha512-wgn28cn12ed02d==", "geekyBoy", "no-refferrer")
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    jsFilePath = path.getRelativeFilePathToIndexHtml(File.FOR_TEST_TEXTFILE3)
    jsLines = htmlBuilder.getJsScriptSrc(6, jsFilePath, "sha512-wgn28cn12ed02d==", "geekyBoy", "no-refferrer")
    self.assertEqual(len(lines), 2 + len(jsLines))
    self.assertEqual(lines[0], "- 1 -")
    self.assertEqual(lines[1], "- 2 -")
    for i in range(0, len(jsLines)):
      self.assertEqual(lines[2 + i], jsLines[i])

  def test_includeFileAsInlineJs_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    body = htmlBody.HtmlBody(file, 1)
    with self.assertRaises(Exception):
      body.includeFileAsInlineJs("nonExistingFile.js")
    with self.assertRaises(Exception):
      body.includeFileAsInlineJs(None)
    with self.assertRaises(Exception):
      body.includeFileAsInlineJs(False)
    with self.assertRaises(Exception):
      body.includeFileAsInlineJs(file)
    with self.assertRaises(Exception):
      body.includeFileAsInlineJs(122)

  def test_includeFileAsInlineJs_example(self):
    file2 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToFile(file2, ["function getTwo() {", "\treturn 2;", "}"])
    file2.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["\tsome line", "\tsome another line here"])
    body = htmlBody.HtmlBody(file, 1)
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    body.includeFileAsInlineJs(filePath2)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 7)
    self.assertEqual(lines[0], "\tsome line")
    self.assertEqual(lines[1], "\tsome another line here")
    self.assertEqual(lines[2], "\t<script>")
    self.assertEqual(lines[3], "\t\tfunction getTwo() {")
    self.assertEqual(lines[4], "\t\t\treturn 2;")
    self.assertEqual(lines[5], "\t\t}")
    self.assertEqual(lines[6], "\t</script>")

  def test_includeFileByTypeAsInlineJs_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    body = htmlBody.HtmlBody(file, 1)
    with self.assertRaises(Exception):
      body.includeFileByTypeAsInlineJs("nonExistingFile.js")
    with self.assertRaises(Exception):
      body.includeFileByTypeAsInlineJs(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2))
    with self.assertRaises(Exception):
      body.includeFileByTypeAsInlineJs(None)
    with self.assertRaises(Exception):
      body.includeFileByTypeAsInlineJs(False)
    with self.assertRaises(Exception):
      body.includeFileByTypeAsInlineJs(file)
    with self.assertRaises(Exception):
      body.includeFileByTypeAsInlineJs(122)

  def test_includeFileByTypeAsInlineJs_example(self):
    file2 = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToFile(file2, ["function getTwo() {", "\treturn 2;", "}"])
    file2.close()
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["\tsome line", "\tsome another line here"])
    body = htmlBody.HtmlBody(file, 1)
    body.includeFileByTypeAsInlineJs(File.FOR_TEST_TEXTFILE2)
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 7)
    self.assertEqual(lines[0], "\tsome line")
    self.assertEqual(lines[1], "\tsome another line here")
    self.assertEqual(lines[2], "\t<script>")
    self.assertEqual(lines[3], "\t\tfunction getTwo() {")
    self.assertEqual(lines[4], "\t\t\treturn 2;")
    self.assertEqual(lines[5], "\t\t}")
    self.assertEqual(lines[6], "\t</script>")
