from modules.checks import checks

def getNextChar(string, index):
  """Raises exception for empty string because the index cannot be set properly.\n
Return values: \n
* found: True | False
* nextChar: empty string if not found"""
  checks.checkIfString(string, 0, 5000)
  checks.checkIntIsBetween(index, 0, len(string) - 1)
  if index == len(string) - 1:
    return False, ""
  return True, string[index + 1]

def getPreviousChar(string, index):
  """Raises exception for empty string because the index cannot be set properly.\n
Return values: \n
* found: True | False
* nextChar: empty string if not found"""
  checks.checkIfString(string, 0, 5000)
  checks.checkIntIsBetween(index, 0, len(string) - 1)
  if index == 0:
    return False, ""
  return True, string[index - 1]

def getStringStartsWithEndsWithNoOverlap(src, startsWithStr, endsWithStr):
  """Returns empty string if not found."""
  checks.checkIfString(src, 2, 500)
  checks.checkIfString(startsWithStr, 1, 500)
  checks.checkIfString(endsWithStr, 1, 500)
  startIdx = src.find(startsWithStr)
  if startIdx == -1:
    return ""
  idxAdd = startIdx + len(startsWithStr)
  originalSrc = src
  src = src[idxAdd:]
  endIdx = src.find(endsWithStr)
  if endIdx == -1:
    return ""
  endIdx += idxAdd + len(endsWithStr)
  return originalSrc[startIdx:endIdx]

def rTrimNewLines(string: str):
  checks.checkIfString(string, 0, 1000000)
  trimmedString = string
  while trimmedString.endswith("\n") or trimmedString.endswith("\r"):
    trimmedString = trimmedString[:-1]
  return trimmedString

def stringListToString(stringList, prefix, suffix, delimiter):
  checks.checkIfPureListOfStrings(stringList)
  checks.checkIfString(delimiter, 0, 30)
  checks.checkIfString(prefix, 0, 30)
  checks.checkIfString(suffix, 0, 30)
  result = ""
  for string in stringList:
    result += string + delimiter
  if delimiter:
    result = result[:-len(delimiter)]
  result = prefix + result + suffix
  return result

def doubleSplit(string, primaryDelimiter, secondaryDelimiter):
  checks.checkIfString(string, 0, 10000)
  checks.checkIfTwoNonEmptyStringsAreDifferent(primaryDelimiter, secondaryDelimiter)
  primaryParts = string.split(primaryDelimiter)
  secondaryParts = []
  for primaryIdx in range(len(primaryParts)):
    primString = primaryParts[primaryIdx]
    secondaryPartials = primString.split(secondaryDelimiter)
    if len(secondaryPartials) > 1:
      primaryParts[primaryIdx] = secondaryPartials[0]
      secondaryParts += secondaryPartials[1:]
  return primaryParts, secondaryParts

def getFirstNewLineCharIdx(string, startIdx, endIdx):
  """Raises error at empty string because indexes cannot be set properly.\n
Return values:\n
* found: True | False \n
* index: -1 if not found"""
  checks.checkIfString(string, 0, 5000)
  checks.checkIntIsBetween(startIdx, 0, endIdx)
  checks.checkIntIsBetween(endIdx, startIdx, len(string) - 1)
  idx = startIdx
  while idx <= endIdx and string[idx] != "\n":
    idx += 1
  if idx > endIdx:
    return False, -1
  return True, idx

def getLastNewLineCharIdx(string, startIdx, endIdx):
  """Raises error at empty string because indexes cannot be set properly.\n
Return values:\n
* found: True | False \n
* index: -1 if not found"""
  checks.checkIfString(string, 0, 5000)
  checks.checkIntIsBetween(startIdx, 0, endIdx)
  checks.checkIntIsBetween(endIdx, startIdx, len(string) - 1)
  idx = endIdx
  while idx >= startIdx and string[idx] != '\n':
    idx -= 1
  if idx < startIdx:
    return False, -1
  return True, idx

