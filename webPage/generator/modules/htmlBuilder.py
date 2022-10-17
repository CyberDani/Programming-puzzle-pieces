from modules import checks
from modules import filerw
from modules import htmlAttributes as attr
from modules import stringUtil

# <html><head> [headWriter] </head><body> [bodyWriter] </body></html>
def buildIndexHtmlFile(indexHtmlHeadWriterFunction, indexHtmlBodyWriterFunction, settings):
  htmlFile = settings.htmlOutputFile
  settings.indentDepth = 2
  htmlFile.write("<html>\n")
  htmlFile.write("\t<head>\n")
  indexHtmlHeadWriterFunction(settings)
  htmlFile.write("\t</head>\n")
  htmlFile.write("\t<body>\n")
  indexHtmlBodyWriterFunction(settings)
  htmlFile.write("\t</body>\n")
  htmlFile.write("</html>\n")

# file1 += file2
def includeFileThenAppendNewLine(htmlFile, includeFilePath, indentDepth):
  lines = filerw.getLinesByPathWithEndingNewLine(includeFilePath)
  tabs = getEscapedTabs(indentDepth)
  filerw.writeStringsPrefixedToFileThenAppendNewLine(htmlFile, tabs, lines)

# file1 += <htmlTag> file2 </htmlTag>
def includeFileSurroundedByHtmlTagThenAppendNewLine(htmlFile, includeFilePath, htmlTag, htmlAttributes, indentDepth):
  """Includes jQuery-like selectors"""
  tabs = getEscapedTabs(indentDepth)
  htmlFile.write(tabs + getOpenedHtmlTag(htmlTag, htmlAttributes) + "\n")
  fileLines = filerw.getLinesByPath(includeFilePath)
  filerw.writeLinesPrefixedToFile(htmlFile, tabs + "\t", fileLines)
  # TODO implement getHtmlTagWithoutJQuery - more performant than this
  htmlTag, attributesFromTag = filterJqueryLikeHtmlSelector(htmlTag)
  htmlFile.write(tabs + getClosedHtmlTag(htmlTag) + "\n")

# <script src=".js" />   ->  file
def addJsScriptSrcToHtmlOutputFile(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  lines = getJsScriptSrc(indentDepth, url, integrity, crossorigin, referrerpolicy)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, lines)

# <link href=".css" />   ->  file
def addCssLinkHrefToHtmlOutputFile(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  lines = getCssLinkHref(indentDepth, url, integrity, crossorigin, referrerpolicy)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, lines)

# <br\> <br\> <br\>  ->  file
def addHtmlNewLineToFile(htmlFile, indentDepth, nrOfNewLines=1):
  newLinesString = getHtmlNewLines(indentDepth, nrOfNewLines)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, [newLinesString])

# <title> Page title </title>  ->  file
def addTitleToHtmlOutputFile(htmlFile, titleString, indentDepth):
  htmlTitle = getHtmlTitle(titleString, indentDepth)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, [htmlTitle])

# <link rel="icon" href="favicon.png">  ->  file
def addFaviconToHtmlOutputFile(htmlFile, faviconPath, indentDepth):
  htmlFavicon = getHtmlFavicon(faviconPath, indentDepth)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, [htmlFavicon])

# <meta name="viewport" content="width=device-width, initial-scale=1.0"/>  ->  file
def addMetaScreenOptimizedForMobileToHtmlOutputFile(htmlFile, indentDepth):
  metaTag = getMetaScreenOptimizedForMobile(indentDepth)
  filerw.writeLinesToExistingFileThenAppendNewLine(htmlFile, [metaTag])

