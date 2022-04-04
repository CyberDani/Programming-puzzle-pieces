from modules import checks

def getLinesByFilePathWithEndingNewLine(filePath):
  checks.checkIfString(filePath, 2, 300)
  f = open(filePath, "r")
  return f.readlines()

def getLinesWithEndingNewLine(file):
  checks.checkIfFile(file)
  return file.readlines()

def getLinesByFilePath(filePath):
  linesWithNewEndingline = getLinesByFilePathWithEndingNewLine(filePath)
  return rTrimNewLines(linesWithNewEndingline)

def getLines(file):
  linesWithNewEndingline = getLinesWithEndingNewLine(file)
  return rTrimNewLines(linesWithNewEndingline)

def writeLinesToFile(file, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  n = len(lines)
  for i in range(n):
    file.write(lines[i])
    if (i < n - 1):
      file.write("\n")

def writeLinesToFileThenAppendNewLine(file, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  for line in lines:
    file.write(line)
    file.write("\n")

def writeStringsPrefixedToFileThenAppendNewLine(file, prefix, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  checks.checkIfString(prefix, 0, 300)
  for line in lines:
    if (line and line != "\n"):
      file.write(prefix + line)
    else:
      file.write("\n")
  file.write("\n")

def rTrimNewLines(stringsArr):
  checks.checkIfPureListOfStrings(stringsArr)
  result = []
  for string in stringsArr:
    trimmedString = string
    while trimmedString.endswith("\n"):
      trimmedString = trimmedString[:-1]
    result.append(trimmedString)
  return result