import os
import sys

from defTypes import appDecisionType
from defTypes import buildSettings
from defTypes import buildType
from defTypes.dirPathType import DirectoryPathType as Dir
from defTypes.filePathType import FilePathType as File

from modules import argumentParser
from modules import counter
from modules import filerw
from modules import htmlBody
from modules import htmlBuilder
from modules import htmlHead
from modules import path
from modules import uTest

# this is the main function being run
def backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments():
  args = argumentParser.getCommandLineArgs()
  invalidUsage, runUnitTests, backup, buildOption, dbBranch = argumentParser.parseArguments(args)
  handleInvalidUsageIfRequired(invalidUsage)
  stepsCounter = counter.SimpleCounter(1)
  handleUnitTestsIfRequired(runUnitTests, stepsCounter)
  handleBackupIfRequired(backup, stepsCounter)
  handleBuildingIfRequired(buildOption, stepsCounter, dbBranch)

def handleInvalidUsageIfRequired(invalidUsage):
  if not invalidUsage:
    return
  print(" [!] Invalid command")
  print(*argumentParser.getScriptUsageLines(), sep="\n")
  sys.exit()

def handleUnitTestsIfRequired(runUnitTests, stepsCounter):
  if not runUnitTests:
    print(stepsCounter.getNextMessage('Skip unit tests'))
    return
  print(stepsCounter.getNextMessage('Evaluate unit tests . . .\n'))
  result, lines = uTest.runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(
                                                                        Dir.PYTHON_GENERATOR_UNIT_TESTS, '*_test.py',
                                                                        [Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1,
                                                                            Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP2])
  print(*lines, sep="\n")
  if result == appDecisionType.AppDecisionType.STOP_APP:
    sys.exit()

def handleBackupIfRequired(backup, stepsCounter):
  if not backup:
    print(stepsCounter.getNextMessage('Skip making backups'))
    return
  print(stepsCounter.getNextMessage('Backup current files . . .'))
  backupFiles()

def handleBuildingIfRequired(buildOption, stepsCounter, dbBranch):
  if buildOption == buildType.BuildType.DO_NOT_BUILD:
    print(stepsCounter.getNextMessage('Skip building'))
    return
  htmlOutputFilePath = path.getAbsoluteFilePath(File.INDEX_HTML_MAIN)
  htmlFile = open(htmlOutputFilePath, "w")
  settings = buildSettings.BuildSettings(htmlOutputFile=htmlFile,
                                         buildOption=buildOption,
                                         dbBranch=dbBranch,
                                         stepsCounter=stepsCounter,
                                         indentDepth=2)
  generateNewHtmlOutputFile(settings)


def generateNewHtmlOutputFile(settings):
  print(settings.stepsCounter.getNextMessage('Generate HTML files . . .'))
  htmlBuilder.buildIndexHtmlFile(writeHtmlHeadContent, writeHtmlBodyContent, settings)

# <head>
def writeHtmlHeadContent(settings):
  head = htmlHead.HtmlHead(settings.htmlOutputFile, settings.indentDepth)
  head.setTitle("Programming puzzle-pieces") \
      .setFavicon("./webPage/images/favicon.png") \
      .setMetaScreenOptimizedForMobile() \
      .includeFileAsInlineCSS("./htmlIncludes/inlineCssStyle.css")
  head.addFontAwesome_v611() \
      .addJquery_v360() \
      .addGoogleIcons() \
      .addMaterialize_v110_alpha() \
      .addGoogleFont("?family=Arima+Madurai:wght@500&display=swap") \
      .addJQueryLoadingOverlay_v217()

# <body>
def writeHtmlBodyContent(settings):
  body = htmlBody.HtmlBody(settings.htmlOutputFile, settings.indentDepth)
  body.includeFileThenAppendNewLine("./htmlIncludes/topNav.txt") \
      .includeFileThenAppendNewLine("./htmlIncludes/sideNav.txt") \
      .includeFileThenAppendNewLine("./htmlIncludes/topQuote.txt") \
      .addHtmlNewLineThenAppendNewLine(1)
  body.openHtmlTagThenAppendNewLine("div", "id=\"webContent\"") \
      .includeFileThenAppendNewLine("../pages/mainPage/svgCurve1.txt") \
      .includeFileThenAppendNewLine("../pages/mainPage/whatThisProjectOffers.txt") \
      .includeFileThenAppendNewLine("../pages/mainPage/svgCurve2.txt") \
      .includeFileThenAppendNewLine("../pages/mainPage/personalRecommendation.txt") \
      .includeFileThenAppendNewLine("../pages/mainPage/svgCurve3.txt") \
      .includeFileThenAppendNewLine("../pages/mainPage/textBelowCurves.txt") \
      .closeLastOpenedHtmlTag()  # div#webContent
  body.includeFileThenAppendNewLine("./htmlIncludes/footer.txt") \
      .addJsScriptSrcThenAppendNewLine("./webPage/scripts/githubApiScripts.js") \
      .addJsScriptSrcThenAppendNewLine("./webPage/scripts/navigationScripts.js") \
      .includeFileAsInlineJs("./htmlIncludes/inlineJs.js")

def backupFiles():
  filerw.moveFileIfExistsIntoAlreadyExistingOrNewlyCreatedDirectory(File.INDEX_HTML_MAIN, Dir.HTML_BACKUP)

backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments()
