import os
import sys
import unittest

sys.path.append('..')
from defTypes import buildType
from defTypes import dbBranchType
from defTypes import buildSettings
from modules import htmlBuilder
from modules import filerw
from modules import counter


def emptyHtmlHeadContent(settings):
  a = 2

def emptyHtmlBodyContent(settings):
  a = 2

def minimalistHtmlHeadContent(settings):
  htmlTabs = htmlBuilder.getEscapedTabs(settings.indentDepth)
  filerw.writeLinesToFileThenAppendNewLine(settings.htmlOutputFile, [htmlTabs + "<title>Hey!</title>"])

def minimalistHtmlBodyContent(settings):
  htmlTabs = htmlBuilder.getEscapedTabs(settings.indentDepth)
  filerw.writeLinesToFileThenAppendNewLine(settings.htmlOutputFile, [htmlTabs + "<h1>Hello!</h1>"])

class HtmlBuilderTests(unittest.TestCase):

  def setUp(self):
    if not os.path.exists('./unitTests/temp'):
      os.makedirs('./unitTests/temp')

  def test_writeIndexHtmlToFile_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    settings = buildSettings.BuildSettings(htmlOutputFile=file,
                                           buildOption=buildType.BuildType.BUILD,
                                           dbBranch=dbBranchType.DbBranchType.DEVEL,
                                           stepsCounter=counter.SimpleCounter(1),
                                           indentDepth=2)
    with self.assertRaises(Exception):
      htmlBuilder.writeIndexHtmlToFile("hello", "hello", settings)
    with self.assertRaises(Exception):
      htmlBuilder.writeIndexHtmlToFile(None, None, settings)
    with self.assertRaises(Exception):
      htmlBuilder.writeIndexHtmlToFile(True, False, settings)

  def test_writeIndexHtmlToFile_emptyHtml(self):
    file = open("./unitTests/temp/test.txt", "w")
    settings = buildSettings.BuildSettings(htmlOutputFile=file,
                                           buildOption=buildType.BuildType.BUILD,
                                           dbBranch=dbBranchType.DbBranchType.DEVEL,
                                           stepsCounter=counter.SimpleCounter(1),
                                           indentDepth=2)
    htmlBuilder.writeIndexHtmlToFile(emptyHtmlHeadContent, emptyHtmlBodyContent, settings)
    file.close()
    emptyHtmlLines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
    self.assertEqual(len(emptyHtmlLines), 6)
    self.assertEqual(emptyHtmlLines[0], "<html>")
    self.assertEqual(emptyHtmlLines[1], "\t<head>")
    self.assertEqual(emptyHtmlLines[2], "\t</head>")
    self.assertEqual(emptyHtmlLines[3], "\t<body>")
    self.assertEqual(emptyHtmlLines[4], "\t</body>")
    self.assertEqual(emptyHtmlLines[5], "</html>")

  def test_writeIndexHtmlToFile_minimalistHtml(self):
    file = open("./unitTests/temp/test.txt", "w")
    settings = buildSettings.BuildSettings(htmlOutputFile=file,
                                           buildOption=buildType.BuildType.BUILD,
                                           dbBranch=dbBranchType.DbBranchType.DEVEL,
                                           stepsCounter=counter.SimpleCounter(1),
                                           indentDepth=2)
    htmlBuilder.writeIndexHtmlToFile(minimalistHtmlHeadContent, minimalistHtmlBodyContent, settings)
    file.close()
    emptyHtmlLines = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
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
    newLines =  htmlBuilder.getHtmlNewLines(indentDepth = 1)
    self.assertEqual(newLines,"\t<br\\>")
    newLines =  htmlBuilder.getHtmlNewLines(indentDepth = 2)
    self.assertEqual(newLines,"\t\t<br\\>")
    newLines =  htmlBuilder.getHtmlNewLines(indentDepth = 3)
    self.assertEqual(newLines,"\t\t\t<br\\>")
    newLines =  htmlBuilder.getHtmlNewLines(indentDepth = 6)
    self.assertEqual(newLines,"\t\t\t\t\t\t<br\\>")

  def test_getHtmlNewLines_normalCases(self):
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = 1)
    self.assertEqual(newLines,"\t<br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 2, nrOfNewLines = 1)
    self.assertEqual(newLines,"\t\t<br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 4, nrOfNewLines = 1)
    self.assertEqual(newLines,"\t\t\t\t<br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = 2)
    self.assertEqual(newLines,"\t<br\\> <br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = 3)
    self.assertEqual(newLines,"\t<br\\> <br\\> <br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 1, nrOfNewLines = 6)
    self.assertEqual(newLines,"\t<br\\> <br\\> <br\\> <br\\> <br\\> <br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 2, nrOfNewLines = 2)
    self.assertEqual(newLines,"\t\t<br\\> <br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 2, nrOfNewLines = 4)
    self.assertEqual(newLines,"\t\t<br\\> <br\\> <br\\> <br\\>")
    newLines = htmlBuilder.getHtmlNewLines(indentDepth = 4, nrOfNewLines = 2)
    self.assertEqual(newLines,"\t\t\t\t<br\\> <br\\>")

  def test_addNewLineToHtmlOutputFile_nonsense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      htmlBuilder.addNewLineToHtmlOutputFile("heyho", indentDepth = 2, nrOfNewLines = 2)
    with self.assertRaises(Exception):
      htmlBuilder.addNewLineToHtmlOutputFile(file, indentDepth = "two", nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.addNewLineToHtmlOutputFile(file, indentDepth = 2, nrOfNewLines = "one")
    with self.assertRaises(Exception):
      htmlBuilder.addNewLineToHtmlOutputFile(file, indentDepth = -2, nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.addNewLineToHtmlOutputFile(file, indentDepth = 0, nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.addNewLineToHtmlOutputFile(file, indentDepth = 100, nrOfNewLines = 1)
    with self.assertRaises(Exception):
      htmlBuilder.addNewLineToHtmlOutputFile(file, indentDepth = 1, nrOfNewLines = -1)
    with self.assertRaises(Exception):
      htmlBuilder.addNewLineToHtmlOutputFile(file, indentDepth = 1, nrOfNewLines = 100)
    with self.assertRaises(Exception):
      htmlBuilder.addNewLineToHtmlOutputFile(file, indentDepth = 1, nrOfNewLines = 0)
    file.close()

  def test_addNewLineToHtmlOutputFile_defaultParameter_nrOfNewLines_1(self):
    for indent in range(1,6):
      newLines =  htmlBuilder.getHtmlNewLines(indent)
      file = open("./unitTests/temp/test.txt", "w")
      htmlBuilder.addNewLineToHtmlOutputFile(file, indent)
      file.close()
      readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
      self.assertEqual(len(readLines),1)
      self.assertEqual(readLines[0],newLines + "\n")

  def test_addFaviconToHtmlOutputFile_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
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
      htmlBuilder.addFaviconToHtmlOutputFile("./unitTests/temp/test.txt", "myFavicon.ico", 2)

  def test_addFaviconToHtmlOutputFile_examples(self):
    for indent in [3, 4, 5]:
      for favicon in ["fav.png", "./media/img/icon.ico", "../../myFavIcon.jpg"]:
        file = open("./unitTests/temp/test.txt", "w")
        htmlBuilder.addFaviconToHtmlOutputFile(file, favicon, indent)
        file.close()
        line = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
        self.assertEqual(len(line), 1)
        self.assertEqual(line[0], htmlBuilder.getHtmlFavicon(favicon, indent))

  def test_addTitleToHtmlOutputFile_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
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
      htmlBuilder.addTitleToHtmlOutputFile("./unitTests/temp/test.txt", "title", 2)

  def test_addTitleToHtmlOutputFile_examples(self):
    for indent in [2, 3, 4]:
      for title in ["title", "my page", "Look At This 23!#"]:
        file = open("./unitTests/temp/test.txt", "w")
        htmlBuilder.addTitleToHtmlOutputFile(file, title, indent)
        file.close()
        line = filerw.getLinesByFilePath("./unitTests/temp/test.txt")
        self.assertEqual(len(line), 1)
        self.assertEqual(line[0], htmlBuilder.getHtmlTitle(title, indent))

  def test_getCssLinkHref_nonsense(self):
    with self.assertRaises(Exception):
      htmlBuilder.getCssLinkHref(indentDepth=-3, url="www.mysite.com/res.css", integrity=None, crossorigin=None, referrerpolicy=None)
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
    result = htmlBuilder.getCssLinkHref(2, "https://cdn.jsdelivr.net/npm/@materializecss/materialize@1.1.0-alpha/dist/css/materialize.min.css", None, None, None)
    self.assertEqual(len(result), 2)
    self.assertEqual(result[0], "\t\t<link href=\"https://cdn.jsdelivr.net/npm/@materializecss/materialize@1.1.0-alpha/dist/css/materialize.min.css\"")
    self.assertEqual(result[1], "\t\t\trel=\"stylesheet\" />")

  def test_getCssLinkHref_containsIntegrity(self):
    result = htmlBuilder.getCssLinkHref(3, "https://www.randomsite.com/resource.css", 
                    "asdsadbsdsadbi32gr3ur", "techguy", "refferrer")
    self.assertEqual(len(result), 3)
    self.assertEqual(result[0], "\t\t\t<link href=\"https://www.randomsite.com/resource.css\"")
    self.assertEqual(result[1], "\t\t\t\tintegrity=\"asdsadbsdsadbi32gr3ur\"")
    self.assertEqual(result[2], "\t\t\t\trel=\"stylesheet\" crossorigin=\"techguy\" referrerpolicy=\"refferrer\" />")

  def test_addCssLinkHrefToHtmlOutputFile_nonsense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(htmlFile=file,indentDepth=-3, 
                                url="www.mysite.com/res.css", integrity=None, crossorigin=None, referrerpolicy=None)
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
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", "sha512-asdasdc-xcx", "abc", "no-refferer")
    with self.assertRaises(Exception):
      htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, 1, "www.mysite.com/res.css", "sha512-asdasdc-xcx", "anonymous", "ab")
    file.close()

  def test_addCssLinkHrefToHtmlOutputFile_normalCases(self):
    self.cssLinkHrefTestHelper(1, "www.mysite.com/res.css", None, None, None)
    self.cssLinkHrefTestHelper(5, "https://cdn.jsdelivr.net/npm/@materializecss/materialize@1.1.0-alpha/dist/css/materialize.min.css", 
                        None, None, None)
    self.cssLinkHrefTestHelper(3, "https://www.randomsite.com/resource.css", "asdsadbsdsadbi32gr3ur", "techguy", "refferrer")

  def cssLinkHrefTestHelper(self, indentDepth, url, integrity, crossorigin, referrerpolicy):
    file = open("./unitTests/temp/test.txt", "w")
    lines = htmlBuilder.getCssLinkHref(indentDepth, url, integrity, crossorigin, referrerpolicy)
    htmlBuilder.addCssLinkHrefToHtmlOutputFile(file, indentDepth, url, integrity, crossorigin, referrerpolicy)
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), len(lines))
    for i in range(len(readLines)):
      self.assertEqual(readLines[i],lines[i] + "\n")

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
      htmlBuilder.getJsScriptSrc(indentDepth=-3, url="www.mysite.com/res.js", integrity=None, crossorigin=None, referrerpolicy=None)
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
    self.jsScriptSrcTestHelper(5, "https://cdn.jsdelivr.net/npm/gasparesganga-jquery-loading-overlay@2.1.7/dist/loadingoverlay.min.js", 
                        None, None, None)
    self.jsScriptSrcTestHelper(3, "https://www.randomsite.com/resource.js", "asfldfohsdofsdflndjfbfd", "TechGuy", "refferrer")

  def jsScriptSrcTestHelper(self, indentDepth, url, integrity, crossorigin, referrerpolicy):
    file = open("./unitTests/temp/test.txt", "w")
    lines = htmlBuilder.getJsScriptSrc(indentDepth, url, integrity, crossorigin, referrerpolicy)
    htmlBuilder.addJsScriptSrcToHtmlOutputFile(file, indentDepth, url, integrity, crossorigin, referrerpolicy)
    file.close()
    readLines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), len(lines))
    for i in range(len(readLines)):
      self.assertEqual(readLines[i],lines[i] + "\n")

  def test_includeFileToHtmlOutputFile_nonsense(self):
    dest = open("./unitTests/temp/test.txt", "w")
    src = open("./unitTests/temp/test2.txt", "w")
    src.close()
    with self.assertRaises(Exception):
      htmlBuilder.includeFileToHtmlOutputFile(dest, "./unitTests/temp/test2.txt", -1)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileToHtmlOutputFile(dest, None, 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileToHtmlOutputFile(None, None, 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileToHtmlOutputFile(None, "./unitTests/temp/test2.txt", 2)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileToHtmlOutputFile(dest, "./unitTests/temp/test2.txt", False)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileToHtmlOutputFile(dest, "./unitTests/temp/test2.txt", None)
    with self.assertRaises(Exception):
      htmlBuilder.includeFileToHtmlOutputFile(None, None, None)

  def test_includeFileToHtmlOutputFile_emptyFile(self):
    src = open("./unitTests/temp/test2.txt", "w")
    src.close()
    dest = open("./unitTests/temp/test.txt", "w")
    htmlBuilder.includeFileToHtmlOutputFile(dest, "./unitTests/temp/test2.txt", 1)
    dest.close()
    lines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 1)
    self.assertEqual(lines[0], "\n")

  def test_includeFileToHtmlOutputFile_normalCases(self):
    lines = self.helper_includeFileToHtmlOutputFile(1, ["be proud of yourself"])
    self.assertEqual(len(lines), 2)
    self.assertEqual(lines[0], "\tbe proud of yourself\n")
    self.assertEqual(lines[1], "\n")
    lines = self.helper_includeFileToHtmlOutputFile(2, ["<div>","\thooray!","</div>"])
    self.assertEqual(len(lines), 4)
    self.assertEqual(lines[0], "\t\t<div>\n")
    self.assertEqual(lines[1], "\t\t\thooray!\n")
    self.assertEqual(lines[2], "\t\t</div>\n")
    self.assertEqual(lines[3], "\n")

  def helper_includeFileToHtmlOutputFile(self, indent, lines):
    src = open("./unitTests/temp/test2.txt", "w")
    filerw.writeLinesToFileThenAppendNewLine(src, lines)
    src.close()
    dest = open("./unitTests/temp/test.txt", "w")
    htmlBuilder.includeFileToHtmlOutputFile(dest, "./unitTests/temp/test2.txt", indent)
    dest.close()
    return filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")