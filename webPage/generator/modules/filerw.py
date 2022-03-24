from modules import checks
from modules import htmlBuilder

def getLinesByFilePathWithEndingNewLine(filePath):
  checks.checkIfString(filePath, 2, 300)
  f = open(filePath, "r")
  return f.readlines()

def writeLinesToFileThenAppendNewLine(file, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  if len(lines) == 0:
    return
  for line in lines:
    file.write(line)
    file.write("\n")

def writeStringsIndentedToFileThenAppendNewLine(file, indentDepth, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  tabs = htmlBuilder.getIndentedTab(indentDepth)
  for line in lines:
    if (line and line != "\n"):
      file.write(tabs + line)
    else:
      file.write("\n")
  file.write("\n")