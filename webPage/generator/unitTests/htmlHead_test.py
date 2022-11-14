import sys

sys.path.append('..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.paths.definitions.filePathTypeForUT import FilePathTypeForUT as File

from modules import htmlBuilder
from modules import filerw
from modules import htmlHead
from modules.paths import path
from modules import webLibs

class HtmlHeadTests(AutoUnitTest):

  def test_constructor_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(file, -2)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(file, None)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(file, "")
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(file, True)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2), 2)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(None, 2)
    with self.assertRaises(Exception):
      htmlHead.HtmlHead(False, 2)

  def test_setTitle_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    with self.assertRaises(Exception):
      head.setTitle("")
    with self.assertRaises(Exception):
      head.setTitle(None)
    with self.assertRaises(Exception):
      head.setTitle(23)

  def test_setTitle_multipleTimes(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    head.setTitle("Title 1")
    with self.assertRaises(Exception):
      head.setTitle("Title 2")
    with self.assertRaises(Exception):
      head.setTitle("Title 3")

  def test_setTitle_example(self):
    for title in ["title", "my page", "Look At This 23!#"]:
      file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
      filerw.writeLinesToExistingFileThenAppendNewLine(file, ["random string", "another random string"])
      head = htmlHead.HtmlHead(file, 2)
      head.setTitle(title)
      file.close()
      line = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
      self.assertEqual(len(line), 3)
      self.assertEqual(line[0], "random string")
      self.assertEqual(line[1], "another random string")
      self.assertEqual(line[2], htmlBuilder.getHtmlTitle(title, 2))

  def test_setFavicon_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    with self.assertRaises(Exception):
      head.setFavicon("")
    with self.assertRaises(Exception):
      head.setFavicon(None)
    with self.assertRaises(Exception):
      head.setFavicon(23)

  def test_setFavicon_multipleTimes(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    head.setFavicon("icon1.png")
    with self.assertRaises(Exception):
      head.setFavicon("icon1.png")
    with self.assertRaises(Exception):
      head.setFavicon("icon2.png")
    with self.assertRaises(Exception):
      head.setFaviconByType(File.FOR_TEST_TEXTFILE3)

  def test_setFavicon_example(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["random string", "another random string"])
    head = htmlHead.HtmlHead(file, 2)
    head.setFavicon("./images/logo.ico")
    file.close()
    line = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(line), 3)
    self.assertEqual(line[0], "random string")
    self.assertEqual(line[1], "another random string")
    self.assertEqual(line[2], htmlBuilder.getHtmlFavicon("./images/logo.ico", 2))

  def test_setFaviconByType_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    head = htmlHead.HtmlHead(file, 2)
    with self.assertRaises(Exception):
      head.setFaviconByType("")
    with self.assertRaises(Exception):
      head.setFaviconByType(filePath)
    with self.assertRaises(Exception):
      head.setFaviconByType(None)
    with self.assertRaises(Exception):
      head.setFaviconByType(23)

  def test_setFaviconByType_multipleTimes(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    head = htmlHead.HtmlHead(file, 2)
    head.setFaviconByType(File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      head.setFaviconByType(File.FOR_TEST_TEXTFILE2)
    with self.assertRaises(Exception):
      head.setFaviconByType(File.FOR_TEST_TEXTFILE3)
    with self.assertRaises(Exception):
      head.setFavicon("icon2.png")

  def test_setFaviconByType_example(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    file = open(filePath, "w")
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["random string", "another random string"])
    head = htmlHead.HtmlHead(file, 2)
    head.setFaviconByType(File.FOR_TEST_TEXTFILE2)
    file.close()
    line = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(line), 3)
    self.assertEqual(line[0], "random string")
    self.assertEqual(line[1], "another random string")
    self.assertEqual(line[2], htmlBuilder.getHtmlFavicon(path.getRelativeFilePathToProjectRoot(File.FOR_TEST_TEXTFILE2),
                                                         2))

  def test_setMetaScreenOptimizedForMobile_multipleTimes(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    head.setMetaScreenOptimizedForMobile()
    with self.assertRaises(Exception):
      head.setMetaScreenOptimizedForMobile()
    with self.assertRaises(Exception):
      head.setMetaScreenOptimizedForMobile()

  def test_setMetaScreenOptimizedForMobile_example(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["random string", "another random string"])
    head = htmlHead.HtmlHead(file, 2)
    head.setMetaScreenOptimizedForMobile()
    file.close()
    line = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(line), 3)
    self.assertEqual(line[0], "random string")
    self.assertEqual(line[1], "another random string")
    self.assertEqual(line[2], htmlBuilder.getMetaScreenOptimizedForMobile(2))

  def test_includeFileAsInlineCSS_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
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
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["random string", "another random string"])
    file.close()
    fileDest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(fileDest, ["<html>", "\t<head>"])
    head = htmlHead.HtmlHead(fileDest, 3)
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    head.includeFileAsInlineCSS(filePath)
    fileDest.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 6)
    self.assertEqual(lines[0], "<html>")
    self.assertEqual(lines[1], "\t<head>")
    self.assertEqual(lines[2], "\t\t\t<style>")
    self.assertEqual(lines[3], "\t\t\t\trandom string")
    self.assertEqual(lines[4], "\t\t\t\tanother random string")
    self.assertEqual(lines[5], "\t\t\t</style>")

  def test_includeFileByTypeAsInlineCSS_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    with self.assertRaises(Exception):
      head.includeFileByTypeAsInlineCSS(file)
    with self.assertRaises(Exception):
      head.includeFileByTypeAsInlineCSS("")
    with self.assertRaises(Exception):
      head.includeFileByTypeAsInlineCSS(None)
    with self.assertRaises(Exception):
      head.includeFileByTypeAsInlineCSS(23)
    with self.assertRaises(Exception):
      head.includeFileByTypeAsInlineCSS(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2))

  def test_includeFileByTypeAsInlineCSS_example(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["random string", "another random string"])
    file.close()
    fileDest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(fileDest, ["<html>", "\t<head>"])
    head = htmlHead.HtmlHead(fileDest, 3)
    head.includeFileByTypeAsInlineCSS(File.FOR_TEST_TEXTFILE2)
    fileDest.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 6)
    self.assertEqual(lines[0], "<html>")
    self.assertEqual(lines[1], "\t<head>")
    self.assertEqual(lines[2], "\t\t\t<style>")
    self.assertEqual(lines[3], "\t\t\t\trandom string")
    self.assertEqual(lines[4], "\t\t\t\tanother random string")
    self.assertEqual(lines[5], "\t\t\t</style>")

  def test_addFontAwesome_v611_multipleTimes(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    head.addFontAwesome_v611()
    with self.assertRaises(Exception):
      head.addFontAwesome_v611()
    with self.assertRaises(Exception):
      head.addFontAwesome_v611()

  def test_addFontAwesome_v611_example(self):
    # get lines to compare with
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    webLibs.addFontAwesome_v611(file, 3)
    file.close()
    faLines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE2)
    # add lib and compare
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 3)
    head.addFontAwesome_v611()
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 3 + len(faLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for faLine in faLines:
      self.assertEqual(faLine, lines[3 + i])
      i += 1

  def test_addJquery_v360_multipleTimes(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    head.addJquery_v360()
    with self.assertRaises(Exception):
      head.addJquery_v360()
    with self.assertRaises(Exception):
      head.addJquery_v360()

  def test_addjQuery_v360_example(self):
    # get lines to compare with
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    webLibs.addJquery_v360(file, 3)
    file.close()
    libLines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE2)
    # add lib and compare
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 3)
    head.addJquery_v360()
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 3 + len(libLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for libLine in libLines:
      self.assertEqual(libLine, lines[3 + i])
      i += 1

  def test_addGoogleIcons_multipleTimes(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    head.addGoogleIcons()
    with self.assertRaises(Exception):
      head.addGoogleIcons()
    with self.assertRaises(Exception):
      head.addGoogleIcons()

  def test_addGoogleIcons_example(self):
    # get lines to compare with
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    webLibs.addGoogleIcons(file, 4)
    file.close()
    libLines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE2)
    # add lib and compare
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 4)
    head.addGoogleIcons()
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 3 + len(libLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for libLine in libLines:
      self.assertEqual(libLine, lines[3 + i])
      i += 1

  def test_addMaterialize_v110_alpha_multipleTimes(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    head.addMaterialize_v110_alpha()
    with self.assertRaises(Exception):
      head.addMaterialize_v110_alpha()
    with self.assertRaises(Exception):
      head.addMaterialize_v110_alpha()

  def test_addMaterialize_v110_alpha_example(self):
    # get lines to compare with
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    webLibs.addMaterialize_v110_alpha(file, 4)
    file.close()
    libLines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE2)
    # add lib and compare
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 4)
    head.addMaterialize_v110_alpha()
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 3 + len(libLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for libLine in libLines:
      self.assertEqual(libLine, lines[3 + i])
      i += 1

  def test_addGoogleFont_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
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
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    head.addGoogleFont("gq4fg43qgq4wfq")
    with self.assertRaises(Exception):
      head.addGoogleFont("asd3as2das?asd")
    with self.assertRaises(Exception):
      head.addGoogleFont("g45g5434gqf")

  def test_addGoogleFont_example(self):
    # get lines to compare with
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    webLibs.addGoogleFont(file, 5, "?fontName=TimesNewRoman&type=bold")
    file.close()
    libLines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE2)
    # add lib and compare
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 5)
    head.addGoogleFont("?fontName=TimesNewRoman&type=bold")
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 3 + len(libLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for libLine in libLines:
      self.assertEqual(libLine, lines[3 + i])
      i += 1

  def test_addJQueryLoadingOverlay_v217_multipleTimes(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    head.addJQueryLoadingOverlay_v217()
    with self.assertRaises(Exception):
      head.addJQueryLoadingOverlay_v217()
    with self.assertRaises(Exception):
      head.addJQueryLoadingOverlay_v217()

  def test_addJQueryLoadingOverlay_v217_example(self):
    # get lines to compare with
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    webLibs.addJQueryLoadingOverlay_v217(file, 5)
    file.close()
    libLines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE2)
    # add lib and compare
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(file, ["line 1", "line 2", "line 3"])
    head = htmlHead.HtmlHead(file, 5)
    head.addJQueryLoadingOverlay_v217()
    file.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 3 + len(libLines))
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "line 2")
    self.assertEqual(lines[2], "line 3")
    i = 0
    for libLine in libLines:
      self.assertEqual(libLine, lines[3 + i])
      i += 1

  def test_function_chaining(self):
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE2,
                                                                                 ["first line", "second line"])
    filerw.writeLinesToExistingOrNewlyCreatedFileByTypeThenAppendNewLineAndClose(File.FOR_TEST_TEXTFILE3,
                                                           ["first line in this as well", "I also have a second line"])
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    head = htmlHead.HtmlHead(file, 2)
    head.setTitle("Programming puzzle-pieces") \
      .setFavicon("./webPage/images/favicon.png") \
      .setMetaScreenOptimizedForMobile() \
      .includeFileAsInlineCSS(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)) \
      .addFontAwesome_v611() \
      .addJquery_v360() \
      .addGoogleIcons() \
      .addMaterialize_v110_alpha() \
      .addGoogleFont("?family=Arima+Madurai:wght@500&display=swap") \
      .addJQueryLoadingOverlay_v217() \
      .includeFileAsInlineCSS(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE3)) \
      .includeFileByTypeAsInlineCSS(File.FOR_TEST_TEXTFILE3)
