from modules.checks import checks
from modules import stringUtil

def getStringFromDictionary(attributesDict):
  checks.checkIfType(attributesDict, dict)
  result = ""
  for key, value in attributesDict.items():
    checks.checkIfString(key, 0, 50)
    result += key
    if value is not None:
      checks.checkIfString(key, 0, 500)
      result += "=\"" + value + "\""
    result += " "
  if result:
    result = result[:-1]
  return result

def combineTwoAttributeStrings(string1, string2):
  """Only the first declaration is taken per string, duplication is removed. \n
Combining value and non-value for the same name is considered corrupt. Duplicates equal values.\n
\n Return values: \n
* corrupt: True | False
* attributes: dictionary of {attributeName -> None | attributeString}"""
  corruptReturn = (True, {})
  corrupt1, attributes1 = getAllAttributes(string1)
  corrupt2, attributes2 = getAllAttributes(string2)
  if corrupt1 or corrupt2:
    return corruptReturn
  if not attributes1:
    return False, attributes2
  if not attributes2:
    return False, attributes1
  result = attributes1
  for key, value in attributes2.items():
    if key not in result:
      result[key] = value
      continue
    lValue = result[key]
    if value is None and lValue is None:
      continue
    if lValue is not None and value is not None:
      result[key] = lValue + " " + value
      continue
    return corruptReturn
  return False, result

def getUniqueValuesByName(htmlAttributes, name):
  """Separated by whitespaces. Only the first declaration is taken (if there are multiple) as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
\n Return values:
* corrupt: True | False
* nameFound: True | False (False if corrupt)
* valueFound: True | False (False if corrupt)
* values: empty list if corrupt **OR** not found **OR** the value is empty **OR** contains only whitespace(s)"""
  nameNotFoundResult = (False, False, False, [])
  valueNotFoundResult = (False, True, False, [])
  corruptResult = (True, False, False, [])
  corrupt, nameFound, valueFound, value = getValueByName(htmlAttributes, name)
  if corrupt:
    return corruptResult
  if not nameFound:
    return nameNotFoundResult
  if not valueFound:
    return valueNotFoundResult
  result = []
  values = value.split()
  for value in values:
    if value not in result:
      result.append(value)
  return False, True, True, result

def getValueByName(htmlAttributes, name):
  """Only the first declaration is taken as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
\n Return values:
* corrupt: True | False
* nameFound: True | False (False if corrupt)
* valueFound: True | False (False if corrupt)
* value: empty string if corrupt or not found"""
  checks.checkIfString(name, 1, 30)
  corruptResult = (True, False, False, "")
  keyNotFoundResult = (False, False, False, "")
  valueNotFoundResult = (False, True, False, "")
  corrupt, keyFound, firstIdx = getAttributeNameIdx(htmlAttributes, name)
  if corrupt:
    return corruptResult
  if not keyFound:
    return keyNotFoundResult
  corrupt, attributeName, attributeValue, startIdx, endIdx = getCurrentOrNextAttribute(htmlAttributes, firstIdx)
  if corrupt:
    return corruptResult
  if attributeValue is None:
    return valueNotFoundResult
  return False, True, True, attributeValue

def getAllAttributes(attributesString):
  """Each attribute is taken and validated once at its first occurrence. \n
\n Return values: \n
* corrupt: True | False
* attributes: dictionary of {attributeName -> None | attributeString}"""
  checks.checkIfString(attributesString, 0, 5000)
  corruptReturn = (True, {})
  result = {}
  index = 0
  while index < len(attributesString):
    corrupt, attributeName, attributeValue, startIdx, endIdx = getCurrentOrNextAttribute(attributesString, index)
    if corrupt:
      return corruptReturn
    if attributeName is None:
      return False, result
    if attributeName not in result:
      result[attributeName] = attributeValue
    index = endIdx + 1
  return False, result

