import io

# include
def includeFileToHtmlOutputFile(htmlFile, includeFilePath, indentDepth):
  lines = getLinesFromFileWithEndingNewLine(includeFilePath)
  tabs = getIndentedTab(indentDepth)
  for line in lines:
    if (line and line != "\n"):
      htmlFile.write(tabs + line)
    else:
      htmlFile.write("\n")
  htmlFile.write("\n")

# <script src=".js" />
def addJsFileAsLink(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  tabs = getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<script src=\"" + url + "\"")
  if (integrity is None or crossorigin is None or referrerpolicy is None):
    if (integrity is not None or crossorigin is not None or referrerpolicy is not None):
      raise Exception("integrity, crossorigin and referrerpolicy must be all set or None")
    htmlFile.write("></script>\n")
    return
  tabs += "\t"
  htmlFile.write("\n" + tabs + "integrity=\"" + integrity + "\"\n")
  htmlFile.write(tabs + "crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\"></script>\n")

# <link href=".css" />
def addCssFileAsLink(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  tabs = getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<link href=\"" + url + "\"")
  if (integrity is None or crossorigin is None or referrerpolicy is None):
    if (integrity is not None or crossorigin is not None or referrerpolicy is not None):
      raise Exception("integrity, crossorigin and referrerpolicy must be all set or None")
    if len(url) > 95:
      htmlFile.write("\n" + tabs + "\t")
    else:
      htmlFile.write(" ")
    htmlFile.write("rel=\"stylesheet\" />\n")
    return
  tabs += "\t"
  htmlFile.write("\n" + tabs + "integrity=\"" + integrity + "\"\n")
  htmlFile.write(tabs + "rel=\"stylesheet\" crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\" />\n")

# <br\> <br\> <br\>  ->  file
def addNewLineToHtmlOutputFile(htmlFile, indentDepth, nrOfNewLines = 1):
  tabs = getIndentedTab(indentDepth)
  newLinesString = getHtmlNewLines(indentDepth, nrOfNewLines)
  writeLinesToFileThenAppendNewLine(htmlFile, [newLinesString])

# <br\> <br\> <br\>
def getHtmlNewLines(indentDepth, nrOfNewLines = 1):
  if (type(nrOfNewLines) != int):
    raise Exception("nrOfNewLines is not an int type for argument " + str(nrOfNewLines))
  if (nrOfNewLines < 0):
    raise Exception("nrOfNewLines < 0 for argument " + str(nrOfNewLines))
  if (type(nrOfNewLines) != int):
    raise Exception("nrOfNewLines is not an int type for argument " + str(nrOfNewLines))
  if (nrOfNewLines == 0):
    raise Exception("I do not really think you want nrOfNewLines = 0")
  if (nrOfNewLines > 50):
    raise Exception("Do you really need that much new lines?")
  result = getIndentedTab(indentDepth)
  for i in range(nrOfNewLines):
    result += "<br\>"
    if i != nrOfNewLines - 1:
      result += " "
  return result

def getLinesFromFileWithEndingNewLine(filePath):
  f = open(filePath, "r")
  return f.readlines()

def writeLinesToFileThenAppendNewLine(file, lines):
  if not isinstance(file, io.TextIOBase):
    raise Exception("file is not a TextIOWrapper type argument")
  if (type(lines) != list):
    raise Exception("lines is not a list type argument")
  if len(lines) == 0:
    return
  for line in lines:
    file.write(line)
    file.write("\n")

# \t\t\t
def getIndentedTab(indentDepth):
  if (type(indentDepth) != int):
    raise Exception("indentDepth is not an int type for argument " + str(indentDepth))
  if (indentDepth < 0):
    raise Exception("indentDepth < 0 for argument " + str(indentDepth))
  if (indentDepth == 0):
    raise Exception("I do not really think you want indentDepth = 0")
  if (indentDepth > 50):
    raise Exception("Do you really need that much indentation?")
  ans=""; 
  for i in range(indentDepth):
    ans += "\t"
  return ans;