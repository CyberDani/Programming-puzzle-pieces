import sys
import unittest

sys.path.append('..')

from modules import htmlBuilder
from modules import filerw
from modules import htmlHead
from modules import webLibs

class HtmlHeadTests(unittest.TestCase):

  def test_constructor_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(file, -2)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(file, None)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(file, "")
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(file, True)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead("./unitTests/temp/test.txt", 2)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(None, 2)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(False, 2)

  def test_setTitle_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    with self.assertRaises(Exception):
      head.setTitle("")
    with self.assertRaises(Exception):
      head.setTitle(None)
    with self.assertRaises(Exception):
      head.setTitle(23)

  def test_setTitle_multipleTimes(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    head.setTitle("Title 1")
    with self.assertRaises(Exception):
      head.setTitle("Title 2")
    with self.assertRaises(Exception):
      head.setTitle("Title 3")

  def test_setTitle_example(self):
    for title in ["title", "my page", "Look At This 23!#"]:
      file = open("./unitTests/temp/test.txt", "w")
      filerw.writeLinesToExistingFileThenAppendNewLine(file, ["random string", "another random string"])
      head = htmlHead.HtmlHead(file, 2)
      head.setTitle(title)
      file.close()
      line = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
      self.assertEqual(len(line), 3)
      self.assertEqual(line[0], "random string")
      self.assertEqual(line[1], "another random string")
      self.assertEqual(line[2], htmlBuilder.getHtmlTitle(title, 2))

  def test_setFavicon_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    with self.assertRaises(Exception):
      head.setFavicon("")
    with self.assertRaises(Exception):
      head.setFavicon(None)
    with self.assertRaises(Exception):
      head.setFavicon(23)

  def test_setFavicon_multipleTimes(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    head.setFavicon("icon1.png")
    with self.assertRaises(Exception):
      head.setFavicon("icon1.png")
    with self.assertRaises(Exception):
      head.setFavicon("icon2.png")

  def test_setFavicon_example(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["random string", "another random string"])
    head = htmlHead.HtmlHead(file, 2)
    head.setFavicon("./images/logo.ico")
    file.close()
    line = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(line), 3)
    self.assertEqual(line[0], "random string")
    self.assertEqual(line[1], "another random string")
    self.assertEqual(line[2], htmlBuilder.getHtmlFavicon("./images/logo.ico", 2))

  def test_setMetaScreenOptimizedForMobile_multipleTimes(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    head.setMetaScreenOptimizedForMobile()
    with self.assertRaises(Exception):
      head.setMetaScreenOptimizedForMobile()
    with self.assertRaises(Exception):
      head.setMetaScreenOptimizedForMobile()

  def test_setMetaScreenOptimizedForMobile_example(self):
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["random string", "another random string"])
    head = htmlHead.HtmlHead(file, 2)
    head.setMetaScreenOptimizedForMobile()
    file.close()
    line = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(line), 3)
    self.assertEqual(line[0], "random string")
    self.assertEqual(line[1], "another random string")
    self.assertEqual(line[2], htmlBuilder.getMetaScreenOptimizedForMobile(2))

  def test_includeFileAsInlineCSS_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    with self.assertRaises(Exception):
      head.includeFileAsInlineCSS(file)
    with self.assertRaises(Exception):
      head.includeFileAsInlineCSS("")
    with self.assertRaises(Exception):
      head.includeFileAsInlineCSS(None)
    with self.assertRaises(Exception):
      head.includeFileAsInlineCSS(23)

  def test_includeFileAsInlineCSS_example(self):
    file = open("./unitTests/temp/test2.txt", "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["random string", "another random string"])
    file.close()
    fileDest = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(fileDest, ["<html>", "\t<head>"])
    head = htmlHead.HtmlHead(fileDest, 3)
    head.includeFileAsInlineCSS("./unitTests/temp/test2.txt")
    fileDest.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 6)
    self.assertEqual(lines[0], "<html>")
    self.assertEqual(lines[1], "\t<head>")
    self.assertEqual(lines[2], "\t\t\t<style>")
    self.assertEqual(lines[3], "\t\t\t\trandom string")
    self.assertEqual(lines[4], "\t\t\t\tanother random string")
    self.assertEqual(lines[5], "\t\t\t</style>")

  def test_addFontAwesome_v611_multipleTimes(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    head.addFontAwesome_v611()
    with self.assertRaises(Exception):
      head.addFontAwesome_v611()
    with self.assertRaises(Exception):
      head.addFontAwesome_v611()

  def test_addFontAwesome_v611_example(self):
    # get lines to compare with
    file = open("./unitTests/temp/test2.txt", "w")
    webLibs.addFontAwesome_v611(file, 3)
    file.close()
    faLines = filerw.getLinesByFilePath("./unitTests/temp/test2.txt")
    # add lib and compare
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 3)
    head.addFontAwesome_v611()
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3 + len(faLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for faLine in faLines:
      self.assertEqual(faLine, lines[3 + i])
      i += 1

  def test_addJquery_v360_multipleTimes(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    head.addJquery_v360()
    with self.assertRaises(Exception):
      head.addJquery_v360()
    with self.assertRaises(Exception):
      head.addJquery_v360()

  def test_addFontAwesome_v611_example(self):
    # get lines to compare with
    file = open("./unitTests/temp/test2.txt", "w")
    webLibs.addJquery_v360(file, 3)
    file.close()
    libLines = filerw.getLinesByFilePath("./unitTests/temp/test2.txt")
    # add lib and compare
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 3)
    head.addJquery_v360()
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3 + len(libLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for libLine in libLines:
      self.assertEqual(libLine, lines[3 + i])
      i += 1

  def test_addGoogleIcons_multipleTimes(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    head.addGoogleIcons()
    with self.assertRaises(Exception):
      head.addGoogleIcons()
    with self.assertRaises(Exception):
      head.addGoogleIcons()

  def test_addGoogleIcons_example(self):
    # get lines to compare with
    file = open("./unitTests/temp/test2.txt", "w")
    webLibs.addGoogleIcons(file, 4)
    file.close()
    libLines = filerw.getLinesByFilePath("./unitTests/temp/test2.txt")
    # add lib and compare
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 4)
    head.addGoogleIcons()
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3 + len(libLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for libLine in libLines:
      self.assertEqual(libLine, lines[3 + i])
      i += 1

  def test_addMaterialize_v110_alpha_multipleTimes(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    head.addMaterialize_v110_alpha()
    with self.assertRaises(Exception):
      head.addMaterialize_v110_alpha()
    with self.assertRaises(Exception):
      head.addMaterialize_v110_alpha()

  def test_addMaterialize_v110_alpha_example(self):
    # get lines to compare with
    file = open("./unitTests/temp/test2.txt", "w")
    webLibs.addMaterialize_v110_alpha(file, 4)
    file.close()
    libLines = filerw.getLinesByFilePath("./unitTests/temp/test2.txt")
    # add lib and compare
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 4)
    head.addMaterialize_v110_alpha()
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3 + len(libLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for libLine in libLines:
      self.assertEqual(libLine, lines[3 + i])
      i += 1

  def test_addGoogleFont_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    with self.assertRaises(Exception):
      head.addGoogleFont("")
    with self.assertRaises(Exception):
      head.addGoogleFont(True)
    with self.assertRaises(Exception):
      head.addGoogleFont(None)
    with self.assertRaises(Exception):
      head.addGoogleFont(23)

  def test_addGoogleFont_multipleTimes(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    head.addGoogleFont("gq4fg43qgq4wfq")
    with self.assertRaises(Exception):
      head.addGoogleFont("asd3as2das?asd")
    with self.assertRaises(Exception):
      head.addGoogleFont("g45g5434gqf")

  def test_addGoogleFont_example(self):
    # get lines to compare with
    file = open("./unitTests/temp/test2.txt", "w")
    webLibs.addGoogleFont(file, 5, "?fontName=TimesNewRoman&type=bold")
    file.close()
    libLines = filerw.getLinesByFilePath("./unitTests/temp/test2.txt")
    # add lib and compare
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 5)
    head.addGoogleFont("?fontName=TimesNewRoman&type=bold")
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3 + len(libLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for libLine in libLines:
      self.assertEqual(libLine, lines[3 + i])
      i += 1

  def test_addJQueryLoadingOverlay_v217_multipleTimes(self):
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    head.addJQueryLoadingOverlay_v217()
    with self.assertRaises(Exception):
      head.addJQueryLoadingOverlay_v217()
    with self.assertRaises(Exception):
      head.addJQueryLoadingOverlay_v217()

  def test_addJQueryLoadingOverlay_v217_example(self):
    # get lines to compare with
    file = open("./unitTests/temp/test2.txt", "w")
    webLibs.addJQueryLoadingOverlay_v217(file, 5)
    file.close()
    libLines = filerw.getLinesByFilePath("./unitTests/temp/test2.txt")
    # add lib and compare
    file = open("./unitTests/temp/test.txt", "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 5)
    head.addJQueryLoadingOverlay_v217()
    file.close()
    lines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3 + len(libLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for libLine in libLines:
      self.assertEqual(libLine, lines[3 + i])
      i += 1

  def test_function_chaining(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose("./unitTests/temp/test2.txt",
                                                                                 ["first line", "second line"])
    filerw.writeLinesToExistingOrNewlyCreatedFileByPathThenAppendNewLineAndClose("./unitTests/temp/test3.txt",
                                                                                 ["first line in this as well", "I also have a second line"])
    file = open("./unitTests/temp/test.txt", "w")
    head = htmlHead.HtmlHead(file, 2)
    head.setTitle("Programming puzzle-pieces") \
      .setFavicon("./webPage/images/favicon.png") \
      .setMetaScreenOptimizedForMobile() \
      .includeFileAsInlineCSS("./unitTests/temp/test2.txt") \
      .addFontAwesome_v611() \
      .addJquery_v360() \
      .addGoogleIcons() \
      .addMaterialize_v110_alpha() \
      .addGoogleFont("?family=Arima+Madurai:wght@500&display=swap") \
      .addJQueryLoadingOverlay_v217() \
      .includeFileAsInlineCSS("./unitTests/temp/test3.txt")
