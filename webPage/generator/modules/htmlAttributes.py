from modules import checks
from modules import stringUtil

# TODO rename getAttributeNameIdx
def getAttributeIdx(htmlAttributes, key):
  """Only the first declaration is taken (if there are multiple) as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
\n Return values:
* corrupt: True | False *(invalidates empty strings, validates string only near the key)*
* firstKeyIdx: **-1** if attribute not found or corrupt """
  checks.checkIfString(htmlAttributes, 0, 3000)
  checks.checkIfString(key, 0, 60)
  notFoundResult = (False, -1)
  corruptResult = (True, -1)
  if not htmlAttributes or not key:
    return notFoundResult
  if stringContainsHtmlDelimiter(key, 0, len(key)):
    return corruptResult
  keyFound, firstKeyIdx = htmlDelimitedFind(htmlAttributes, key, 0, len(htmlAttributes))
  while keyFound:
    corrupt, isWithinAttributeValue = indexIsWithinHtmlAttributeValue(htmlAttributes, firstKeyIdx)
    if corrupt:
      return corruptResult
    if isWithinAttributeValue:
      lastKeyIdx = firstKeyIdx + len(key) - 1
      # lastKeyIdx + 1 exists, it is at least the closing quote
      keyFound, firstKeyIdx = htmlDelimitedFind(htmlAttributes, key, lastKeyIdx + 1, len(htmlAttributes))
      continue
    return False, firstKeyIdx
  return notFoundResult

# TODO test attribute: title = '=====' and title = 'number="two"' and title = 'number == "two"'
# TODO test integrity=\"sha512-6PM0qxuIQ==\" for below functions (an equal character in value is still valid)
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

# -> corrupt, attributes {name -> value}
def getHtmlAttributes(attributesString, startIdx):
  """Each attribute is taken and validated once at its first occurrence. \n
Raises exception if <attributesString> is empty because startIdx cannot be set properly \n
\n Return values: \n
* corrupt: True | False
* attributes: dictionary of {attributeName -> None | attributeString}"""
  corruptReturn = (True, {})
  notFoundReturn = (False, {})
  corrupt, attributeName, attributeValue, startIdx, endIdx = getNextHtmlAttribute(attributesString, startIdx)
  if corrupt:
    return corruptReturn
  return notFoundReturn

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

def thereIsAttributeNameBeforeIdx(htmString, idx):
  checks.checkIfString(htmString, 0, 4000)
  checks.checkIntIsBetween(idx, 0, len(htmString) - 1)
  if idx == 0:
    return False
  idx -= 1
  while idx >= 0:
    currentChar = htmString[idx]
    if currentChar == "'" or currentChar == '"' or currentChar == "=":
      return False
    if not currentChar.isspace():
      return True
    idx -= 1
  return False

def isThereAnyQuoteChar(htmlString, inclusiveStartIdx, inclusiveEndIdx):
  """Raises exception for empty string because the index cannot be set properly."""
  checks.checkIfString(htmlString, 0, 4000)
  checks.checkIntIsBetween(inclusiveStartIdx, 0, len(htmlString) - 1)
  checks.checkIntIsBetween(inclusiveEndIdx, inclusiveStartIdx, len(htmlString) - 1)
  if htmlString.find("'", inclusiveStartIdx, inclusiveEndIdx + 1) != -1:
    return True
  return htmlString.find('"', inclusiveStartIdx, inclusiveEndIdx + 1) != -1

def nextNonWhiteSpaceCharIsHtmlDelimiter(htmlString, index):
  """Raises exception for empty string because the index cannot be set properly."""
  checks.checkIfString(htmlString, 0, 4000)
  checks.checkIntIsBetween(index, 0, len(htmlString) - 1)
  if index == len(htmlString) - 1:
    return False
  idx = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlString, index + 1, len(htmlString))
  return idx != -1 and charIsHtmlDelimiter(htmlString[idx])

# TODO try to better clean code it
def indexIsWithinHtmlAttributeValue(attributeString, index):
  """Main quotes and the equal character are considered not to be within attribute value.
Raises exception for empty string because the index cannot be set properly.
\n Return values:
* corrupt: True | False (validates only a portion of text to ensure the correctness of the result)
* isAttributeValue: True | False, None if corrupt"""
  corruptResult = (True, None)
  equalIdxsBefore = stringUtil.findAll(attributeString, "=", 0, index)
  equalFoundAfter, referenceIdxFromRight = stringUtil.find(attributeString, "=", index, len(attributeString) - 1,
                                                           notFoundValue=len(attributeString) - 1)
  if not equalIdxsBefore:
    if isThereAnyQuoteChar(attributeString, 0, referenceIdxFromRight):
      return corruptResult
    return False, False

  maxEqualIdxQuoteIdxsPair = (-1, -1, -1)
  for equalIdx in equalIdxsBefore:
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                            = getQuoteIndexesAfterEqualChar(attributeString, equalIdx)
    if not corrupt:
      if closingQuoteIdx > maxEqualIdxQuoteIdxsPair[2]:
        maxEqualIdxQuoteIdxsPair = (equalIdx, openingQuoteCharIdx, closingQuoteIdx)
  closingQuoteIdx = maxEqualIdxQuoteIdxsPair[2]
  if closingQuoteIdx == -1:
    return corruptResult
  if index <= maxEqualIdxQuoteIdxsPair[1] or index == closingQuoteIdx:
    return False, False
  isWithinAttributeValue = closingQuoteIdx > index
  if closingQuoteIdx == len(attributeString) - 1:
    return False, isWithinAttributeValue
  equalFoundAfter, referenceIdxFromRight = stringUtil.find(attributeString, "=", closingQuoteIdx + 1,
                                                      len(attributeString) - 1, notFoundValue=len(attributeString) - 1)
  isThereAnyQuoteCharAfter = isThereAnyQuoteChar(attributeString, closingQuoteIdx + 1, referenceIdxFromRight)
  if isThereAnyQuoteCharAfter:
    return corruptResult
  return False, isWithinAttributeValue