def getAllAttributeNames(attributesString):
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
    corrupt, attributeName, attributeValue, startIdx, endIdx = getCurrentOrNextAttribute(attributesString, idx)
    if corrupt:
      return corruptResult
    if attributeName is None:
      nextNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, idx, len(attributesString) - 1)
      if nextNonSpaceCharIdx != -1:
        return False, result
      break
    if attributeName not in result:
      result.append(attributeName)
    idx = endIdx + 1
    continue
  return False, result

def getCurrentOrNextAttribute(attributesString, index):
  """Index must point to attribute name or before / after attribute. Otherwise, the result is undefined behavior. \n
Does not validate text before and after the attribute.
Only the first attribute is taken and validated. Raises exception for empty string.
\n Return values:
* <corrupt>: True | False
* <attributeName>, <attributeValue> : **None** if corrupt or not found
* <attrStartIdx>, <attrEndIdx> : **-1** if corrupt or not found"""
  noAttributeResult = (False, None, None, -1, -1)
  corruptResult = (True, None, None, -1, -1)
  corrupt, found, attributeName, firstCharIdx, lastCharIdx = getCurrentOrNextName(attributesString, index)
  if corrupt:
    return corruptResult
  if not found:
    return noAttributeResult
  if lastCharIdx == len(attributesString) - 1:
    return False, attributeName, None, firstCharIdx, lastCharIdx
  corrupt, found, firstQuoteIdx, secondQuoteIdx = getCurrentValue(attributesString, lastCharIdx + 1)
  if corrupt:
    return corruptResult
  if not found:
    return False, attributeName, None, firstCharIdx, lastCharIdx
  return False, attributeName, attributesString[firstQuoteIdx + 1:secondQuoteIdx], firstCharIdx, secondQuoteIdx

def getAttributeNameIdx(htmlAttributes, name):
  """Only the first declaration is taken (if there are multiple) as stated by the standard:
https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
\n Return values:
* corrupt: True | False *(invalidates empty strings, validates string only near the key)*
* attributeNameFound: True | False, None if corrupt
* firstKeyIdx: **-1** if attribute not found or corrupt """
  checks.checkIfString(htmlAttributes, 0, 3000)
  checks.checkIfString(name, 0, 60)
  notFoundResult = (False, False, -1)
  corruptResult = (True, None, -1)
  if not htmlAttributes or not name:
    return notFoundResult
  if stringContainsHtmlDelimiter(name, 0, len(name) - 1):
    return corruptResult
  keyFound, firstKeyIdx = htmlDelimitedFind(htmlAttributes, name, 0, len(htmlAttributes) - 1)
  while keyFound:
    corrupt, isWithinAttributeValue = indexIsWithinHtmlAttributeValue(htmlAttributes, firstKeyIdx)
    if corrupt:
      return corruptResult
    if isWithinAttributeValue:
      # firstKeyIdx + len(name) exists, it is at least the closing quote
      keyFound, firstKeyIdx = htmlDelimitedFind(htmlAttributes, name, firstKeyIdx + len(name), len(htmlAttributes) - 1)
      continue
    return False, True, firstKeyIdx
  return notFoundResult

def getCurrentOrNextName(attributesString, index):
  """Index must point to attribute name or before / after attribute. Otherwise, the result is undefined behavior.\n
Does not validate string before and after the attribute name. Raises error for empty string.\n
Return values:\n
* corrupt : True | False *(does not validate the attribute value)*
* found: True | False *(false if corrupt)*
* attributeName: **None** if corrupt or not found
* firstCharIdx, lastCharIdx: **-1** if corrupt or not found """
  corruptResult = (True, False, None, -1, -1)
  notFoundResult = (False, False, None, -1, -1)
  corrupt, found, firstIdx = jumpToFirstIdxOfCurrentOrNextName(attributesString, index)
  if corrupt:
    return corruptResult
  if not found:
    return notFoundResult
  found, delimiterAfterLastIdx = getFirstHtmlDelimiter(attributesString, firstIdx, len(attributesString) - 1)
  if not found:
    return False, True, attributesString[firstIdx:len(attributesString)], firstIdx, len(attributesString) - 1
  return False, True, attributesString[firstIdx:delimiterAfterLastIdx], firstIdx, delimiterAfterLastIdx - 1