# <script src=".js" />
def getJsScriptSrc(indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  # "a.io/s.js" -> length 9
  checks.checkIfString(url, 9, 500)
  checks.checkIfAllNoneOrString([integrity, crossorigin, referrerpolicy], 5, 200)
  tabs = getEscapedTabs(indentDepth)
  result = [tabs + "<script src=\"" + url + "\""]
  if integrity is None:
    result[0] += "></script>"
    return result
  tabs += "\t"
  # integrity deserves its own line because usually it is a long string
  result.append(tabs + "integrity=\"" + integrity + "\"")
  result.append(tabs + "crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\"></script>")
  return result

# <link href=".css" />
def getCssLinkHref(indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  # "a.io/s.css" -> length 10
  checks.checkIfString(url, 10, 500)
  checks.checkIfAllNoneOrString([integrity, crossorigin, referrerpolicy], 5, 200)
  tabs = getEscapedTabs(indentDepth)
  result = [tabs + "<link href=\"" + url + "\""]
  tabs += "\t"
  if integrity is None:
    if len(url) > 95:
      result.append(tabs + "rel=\"stylesheet\" />")
    else:
      result[0] += " rel=\"stylesheet\" />"
    return result
  # integrity deserves its own line because usually it is a long string
  result.append(tabs + "integrity=\"" + integrity + "\"")
  result.append(tabs + "rel=\"stylesheet\" crossorigin=\"" + crossorigin
                + "\" referrerpolicy=\"" + referrerpolicy + "\" />")
  return result

# <link rel="icon" href="favicon.png">
def getHtmlFavicon(faviconPath, indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 150)
  checks.checkIfString(faviconPath, 3, 300)
  result = getEscapedTabs(indentDepth)
  result += "<link rel=\"icon\" href=\"" + faviconPath + "\">"
  return result

# <title> page title </title>
def getHtmlTitle(titleString, indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 150)
  checks.checkIfString(titleString, 2, 300)
  result = getEscapedTabs(indentDepth)
  result += "<title>" + titleString + "</title>"
  return result

# <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
def getMetaScreenOptimizedForMobile(indentDepth):
  tabs = getEscapedTabs(indentDepth)
  metaTag = tabs + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>"
  return metaTag

# <br\> <br\> <br\>
def getHtmlNewLines(indentDepth, nrOfNewLines=1):
  checks.checkIntIsBetween(nrOfNewLines, 1, 50)
  result = getEscapedTabs(indentDepth)
  for i in range(nrOfNewLines):
    result += "<br\\>"
    if i != nrOfNewLines - 1:
      result += " "
  return result

# TODO add corrupt return value
def filterJqueryLikeHtmlSelector(specialHtmlTag):
  """Raises exception if corrupt.\n
Return values:\n
* htmlTag: string
* htmlAttributes: string"""
  classes, ids = stringUtil.doubleSplit(specialHtmlTag, ".", "#")
  checks.checkIfNonEmptyList(classes)
  htmlTag = classes[0]
  classes = classes[1:]
  checks.checkIfStringIsAlphaNumerical(htmlTag)
  checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(classes)
  checks.checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(ids)
  idString = stringUtil.stringListToString(ids, prefix="", suffix="", delimiter=" ")
  classString = stringUtil.stringListToString(classes, prefix="", suffix="", delimiter=" ")
  htmlAttributes = ""
  if idString:
    htmlAttributes += "id=\"" + idString + "\""
    if classString:
      htmlAttributes += " "
  if classString:
    htmlAttributes += "class=\"" + classString + "\""
  return htmlTag, htmlAttributes

# TODO add corrupt return value
# <htmlTag attributes>
def getOpenedHtmlTag(htmlTag, attributes=""):
  """Includes jQuery-like selectors.\n
Raises exception for any corrupt data and empty html tag."""
  checks.checkIfString(htmlTag, 1, 100)
  checks.checkIfString(attributes, 0, 500)
  htmlTag, attributesFromTag = filterJqueryLikeHtmlSelector(htmlTag)
  checks.checkIfStringIsAlphaNumerical(htmlTag)
  # TODO add corrupt return value
  corrupt, attributesDict = attr.combineTwoAttributeStrings(attributesFromTag, attributes)
  if corrupt:
    raise Exception("corrupt data found")
  if not corrupt:
    attributes = attr.getStringFromDictionary(attributesDict)
  result = "<" + htmlTag
  if attributes:
    result += " " + attributes
  result += ">"
  return result

def getClosedHtmlTag(htmlTag):
  checks.checkIfString(htmlTag, 1, 100)
  # TODO getHtmlTagWithoutJQuery
  htmlTag, attributesFromTag = filterJqueryLikeHtmlSelector(htmlTag)
  checks.checkIfStringIsAlphaNumerical(htmlTag)
  return "</" + htmlTag + ">"

# \t\t\t
def getEscapedTabs(indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 50)
  ans = ""
  for i in range(indentDepth):
    ans += "\t"
  return ans