def htmlDelimitedFind(stringToScan, stringToMatch, inclusiveStartIndex, exclusiveEndIdx):
  """Validates outside the [start, end] indexes. Raises exception for empty strings.
\n Return values:
* found: True | False
* firstIndex: position within <stringToScan> from where <stringToMatch> begins, -1 if not found"""
  checks.checkIfString(stringToScan, 0, 5000)
  checks.checkIfString(stringToMatch, 1, 5000)
  checks.checkIntIsBetween(inclusiveStartIndex, 0, len(stringToScan) - 1)
  checks.checkIntIsBetween(exclusiveEndIdx, inclusiveStartIndex + 1, len(stringToScan))
  firstIdx = stringToScan.find(stringToMatch, inclusiveStartIndex, exclusiveEndIdx)
  while firstIdx != -1:
    if stringIsHtmlDelimited(stringToScan, firstIdx, len(stringToMatch)):
      return True, firstIdx
    lastKeyIdx = firstIdx + len(stringToMatch) - 1
    firstIdx = stringToScan.find(stringToMatch, lastKeyIdx + 1, len(stringToScan))
    continue
  return firstIdx != -1, firstIdx

def stringContainsHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx):
  """Raises exception for empty string because the index cannot be set properly"""
  checks.checkIfString(string, inclusiveStartIdx, 5000)
  checks.checkIntIsBetween(exclusiveEndIdx, inclusiveStartIdx, len(string))
  for idx in range(inclusiveStartIdx, exclusiveEndIdx):
    if charIsHtmlDelimiter(string[idx]):
      return True
  return False

def getQuoteIndexesAfterEqualChar(htmlString, equalCharIdx):
  """Validates adjacent chars near equal and main quotes. \n
Can be a false positive: attribute value looking string inside an attribute value. Use indexIsWithinHtmlAttributeValue
if you need this guarantee covered.\n
Raises exception for empty string because the index cannot be set properly.\n
\n Return values:
* corrupt: True | False (also validates the equal character)
* openingQuoteCharIdx: -1 if corrupt
* closingQuoteIdx: -1 if corrupt
* quoteChar: empty string if corrupt"""
  corruptResult = (True, -1, -1, "")
  corrupt, openingQuoteCharIdx = validateAdjacentCharsNearEqualChar(htmlString, equalCharIdx)
  if corrupt:
    return corruptResult
  corrupt, closingQuoteIdx, mainQuoteChar = getAndValidateClosingQuote(htmlString, openingQuoteCharIdx)
  if corrupt:
    return corruptResult
  return corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar

def validateAdjacentCharsNearEqualChar(htmlString, equalIndex):
  """Raises exception for empty string because the index cannot be set properly.
\nAssumes but does not check if equal is in outside an attribute value.\n
\nReturn values: \n
* corrupt: True | False (also validates the equal character)
* attrOpeningQuoteIndex: -1 if corrupt"""
  checks.checkIfString(htmlString, 0, 4000)
  checks.checkIntIsBetween(equalIndex, 0, len(htmlString) - 1)
  corruptResult = (True, -1)
  if htmlString[equalIndex] != "=":
    return corruptResult
  if equalIndex == 0 or equalIndex == len(htmlString) - 1:
    return corruptResult
  if not thereIsAttributeNameBeforeIdx(htmlString, equalIndex):
    return corruptResult
  quoteIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlString, equalIndex + 1, len(htmlString))
  if htmlString[quoteIdx] != "'" and htmlString[quoteIdx] != '"':
    return corruptResult
  return False, quoteIdx

def getAndValidateClosingQuote(htmlAttributes, openingQuoteCharIdx):
  """Validates characters near the closing quote char, but not the opening \n
Raises exception for empty string because the index cannot be set properly.
\n Return values:
* corrupt: True | False
* closingQuoteIdx: **-1** if corrupt
* quoteChar: empty string if corrupt"""
  checks.checkIfString(htmlAttributes, 0, 4000)
  checks.checkIntIsBetween(openingQuoteCharIdx, 0, len(htmlAttributes) - 1)
  corruptResult = (True, -1, "")
  mainQuoteChar = htmlAttributes[openingQuoteCharIdx]
  if mainQuoteChar != "'" and mainQuoteChar != '"':
    return corruptResult
  closingQuoteIdx = htmlAttributes.find(mainQuoteChar, openingQuoteCharIdx + 1, len(htmlAttributes))
  if closingQuoteIdx == -1:
    return corruptResult
  if nextNonWhiteSpaceCharIsHtmlDelimiter(htmlAttributes, closingQuoteIdx):
    return corruptResult
  return False, closingQuoteIdx, mainQuoteChar

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
