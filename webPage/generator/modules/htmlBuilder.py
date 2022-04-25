from modules import checks
from modules import filerw

# <html><head> [headWriter] </head><body> [bodyWriter] </body></html>
def writeIndexHtmlToFile(indexHtmlHeadWriterFunction, indexHtmlBodyWriterFunction, settings):
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
def includeFileToHtmlOutputFile(htmlFile, includeFilePath, indentDepth):
  lines = filerw.getLinesByFilePathWithEndingNewLine(includeFilePath)
  tabs = getHtmlTabs(indentDepth)
  filerw.writeStringsPrefixedToFileThenAppendNewLine(htmlFile, tabs, lines)

# <script src=".js" />   ->  file
def addJsScriptSrcToHtmlOutputFile(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  lines = getJsScriptSrc(indentDepth, url, integrity, crossorigin, referrerpolicy)
  filerw.writeLinesToFileThenAppendNewLine(htmlFile, lines)

# <link href=".css" />   ->  file
def addCssLinkHrefToHtmlOutputFile(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  lines = getCssLinkHref(indentDepth, url, integrity, crossorigin, referrerpolicy)
  filerw.writeLinesToFileThenAppendNewLine(htmlFile, lines)

# <br\> <br\> <br\>  ->  file
def addNewLineToHtmlOutputFile(htmlFile, indentDepth, nrOfNewLines = 1):
  newLinesString = getHtmlNewLines(indentDepth, nrOfNewLines)
  filerw.writeLinesToFileThenAppendNewLine(htmlFile, [newLinesString])

# <title> Page title </title>  ->  file
def addTitleToHtmlOutputFile(htmlFile, titleString, indentDepth):
  htmlTitle = getHtmlTitle(titleString, indentDepth)
  filerw.writeLinesToFileThenAppendNewLine(htmlFile, [htmlTitle])

# <script src=".js" />
def getJsScriptSrc(indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  #"a.io/s.js" -> length 9
  checks.checkIfString(url, 9, 500)
  checks.checkIfAllNoneOrString([integrity, crossorigin, referrerpolicy], 5, 200)
  tabs = getHtmlTabs(indentDepth)
  result = [tabs + "<script src=\"" + url + "\""]
  if (integrity is None):
    result[0] += "></script>"
    return result
  tabs += "\t"
  # integrity deserves its own line because usually it is a long string
  result.append(tabs + "integrity=\"" + integrity + "\"")
  result.append(tabs + "crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\"></script>")
  return result

# <link href=".css" />
def getCssLinkHref(indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  #"a.io/s.css" -> length 10
  checks.checkIfString(url, 10, 500)
  checks.checkIfAllNoneOrString([integrity, crossorigin, referrerpolicy], 5, 200)
  tabs = getHtmlTabs(indentDepth)
  result = [tabs + "<link href=\"" + url + "\""]
  tabs += "\t"
  if (integrity is None):
    if len(url) > 95:
      result.append(tabs + "rel=\"stylesheet\" />")
    else:
      result[0] += " rel=\"stylesheet\" />"
    return result
  # integrity deserves its own line because usually it is a long string
  result.append(tabs + "integrity=\"" + integrity + "\"")
  result.append(tabs + "rel=\"stylesheet\" crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\" />")
  return result

# <title> page title </title>
def getHtmlTitle(titleString, indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 150)
  checks.checkIfString(titleString, 2, 300)
  result = getHtmlTabs(indentDepth)
  result += "<title>" + titleString + "</title>"
  return result

# <br\> <br\> <br\>
def getHtmlNewLines(indentDepth, nrOfNewLines = 1):
  checks.checkIntIsBetween(nrOfNewLines, 1, 50)
  result = getHtmlTabs(indentDepth)
  for i in range(nrOfNewLines):
    result += "<br\>"
    if i != nrOfNewLines - 1:
      result += " "
  return result

# \t\t\t
def getHtmlTabs(indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 50)
  ans=""; 
  for i in range(indentDepth):
    ans += "\t"
  return ans;