def indexIsWithinHtmlAttributeValue(attributeString, index):
  """Main quotes and the equal character are considered not to be within attribute value.
Raises exception for empty string because the index cannot be set properly.
\n Return values:
* corrupt: True | False (validates only a portion of text to ensure the correctness of the result)
* isAttributeValue: True | False, None if corrupt"""
  corruptResult = (True, None)
  notFoundResult = (False, False)
  corrupt, found, equalIdx, openingQuoteIdx, closingQuoteIdx = getLastValueByFoundEquals(attributeString, 0, index)
  if corrupt:
    return corruptResult
  if not found or index <= openingQuoteIdx or index == closingQuoteIdx:
    return notFoundResult
  isWithinAttributeValue = closingQuoteIdx > index
  if closingQuoteIdx == len(attributeString) - 1:
    return False, isWithinAttributeValue
  equalFoundAfter, referenceIdxFromRight = stringUtil.find(attributeString, "=", closingQuoteIdx + 1,
                                                      len(attributeString) - 1, notFoundValue=len(attributeString) - 1)
  isThereAnyQuoteCharAfter = isThereAnyQuoteChar(attributeString, closingQuoteIdx + 1, referenceIdxFromRight)
  if isThereAnyQuoteCharAfter:
    return corruptResult
  return False, isWithinAttributeValue

def jumpToFirstIdxOfCurrentOrNextName(attributesString, index):
  """Index must point to an attribute name or before or after attributes. Otherwise, the result is undefined behavior.\n
Does not validate string before the index and after the attribute name. Raises error for empty string.\n
Return values:\n
* corrupt : True | False *(does not validate the attribute value)*
* found: True | False *(false if corrupt)*
* firstCharIdx: **-1** if corrupt or not found """
  checks.checkIfString(attributesString, 1, 5000)
  checks.checkIntIsBetween(index, 0, len(attributesString) - 1)
  corruptResult = (True, False, -1)
  notFoundResult = (False, False, -1)
  if attributesString[index].isspace():
    found, index = getFirstHtmlDelimiterThenSkipWhiteSpaces(attributesString, index, len(attributesString) - 1)
    if not found:
      return notFoundResult
  if charIsHtmlDelimiter(attributesString[index]):
    return corruptResult
  found, index = getLastHtmlDelimiter(attributesString, 0, index)
  if not found:
    index = -1
  return False, True, index + 1

def getCurrentValue(attributesString, index):
  """Index must point at most to the equal character before the value. Otherwise, the result is undefined behavior.\n
Raises exception for empty string.\n
Return values:\n
* corrupt : True | False
* found: True | False (False if corrupt)
* openingQuoteIdx, closingQuoteIdx: **-1** if corrupt or not found """
  checks.checkIfString(attributesString, 0, 5000)
  checks.checkIntIsBetween(index, 0, len(attributesString) - 1)
  notFoundResult = (False, False, -1, -1)
  corruptResult = (True, False, -1, -1)
  found, firstNonSpaceCharIdx = getFirstHtmlDelimiterThenSkipWhiteSpaces(attributesString, index, len(attributesString) - 1)
  if not found:
    return notFoundResult
  firstNonSpaceChar = attributesString[firstNonSpaceCharIdx]
  if firstNonSpaceChar != "=":
    return charIsQuote(firstNonSpaceChar), False, -1, -1
  corrupt, openingQuoteIdx, closingQuoteIdx, quoteChar = getQuoteIndexesByEqualChar(attributesString,
                                                                                    firstNonSpaceCharIdx)
  if corrupt:
    return corruptResult
  return False, True, openingQuoteIdx, closingQuoteIdx

