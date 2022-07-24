from modules import checks

# <endsWithStr> must be after <startsWithStr>
# Return empty string if 
def getStringStartsWithEndsWithNoOverlap(src, startsWithStr, endsWithStr):
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
