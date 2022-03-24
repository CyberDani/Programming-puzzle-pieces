from modules import checks
from modules import filerw

# file1 += file2
def includeFileToHtmlOutputFile(htmlFile, includeFilePath, indentDepth):
  lines = filerw.getLinesByFilePathWithEndingNewLine(includeFilePath)
  filerw.writeStringsIndentedToFileThenAppendNewLine(htmlFile, indentDepth, lines)

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

# <script src=".js" />
def getJsScriptSrc(indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  #"a.io/s.js" -> length 9
  checks.checkIfString(url, 9, 500)
  checks.checkIfAllNoneOrString([integrity, crossorigin, referrerpolicy], 5, 200)
  tabs = getIndentedTab(indentDepth)
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
  tabs = getIndentedTab(indentDepth)
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

# <br\> <br\> <br\>
def getHtmlNewLines(indentDepth, nrOfNewLines = 1):
  checks.checkIntIsBetween(nrOfNewLines, 1, 50)
  result = getIndentedTab(indentDepth)
  for i in range(nrOfNewLines):
    result += "<br\>"
    if i != nrOfNewLines - 1:
      result += " "
  return result

# \t\t\t
def getIndentedTab(indentDepth):
  checks.checkIntIsBetween(indentDepth, 1, 50)
  ans=""; 
  for i in range(indentDepth):
    ans += "\t"
  return ans;