def htmlDelimitedFind(stringToScan, stringToMatch, startIndex, endIndex):
  """Validates outside the [start, end] indexes. Raises exception for empty strings.
\n Return values:
* found: True | False
* firstIndex: position within <stringToScan> from where <stringToMatch> begins, -1 if not found"""
  checks.checkIfString(stringToScan, 0, 5000)
  checks.checkIfString(stringToMatch, 1, 5000)
  checks.checkIntIsBetween(startIndex, 0, len(stringToScan) - 1)
  checks.checkIntIsBetween(endIndex, startIndex, len(stringToScan) - 1)
  firstIdx = stringToScan.find(stringToMatch, startIndex, endIndex + 1)
  while firstIdx != -1:
    if stringIsHtmlDelimited(stringToScan, firstIdx, len(stringToMatch)):
      return True, firstIdx
    lastKeyIdx = firstIdx + len(stringToMatch) - 1
    firstIdx = stringToScan.find(stringToMatch, lastKeyIdx + 1, len(stringToScan))
    continue
  return firstIdx != -1, firstIdx

def getLastValueByFoundEquals(attributeString, startIdx, endIdx):
  """Raises exception for empty string because the index cannot be set properly
\n Return values:
* corrupt: True | False (does not validate what comes after the value, if not found checks only quotes)
* found: True | False (False if corrupt)
* equalIdx, openingQuoteIdx, closingQuoteIdx: -1 if corrupt or not found"""
  corruptResult = (True, False, -1, -1, -1)
  notFoundResult = (False, False, -1, -1, -1)
  corrupt, values = getValuesSafelyByFoundEquals(attributeString, startIdx, endIdx)
  if corrupt:
    return corruptResult
  if not values:
    return notFoundResult
  lastValue = values[-1]
  equalIdx = lastValue[0]
  openingQuoteIdx = lastValue[1]
  closingQuoteIdx = lastValue[2]
  return False, True, equalIdx, openingQuoteIdx, closingQuoteIdx

def getFirstHtmlDelimiterThenSkipWhiteSpaces(string, startIdx, endIdx):
  """Raises exception for empty string because the indexes cannot be set properly.
\nReturn values:\n
* found: True | False (not found if <endIdx> is whitespace)
* idx: -1 if not found"""
  checks.checkIfType(endIdx, int)
  notFoundResult = (False, -1)
  found, firstDelimiterIdx = getFirstHtmlDelimiter(string, startIdx, endIdx)
  if not found:
    return notFoundResult
  found, firstNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(string, firstDelimiterIdx, endIdx)
  if not found:
    return notFoundResult
  return True, firstNonSpaceCharIdx

def getLastHtmlDelimiter(string, startIdx, endIdx):
  """Raises exception for empty string because the indexes cannot be set properly.
\nReturn values:\n
* found: True | False
* idx: -1 if not found"""
  checks.checkIfString(string, startIdx, 5000)
  checks.checkIntIsBetween(endIdx, startIdx, len(string) - 1)
  notFoundResult = (False, -1)
  idx = endIdx
  while idx >= startIdx and not charIsHtmlDelimiter(string[idx]):
    idx -= 1
  if idx == startIdx - 1:
    return notFoundResult
  return True, idx

