# main function
def generateHtmlOutputFile():
  # TODO: create backup of the original index.html in case of any error
  # TODO: make the file path as a configuration somewhere 
  htmlOutputFilePath = "../../index2.html"
  htmlFile = open(htmlOutputFilePath, "w")
  writeHtmlContentToFile(htmlFile)

def writeHtmlContentToFile(htmlFile):
  htmlFile.write("<html>\n")
  htmlFile.write("\t<head>\n")
  writeHtmlHeadContent(htmlFile, 2)
  htmlFile.write("\t</head>\n")
  htmlFile.write("\t<body>\n")
  writeHtmlBodyContent(htmlFile, 2)
  htmlFile.write("\t</body>\n")
  htmlFile.write("</html>\n")

def writeHtmlHeadContent(htmlFile, indentDepth):
  tabs = getIndentedTab(indentDepth)
  # TODO: see what is worth to add as a configuration
  htmlFile.write(tabs + "<title>Programming puzzle-pieces</title>\n")
  htmlFile.write(tabs + "<link rel=\"icon\" href=\"./webPage/images/favicon.png\">\n")
  # Let browser know website is optimized for mobile
  htmlFile.write(tabs + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>\n")
  htmlFile.write(tabs + "<style>\n")
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/inlineCssStyle.css", indentDepth + 1)
  htmlFile.write(tabs + "</style>\n")
  
def writeHtmlBodyContent(htmlFile, indentDepth):
  tabs = getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<h1>Hello World again</h1>\n")

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

generateHtmlOutputFile()