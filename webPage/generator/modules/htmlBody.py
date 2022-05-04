from modules import checks
from modules import htmlBuilder

class HtmlBody:
  def __init__(self, htmlFile, indentDepth):
    checks.checkIntIsBetween(indentDepth, 1, 30)
    checks.checkIfFile(htmlFile)
    self.htmlFile = htmlFile
    self.indentDepth = indentDepth
    self.openedHtmlTags = []

  def includeFileThenAppendNewLine(self, filePath):
    htmlBuilder.includeFileThenAppendNewLine(self.htmlFile, filePath, self.indentDepth)
    return self

  def openHtmlTagThenAppendNewLine(self, htmlTag, options = ""):
    tabs = htmlBuilder.getEscapedTabs(self.indentDepth)
    openedHtmlTag = htmlBuilder.getOpenedHtmlTag(htmlTag, options)
    self.htmlFile.write(tabs + openedHtmlTag + "\n")
    self.openedHtmlTags.append(htmlTag)
    self.indentDepth += 1
    return self

  def closeLastOpenedHtmlTag(self):
    if len(self.openedHtmlTags) == 0:
      raise Exception("There is not any opened html tag remained to closed")
    self.indentDepth -= 1
    tabs = htmlBuilder.getEscapedTabs(self.indentDepth)
    lastTag = self.openedHtmlTags[-1]
    closedHtmlTag = tabs + htmlBuilder.getClosedHtmlTag(lastTag)
    self.htmlFile.write(closedHtmlTag + "\n")
    del self.openedHtmlTags[-1]
    return self
