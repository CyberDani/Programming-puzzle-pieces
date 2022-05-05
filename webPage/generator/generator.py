import os
import sys

from defTypes import appDecisionType
from defTypes import buildSettings
from defTypes import buildType

from modules import argumentParser
from modules import counter
from modules import htmlBuilder
from modules import htmlBody
from modules import htmlHead
from modules import uTest

# this is the main function being run
def backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments():
  args = argumentParser.getCommandLineArgs()
  invalidUsage, runUnitTests, buildOption, dbBranch = argumentParser.parseArguments(args)
  if invalidUsage:
    print(" [!] Invalid command")
    argumentParser.displayScriptUsage()
    return
  stepsCounter = counter.SimpleCounter(1)
  if runUnitTests:
    result = uTest.runAndEvaluateUnitTests(stepsCounter)
    if result == appDecisionType.AppDecisionType.STOP_APP:
      sys.exit()
  if buildOption != buildType.BuildType.DO_NOT_BUILD:
    backupFiles(stepsCounter)
    htmlOutputFilePath = "../../index.html"
    htmlFile = open(htmlOutputFilePath, "w")
    settings = buildSettings.BuildSettings(htmlOutputFile=htmlFile,
                                           buildOption=buildOption,
                                           dbBranch=dbBranch,
                                           stepsCounter=stepsCounter,
                                           indentDepth=2)
    generateNewHtmlOutputFile(settings)
  else:
    print("No backup or generation was made")

def backupFiles(stepsCounter):
  print(stepsCounter.getNextMessage('Backup all HTML files . . .'))
  backupIndexHtml()

def generateNewHtmlOutputFile(settings):
  print(settings.stepsCounter.getNextMessage('Generate HTML files . . .'))
  htmlBuilder.buildIndexHtmlFile(writeHtmlHeadContent, writeHtmlBodyContent, settings)

def backupIndexHtml():
  os.replace("../../index.html", "./backup/index.html")

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


backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments()
