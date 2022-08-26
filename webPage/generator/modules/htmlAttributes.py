from modules import checks
from modules import stringUtil

def getAttributeIdx(htmlAttributes, key):
  """Only the first declaration is taken (if there are multiple) as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
\n Return values:
* corrupt: True | False *(does not validate the attribute value)*
* firstIdx: **-1** if attribute not found or corrupt """
  checks.checkIfString(htmlAttributes, 0, 3000)
  checks.checkIfString(key, 0, 60)
  notFoundResult = (False, -1)
  corruptResult = (True, -1)
  if not htmlAttributes or not key:
    return notFoundResult
  # TODO delimitedFind(string, key,  before=[whitespace, nothing, "<"], after=[whitespace, nothing, "="],
  #                   corruptIfBefore = [",'] corruptIfAfter = [",'], 0, len(str))
  firstIdx = htmlAttributes.find(key, 0, len(htmlAttributes))
  while firstIdx != -1:
    # TODO checkAttributeNameFromRight + checkAttributeNameFromLeft -> invalid, ok
    # Right
    thereIsNextChar = firstIdx + len(key) < len(htmlAttributes)
    firstCharAfterKey = None
    if thereIsNextChar:
      firstCharAfterKey = htmlAttributes[firstIdx + len(key)]
    if thereIsNextChar and (firstCharAfterKey == "'" or firstCharAfterKey == '"'):
      return corruptResult
    validatedFromRight = not thereIsNextChar or firstCharAfterKey == "=" or firstCharAfterKey.isspace()
    # Left
    if firstIdx > 0 and (htmlAttributes[firstIdx - 1] == '"' or htmlAttributes[firstIdx - 1] == "'"):
      return corruptResult
    validatedFromLeft = firstIdx == 0 or htmlAttributes[firstIdx - 1].isspace()
    if validatedFromRight and validatedFromLeft:
      return False, firstIdx
    firstIdx = htmlAttributes.find(key, firstIdx + 1, len(htmlAttributes))
  return notFoundResult

# TODO test "class'myclass' class='myclass' -- should return corrupt
#  without any error"
# TODO add corrupt return variable after you fix the unsure situation
def extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(htmlAttributes, key):
  """Returns **None** if corrupt or there is no attribute value. Returns an **empty list** if the value is empty
  or has only whitespaces\n
  Only the first declaration is taken (if there are multiple) as stated by the standard:
  https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
  checks.checkIfString(htmlAttributes, 0, 800)
  checks.checkIfString(key, 1, 30)
  result = []
  notFoundResult = None
  corruptResult = None
  corrupt, firstIdx = getAttributeIdx(htmlAttributes, key)
  if corrupt:
    return corruptResult
  if firstIdx == -1:
    return notFoundResult
  corrupt, attributeName, attributeValue, startIdx, endIdx = getNextHtmlAttribute(htmlAttributes, firstIdx)
  if corrupt:
    return corruptResult
  if attributeValue is None:
    return notFoundResult
  # TODO getSplitUniqueElements(Char::WHITESPACE)
  values = attributeValue.split()
  for value in values:
    if value not in result:
      result.append(value)
  return result

def getListOfHtmlAttributeNames(attributesString):
  """ Only the first declaration is taken per each attribute name (if there are multiple) as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html\n
\n Return values:
* <corrupt>: True | False
* <attributeNames>: empty list if corrupt or attribute not found"""
  checks.checkIfString(attributesString, 0, 1000)
  result = []
  corruptResult = (True, [])
  idx = 0
  while idx < len(attributesString):
    corrupt, attributeName, attributeValue, startIdx, endIdx = getNextHtmlAttribute(attributesString, idx)
    if corrupt:
      return corruptResult
    if attributeName is None:
      nextNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, idx, len(attributesString))
      if nextNonSpaceCharIdx != -1:
        return False, []
      break
    if attributeName not in result:
      result.append(attributeName)
    idx = endIdx + 1
    continue
  return False, result


def getNextHtmlAttribute(attributesString, startIdx):
  """ Raises exception if <startIdx> is not valid. This means that <attributesString> cannot be an empty string as
