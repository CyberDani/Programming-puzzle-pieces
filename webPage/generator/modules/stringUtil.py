from modules import checks

def getNextChar(string, index):
  """Returns **None** if there is no next char. \n
  Raises exception for empty string because the index cannot be set properly."""
  checks.checkIfString(string, 0, 5000)
  checks.checkIntIsBetween(index, 0, len(string) - 1)
  if index == len(string) - 1:
    return None
  return string[index + 1]

def getPreviousChar(string, index):
  """Returns **None** if there is no previous char. \n
  Raises exception for empty string because the index cannot be set properly."""
  checks.checkIfString(string, 0, 5000)
  checks.checkIntIsBetween(index, 0, len(string) - 1)
  if index == 0:
    return None
  return string[index - 1]

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

def rTrimNewLines(string):
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

def getFirstNonWhiteSpaceCharIdx(string, inclusiveStartIdx, exclusiveEndIdx):
  """Raises error at empty string because indexes cannot be set properly.\n
Return values:\n
* found: True | False \n
* index: -1 if not found"""
  checks.checkIfString(string, 0, 5000)
  checks.checkIntIsBetween(inclusiveStartIdx, 0, exclusiveEndIdx - 1)
  checks.checkIntIsBetween(exclusiveEndIdx, inclusiveStartIdx + 1, len(string))
  idx = inclusiveStartIdx
  while idx < exclusiveEndIdx and string[idx].isspace():
    idx += 1
  if idx == exclusiveEndIdx:
    return False, -1
  return True, idx

def getLastNonWhiteSpaceCharIdx(string, inclusiveStartIdx, exclusiveEndIdx):
  """Raises error at empty string because indexes cannot be set properly.\n
Return values:\n
* found: True | False \n
* index: -1 if not found"""
  checks.checkIfString(string, 0, 5000)
  checks.checkIntIsBetween(inclusiveStartIdx, 0, exclusiveEndIdx - 1)
  checks.checkIntIsBetween(exclusiveEndIdx, inclusiveStartIdx + 1, len(string))
  idx = exclusiveEndIdx - 1
  while idx >= inclusiveStartIdx and string[idx].isspace():
    idx -= 1
  if idx == inclusiveStartIdx - 1:
    return False, -1
  return True, idx

def beforeWhitespaceDelimitedFind(stringToScan, stringToFind, inclusiveStartIdx, exclusiveEndIdx):
  """Returns **-1** if not found \n
  Raises error at empty strings because indexes cannot be set properly for scanning an empty string,
  or it does not make sense to find an empty string"""
  checks.checkIfString(stringToScan, inclusiveStartIdx, 5000)
  checks.checkIfString(stringToFind, 1, 500)
  checks.checkIntIsBetween(exclusiveEndIdx, inclusiveStartIdx + 1, len(stringToScan))
  findIdx = -1
  while findIdx == -1 and inclusiveStartIdx < exclusiveEndIdx:
    findIdx = stringToScan.find(stringToFind, inclusiveStartIdx, exclusiveEndIdx)
    if findIdx == -1:
      return -1
    if findIdx > 0 and not stringToScan[findIdx - 1].isspace():
      inclusiveStartIdx = findIdx + 1
      findIdx = -1
  return findIdx

def find(stringToScan, stringToFind, inclusiveStartIdx, inclusiveEndIdx, notFoundValue):
  """Raises exception if any string is empty\n
Return values:\n
* found: True | False
* index: position at which is the first find, otherwise <notFoundValue> if not found"""
  checks.checkIfString(stringToScan, inclusiveStartIdx, 4000)
  checks.checkIfString(stringToFind, 1, 400)
  checks.checkIntIsBetween(inclusiveEndIdx, inclusiveStartIdx, len(stringToScan) - 1)
  checks.checkIfType(notFoundValue, int)
  idx = stringToScan.find(stringToFind, inclusiveStartIdx, inclusiveEndIdx + 1)
  if idx == -1:
    return False, notFoundValue
  return True, idx

def rfind(stringToScan, stringToFind, inclusiveStartIdx, inclusiveEndIdx, notFoundValue):
  """Raises exception if any string is empty\n
Return values:\n
* found: True | False
* index: position at which is the first find, otherwise <notFoundValue> if not found"""
  checks.checkIfString(stringToScan, inclusiveStartIdx, 4000)
  checks.checkIfString(stringToFind, 1, 400)
  checks.checkIntIsBetween(inclusiveEndIdx, inclusiveStartIdx, len(stringToScan) - 1)
  checks.checkIfType(notFoundValue, int)
  idx = stringToScan.rfind(stringToFind, inclusiveStartIdx, inclusiveEndIdx + 1)
  if idx == -1:
    return False, notFoundValue
  return True, idx

def findAll(stringToScan, stringToFind, inclusiveStartIdx, inclusiveEndIdx):
  """Includes overlaps. Raises exception if any string is empty\n
Return value:\n
* indexes: list of ints in ascending order containing indexes for every match"""
  checks.checkIfString(stringToScan, inclusiveStartIdx, 4000)
  checks.checkIfString(stringToFind, 1, 400)
  checks.checkIntIsBetween(inclusiveEndIdx, inclusiveStartIdx, len(stringToScan) - 1)
  result = []
  idx = stringToScan.find(stringToFind, inclusiveStartIdx, inclusiveEndIdx + 1)
  while idx != -1:
    result.append(idx)
    if idx == inclusiveEndIdx:
      break
    idx = stringToScan.find(stringToFind, idx + 1, inclusiveEndIdx + 1)
  return result
