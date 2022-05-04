from modules import checks
from modules import htmlBuilder

class HtmlBody:
  def __init__(self, htmlFile, indentDepth):
    checks.checkIntIsBetween(indentDepth, 1, 30)
    checks.checkIfFile(htmlFile)
    self.htmlFile = htmlFile
    self.indentDepth = indentDepth

  def includeFileThenAppendNewLine(self, filePath):
    htmlBuilder.includeFileThenAppendNewLine(self.htmlFile, filePath, self.indentDepth)
    return self
