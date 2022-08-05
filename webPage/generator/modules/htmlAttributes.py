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

# TODO this function is too long, make it shorter
def extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(htmlAttributes, key):
  """Does not raise error if htmlAttributes is corrupt, it returns an empty list\n
  Only the first declaration is taken (if there are multiple) as stated by the standard:
  https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
  checks.checkIfString(htmlAttributes, 0, 800)
  checks.checkIfString(key, 1, 30)
  result = []
  firstIdx = getAttributeIdx(htmlAttributes, key)
  if firstIdx == -1:
    return result
  startIdx = firstIdx + len(key)
  if startIdx >= len(htmlAttributes):
    return result
  nonSpaceIdxAfterKey = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlAttributes, startIdx, len(htmlAttributes))
  if nonSpaceIdxAfterKey == -1:
    return result
  firstCharAfterAttribute = htmlAttributes[nonSpaceIdxAfterKey]
  if firstCharAfterAttribute != '=':
    return result
  startIdx = nonSpaceIdxAfterKey + 1
  if len(htmlAttributes) == startIdx:
    return result
  firstNonSpaceIdxAfterEqual = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlAttributes, startIdx, len(htmlAttributes))
  if firstNonSpaceIdxAfterEqual == -1:
    return result
  firstCharAfterEqual = htmlAttributes[firstNonSpaceIdxAfterEqual]
  if firstCharAfterEqual != "'" and firstCharAfterEqual != "\"":
    return result
  startingQuoteIdx = firstNonSpaceIdxAfterEqual
  quoteCharUsed = firstCharAfterEqual
  startIdx = firstNonSpaceIdxAfterEqual + 1
  if len(htmlAttributes) == startIdx:
    return result
  closingQuotePos = htmlAttributes.find(quoteCharUsed, startIdx)
  if closingQuotePos == -1:
    return result
  if closingQuotePos == startIdx:
    return result
  valueIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(htmlAttributes, startIdx, closingQuotePos)
  if valueIdx == -1:
    return result
  # TODO getFirstWhiteSpaceCharIdx
  # TODO getFirstCharIdx(string, skip=[WhiteSpace, ","], find=[AnyChar, "="])
  attrValues = htmlAttributes[startingQuoteIdx + 1 : closingQuotePos]
  values = attrValues.split()
  for value in values:
    if value not in result:
      result.append(value)
  return result

# TODO this function is too long, make it shorter
def getListOfHtmlAttributes(attributesString):
  """Returns empty list if attribute not found, for empty string and if **<attributesString>** is corrupt \n
     Only the first declaration is taken (if there are multiple) as stated by the standard:
     https://stackoverflow.com/questions/9512330/multiple-class-attributes-in-html"""
  checks.checkIfString(attributesString, 0, 1000)
  result = []
  currentAttribute = ""
  idx = 0
  while idx < len(attributesString):
    currentChar = attributesString[idx]
    if currentChar.isspace() or currentChar == "=":
      if currentAttribute and currentChar.isspace():
        if idx + 1 == len(attributesString) or \
          (not attributesString[idx + 1].isspace() and attributesString[idx + 1] != "="):
          if currentAttribute not in result:
            result.append(currentAttribute)
          currentAttribute = ""
        idx += 1
        continue
      elif currentAttribute and currentChar == "=":
        if idx == len(attributesString) - 1:
          return []
        nextNonSpaceCharIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(attributesString, idx + 1, len(attributesString))
        if nextNonSpaceCharIdx == -1:
          return []
        nextNonSpaceChar = attributesString[nextNonSpaceCharIdx]
        if nextNonSpaceChar != "\"" and nextNonSpaceChar != "'":
          return []
        quoteCharUsed = nextNonSpaceChar
        closingQuoteIdx = attributesString.find(quoteCharUsed, nextNonSpaceCharIdx + 1)
        if closingQuoteIdx == -1:
          return []
        if currentAttribute not in result:
          result.append(currentAttribute)
        currentAttribute = ""
        idx = closingQuoteIdx + 1
        continue
      elif not currentAttribute and currentChar.isspace():
        idx += 1
        continue
      return []
    else:
      currentAttribute += currentChar
      idx += 1
      continue
  if currentAttribute and currentAttribute not in result:
    result.append(currentAttribute)
  return result