there is no first index. \n
Only the first attribute is taken and validated \n
\n Return values:
* <corrupt>: True | False
* <attributeName>, <attributeValue> : **None** if no attribute was found or <attributesString> is corrupt
* <attrStartIdx>, <attrEndIdx> : inclusive, **-1** if no attribute was found or attributesString is corrupt"""
  noAttributeResult = (False, None, None, -1, -1)
  corruptResult = (True, None, None, -1, -1)
  corrupt, attributeName, firstCharIdx, lastCharIdx = getNextHtmlAttributeName(attributesString, startIdx)
  if corrupt:
    return corruptResult
  if firstCharIdx == -1:
    return noAttributeResult
  if lastCharIdx == len(attributesString) - 1:
    return False, attributeName, None, firstCharIdx, lastCharIdx
  corrupt, firstQuoteIdx, secondQuoteIdx = getNextHtmlAttributeValueIfExists(attributesString, lastCharIdx + 1)
  if corrupt:
    return corruptResult
  if firstQuoteIdx == -1:
    return False, attributeName, None, firstCharIdx, lastCharIdx
  return False, attributeName, attributesString[firstQuoteIdx + 1:secondQuoteIdx], firstCharIdx, secondQuoteIdx

# TODO see if you can make it prettier
def getNextHtmlAttributeValueIfExists(attributesString, startIdx):
  """Raises error at empty string because <startIdx> cannot be set properly\n
You DO NOT want to call this before checking for an attribute name first, e.g. calling *getNextHtmlAttributeName()*\n
Return values:\n
* corrupt : True | False
* firstQuoteIdx, secondQuoteIdx: **-1** if corrupt or there is no attribute value """
  checks.checkIfString(attributesString, 0, 1000)
  checks.checkIntIsBetween(startIdx, 0, len(attributesString) - 1)
  firstNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, startIdx, len(attributesString))
  if firstNonSpaceCharIdx == -1:
    return False, -1, -1
  firstNonSpaceChar = attributesString[firstNonSpaceCharIdx]
  if firstNonSpaceChar != "=":
    isCorrupt = firstNonSpaceChar == "'" or firstNonSpaceChar == "\""
    return isCorrupt, -1, -1
  if firstNonSpaceCharIdx == len(attributesString) - 1:
    return True, -1, -1
  nonSpaceCharIdxAfterEq = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, firstNonSpaceCharIdx + 1,
                                                                   len(attributesString))
  quoteChar = attributesString[nonSpaceCharIdxAfterEq]
  if quoteChar != "'" and quoteChar != "\"":
    return True, -1, -1
  secondQuoteIdx = attributesString.find(quoteChar, nonSpaceCharIdxAfterEq + 1)
  if secondQuoteIdx == -1:
    return True, -1, -1
  return False, nonSpaceCharIdxAfterEq, secondQuoteIdx

# TODO see if you can make it look prettier
def getNextHtmlAttributeName(attributesString, startIdx):
  """Raises error at empty string because <startIdx> cannot be set properly\n
Return values:\n
* corrupt : True | False *(does not validate the attribute value)*
* attributeName: **None** if corrupt or there is no attribute
* firstCharIdx, lastCharIdx: **-1** if corrupt or there is no attribute """
  checks.checkIfString(attributesString, 0, 1000)
  checks.checkIntIsBetween(startIdx, 0, len(attributesString) - 1)
  corruptResult = (True, None, -1, -1)
  firstNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, startIdx, len(attributesString))
  if firstNonSpaceCharIdx == -1:
    return False, None, -1, -1
  firstNonSpaceChar = attributesString[firstNonSpaceCharIdx]
  if firstNonSpaceChar == "=" or firstNonSpaceChar == "'" or firstNonSpaceChar == "\"":
    return corruptResult
  currentIdx = firstNonSpaceCharIdx
  attributeName = ""
  while currentIdx < len(attributesString):
    currentChar = attributesString[currentIdx]
    if currentChar.isspace() or currentChar == "=":
      return False, attributeName, firstNonSpaceCharIdx, currentIdx-1
    if currentChar == "'" or currentChar == '"':
      return corruptResult
    attributeName += currentChar
    currentIdx += 1
  return False, attributeName, firstNonSpaceCharIdx, len(attributesString) - 1
