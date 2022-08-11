from modules import checks
from modules import stringUtil

def getAttributeIdx(htmlAttributes, key):
  """Returns -1 if attribute not found and for empty string \n
   Only the first declaration is taken (if there are multiple) as stated by the standard:
   https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
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

# TODO this function is too long, make it shorter
def getNextHtmlAttribute(attributesString, startIdx):
  """ Raises exception if <startIdx> is not valid. This means that <attributesString> cannot be an empty string as
there is no first index. \n
<attributesString> can be considered corrupt only within the context of the first attribute \n
<startIdx>-1 is not accessed for full word check
\n Return values:
* <attributeName>, <attributeValue> : **None** if no attribute was found or <attributesString> is corrupt
* <attrStartIdx>, <attrEndIdx> : inclusive, **-1** if no attribute was found or attributesString is corrupt"""
  checks.checkIfString(attributesString, 0, 1000)
  checks.checkIntIsBetween(startIdx, 0, len(attributesString) - 1)
  attrStartIdx = -1
  currentIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, startIdx, len(attributesString))
  if currentIdx == -1:
    return None, None, -1, -1
  currentAttribute = ""
  lastEndIdx = -1
  equalFound = False
  while currentIdx < len(attributesString):
    currentChar = attributesString[currentIdx]
    # Equal
    if currentChar == "=":
      if equalFound or not currentAttribute:
        return None, None, -1, -1
      equalFound = True
    # Apostrophe
    elif currentChar == "'" or currentChar == "\"":
      if not equalFound:
        return None, None, -1, -1
      closingQuoteCharIdx = attributesString.find(currentChar, currentIdx + 1)
      if closingQuoteCharIdx == -1:
        return None, None, -1, -1
      return currentAttribute, attributesString[currentIdx + 1:closingQuoteCharIdx], attrStartIdx, closingQuoteCharIdx
    # Not equal, not apostrophe and not space
    elif not currentChar.isspace():
      if lastEndIdx > 0:
        return currentAttribute, None, attrStartIdx, lastEndIdx
      if not currentAttribute:
        attrStartIdx = currentIdx
      currentAttribute += currentChar
    # First space
    elif currentChar.isspace() and not attributesString[currentIdx - 1].isspace():
      lastEndIdx = currentIdx - 1
    currentIdx += 1
  if equalFound:
    return None, None, -1, -1
  if lastEndIdx > 0:
    return currentAttribute, None, attrStartIdx, lastEndIdx
  return currentAttribute, None, attrStartIdx, len(attributesString) - 1

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