def getFirstNonWhiteSpaceCharIdx(string, startIdx, endIdx):
  """Raises error at empty string because indexes cannot be set properly.\n
Return values:\n
* found: True | False \n
* index: -1 if not found"""
  checks.checkIfString(string, 0, 5000)
  checks.checkIntIsBetween(startIdx, 0, endIdx)
  checks.checkIntIsBetween(endIdx, startIdx, len(string) - 1)
  idx = startIdx
  while idx <= endIdx and string[idx].isspace():
    idx += 1
  if idx > endIdx:
    return False, -1
  return True, idx

def getLastNonWhiteSpaceCharIdx(string, startIdx, endIdx):
  """Raises error at empty string because indexes cannot be set properly.\n
Return values:\n
* found: True | False \n
* index: -1 if not found"""
  checks.checkIfString(string, 0, 5000)
  checks.checkIntIsBetween(startIdx, 0, endIdx)
  checks.checkIntIsBetween(endIdx, startIdx, len(string) - 1)
  idx = endIdx
  while idx >= startIdx and string[idx].isspace():
    idx -= 1
  if idx < startIdx:
    return False, -1
  return True, idx

def beforeWhitespaceDelimitedFind(stringToScan, stringToFind, startIdx, endIdx):
  """Raises error for empty strings because indexes cannot be set properly.\n
Return values: \n
* found: True | False
* index: -1 if not found"""
  checks.checkIfString(stringToScan, startIdx, 5000)
  checks.checkIfString(stringToFind, 1, 500)
  checks.checkIntIsBetween(endIdx, startIdx, len(stringToScan) - 1)
  findIdx = -1
  while findIdx == -1 and startIdx <= endIdx:
    findIdx = stringToScan.find(stringToFind, startIdx, endIdx + 1)
    if findIdx == -1:
      return False, -1
    if findIdx > startIdx and not stringToScan[findIdx - 1].isspace():
      startIdx = findIdx + 1
      findIdx = -1
  return findIdx != -1, findIdx

def whitespaceDelimitedFind(stringToScan, stringToFind, startIdx, endIdx):
  """Raises error for empty strings because indexes cannot be set properly.\n
Return values: \n
* found: True | False
* index: -1 if not found"""
  checks.checkIfString(stringToScan, startIdx, 5000)
  checks.checkIfString(stringToFind, 1, 500)
  checks.checkIntIsBetween(endIdx, startIdx, len(stringToScan) - 1)
  findIdx = -1
  while findIdx == -1 and startIdx <= endIdx:
    found, findIdx = beforeWhitespaceDelimitedFind(stringToScan, stringToFind, startIdx, endIdx)
    if not found:
      return False, -1
    lastCharIdx = findIdx + len(stringToFind) - 1
    if lastCharIdx < endIdx and not stringToScan[lastCharIdx + 1].isspace():
      startIdx = findIdx + 1
      findIdx = -1
  return findIdx != -1, findIdx

def find(stringToScan, stringToFind, startIdx, endIdx, notFoundValue):
  """Raises exception if any string is empty\n
Return values:\n
* found: True | False
* index: position at which is the first find, otherwise <notFoundValue> if not found"""
  checks.checkIfString(stringToScan, startIdx, 4000)
  checks.checkIfString(stringToFind, 1, 400)
  checks.checkIntIsBetween(endIdx, startIdx, len(stringToScan) - 1)
  checks.checkIfType(notFoundValue, int)
  idx = stringToScan.find(stringToFind, startIdx, endIdx + 1)
  if idx == -1:
    return False, notFoundValue
  return True, idx

def rfind(stringToScan, stringToFind, startIdx, endIdx, notFoundValue):
  """Raises exception if any string is empty\n
Return values:\n
* found: True | False
* index: position at which is the first find, otherwise <notFoundValue> if not found"""
  checks.checkIfString(stringToScan, startIdx, 4000)
  checks.checkIfString(stringToFind, 1, 400)
  checks.checkIntIsBetween(endIdx, startIdx, len(stringToScan) - 1)
  checks.checkIfType(notFoundValue, int)
  idx = stringToScan.rfind(stringToFind, startIdx, endIdx + 1)
  if idx == -1:
    return False, notFoundValue
  return True, idx

