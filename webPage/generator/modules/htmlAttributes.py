from modules import checks
from modules import stringUtil

# TODO this function looks ugly, clean code it
def getAttributeIdx(htmlAttributes, key):
  """Only the first declaration is taken (if there are multiple) as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
\n Return values:
* corrupt: True | False *(does not validate the attached attribute value and the rest of string out of key context)*
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
    # continue if not a full word
    if not stringIsHtmlDelimited(htmlAttributes, firstIdx, len(key)):
      firstIdx = htmlAttributes.find(key, firstIdx + 1, len(htmlAttributes))
      continue

    # Check if seems to be part of attribute value from right
    firstEqualIdxAfterKey = htmlAttributes.find("=", firstIdx + len(key))
    referenceIdxFromRight = firstEqualIdxAfterKey
    if referenceIdxFromRight == -1:
      referenceIdxFromRight = len(htmlAttributes) - 1
    nrOfSimpleQuotesAfter = htmlAttributes.count("'", firstIdx + len(key), referenceIdxFromRight + 1)
    nrOfDoubleQuotesAfter = htmlAttributes.count('"', firstIdx + len(key), referenceIdxFromRight + 1)
    seemsToBeAttributeValueFromRight = nrOfSimpleQuotesAfter > 0 or nrOfDoubleQuotesAfter > 0

    # Check if seems to be part of attribute value from left
    referenceIdxFromLeft = htmlAttributes.rfind("=", 0, firstIdx)
    if referenceIdxFromLeft == 0:
      return corruptResult
    equalFoundBefore = True
    if referenceIdxFromLeft == -1:
      referenceIdxFromLeft = 0
      equalFoundBefore = False
    # check if there is attribute name before equal
    if equalFoundBefore:
      idx = referenceIdxFromLeft - 1
      while idx >= 0:
        currentChar = htmlAttributes[idx]
        if currentChar == "'" or currentChar == '"' or currentChar == "=":
          return corruptResult
        if not currentChar.isspace():
          break
        idx -= 1
      if idx == -1:
        return corruptResult
    # another check
    nrOfMainQuotesBefore = 0
    if equalFoundBefore:
      firstNonSpaceCharIdxAfterEqual = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlAttributes, referenceIdxFromLeft + 1,
                                                                            len(htmlAttributes))
      firstNonSpaceCharAfterEqual = htmlAttributes[firstNonSpaceCharIdxAfterEqual]
      if firstNonSpaceCharAfterEqual != "'" and firstNonSpaceCharAfterEqual != '"':
        return corruptResult
      nrOfMainQuotesBefore = htmlAttributes.count(firstNonSpaceCharAfterEqual, referenceIdxFromLeft, firstIdx)
    nrOfSimpleQuotesBefore = htmlAttributes.count("'", referenceIdxFromLeft, firstIdx)
    nrOfDoubleQuotesBefore = htmlAttributes.count('"', referenceIdxFromLeft, firstIdx)
    if nrOfMainQuotesBefore > 3:
      return corruptResult
    seemsToBeAttributeValueFromLeft = nrOfMainQuotesBefore == 1 or nrOfMainQuotesBefore == 3

    if equalFoundBefore != (nrOfSimpleQuotesBefore + nrOfDoubleQuotesBefore > 0):
      return corruptResult

    if seemsToBeAttributeValueFromLeft != seemsToBeAttributeValueFromRight:
      return corruptResult

    if seemsToBeAttributeValueFromLeft:
      firstSimpleQuoteIdxBefore = htmlAttributes.rfind("'", referenceIdxFromLeft, firstIdx)
      firstDoubleQuoteIdxBefore = htmlAttributes.rfind('"', referenceIdxFromLeft, firstIdx)
      mainQuoteCharIdx = -1
      if firstSimpleQuoteIdxBefore == -1:
        mainQuoteCharIdx = firstDoubleQuoteIdxBefore
      elif firstDoubleQuoteIdxBefore == -1:
        mainQuoteCharIdx = firstSimpleQuoteIdxBefore
      elif firstSimpleQuoteIdxBefore < firstDoubleQuoteIdxBefore:
        mainQuoteCharIdx = firstSimpleQuoteIdxBefore
      else:
        mainQuoteCharIdx = firstDoubleQuoteIdxBefore
      mainQuoteChar = htmlAttributes[mainQuoteCharIdx]
      if mainQuoteChar == "'" and (nrOfSimpleQuotesBefore != 1 or nrOfSimpleQuotesAfter != 1):
        return corruptResult
      if mainQuoteChar == '"' and (nrOfDoubleQuotesBefore != 1 or nrOfDoubleQuotesAfter != 1):
        return corruptResult
      endingQuoteIdx = -1
      if mainQuoteChar == "'":
        endingQuoteIdx = htmlAttributes.find("'", mainQuoteCharIdx + 1, referenceIdxFromRight + 1)
      else:
        endingQuoteIdx = htmlAttributes.find('"', mainQuoteCharIdx + 1, referenceIdxFromRight + 1)
      # after endingQuote there should be no more quotes
      idx = endingQuoteIdx + 1
      while idx < len(htmlAttributes):
        currentChar = htmlAttributes[idx]
        if currentChar.isspace():
          idx += 1
          continue
        if currentChar == "=":
          return corruptResult
        if currentChar == "'" or currentChar == '"':
          return corruptResult
        break

    if seemsToBeAttributeValueFromLeft and seemsToBeAttributeValueFromRight:
      firstIdx = htmlAttributes.find(key, firstIdx + 1, len(htmlAttributes))
      continue

    return False, firstIdx
  return notFoundResult

# TODO test 'class="note"id="red"' below functions, it is valid HTML even if there is no space in ' note"id '

def extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(htmlAttributes, key):
  """Only the first declaration is taken (if there are multiple) as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
\n Return values:
* <corrupt>: True | False
* <values>: **None** if corrupt or attribute name not found, empty list if the value is empty or whitspace"""
  checks.checkIfString(htmlAttributes, 0, 800)
  checks.checkIfString(key, 1, 30)
  result = []
  notFoundResult = (False, None)
  corruptResult = (True, None)
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
  return False, result

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
# TODO use corruptResult as for the other functions
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

def stringIsHtmlDelimited(htmlString, firstCharIdx, lengthOfString):
  """Intended for full word check in case of HTML attribute names and values. \n
Raises exception for empty string because the index cannot be set properly."""
  return htmlDelimitedFromLeft(htmlString, firstCharIdx) and \
         htmlDelimitedFromRight(htmlString, firstCharIdx + lengthOfString - 1)

def htmlDelimitedFromLeft(htmlString, index):
  """Intended for full word check in case of HTML attribute names and values. \n
Raises exception for empty string because the index cannot be set properly."""
  previousChar = stringUtil.getPreviousChar(htmlString, index)
  return previousChar is None or charIsHtmlDelimiter(previousChar)

def htmlDelimitedFromRight(htmlString, index):
  """Intended for full word check in case of HTML attribute names and values. \n
Raises exception for empty string because the index cannot be set properly."""
  nextChar = stringUtil.getNextChar(htmlString, index)
  return nextChar is None or charIsHtmlDelimiter(nextChar)

def charIsHtmlDelimiter(ch):
  """HTML attribute delimiters: Whitespace, equal, single-quote, double-quote"""
  checks.checkIfChar(ch)
  return ch.isspace() or ch == "=" or ch == '"' or ch == "'"