def getValuesSafelyByFoundEquals(attributeString, startIdx, endIdx):
  """Safe version of "getValuesByFoundEquals" with a bit of performance overhead and extra check for corrupt data.
Index can point anywhere. \n
Raises exception for empty string.
\n Return values:
* corrupt: True | False (does not validate what comes after the value, if not found checks only quotes)
* values: list of (equalIdx, openingQuoteIdx, closingQuoteIdx) triplets"""
  checks.checkIfString(attributeString, 0, 5000)
  checks.checkIntIsBetween(startIdx, 0, len(attributeString) - 1)
  checks.checkIntIsBetween(endIdx, startIdx, len(attributeString) - 1)
  corruptResult = (True, [])
  corrupt, values = getValuesByFoundEquals(attributeString, 0, endIdx)
  if corrupt:
    return corruptResult
  if not values:
    equalFoundAfter, referenceIdxFromRight = stringUtil.find(attributeString, "=", startIdx,
                                                             len(attributeString) - 1,
                                                             notFoundValue=len(attributeString) - 1)
    return isThereAnyQuoteChar(attributeString, 0, referenceIdxFromRight), []
  result = []
  for value in values:
    if startIdx <= value[0] <= endIdx:
      result.append(value)
  return False, result

def getFirstHtmlDelimiter(string, startIdx, endIdx):
  """Raises exception for empty string because the indexes cannot be set properly.
\nReturn values:\n
* found: True | False
* idx: -1 if not found"""
  checks.checkIfString(string, startIdx, 5000)
  checks.checkIntIsBetween(endIdx, startIdx, len(string) - 1)
  notFoundResult = (False, -1)
  idx = startIdx
  while idx <= endIdx and not charIsHtmlDelimiter(string[idx]):
    idx += 1
  if idx == endIdx + 1:
    return notFoundResult
  return True, idx

def isThereAnyQuoteChar(htmlString, startIdx, endIdx):
  """Raises exception for empty string because the index cannot be set properly."""
  checks.checkIfString(htmlString, 0, 4000)
  checks.checkIntIsBetween(startIdx, 0, len(htmlString) - 1)
  checks.checkIntIsBetween(endIdx, startIdx, len(htmlString) - 1)
  if htmlString.find("'", startIdx, endIdx + 1) != -1:
    return True
  return htmlString.find('"', startIdx, endIdx + 1) != -1

def getValuesByFoundEquals(string, startIdx, endIdx):
  """Returns false result if startIdx points within a value which contains equal char. It is the job of higher level
functions to handle this correctly.
\n Return values:
* corrupt: True | False
* values: list of (equalIdx, openingQuoteIdx, closingQuoteIdx) triplets
"""
  possibleValues = getPossibleValuesByFoundEquals(string, startIdx, endIdx)
  result = []
  n = len(possibleValues)
  idx = 0
  while idx < n:
    currentValue = possibleValues[idx]
    if currentValue[1]:
      return True, []
    result.append((currentValue[0], currentValue[2], currentValue[3]))
    closingQuoteIdx = currentValue[3]
    idx += 1
    while idx < n and possibleValues[idx][0] < closingQuoteIdx:
      idx += 1
  return False, result

def stringContainsHtmlDelimiter(string, startIdx, endIdx):
  """Raises exception for empty string because the index cannot be set properly"""
  checks.checkIfString(string, startIdx, 5000)
  checks.checkIntIsBetween(endIdx, startIdx, len(string) - 1)
  for idx in range(startIdx, endIdx + 1):
    if charIsHtmlDelimiter(string[idx]):
      return True
  return False

def getPossibleValuesByFoundEquals(string, startIdx, endIdx):
  """Collects also corrupt and false values (value looking strings within value). It is the job of a higher level
function "getValuesByFoundEquals" to filter them correctly. \n
Raises exception for empty string.\n
\n Return value:
* possibleValues: list of (equalIdx, corrupt, openingQuoteIdx, closingQuoteIdx) quartets"""
  possibleValues = []
  equalIdxsBefore = stringUtil.findAll(string, "=", startIdx, endIdx)
  for equalIdx in equalIdxsBefore:
    corrupt, openingQuoteIdx, closingQuoteIdx, mainQuoteChar = getQuoteIndexesByEqualChar(string, equalIdx)
    possibleValues.append((equalIdx, corrupt, openingQuoteIdx, closingQuoteIdx))
  return possibleValues

