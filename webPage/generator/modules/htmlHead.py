from modules import checks
from modules import htmlBuilder
from modules.paths import path
from modules.paths.definitions.dirPathTypeForProd import DirectoryPathTypeForProd as dir
from modules import webLibs

class HtmlHead:
  def __init__(self, htmlFile, indentDepth):
    checks.checkIntIsBetween(indentDepth, 1, 30)
    checks.checkIfFile(htmlFile)
    self.htmlFile = htmlFile
    self.indentDepth = indentDepth
    self.titleSet = False
    self.faviconSet = False
    self.metaScreenOptimizedForMobile = False
    self.fontAwesomeLibAdded = False
    self.jQueryLibAdded = False
    self.googleIconsLibAdded = False
    self.materializeLibAdded = False
    self.googleFontLibAdded = False
    self.jQueryLoadingOverlayLibAdded = False

  def setTitle(self, title):
    if self.titleSet:
      raise Exception("A title is already set, will not add '{}'.".format(title))
    self.titleSet = True
    htmlBuilder.addTitleToHtmlOutputFile(self.htmlFile, title, self.indentDepth)
    return self

  def setFavicon(self, favIconPath):
    if self.faviconSet:
      raise Exception("A favicon is already set, will not add '{}'.".format(favIconPath))
    self.faviconSet = True
    htmlBuilder.addFaviconToHtmlOutputFile(self.htmlFile, favIconPath, self.indentDepth)
    return self

  def setFaviconByType(self, favIconPathType):
    favIconPath = path.getRelativeFilePathToDirectory(favIconPathType, dir.INDEX_HTML_LOCATION)
    return self.setFavicon(favIconPath)

  def setMetaScreenOptimizedForMobile(self):
    if self.metaScreenOptimizedForMobile:
      raise Exception("A meta tag for optimizing screen for mobile had already been added")
    self.metaScreenOptimizedForMobile = True
    htmlBuilder.addMetaScreenOptimizedForMobileToHtmlOutputFile(self.htmlFile, self.indentDepth)
    return self

  def includeFileAsInlineCSS(self, filePath):
    htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(self.htmlFile, filePath,
                                                                "style", "", self.indentDepth)
    return self

  def includeFileByTypeAsInlineCSS(self, filePathType):
    filePath = path.getAbsoluteFilePath(filePathType)
    return self.includeFileAsInlineCSS(filePath)

  def addFontAwesome_v611(self):
    if self.fontAwesomeLibAdded:
      raise Exception("Fontawesome library had already been added")
    self.fontAwesomeLibAdded = True
    webLibs.addFontAwesome_v611(self.htmlFile, self.indentDepth)
    return self

  def addJquery_v360(self):
    if self.jQueryLibAdded:
      raise Exception("jQuery library had already been added")
    self.jQueryLibAdded = True
    webLibs.addJquery_v360(self.htmlFile, self.indentDepth)
    return self

  def addGoogleIcons(self):
    if self.googleIconsLibAdded:
      raise Exception("Google Icons library had already been added")
    self.googleIconsLibAdded = True
    webLibs.addGoogleIcons(self.htmlFile, self.indentDepth)
    return self

  def addMaterialize_v110_alpha(self):
    if self.materializeLibAdded:
      raise Exception("Materialize library had already been added")
    self.materializeLibAdded = True
    webLibs.addMaterialize_v110_alpha(self.htmlFile, self.indentDepth)
    return self

  def addGoogleFont(self, fontString):
    if self.googleFontLibAdded:
      raise Exception("Google font library had already been added")
    self.googleFontLibAdded = True
    webLibs.addGoogleFont(self.htmlFile, self.indentDepth, fontString)
    return self

  def addJQueryLoadingOverlay_v217(self):
    if self.jQueryLoadingOverlayLibAdded:
      raise Exception("jQuery Loading Overlay library had already been added")
    self.jQueryLoadingOverlayLibAdded = True
    webLibs.addJQueryLoadingOverlay_v217(self.htmlFile, self.indentDepth)
    return self
