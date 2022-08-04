import sys
import unittest

sys.path.append('..')

from defTypes import buildType
from defTypes import dbBranchType
from defTypes import buildSettings
from defTypes.filePathType import FilePathType as File

from modules import htmlBuilder
from modules import filerw
from modules import counter
from modules import path

def emptyHtmlHeadContent(settings):
  a = 2

def emptyHtmlBodyContent(settings):
  a = 2

def minimalistHtmlHeadContent(settings):
  htmlTabs = htmlBuilder.getEscapedTabs(settings.indentDepth)
  filerw.writeLinesToExistingFileThenAppendNewLine(settings.htmlOutputFile, [htmlTabs + "<title>Hey!</title>"])

def minimalistHtmlBodyContent(settings):
  htmlTabs = htmlBuilder.getEscapedTabs(settings.indentDepth)
  filerw.writeLinesToExistingFileThenAppendNewLine(settings.htmlOutputFile, [htmlTabs + "<h1>Hello!</h1>"])

class HtmlBuilderTests(unittest.TestCase):

  def test_writeIndexHtmlToFile_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    settings = buildSettings.BuildSettings(htmlOutputFile=file,
                                           buildOption=buildType.BuildType.BUILD,
                                           dbBranch=dbBranchType.DbBranchType.DEVEL,
                                           stepsCounter=counter.SimpleCounter(1),
                                           indentDepth=2)
    with self.assertRaises(Exception):
      htmlBuilder.buildIndexHtmlFile("hello", "hello", settings)
    with self.assertRaises(Exception):
      htmlBuilder.buildIndexHtmlFile(None, None, settings)
    with self.assertRaises(Exception):
      htmlBuilder.buildIndexHtmlFile(True, False, settings)

  def test_writeIndexHtmlToFile_emptyHtml(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    settings = buildSettings.BuildSettings(htmlOutputFile=file,
                                           buildOption=buildType.BuildType.BUILD,
                                           dbBranch=dbBranchType.DbBranchType.DEVEL,
                                           stepsCounter=counter.SimpleCounter(1),
                                           indentDepth=2)
    htmlBuilder.buildIndexHtmlFile(emptyHtmlHeadContent, emptyHtmlBodyContent, settings)
    file.close()
    emptyHtmlLines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(emptyHtmlLines), 6)
    self.assertEqual(emptyHtmlLines[0], "<html>")
    self.assertEqual(emptyHtmlLines[1], "\t<head>")
    self.assertEqual(emptyHtmlLines[2], "\t</head>")
    self.assertEqual(emptyHtmlLines[3], "\t<body>")
    self.assertEqual(emptyHtmlLines[4], "\t</body>")
    self.assertEqual(emptyHtmlLines[5], "</html>")

  def test_writeIndexHtmlToFile_minimalistHtml(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    settings = buildSettings.BuildSettings(htmlOutputFile=file,
                                           buildOption=buildType.BuildType.BUILD,
                                           dbBranch=dbBranchType.DbBranchType.DEVEL,
                                           stepsCounter=counter.SimpleCounter(1),
                                           indentDepth=2)
    htmlBuilder.buildIndexHtmlFile(minimalistHtmlHeadContent, minimalistHtmlBodyContent, settings)
    file.close()
    emptyHtmlLines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(emptyHtmlLines), 8)
    self.assertEqual(emptyHtmlLines[0], "<html>")
    self.assertEqual(emptyHtmlLines[1], "\t<head>")
    self.assertEqual(emptyHtmlLines[2], "\t\t<title>Hey!</title>")
    self.assertEqual(emptyHtmlLines[3], "\t</head>")
    self.assertEqual(emptyHtmlLines[4], "\t<body>")
    self.assertEqual(emptyHtmlLines[5], "\t\t<h1>Hello!</h1>")
    self.assertEqual(emptyHtmlLines[6], "\t</body>")
    self.assertEqual(emptyHtmlLines[7], "</html>")

  def test_getEscapedTabs_nonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getEscapedTabs(0)
    with self.assertRaises(Exception):
      htmlBuilder.getEscapedTabs(-1)
    with self.assertRaises(Exception):
      htmlBuilder.getEscapedTabs(-10)
    with self.assertRaises(Exception):
      htmlBuilder.getEscapedTabs(124)
    with self.assertRaises(Exception):
      htmlBuilder.getEscapedTabs('hello')
    with self.assertRaises(Exception):
      htmlBuilder.getEscapedTabs(False)
    with self.assertRaises(Exception):
      htmlBuilder.getEscapedTabs(None)

  def test_getEscapedTabs_examples(self):
    self.assertEqual(htmlBuilder.getEscapedTabs(1), '\t')
    self.assertEqual(htmlBuilder.getEscapedTabs(2), '\t\t')
    self.assertEqual(htmlBuilder.getEscapedTabs(3), '\t\t\t')
    self.assertEqual(htmlBuilder.getEscapedTabs(4), '\t\t\t\t')
    self.assertEqual(htmlBuilder.getEscapedTabs(5), '\t\t\t\t\t')
    self.assertEqual(htmlBuilder.getEscapedTabs(10), '\t\t\t\t\t\t\t\t\t\t')

  def test_getHtmlNewLines_nonsense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlNewLines(indentDepth = "two", nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlNewLines(indentDepth = 2, nrOfNewLines = "one")
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlNewLines(indentDepth = -2, nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlNewLines(indentDepth = 0, nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlNewLines(indentDepth = 100, nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = -1)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = 100)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = 0)

  def test_getHtmlNewLines_defaultParameter_nrOfNewLines_1(self):
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 1)
    self.assertEqual(newLines, "\t<br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 2)
    self.assertEqual(newLines, "\t\t<br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 3)
    self.assertEqual(newLines, "\t\t\t<br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 6)
    self.assertEqual(newLines, "\t\t\t\t\t\t<br\\>")

  def test_getHtmlNewLines_normalCases(self):
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = 1)
    self.assertEqual(newLines, "\t<br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 2, nrOfNewLines = 1)
    self.assertEqual(newLines, "\t\t<br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 4, nrOfNewLines = 1)
    self.assertEqual(newLines, "\t\t\t\t<br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = 2)
    self.assertEqual(newLines, "\t<br\\> <br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = 3)
    self.assertEqual(newLines, "\t<br\\> <br\\> <br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = 6)
    self.assertEqual(newLines, "\t<br\\> <br\\> <br\\> <br\\> <br\\> <br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 2, nrOfNewLines = 2)
    self.assertEqual(newLines, "\t\t<br\\> <br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 2, nrOfNewLines = 4)
    self.assertEqual(newLines, "\t\t<br\\> <br\\> <br\\> <br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 4, nrOfNewLines = 2)
    self.assertEqual(newLines, "\t\t\t\t<br\\> <br\\>")

  def test_addNewLineToHtmlOutputFile_nonsense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      htmlBuilder.addHtmlNewLineToFile("heyho", indentDepth = 2, nrOfNewLines = 2)
    with self.assertRaises(Exception):
      htmlBuilder.addHtmlNewLineToFile(file, indentDepth ="two", nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.addHtmlNewLineToFile(file, indentDepth = 2, nrOfNewLines ="one")
    with self.assertRaises(Exception):
      htmlBuilder.addHtmlNewLineToFile(file, indentDepth = -2, nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.addHtmlNewLineToFile(file, indentDepth = 0, nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.addHtmlNewLineToFile(file, indentDepth = 100, nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.addHtmlNewLineToFile(file, indentDepth = 1, nrOfNewLines = -1)
    with self.assertRaises(Exception):
      htmlBuilder.addHtmlNewLineToFile(file, indentDepth = 1, nrOfNewLines = 100)
    with self.assertRaises(Exception):
      htmlBuilder.addHtmlNewLineToFile(file, indentDepth = 1, nrOfNewLines = 0)
    file.close()

  def test_addNewLineToHtmlOutputFile_defaultParameter_nrOfNewLines_1(self):
    for indent in range(1, 6):
      newLines = htmlBuilder.getHtmlNewLines(indent)
      file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
      htmlBuilder.addHtmlNewLineToFile(file, indent)
      file.close()
      readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
      self.assertEqual(len(readLines), 1)
      self.assertEqual(readLines[0], newLines + "\n")

  def test_addFaviconToHtmlOutputFile_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      htmlBuilder.addFaviconToHtmlOutputFile(file, "favicon.png", -1)
    with self.assertRaises(Exception):
      htmlBuilder.addFaviconToHtmlOutputFile(file, "/img/fav.ico", None)
    with self.assertRaises(Exception):
      htmlBuilder.addFaviconToHtmlOutputFile(file, "./images/f.png", True)
    with self.assertRaises(Exception):
      htmlBuilder.addFaviconToHtmlOutputFile(file, None, 2)
    with self.assertRaises(Exception):
      htmlBuilder.addFaviconToHtmlOutputFile(file, 34, 2)
    with self.assertRaises(Exception):
      htmlBuilder.addFaviconToHtmlOutputFile(file, False, 2)
    with self.assertRaises(Exception):
      htmlBuilder.addFaviconToHtmlOutputFile(file, "", 2)
    with self.assertRaises(Exception):
      htmlBuilder.addFaviconToHtmlOutputFile(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1), "myFavicon.ico", 2)

  def test_addFaviconToHtmlOutputFile_examples(self):
    for indent in [3, 4, 5]:
      for favicon in ["fav.png", "./media/img/icon.ico", "../../myFavIcon.jpg"]:
        file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
        htmlBuilder.addFaviconToHtmlOutputFile(file, favicon, indent)
        file.close()
        line = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
        self.assertEqual(len(line), 1)
        self.assertEqual(line[0], htmlBuilder.getHtmlFavicon(favicon, indent))

  def test_addTitleToHtmlOutputFile_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      htmlBuilder.addTitleToHtmlOutputFile(file, "title", -1)
    with self.assertRaises(Exception):
      htmlBuilder.addTitleToHtmlOutputFile(file, "title", None)
    with self.assertRaises(Exception):
      htmlBuilder.addTitleToHtmlOutputFile(file, "title", True)
    with self.assertRaises(Exception):
      htmlBuilder.addTitleToHtmlOutputFile(file, None, 2)
    with self.assertRaises(Exception):
      htmlBuilder.addTitleToHtmlOutputFile(file, 34, 2)
    with self.assertRaises(Exception):
      htmlBuilder.addTitleToHtmlOutputFile(file, False, 2)
    with self.assertRaises(Exception):
      htmlBuilder.addTitleToHtmlOutputFile(file, "", 2)
    with self.assertRaises(Exception):
      htmlBuilder.addTitleToHtmlOutputFile(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1), "title", 2)

  def test_addTitleToHtmlOutputFile_examples(self):
    for indent in [2, 3, 4]:
      for title in ["title", "my page", "Look At This 23!#"]:
        file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
        htmlBuilder.addTitleToHtmlOutputFile(file, title, indent)
        file.close()
        line = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
        self.assertEqual(len(line), 1)
        self.assertEqual(line[0], htmlBuilder.getHtmlTitle(title, indent))

  def test_addMetaScreenOptimizedForMobileToHtmlOutputFile_nonSense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      htmlBuilder.addMetaScreenOptimizedForMobileToHtmlOutputFile(file, -3)
    with self.assertRaises(Exception):
      htmlBuilder.addMetaScreenOptimizedForMobileToHtmlOutputFile(file, "2")
    with self.assertRaises(Exception):
      htmlBuilder.addMetaScreenOptimizedForMobileToHtmlOutputFile(path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1), 2)

  def test_addMetaScreenOptimizedForMobileToHtmlOutputFile_examples(self):
    for indent in range(1, 5):
      file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
      htmlBuilder.addMetaScreenOptimizedForMobileToHtmlOutputFile(file, indent)
      file.close()
      lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
      self.assertEqual(len(lines), 1)
      self.assertEqual(lines[0], htmlBuilder.getMetaScreenOptimizedForMobile(indent))

  def test_getCssLinkHref_nonsense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(indentDepth=-3, url="www.mysite.com/res.css",
                                 integrity=None, crossorigin=None, referrerpolicy=None)
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(2, False, None, None, None)
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(2, "", None, None, None)
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "hello", None, None, None)
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", "sha215-23", None, None)
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", None, "anonymous", None)
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", None, None, "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", None, "anonymous", "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", "sha512-23", None, "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", "sha512-23", "anonymous", None)
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", "a", "x", "z")
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", "abc", "anonymous", "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", "sha512-asdasdc-xcx", "abc", "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", "sha512-asdasdc-xcx", "anonymous", "ab")

  def test_getCssLinkHref_justUrl(self):
    result = htmlBuilder.getCssLinkHref(1, "www.mysite.com/res.css", None, None, None)
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "\t<link href=\"www.mysite.com/res.css\" rel=\"stylesheet\" />")
    result = htmlBuilder.getCssLinkHref(2, "https://cdn.jsdelivr.net/npm/@materializecss/materialize"
                                           "@1.1.0-alpha/dist/css/materialize.min.css", None, None, None)
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "\t\t<link href=\"https://cdn.jsdelivr.net/npm/@materializecss/materialize"
                                "@1.1.0-alpha/dist/css/materialize.min.css\"")
    self.assertEqual(result[1], "\t\t\trel=\"stylesheet\" />")

  def test_getCssLinkHref_containsIntegrity(self):
    result = htmlBuilder.getCssLinkHref(3, "https://www.randomsite.com/resource.css", 
                    "asdsadbsdsadbi32gr3ur", "techguy", "refferrer")
    self.assertEqual(len(result), 3)
    self.assertEqual(result[0], "\t\t\t<link href=\"https://www.randomsite.com/resource.css\"")
    self.assertEqual(result[1], "\t\t\t\tintegrity=\"asdsadbsdsadbi32gr3ur\"")
    self.assertEqual(result[2], "\t\t\t\trel=\"stylesheet\" crossorigin=\"techguy\" referrerpolicy=\"refferrer\" />")

  def test_addCssLinkHrefToHtmlOutputFile_nonsense(self):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(htmlFile=file, indentDepth=-3, url="www.mysite.com/res.css",
                                                 integrity=None, crossorigin=None, referrerpolicy=None)
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile("file.html", 2, "https://site.com/random.css", None, None, None)
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 2, False, None, None, None)
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 2, "", None, None, None)
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "hello", None, None, None)
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", "sha215-23", None, None)
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", None, "anonymous", None)
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", None, None, "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", None, "anonymous", "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", "sha512-23", None, "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", "sha512-23", "anonymous", None)
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", "a", "x", "z")
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", "abc", "anonymous", "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", "sha512-asdasdc-xcx",
                                                 "abc", "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", "sha512-asdasdc-xcx",
                                                 "anonymous", "ab")
    file.close()

  def test_addCssLinkHrefToHtmlOutputFile_normalCases(self):
    self.cssLinkHrefTestHelper(1, "www.mysite.com/res.css", None, None, None)
    self.cssLinkHrefTestHelper(5, "https://cdn.jsdelivr.net/npm/@materializecss/materialize@1.1.0-alpha"
                                  "/dist/css/materialize.min.css",
                        None, None, None)
    self.cssLinkHrefTestHelper(3, "https://www.randomsite.com/resource.css", "asdsadbsdsadbi32gr3ur",
                               "techguy", "refferrer")

  def cssLinkHrefTestHelper(self, indentDepth, url, integrity, crossorigin, referrerpolicy):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    lines = htmlBuilder.getCssLinkHref(indentDepth, url, integrity, crossorigin, referrerpolicy)
    htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, indentDepth, url, integrity, crossorigin, referrerpolicy)
    file.close()
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), len(lines))
    for i in range(len(readLines)):
      self.assertEqual(readLines[i], lines[i] + "\n")

  def test_getHtmlFavicon_nonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlFavicon("favicon.ico", -1)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlFavicon("fav.png", None)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlFavicon("images/favicon.ico", True)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlFavicon(None, 1)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlFavicon(34, 2)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlFavicon(False, 3)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlFavicon("", 4)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlFavicon("X", 5)

  def test_getHtmlFavicon_examples(self):
    self.assertEqual(htmlBuilder.getHtmlFavicon("favicon.png", 1), "\t<link rel=\"icon\" href=\"favicon.png\">")
    self.assertEqual(htmlBuilder.getHtmlFavicon("/images/fav.ico", 2),
                     "\t\t<link rel=\"icon\" href=\"/images/fav.ico\">")
    self.assertEqual(htmlBuilder.getHtmlFavicon("../media/img/F.ico", 3),
                     "\t\t\t<link rel=\"icon\" href=\"../media/img/F.ico\">")

  def test_getHtmlTitle_nonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlTitle("title", -1)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlTitle("title", None)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlTitle("title", True)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlTitle(None, 2)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlTitle(34, 2)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlTitle(False, 2)
    with self.assertRaises(Exception):
      htmlBuilder.getHtmlTitle("", 2)

  def test_getHtmlTitle_examples(self):
    self.assertEqual(htmlBuilder.getHtmlTitle("Title", 2), "\t\t<title>Title</title>")
    self.assertEqual(htmlBuilder.getHtmlTitle("My pagE", 3), "\t\t\t<title>My pagE</title>")
    self.assertEqual(htmlBuilder.getHtmlTitle("awesome title here", 4), "\t\t\t\t<title>awesome title here</title>")

  def test_getJsScriptSrc_nonsense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(indentDepth=-3, url="www.mysite.com/res.js",
                                 integrity=None, crossorigin=None, referrerpolicy=None)
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(2, False, None, None, None)
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(2, "", None, None, None)
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "hello", None, None, None)
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "www.mysite.com/res.js", "sha215-23", None, None)
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "www.mysite.com/res.js", None, "anonymous", None)
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "www.mysite.com/res.js", None, None, "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "www.mysite.com/res.js", None, "anonymous", "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "www.mysite.com/res.js", "sha512-23", None, "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "www.mysite.com/res.js", "sha512-23", "anonymous", None)
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "www.mysite.com/res.js", "a", "x", "z")
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "www.mysite.com/res.js", "abc", "anonymous", "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "www.mysite.com/res.js", "sha512-asdasdc-xcx", "abc", "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.getJsScriptSrc(1, "www.mysite.com/res.js", "sha512-asdasdc-xcx", "anonymous", "ab")

  def test_getJsScriptSrc_justUrl(self):
    result = htmlBuilder.getJsScriptSrc(1, "https://randomsite.com/myscript.js", None, None, None)
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "\t<script src=\"https://randomsite.com/myscript.js\"></script>")
    result = htmlBuilder.getJsScriptSrc(2, "https://code.jquery.com/jquery-3.6.0.min.js", None, None, None)
    self.assertEqual(len(result), 1)
    self.assertEqual(result[0], "\t\t<script src=\"https://code.jquery.com/jquery-3.6.0.min.js\"></script>")

  def test_getJsScriptSrc_containsIntegrity(self):
    result = htmlBuilder.getJsScriptSrc(3, "https://randomsite.com/mySuperScript.js", 
                    "sha512-adasdbidbeiebewiwbf==", "theGeek", "no-refferrer")
    self.assertEqual(len(result), 3)
    self.assertEqual(result[0], "\t\t\t<script src=\"https://randomsite.com/mySuperScript.js\"")
    self.assertEqual(result[1], "\t\t\t\tintegrity=\"sha512-adasdbidbeiebewiwbf==\"")
    self.assertEqual(result[2], "\t\t\t\tcrossorigin=\"theGeek\" referrerpolicy=\"no-refferrer\"></script>")

  def test_addJsScriptSrcToHtmlOutputFile_normalCases(self):
    self.jsScriptSrcTestHelper(1, "www.myAwesomeSite.com/script.js", None, None, None)
    self.jsScriptSrcTestHelper(5, "https://cdn.jsdelivr.net/npm/gasparesganga-jquery-loading-overlay"
                                  "@2.1.7/dist/loadingoverlay.min.js",
                                  None, None, None)
    self.jsScriptSrcTestHelper(3, "https://www.randomsite.com/resource.js", "asfldfohsdofsdflndjfbfd",
                                  "TechGuy", "refferrer")

  def jsScriptSrcTestHelper(self, indentDepth, url, integrity, crossorigin, referrerpolicy):
    file = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    lines = htmlBuilder.getJsScriptSrc(indentDepth, url, integrity, crossorigin, referrerpolicy)
    htmlBuilder.addJsScriptSrcToHtmlOutputFile(file, indentDepth, url, integrity, crossorigin, referrerpolicy)
    file.close()
    readLines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(readLines), len(lines))
    for i in range(len(readLines)):
      self.assertEqual(readLines[i], lines[i] + "\n")

  def test_getMetaScreenOptimizedForMobile_nonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getMetaScreenOptimizedForMobile(-1)
    with self.assertRaises(Exception):
      htmlBuilder.getMetaScreenOptimizedForMobile(None)
    with self.assertRaises(Exception):
      htmlBuilder.getMetaScreenOptimizedForMobile(False)
    with self.assertRaises(Exception):
      htmlBuilder.getMetaScreenOptimizedForMobile("zero")
    with self.assertRaises(Exception):
      htmlBuilder.getMetaScreenOptimizedForMobile("")
    with self.assertRaises(Exception):
      htmlBuilder.getMetaScreenOptimizedForMobile([])

  def test_getMetaScreenOptimizedForMobile_examples(self):
    self.assertEqual(htmlBuilder.getMetaScreenOptimizedForMobile(1),
                     "\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>")
    self.assertEqual(htmlBuilder.getMetaScreenOptimizedForMobile(2),
                     "\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>")
    self.assertEqual(htmlBuilder.getMetaScreenOptimizedForMobile(3),
                     "\t\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>")
    self.assertEqual(htmlBuilder.getMetaScreenOptimizedForMobile(4),
                     "\t\t\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>")
    self.assertEqual(htmlBuilder.getMetaScreenOptimizedForMobile(5),
                     "\t\t\t\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>")

  def test_includeFileSurroundedByHtmlTagToHtmlOutputFile_nonSense(self):
    dest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    src = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    src.close()
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, "div", "", -1)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, src, "div", "", 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, None, "div", "", 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(None, None, "div", "", 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(None, filePath2, "div", "", 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, "div", "", False)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, "div", "", None)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(None, None, "div", "", None)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, "", "", 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, "div", None, 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, "span", 12, 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, 22, "", 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, None, "", 2)

  def test_includeFileSurroundedByHtmlTagToHtmlOutputFile_emptyFile(self):
    src = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    src.close()
    dest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, "a", "href='url.com'", 1)
    dest.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "\t<a href='url.com'>")
    self.assertEqual(lines[1], "\t</a>")

  def test_includeFileSurroundedByHtmlTagToHtmlOutputFile_emptyFile_2(self):
    src = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    src.close()
    dest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, "div", "", 2)
    dest.close()
    lines = filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "\t\t<div>")
    self.assertEqual(lines[1], "\t\t</div>")

  def test_includeFileSurroundedByHtmlTagToHtmlOutputFile_examples(self):
    lines = self.helper_includeFileSurroundedByHtmlTagToHtmlOutputFile(1, ["be proud of yourself"],
                                                                       "span", "class='myClass'")
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "\t<span class='myClass'>")
    self.assertEqual(lines[1], "\t\tbe proud of yourself")
    self.assertEqual(lines[2], "\t</span>")
    lines = self.helper_includeFileSurroundedByHtmlTagToHtmlOutputFile(2, ["<div>", "\thooray!", "</div>"],
                                                                       "footer", "")
    self.assertEqual(len(lines), 5)
    self.assertEqual(lines[0], "\t\t<footer>")
    self.assertEqual(lines[1], "\t\t\t<div>")
    self.assertEqual(lines[2], "\t\t\t\thooray!")
    self.assertEqual(lines[3], "\t\t\t</div>")
    self.assertEqual(lines[4], "\t\t</footer>")

  def test_includeFileSurroundedByHtmlTagToHtmlOutputFile_examples_2(self):
    lines = self.helper_includeFileSurroundedByHtmlTagToHtmlOutputFile_2(3, ["be proud of yourself", "find a meaning"],
                                                                       "span", "class='myClass'")
    self.assertEqual(len(lines), 7)
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "\tline 2")
    self.assertEqual(lines[2], "\t\t\tline 3")
    self.assertEqual(lines[3], "\t\t\t<span class='myClass'>")
    self.assertEqual(lines[4], "\t\t\t\tbe proud of yourself")
    self.assertEqual(lines[5], "\t\t\t\tfind a meaning")
    self.assertEqual(lines[6], "\t\t\t</span>")
    lines = self.helper_includeFileSurroundedByHtmlTagToHtmlOutputFile_2(2, ["<div>", "\thooray!", "</div>"],
                                                                       "footer", "")
    self.assertEqual(len(lines), 8)
    self.assertEqual(lines[0], "line 1")
    self.assertEqual(lines[1], "\tline 2")
    self.assertEqual(lines[2], "\t\t\tline 3")
    self.assertEqual(lines[3], "\t\t<footer>")
    self.assertEqual(lines[4], "\t\t\t<div>")
    self.assertEqual(lines[5], "\t\t\t\thooray!")
    self.assertEqual(lines[6], "\t\t\t</div>")
    self.assertEqual(lines[7], "\t\t</footer>")

  @staticmethod
  def helper_includeFileSurroundedByHtmlTagToHtmlOutputFile_2(indent, lines, htmlTag, htmlTagOption):
    src = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToExistingFileThenAppendNewLine(src, lines)
    src.close()
    dest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(dest, ["line 1", "\tline 2", "\t\t\tline 3"])
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, htmlTag, htmlTagOption, indent)
    dest.close()
    return filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)

  @staticmethod
  def helper_includeFileSurroundedByHtmlTagToHtmlOutputFile(indent, lines, htmlTag, htmlTagOption):
    src = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToExistingFileThenAppendNewLine(src, lines)
    src.close()
    dest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(dest, filePath2, htmlTag, htmlTagOption, indent)
    dest.close()
    return filerw.getLinesByType(File.FOR_TEST_TEXTFILE1)

  def test_includeFileToHtmlOutputFile_nonSense(self):
    dest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    src = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    src.close()
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileThenAppendNewLine(dest, filePath2, -1)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileThenAppendNewLine(dest, None, 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileThenAppendNewLine(None, None, 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileThenAppendNewLine(None, filePath2, 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileThenAppendNewLine(dest, filePath2, False)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileThenAppendNewLine(dest, filePath2, None)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileThenAppendNewLine(None, None, None)

  def test_includeFileToHtmlOutputFile_emptyFile(self):
    src = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    src.close()
    dest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    htmlBuilder.includeFileThenAppendNewLine(dest, filePath2, 1)
    dest.close()
    lines = filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)
    self.assertEqual(len(lines), 1)
    self.assertEqual(lines[0], "\n")

  def test_includeFileToHtmlOutputFile_normalCases(self):
    lines = self.helper_includeFileToHtmlOutputFile(1, ["be proud of yourself"])
    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "\tbe proud of yourself\n")
    self.assertEqual(lines[1], "\n")
    lines = self.helper_includeFileToHtmlOutputFile(2, ["<div>", "\thooray!", "</div>"])
    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "\t\t<div>\n")
    self.assertEqual(lines[1], "\t\t\thooray!\n")
    self.assertEqual(lines[2], "\t\t</div>\n")
    self.assertEqual(lines[3], "\n")

  def test_includeFileToHtmlOutputFile_normalCases_2(self):
    lines = self.helper_includeFileToHtmlOutputFile_2(1, ["be proud of yourself"])
    self.assertEqual(len(lines), 5)
    self.assertEqual(lines[0], "> first line\n")
    self.assertEqual(lines[1], ">> second line\n")
    self.assertEqual(lines[2], ">>> third line\n")
    self.assertEqual(lines[3], "\tbe proud of yourself\n")
    self.assertEqual(lines[4], "\n")
    lines = self.helper_includeFileToHtmlOutputFile_2(2, ["<div>", "\thooray!", "</div>"])
    self.assertEqual(len(lines), 7)
    self.assertEqual(lines[0], "> first line\n")
    self.assertEqual(lines[1], ">> second line\n")
    self.assertEqual(lines[2], ">>> third line\n")
    self.assertEqual(lines[3], "\t\t<div>\n")
    self.assertEqual(lines[4], "\t\t\thooray!\n")
    self.assertEqual(lines[5], "\t\t</div>\n")
    self.assertEqual(lines[6], "\n")

  @staticmethod
  def helper_includeFileToHtmlOutputFile_2(indent, lines):
    src = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToExistingFileThenAppendNewLine(src, lines)
    src.close()
    dest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filerw.writeLinesToExistingFileThenAppendNewLine(dest, ["> first line", ">> second line", ">>> third line"])
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    htmlBuilder.includeFileThenAppendNewLine(dest, filePath2, indent)
    dest.close()
    return filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)

  @staticmethod
  def helper_includeFileToHtmlOutputFile(indent, lines):
    src = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE2)
    filerw.writeLinesToExistingFileThenAppendNewLine(src, lines)
    src.close()
    dest = filerw.getFileWithWritePerm(File.FOR_TEST_TEXTFILE1)
    filePath2 = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE2)
    htmlBuilder.includeFileThenAppendNewLine(dest, filePath2, indent)
    dest.close()
    return filerw.getLinesByTypeWithEndingNewLine(File.FOR_TEST_TEXTFILE1)

  def test_filterJqueryLikeHtmlSelector_nonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector(None)
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector(False)
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector(["div"])
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector(2)
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("[div]")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("3+2")

  def test_filterJqueryLikeHtmlSelector_invalidSelector(self):
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("#hello")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector(".hello")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("..........")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("####")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector(".")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("#")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello.")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello#")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello..")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello##")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello#.")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello.#")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello.abc.")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello#abc#")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello.abc#")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello#abc.")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello.#abc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello#.abc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello# abc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello. abc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello#  abc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello.  abc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello#qwe abc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello.123 abc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello#123  abc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello.123  abc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello#\nabc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello.\nabc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello#qwe\nabc")
    with self.assertRaises(Exception):
      htmlBuilder.filterJqueryLikeHtmlSelector("hello.qwe\nabc")

  def test_filterJqueryLikeHtmlSelector_onlyHtmlTag(self):
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div")
    self.assertEqual(htmlTag, "div")
    self.assertFalse(htmlOptions)
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("table")
    self.assertEqual(htmlTag, "table")
    self.assertFalse(htmlOptions)
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("span")
    self.assertEqual(htmlTag, "span")
    self.assertFalse(htmlOptions)

  def test_filterJqueryLikeHtmlSelector_oneSelector(self):
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div.My-clasS")
    self.assertEqual(htmlTag, "div")
    self.assertEqual(htmlOptions, "class=\"My-clasS\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("table#importantId")
    self.assertEqual(htmlTag, "table")
    self.assertEqual(htmlOptions, "id=\"importantId\"")

  def test_filterJqueryLikeHtmlSelector_twoSelector(self):
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div.My-clasS.secondClass")
    self.assertEqual(htmlTag, "div")
    self.assertEqual(htmlOptions, "class=\"My-clasS secondClass\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("table#importantId#secondId")
    self.assertEqual(htmlTag, "table")
    self.assertEqual(htmlOptions, "id=\"importantId secondId\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("span.class#id")
    self.assertEqual(htmlTag, "span")
    self.assertEqual(htmlOptions, "id=\"id\" class=\"class\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("h1#myId.myClass")
    self.assertEqual(htmlTag, "h1")
    self.assertEqual(htmlOptions, "id=\"myId\" class=\"myClass\"")

  def test_filterJqueryLikeHtmlSelector_threeSelector(self):
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div.cl1.cl2.cl3")
    self.assertEqual(htmlTag, "div")
    self.assertEqual(htmlOptions, "class=\"cl1 cl2 cl3\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div.cl1.cl2#id3")
    self.assertEqual(htmlTag, "div")
    self.assertEqual(htmlOptions, "id=\"id3\" class=\"cl1 cl2\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div.cl1#id2.cl3")
    self.assertEqual(htmlTag, "div")
    self.assertEqual(htmlOptions, "id=\"id2\" class=\"cl1 cl3\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div.cl1#id2#id3")
    self.assertEqual(htmlTag, "div")
    self.assertEqual(htmlOptions, "id=\"id2 id3\" class=\"cl1\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div#id1.cl2.cl3")
    self.assertEqual(htmlTag, "div")
    self.assertEqual(htmlOptions, "id=\"id1\" class=\"cl2 cl3\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div#id1.cl2#id3")
    self.assertEqual(htmlTag, "div")
    self.assertEqual(htmlOptions, "id=\"id1 id3\" class=\"cl2\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div#id1#id2.cl3")
    self.assertEqual(htmlTag, "div")
    self.assertEqual(htmlOptions, "id=\"id1 id2\" class=\"cl3\"")
    htmlTag, htmlOptions = htmlBuilder.filterJqueryLikeHtmlSelector("div#id1#id2#id3")
    self.assertEqual(htmlTag, "div")
    self.assertEqual(htmlOptions, "id=\"id1 id2 id3\"")

  def test_extractDifferentValuesFromHtmlAttributesByKey_nonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", "")
    with self.assertRaises(Exception):
      htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", 123)
    with self.assertRaises(Exception):
      htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", False)
    with self.assertRaises(Exception):
      htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", None)
    with self.assertRaises(Exception):
      htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'",
                                                                                   ["option"])
    with self.assertRaises(Exception):
      htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(None, "option")
    with self.assertRaises(Exception):
      htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(234, "src")
    with self.assertRaises(Exception):
      htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(123, None)

  def test_extractDifferentValuesFromHtmlAttributesByKey_emptyAttributes(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("", "title")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("", "src")
    self.assertEqual(attributes, [])

  def test_extractDifferentValuesFromHtmlAttributesByKey_attrNotFound(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                                             "href=\"img/favicon.ico\" type=\"image/x-icon\"", "title")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\""
                                                       "masthead_custom_styles\" is=\"custom-style\" id=\"ext-styles\" "
                                                       "nonce=\"tG2l8WDVY7XYzWdAOVtRzA\"", "style")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                                              "src=\"jsbin/spf.vflset/spf.js\"", "alt")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"anim\"", "id")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"animated bold\"",
                                                                                         "id")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"animated bold\" "
                                                                                "selected class=\"active-tab\"", "id")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "upgrade")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "masthead")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "dark")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "shell")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "chunked")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "e")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "disable")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "clas")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "lot")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("_value=\"audi\"",
                                                                                              "value")
    self.assertEqual(attributes, [])

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_attrIsNotKeyValue(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\" selected",
                                                                                         "selected")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\" selected "
                                                                                       "class=\"myClass\"", "selected")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("selected value=\"audi\"",
                                                                                         "selected")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("selected", "selected")
    self.assertEqual(attributes, [])

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_emptyValue(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"\"", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"  \"", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"\t\"", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\" \r\n \t \"",
                                                                                              "value")
    self.assertEqual(attributes, [])

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_corrupt(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"   ", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value= ", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value= \n \t ", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi'", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='audi\"", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value \"audi\"", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value\"audi\"", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value 'audi'", "value")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value'audi'", "value")
    self.assertEqual(attributes, [])

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_quotes(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\"", "value")
    self.assertEqual(attributes, ["audi"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='audi'", "value")
    self.assertEqual(attributes, ["audi"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi'A3\"",
                                                                                              "value")
    self.assertEqual(attributes, ["audi'A3"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi'A3'\"",
                                                                                              "value")
    self.assertEqual(attributes, ["audi'A3'"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='audi\"A3'",
                                                                                              "value")
    self.assertEqual(attributes, ["audi\"A3"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='\"audi\"A3\"'",
                                                                                         "value")
    self.assertEqual(attributes, ["\"audi\"A3\""])

  def test_extractDifferentValuesFromHtmlAttributesByKey_oneValueFound(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                                             "href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, ["img/favicon.ico"])
    # I have found these tricky examples while implementing beforeWhitespaceDelimitedFind as an effort to minimize
    # code length
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                            "xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, ["img/favicon.ico"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                          "no-href=\"false\" xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, ["img/favicon.ico"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
        "hrefhref=\"image\" no-href=\"false\" xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, ["img/favicon.ico"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                                            "nonce=\"lix9PsSUHJxW7ghXrU5s0A\"", "nonce")
    self.assertEqual(attributes, ["lix9PsSUHJxW7ghXrU5s0A"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "disable-upgrade")
    self.assertEqual(attributes, ["true"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"preload\" href="
                                "\"https://r3---sn-8vq54voxgv-vu26.googlevideo.com/generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])

  def test_extractDifferentValuesFromHtmlAttributesByKey_whitespaces(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                         "rel =\"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                          "rel = \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                          "rel= \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                    "rel \n\r\t\t\t = \n\r\t\t\t \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                "\n\trel \n\r\t\t\t = \n\r\t\t\t \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
          "\n\trel \n\r\t\t\t = \n\r\t\t\t \"\r\n\t\t preload \t\t\t\n\t  \" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])

  def test_extractDifferentValuesFromHtmlAttributesByKey_multipleValuesFound(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                "method=\"get\" class=\"add_search_params pure-form\" style=\"display:inline-block\"",
                                "class")
    self.assertEqual(attributes, ["add_search_params", "pure-form"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                "method=\"get\" class=\"add_search_params pure-form hide-xs hide-sm hide-md\" "
                                "style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, ["add_search_params", "pure-form", "hide-xs", "hide-sm", "hide-md"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                "method=\"get\" class\n=\n\"add_search_params\tpure-form\r\nhide-xs     hide-sm"
                                "\t\t\t\n\r   \n\r    hide-md\n\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, ["add_search_params", "pure-form", "hide-xs", "hide-sm", "hide-md"])

  def test_extractDifferentValuesFromHtmlAttributesByKey_multipleDeclarations(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
              "method=\"get\" class=\"add_search_params cl2 cl3\" class=\"pure-form\" style=\"display:inline-block\"",
              "class")
    self.assertEqual(attributes, ["add_search_params", "cl2", "cl3"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
              "method=\"get\" class=\"add_search_params\" class=\"pure-form cl2 cl3\" style=\"display:inline-block\"",
              "class")
    self.assertEqual(attributes, ["add_search_params"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" class "
                              "method=\"get\" class=\"pure-form cl2 cl3\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, [])

  def test_extractDifferentValuesFromHtmlAttributesByKey_valueRepeats(self):
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                            "method=\"get\" class=\"cl1 cl1\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, ["cl1"])
    attributes = htmlBuilder.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                            "method=\"get\" class=\"cl1 cl1 cl2 cl1 cl3 cl2\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, ["cl1", "cl2", "cl3"])

  def test_getAttributeIdx_nonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getAttributeIdx("htmlAttribute", 12)
    with self.assertRaises(Exception):
      htmlBuilder.getAttributeIdx("htmlAttribute", None)
    with self.assertRaises(Exception):
      htmlBuilder.getAttributeIdx(None, None)
    with self.assertRaises(Exception):
      htmlBuilder.getAttributeIdx(12, False)
    with self.assertRaises(Exception):
      htmlBuilder.getAttributeIdx(None, "class")
    with self.assertRaises(Exception):
      htmlBuilder.getAttributeIdx(False, "id")

  def test_getAttributeIdx_emptyString(self):
    idx = htmlBuilder.getAttributeIdx("", "class")
    self.assertEqual(idx, -1)
    idx = htmlBuilder.getAttributeIdx("id=\"content\" class=\"clearfix\"", "")
    self.assertEqual(idx, -1)

  def test_getAttributeIdx_attrNotFound(self):
    idx = htmlBuilder.getAttributeIdx("htmlAttribute", "class")
    self.assertEqual(idx, -1)
    idx = htmlBuilder.getAttributeIdx("htmlAttribute no-href", "href")
    self.assertEqual(idx, -1)
    idx = htmlBuilder.getAttributeIdx("htmlAttribute hrefx", "href")
    self.assertEqual(idx, -1)
    idx = htmlBuilder.getAttributeIdx("htmlAttribute hrefhref", "href")
    self.assertEqual(idx, -1)
    idx = htmlBuilder.getAttributeIdx("no-href class='idk'", "href")
    self.assertEqual(idx, -1)
    idx = htmlBuilder.getAttributeIdx("hrefx class='idk'", "href")
    self.assertEqual(idx, -1)
    idx = htmlBuilder.getAttributeIdx("hrefhref class='idk'", "href")
    self.assertEqual(idx, -1)
    idx = htmlBuilder.getAttributeIdx("selected no-href class='idk'", "href")
    self.assertEqual(idx, -1)
    idx = htmlBuilder.getAttributeIdx("selected hrefx class='idk'", "href")
    self.assertEqual(idx, -1)
    idx = htmlBuilder.getAttributeIdx("selected hrefhref class='idk'", "href")
    self.assertEqual(idx, -1)

  def test_getAttributeIdx_attrFound(self):
    idx = htmlBuilder.getAttributeIdx("selected", "selected")
    self.assertEqual(idx, 0)
    idx = htmlBuilder.getAttributeIdx("default='1'", "default")
    self.assertEqual(idx, 0)
    idx = htmlBuilder.getAttributeIdx("default=\"1\"", "default")
    self.assertEqual(idx, 0)
    string = "value='234' selected"
    idx = htmlBuilder.getAttributeIdx(string, "selected")
    self.assertEqual(idx, string.find("selected"))
    idx = htmlBuilder.getAttributeIdx("selected class=\"className\"", "selected")
    self.assertEqual(idx, 0)
    idx = htmlBuilder.getAttributeIdx("selected greyed-out", "selected")
    self.assertEqual(idx, 0)
    string = "value='234' selected=\"false\""
    idx = htmlBuilder.getAttributeIdx(string, "selected")
    self.assertEqual(idx, string.find("selected"))
    idx = htmlBuilder.getAttributeIdx("selected=\"false\" class=\"className\"", "selected")
    self.assertEqual(idx, 0)
    idx = htmlBuilder.getAttributeIdx("selected=\"false\" greyed-out", "selected")
    self.assertEqual(idx, 0)
    string = "htmlAttribute no-href href"
    idx = htmlBuilder.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find(" href") + 1)
    string = "htmlAttribute hrefx href=\"value\""
    idx = htmlBuilder.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find("href="))
    string = "htmlAttribute hrefhref='value2' href='value3'"
    idx = htmlBuilder.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find("href='value3'"))
    string = "no-href=\"noValue\" href class='idk'"
    idx = htmlBuilder.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find("href class"))
    string = "hrefx href class='idk'"
    idx = htmlBuilder.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find("href class"))

  def test_getAttributeIdx_attrFoundMultipleTime(self):
    idx = htmlBuilder.getAttributeIdx("selected selected='false' selected selected", "selected")
    self.assertEqual(idx, 0)
    idx = htmlBuilder.getAttributeIdx("default='1' class=\"myClass\" default", "default")
    self.assertEqual(idx, 0)
    string = "htmlAttribute hrefhref='value2' href='value3' href href='val4'"
    idx = htmlBuilder.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find("href='value3'"))

  def test_getListOfHtmlAttributes_nonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getListOfHtmlAttributes(12)
    with self.assertRaises(Exception):
      htmlBuilder.getListOfHtmlAttributes(None)
    with self.assertRaises(Exception):
      htmlBuilder.getListOfHtmlAttributes(False)
    with self.assertRaises(Exception):
      htmlBuilder.getListOfHtmlAttributes([])

  def test_getListOfHtmlAttributes_onlyEmptyAndWhiteSpace(self):
    attributes = htmlBuilder.getListOfHtmlAttributes("")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.getListOfHtmlAttributes(" ")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.getListOfHtmlAttributes("\t")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.getListOfHtmlAttributes("\n")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.getListOfHtmlAttributes("  \t\t\t\t \r\r  ")
    self.assertEqual(attributes, [])
    attributes = htmlBuilder.getListOfHtmlAttributes("\n      \t   \t        \n")
    self.assertEqual(attributes, [])

  def test_getListOfHtmlAttributes_oneAttribute(self):
    attributes = htmlBuilder.getListOfHtmlAttributes("selected")
    self.assertEqual(attributes, ["selected"])
    attributes = htmlBuilder.getListOfHtmlAttributes(" \n  \t selected \n\r \t ")
    self.assertEqual(attributes, ["selected"])
    attributes = htmlBuilder.getListOfHtmlAttributes("selected \n\r \t ")
    self.assertEqual(attributes, ["selected"])
    attributes = htmlBuilder.getListOfHtmlAttributes(" \n  \t selected")
    self.assertEqual(attributes, ["selected"])
    attributes = htmlBuilder.getListOfHtmlAttributes("style=\"float:right;margin:11px 14px 0 0;"
                                                     "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98\"")
    self.assertEqual(attributes, ["style"])
    attributes = htmlBuilder.getListOfHtmlAttributes("style='float:right;margin:11px 14px 0 0;"
                                                     "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98'")
    self.assertEqual(attributes, ["style"])
    attributes = htmlBuilder.getListOfHtmlAttributes(" \n\r style\t\t\t=\n'float:right;margin:11px 14px 0 0;"
                                               "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98' \n\r ")
    self.assertEqual(attributes, ["style"])
    attributes = htmlBuilder.getListOfHtmlAttributes(" \n\r style\t\t\t=\n'\t\tfloat:right;margin:11px 14px 0 0;"
                                         "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98\t\t' \n\r ")
    self.assertEqual(attributes, ["style"])
    attributes = htmlBuilder.getListOfHtmlAttributes("\nproperty\n=\n\"\narticle:published_time\n\"\n")
    self.assertEqual(attributes, ["property"])
    attributes = htmlBuilder.getListOfHtmlAttributes("\nproperty\n=\n\"\narticle:published_time\"")
    self.assertEqual(attributes, ["property"])
    attributes = htmlBuilder.getListOfHtmlAttributes("property\n=\n\"\narticle:published_time\n\"\n")
    self.assertEqual(attributes, ["property"])

  def test_getOpenedHtmlTag_nonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag("")
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag("<div")
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag("<div>")
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag("/div")
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag("div\nspan")
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag("ul selected")
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag("", "focused")
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag(12)
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag(2, "option2")
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag(None)
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag(None, "selected")
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag("abc", None)
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag("abc", 12)
    with self.assertRaises(Exception):
      htmlBuilder.getOpenedHtmlTag("abc", False)

  def test_getOpenedHtmlTag_examples(self):
    self.assertEqual(htmlBuilder.getOpenedHtmlTag("b"), "<b>")
    self.assertEqual(htmlBuilder.getOpenedHtmlTag("div"), "<div>")
    self.assertEqual(htmlBuilder.getOpenedHtmlTag("footer"), "<footer>")
    self.assertEqual(htmlBuilder.getOpenedHtmlTag("ul", "selected"), "<ul selected>")
    self.assertEqual(htmlBuilder.getOpenedHtmlTag("a", "href='webpage.com'"), "<a href='webpage.com'>")
    self.assertEqual(htmlBuilder.getOpenedHtmlTag("a", "href='webpage.com' class='new-link'"),
                    "<a href='webpage.com' class='new-link'>")

  def test_getClosedHtmlTag_nonSense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getClosedHtmlTag("")
    with self.assertRaises(Exception):
      htmlBuilder.getClosedHtmlTag(12)
    with self.assertRaises(Exception):
      htmlBuilder.getClosedHtmlTag(None)
    with self.assertRaises(Exception):
      htmlBuilder.getClosedHtmlTag("<div")
    with self.assertRaises(Exception):
      htmlBuilder.getClosedHtmlTag("<div>")
    with self.assertRaises(Exception):
      htmlBuilder.getClosedHtmlTag("/div")
    with self.assertRaises(Exception):
      htmlBuilder.getClosedHtmlTag("div\nspan")
    with self.assertRaises(Exception):
      htmlBuilder.getClosedHtmlTag("ul selected")

  def test_getClosedHtmlTag_examples(self):
    self.assertEqual(htmlBuilder.getClosedHtmlTag("b"), "</b>")
    self.assertEqual(htmlBuilder.getClosedHtmlTag("style"), "</style>")
    self.assertEqual(htmlBuilder.getClosedHtmlTag("script"), "</script>")
    self.assertEqual(htmlBuilder.getClosedHtmlTag("navbar"), "</navbar>")
