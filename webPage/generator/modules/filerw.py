from modules import checks

def getLinesByFilePathWithEndingNewLine(filePath):
  checks.checkIfString(filePath, 2, 300)
  f = open(filePath, "r")
  return f.readlines()

def getLinesWithEndingNewLine(file):
  checks.checkIfFile(file)
  return file.readlines()

def writeLinesToFileThenAppendNewLine(file, lines):
  checks.checkIfFile(file)
  checks.checkIfPureListOfStrings(lines)
  if len(lines) == 0:
    return
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