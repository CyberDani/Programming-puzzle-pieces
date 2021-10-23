# include
def includeFileToHtmlOutputFile(htmlFile, includeFilePath, indentDepth):
  lines = getLinesFromFile(includeFilePath)
  tabs = getIndentedTab(indentDepth)
  for line in lines:
    if (line and line != "\n"):
      htmlFile.write(tabs + line)
    else:
      htmlFile.write("\n")
  htmlFile.write("\n")

def getLinesFromFile(filePath):
  f = open(filePath, "r")
  return f.readlines()

# <br \>
def addNewLineToHtmlOutputFile(htmlFile, indentDepth):
  tabs = getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<br \>\n")

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

def getIndentedTab(indentDepth):
  if (type(indentDepth) != int):
    raise Exception("indentDepth is not an int type for argument " + str(indentDepth))
  if (indentDepth < 0):
    raise Exception("indentDepth < 0 for argument " + str(indentDepth))
  if (indentDepth == 0):
    raise Exception("I do not really think you want indentDepth == 0")
  if (indentDepth > 50):
    raise Exception("Do you really need that much indentation?")
  ans=""; 
  for i in range(indentDepth):
    ans += "\t"
  return ans;