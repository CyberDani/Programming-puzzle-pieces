import os
import unittest

from defTypes import buildSettings
from defTypes import buildType

from modules import argumentParser
from modules import counter
from modules import htmlBuilder
from modules import htmlBody
from modules import htmlHead

# this is the main function being run
def backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments():
  args = argumentParser.getCommandLineArgs()
  # TODO: write a function which return what to do based on these factors, e.g. STOP_APP, CONTINUE
  invalidUsage, runUnitTests, buildOption, dbBranch = argumentParser.parseArguments(args)
  if invalidUsage:
    print(" [!] Invalid command")
    argumentParser.displayScriptUsage()
    return
  stepsCounter = counter.SimpleCounter(1)
  if runUnitTests:
    print(stepsCounter.getNextMessage('Validate unit tests . . .\n'))
    unitTestsResult = collectAndRunUnitTests()
    # r.testsRun, len(r.errors), len(r.failures), r.printErrors()
    if not unitTestsResult.wasSuccessful():
      print('\n ======= UNIT TEST FAILED ======= ')
      print('\n [!] No operation can be done until all tests pass!')
      return
    else:
      print('\n - ALL UNIT TESTS PASSED -\n')
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

def collectAndRunUnitTests():
  suites = unittest.TestSuite()
  loader = unittest.TestLoader()
  # possible arguments: sys.stdout, verbosity=2, failfast=failfast, buffer=true
  runner = unittest.TextTestRunner()
  # suites.addTest(loader.loadTestsFromName('unitTests.unitTestsRunner_test'))
  suites.addTest(loader.discover('./unitTests/', pattern='*_test.py'))
  result = runner.run(suites)
  return result

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
  # TODO: you did not test chaining
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
  htmlFile = settings.htmlOutputFile
  body.includeFileThenAppendNewLine("./htmlIncludes/topNav.txt") \
      .includeFileThenAppendNewLine("./htmlIncludes/sideNav.txt") \
      .includeFileThenAppendNewLine("./htmlIncludes/topQuote.txt")
  htmlBuilder.addHtmlNewLineToFile(htmlFile, settings.indentDepth)

  body.openHtmlTagThenAppendNewLine("div", "id=\"webContent\"") \
      .includeFileThenAppendNewLine("../pages/mainPage/svgCurve1.txt") \
      .includeFileThenAppendNewLine("../pages/mainPage/whatThisProjectOffers.txt") \
      .includeFileThenAppendNewLine("../pages/mainPage/svgCurve2.txt") \
      .includeFileThenAppendNewLine("../pages/mainPage/personalRecommendation.txt") \
      .includeFileThenAppendNewLine("../pages/mainPage/svgCurve3.txt") \
      .includeFileThenAppendNewLine("../pages/mainPage/textBelowCurves.txt") \
      .closeLastOpenedHtmlTag()

  body.includeFileThenAppendNewLine("./htmlIncludes/footer.txt")
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, settings.indentDepth, "./webPage/scripts/githubApiScripts.js")
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, settings.indentDepth, "./webPage/scripts/navigationScripts.js")
  htmlBuilder.includeFileSurroundedByHtmlTagThenAppendNewLine(htmlFile, "./htmlIncludes/inlineJs.js",
                                                             "script", "", settings.indentDepth)


backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments()
