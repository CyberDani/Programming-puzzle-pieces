from modules import checks
from modules import stringUtil

def getAttributeIdx(htmlAttributes, key):
  """Returns -1 if attribute not found and for empty string \n
   Does not check for corrupt <htmlAttributes>, e.g.: \"key "invalid, no '=' before"\"\n
   Only the first declaration is taken (if there are multiple) as stated by the standard:
   https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html
   """
  checks.checkIfString(htmlAttributes, 0, 3000)
  checks.checkIfString(key, 0, 60)
  if not htmlAttributes or not key:
    return -1
  # TODO delimitedFind(string, key,  before=[whitespace, "<"], after=[whitespace, "="], 0, len(string))
  firstIdx = stringUtil.beforeWhitespaceDelimitedFind(htmlAttributes, key, 0, len(htmlAttributes))
  while firstIdx != -1 and firstIdx + len(key) < len(htmlAttributes) \
          and not htmlAttributes[firstIdx + len(key)].isspace() and htmlAttributes[firstIdx + len(key)] != "=":
    firstIdx = stringUtil.beforeWhitespaceDelimitedFind(htmlAttributes, key, firstIdx + 1, len(htmlAttributes))
  return firstIdx

def extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(htmlAttributes, key):
  """Does not raise error if htmlAttributes is corrupt, it returns **None**\n
  Returns **None** if there is no attribute value, and an **empty list** if the value is empty or has only whitespaces\n
  Only the first declaration is taken (if there are multiple) as stated by the standard:
  https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
  checks.checkIfString(htmlAttributes, 0, 800)
  checks.checkIfString(key, 1, 30)
  result = []
  firstIdx = getAttributeIdx(htmlAttributes, key)
  if firstIdx == -1:
    return None
  attributeName, attributeValue, startIdx, endIdx = getNextHtmlAttribute(htmlAttributes, firstIdx)
  if attributeValue is None:
    return None
  # TODO getSplitUniqueElements(Char::WHITESPACE)
  values = attributeValue.split()
  for value in values:
    if value not in result:
      result.append(value)
  return result

def getNextHtmlAttribute(attributesString, startIdx):
  """ Raises exception if <startIdx> is not valid. This means that <attributesString> cannot be an empty string as
there is no first index. \n
<attributesString> can be considered corrupt only within the context of the first attribute \n
<startIdx>-1 is not accessed for full word check
\n Return values:
* <attributeName>, <attributeValue> : **None** if no attribute was found or <attributesString> is corrupt
* <attrStartIdx>, <attrEndIdx> : inclusive, **-1** if no attribute was found or attributesString is corrupt"""
  corrupt, attributeName, firstCharIdx, lastCharIdx = getNextHtmlAttributeName(attributesString, startIdx)
  if corrupt or firstCharIdx == -1:
    return None, None, -1, -1
  if lastCharIdx == len(attributesString) - 1:
    return attributeName, None, firstCharIdx, lastCharIdx
  corrupt, firstQuoteIdx, secondQuoteIdx = getNextHtmlAttributeValueIfExists(attributesString, lastCharIdx + 1)
  if corrupt:
    return None, None, -1, -1
  if firstQuoteIdx == -1:
    return attributeName, None, firstCharIdx, lastCharIdx
  return attributeName, attributesString[firstQuoteIdx + 1:secondQuoteIdx], firstCharIdx, secondQuoteIdx

def getListOfHtmlAttributeNames(attributesString):
  """Returns empty list if attribute not found, for empty string and if **<attributesString>** is corrupt \n
     Only the first declaration is taken (if there are multiple) as stated by the standard:
     https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
  checks.checkIfString(attributesString, 0, 1000)
  result = []
  idx = 0
  while idx < len(attributesString):
    attributeName, attributeValue, startIdx, endIdx = getNextHtmlAttribute(attributesString, idx)
    if attributeName is None:
      nextNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, idx, len(attributesString))
      if nextNonSpaceCharIdx != -1:
        return []
      break
    if attributeName not in result:
      result.append(attributeName)
    idx = endIdx + 1
    continue
  return result

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
You DO NOT want to call this before checking for an attribute name first, e.g. calling *getNextHtmlAttributeName()*\n
Return values:\n
* corrupt : True | False
* attributeName: **None** if corrupt or there is no attribute name
* firstCharIdx, lastCharIdx: **-1** if corrupt or there is no attribute name """
  checks.checkIfString(attributesString, 0, 1000)
  checks.checkIntIsBetween(startIdx, 0, len(attributesString) - 1)
  firstNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, startIdx, len(attributesString))
  if firstNonSpaceCharIdx == -1:
    return False, None, -1, -1
  firstNonSpaceChar = attributesString[firstNonSpaceCharIdx]
  if firstNonSpaceChar == "=" or firstNonSpaceChar == "'" or firstNonSpaceChar == "\"":
    return True, None, -1, -1
  currentIdx = firstNonSpaceCharIdx
  attributeName = ""
  while currentIdx < len(attributesString):
    currentChar = attributesString[currentIdx]
    if currentChar.isspace() or currentChar == "=":
      return False, attributeName, firstNonSpaceCharIdx, currentIdx-1
    if currentChar == "'" or currentChar == '"':
      return True, None, -1, -1
    attributeName += currentChar
    currentIdx += 1
  return False, attributeName, firstNonSpaceCharIdx, len(attributesString) - 1
