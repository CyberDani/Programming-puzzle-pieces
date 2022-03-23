import os
import sys
import unittest

sys.path.append('..')
from modules import htmlBuilder

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
    with self.assertRaises(Exception):
      htmlBuilder.getIndentedTab(False)

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
      readLines = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
      self.assertEqual(len(readLines),1)
      self.assertEqual(readLines[0],newLines + "\n")

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
    readLines = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), len(lines))
    for i in range(len(readLines)):
      self.assertEqual(readLines[i],lines[i] + "\n")

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
    readLines = htmlBuilder.getLinesFromFileWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(readLines), len(lines))
    for i in range(len(readLines)):
      self.assertEqual(readLines[i],lines[i] + "\n")