def getQuoteIndexesByEqualChar(htmlString, equalCharIdx):
  """Validates adjacent chars near equal and main quotes. \n
There are known false results when the equal char is within a value. Higher level functions will filter them.\n
Raises exception for empty string because the index cannot be set properly.\n
\n Return values:
* corrupt: True | False
* openingQuoteCharIdx, closingQuoteIdx: -1 if corrupt
* quoteChar: empty string if corrupt"""
  corruptResult = (True, -1, -1, "")
  corrupt, openingQuoteCharIdx = validateAdjacentCharsNearEqualChar(htmlString, equalCharIdx)
  if corrupt:
    return corruptResult
  corrupt, closingQuoteIdx, mainQuoteChar = getAndValidateClosingQuote(htmlString, openingQuoteCharIdx)
  if corrupt:
    return corruptResult
  return corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar

def stringIsHtmlDelimited(htmlString, firstCharIdx, lengthOfString):
  """Intended for full word check in case of HTML attribute names and values. \n
Raises exception for empty string because the index cannot be set properly."""
  return htmlDelimitedFromLeft(htmlString, firstCharIdx) and \
              htmlDelimitedFromRight(htmlString, firstCharIdx + lengthOfString - 1)

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
  if not isThereNonDelimiterCharBeforeIdx(htmlString, equalIndex):
    return corruptResult
  found, quoteIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlString, equalIndex + 1, len(htmlString) - 1)
  if not found or (htmlString[quoteIdx] != "'" and htmlString[quoteIdx] != '"'):
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
  if not charIsQuote(mainQuoteChar):
    return corruptResult
  closingQuoteIdx = htmlAttributes.find(mainQuoteChar, openingQuoteCharIdx + 1, len(htmlAttributes))
  if closingQuoteIdx == -1:
    return corruptResult
  if nextNonWhiteSpaceCharIsHtmlDelimiter(htmlAttributes, closingQuoteIdx):
    return corruptResult
  return False, closingQuoteIdx, mainQuoteChar

def htmlDelimitedFromLeft(htmlString, index):
  """Intended for full word check in case of HTML attribute names and values. \n
Raises exception for empty string because the index cannot be set properly."""
  found, previousChar = stringUtil.getPreviousChar(htmlString, index)
  if not found:
    return True
  return charIsHtmlDelimiter(previousChar)

def htmlDelimitedFromRight(htmlString, index):
  """Intended for full word check in case of HTML attribute names and values. \n
Raises exception for empty string because the index cannot be set properly."""
  found, nextChar = stringUtil.getNextChar(htmlString, index)
  if not found:
    return True
  return charIsHtmlDelimiter(nextChar)

def isThereNonDelimiterCharBeforeIdx(htmString, idx):
  """Skips whitespaces."""
  checks.checkIfString(htmString, 0, 4000)
  checks.checkIntIsBetween(idx, 0, len(htmString) - 1)
  while idx >= 1:
    idx -= 1
    currentChar = htmString[idx]
    if currentChar.isspace():
      continue
    if charIsHtmlDelimiter(currentChar):
      return False
    return True
  return False

def nextNonWhiteSpaceCharIsHtmlDelimiter(htmlString, index):
  """Raises exception for empty string because the index cannot be set properly."""
  checks.checkIfString(htmlString, 0, 4000)
  checks.checkIntIsBetween(index, 0, len(htmlString) - 1)
  if index == len(htmlString) - 1:
    return False
  found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlString, index + 1, len(htmlString) - 1)
  return found and charIsHtmlDelimiter(htmlString[idx])

def charIsHtmlDelimiter(ch):
  """HTML attribute delimiters: Whitespace, equal, single-quote, double-quote"""
  checks.checkIfChar(ch)
  return ch.isspace() or ch == "=" or charIsQuote(ch)

def charIsQuote(ch):
  """single or double quote"""
  checks.checkIfChar(ch)
  return ch == '"' or ch == "'"
