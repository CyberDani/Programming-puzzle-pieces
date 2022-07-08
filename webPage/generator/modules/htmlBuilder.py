from modules import checks
from modules import filerw

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
def includeFileSurroundedByHtmlTagThenAppendNewLine(htmlFile, includeFilePath, htmlTag, htmlTagOption, indentDepth):
  tabs = getEscapedTabs(indentDepth)
  htmlFile.write(tabs + getOpenedHtmlTag(htmlTag, htmlTagOption) + "\n")
  fileLines = filerw.getLinesByPath(includeFilePath)
  filerw.writeLinesPrefixedToFile(htmlFile, tabs + "\t", fileLines)
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
def getHtmlNewLines(indentDepth, nrOfNewLines = 1):
  checks.checkIntIsBetween(nrOfNewLines, 1, 50)
  result = getEscapedTabs(indentDepth)
  for i in range(nrOfNewLines):
    result += "<br\\>"
    if i != nrOfNewLines - 1:
      result += " "
  return result

# <htmlTag options>
def getOpenedHtmlTag(htmlTag, options = ""):
  checks.checkIfString(htmlTag, 1, 100)
  checks.checkIfString(options, 0, 500)
  checks.checkIfStringIsAlphaNumerical(htmlTag)
  result = "<" + htmlTag
  if len(options) > 0:
    result += " " + options
  result += ">"
  return result

def getClosedHtmlTag(htmlTag):
  checks.checkIfString(htmlTag, 1, 100)
  checks.checkIfStringIsAlphaNumerical(htmlTag)
  return "</" + htmlTag + ">"

# \t\t\t
def getEscapedTabs(indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 50)
  ans = ""
  for i in range(indentDepth):
    ans += "\t"
  return ans
