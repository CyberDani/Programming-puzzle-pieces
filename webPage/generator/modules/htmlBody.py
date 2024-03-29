from modules import checks
from modules import htmlBuilder
from modules.paths import path
from modules.paths.definitions.dirPathTypeForProd import DirectoryPathTypeForProd as dir

class HtmlBody:
  def __init__(self, htmlFile, indentDepth):
    checks.checkIntIsBetween(indentDepth, 1, 30)
    checks.checkIfFile(htmlFile)
    self.htmlFile = htmlFile
    self.indentDepth = indentDepth
    self.openedHtmlTags = []

  def includeFileByTypeThenAppendNewLine(self, filePathType):
    filePath = path.getAbsoluteFilePath(filePathType)
    return self.includeFileThenAppendNewLine(filePath)

  def includeFileThenAppendNewLine(self, filePath):
    htmlBuilder.includeFileThenAppendNewLine(self.htmlFile, filePath, self.indentDepth)
    return self

  def openHtmlTagThenAppendNewLine(self, htmlTag, attributes =""):
    """Includes jQuery-like selectors."""
    tabs = htmlBuilder.getEscapedTabs(self.indentDepth)
    openedHtmlTag = htmlBuilder.getOpenedHtmlTag(htmlTag, attributes)
    self.htmlFile.write(tabs + openedHtmlTag + "\n")
    self.openedHtmlTags.append(htmlTag)
    self.indentDepth += 1
    return self

  def closeLastOpenedHtmlTag(self):
    if len(self.openedHtmlTags) == 0:
      raise Exception("There is not any opened html tag remained to close")
    self.indentDepth -= 1
    tabs = htmlBuilder.getEscapedTabs(self.indentDepth)
    lastTag = self.openedHtmlTags[-1]
    closedHtmlTag = tabs + htmlBuilder.getClosedHtmlTag(lastTag)
    self.htmlFile.write(closedHtmlTag + "\n")
    del self.openedHtmlTags[-1]
    return self

  def addHtmlNewLineThenAppendNewLine(self, nrOfNewLines = 1):
    htmlBuilder.addHtmlNewLineToFile(self.htmlFile, self.indentDepth, nrOfNewLines)
    return self

  def addJsScriptSrcThenAppendNewLine(self, url, integrity=None, crossorigin=None, referrerpolicy=None):
    htmlBuilder.addJsScriptSrcToHtmlOutputFile(self.htmlFile, self.indentDepth, url,
                                               integrity, crossorigin, referrerpolicy)
    return self

  def addJsScriptSrcByTypeThenAppendNewLine(self, filePathType, integrity=None, crossorigin=None, referrerpolicy=None):
    localRelUrl = path.getRelativeFilePathToDirectory(filePathType, dir.INDEX_HTML_LOCATION)
    return self.addJsScriptSrcThenAppendNewLine(localRelUrl, integrity, crossorigin, referrerpolicy)

  def includeFileAsInlineJs(self, filePath):
    htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(self.htmlFile, filePath,
                                                                "script", "", self.indentDepth)
    return self

  def includeFileByTypeAsInlineJs(self, filePathType):
    filePath = path.getAbsoluteFilePath(filePathType)
    return self.includeFileAsInlineJs(filePath)