def findAll(stringToScan, stringToFind, startIdx, endIdx):
  """Includes overlaps. Raises exception if any string is empty\n
Return value:\n
* indexes: list of ints in ascending order containing indexes for every match"""
  checks.checkIfString(stringToScan, startIdx, 4000)
  checks.checkIfString(stringToFind, 1, 400)
  checks.checkIntIsBetween(endIdx, startIdx, len(stringToScan) - 1)
  result = []
  idx = stringToScan.find(stringToFind, startIdx, endIdx + 1)
  while idx != -1:
    result.append(idx)
    if idx == endIdx:
      break
    idx = stringToScan.find(stringToFind, idx + 1, endIdx + 1)
  return result

def findNthOccurrence(stringToScan, stringToFind, n, startIdx, endIdx):
  """Includes overlaps. Raises exception if any string is empty\n
Return value:\n
* found: True | False
* index: position of the nth find, otherwise -1"""
  checks.checkIfString(stringToScan, startIdx, 4000)
  checks.checkIfString(stringToFind, 1, 400)
  checks.checkIntIsBetween(endIdx, startIdx, len(stringToScan) - 1)
  checks.checkIntIsBetween(n, 1, 400)
  notFoundResult = (False, -1)
  if n > len(stringToScan):
    return notFoundResult
  i = 0
  idx = -1
  while i < n:
    idx = stringToScan.find(stringToFind, startIdx, endIdx + 1)
    if idx == -1:
      return notFoundResult
    i += 1
    if idx == endIdx:
      break
    startIdx = idx + 1
  return True, idx

def findFirstInLinePythonStringConstant(stringToScan, startIdx, endIdx):
  """ Raises exception if string is empty. Detects a multiline string as multiple strings. Ignores invalid strings. \n
Return value: \n
* found: True | False
* openingQuoteIdx: -1 if not found
* closingQuoteIdx: -1 if not found"""
  checks.checkIfString(stringToScan, startIdx, 4000)
  checks.checkIntIsBetween(endIdx, startIdx, len(stringToScan) - 1)
  notFoundValue = False, -1, -1
  simpleQuoteFound, simpleQuoteIdx = find(stringToScan, "'", startIdx, endIdx, 700000)
  doubleQuoteFound, doubleQuoteIdx = find(stringToScan, '"', startIdx, endIdx, 700000)
  if not simpleQuoteFound and not doubleQuoteFound:
    return notFoundValue
  openingQuoteIdx = simpleQuoteIdx if simpleQuoteIdx < doubleQuoteIdx else doubleQuoteIdx
  if openingQuoteIdx == endIdx:
    return notFoundValue
  quoteChar = stringToScan[openingQuoteIdx]
  leftSideIdx = openingQuoteIdx + 1
  while True:
    closingQuoteFound, closingQuoteIdx = find(stringToScan, quoteChar, leftSideIdx, endIdx, -1)
    if not closingQuoteFound:
      return notFoundValue
    nrOfSlashesBefore = 0
    while stringToScan[closingQuoteIdx - nrOfSlashesBefore - 1] == "\\":
      if closingQuoteIdx == endIdx: return notFoundValue
      nrOfSlashesBefore += 1
    if nrOfSlashesBefore % 2 == 1:
      leftSideIdx = closingQuoteIdx + 1
      continue
    break
  return True, openingQuoteIdx, closingQuoteIdx

def indexIsOutsideOfPythonStringConstant(stringToScan, index):
  """Tells if an index is outside of a python string constant meaning that it also cannot be one of the surrounding
quotes. \n Raises exception if string is empty."""
  checks.checkIfString(stringToScan, 0, 4000)
  checks.checkIntIsBetween(index, 0, len(stringToScan) - 1)
  startIdx = 0
  endIdx = len(stringToScan) - 1
  while startIdx <= endIdx:
    found, openingQuoteIdx, closingQuoteIdx = findFirstInLinePythonStringConstant(stringToScan, startIdx, endIdx)
    if not found:
      return True
    if index < openingQuoteIdx:
      return True
    if index <= closingQuoteIdx:
      return False
    startIdx = closingQuoteIdx + 1
  return False
