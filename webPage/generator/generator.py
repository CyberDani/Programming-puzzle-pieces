import os
import unittest

from defTypes import buildSettings
from defTypes import buildType
from defTypes import dbBranchType
from modules import argumentParser
from modules import counter
from modules import htmlBuilder
from modules import webLibs

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
  #possible arguments: sys.stdout, verbosity=2, failfast=failfast, buffer=true
  runner = unittest.TextTestRunner()
  #suites.addTest(loader.loadTestsFromName('unitTests.unitTestsRunner_test'))
  suites.addTest(loader.discover('./unitTests/', pattern='*_test.py'))
  result = runner.run(suites)
  return result

def backupFiles(stepsCounter):
  print(stepsCounter.getNextMessage('Backup all HTML files . . .'))
  backupIndexHtml()

def generateNewHtmlOutputFile(settings):
  print(settings.stepsCounter.getNextMessage('Generate HTML files . . .'))
  htmlBuilder.writeIndexHtmlToFile(writeHtmlHeadContent, writeHtmlBodyContent, settings)

def backupIndexHtml():
  os.replace("../../index.html", "./backup/index.html")

# <head>
def writeHtmlHeadContent(settings):
  tabs = htmlBuilder.getEscapedTabs(settings.indentDepth)
  htmlFile = settings.htmlOutputFile
  # TODO: see what is worth to add as a configuration
  htmlBuilder.addTitleToHtmlOutputFile(htmlFile, "Programming puzzle-pieces", settings.indentDepth)
  htmlBuilder.addFaviconToHtmlOutputFile(htmlFile, "./webPage/images/favicon.png", settings.indentDepth)
  htmlBuilder.addMetaScreenOptimizedForMobileToHtmlOutputFile(htmlFile, settings.indentDepth)
  htmlBuilder.includeFileSurroundedByHtmlTagToHtmlOutputFile(htmlFile, "./htmlIncludes/inlineCssStyle.css",
                                                             "style", "", settings.indentDepth)
  webLibs.addFontAwesome_v611(htmlFile, settings.indentDepth)
  webLibs.addJquery_v360(htmlFile, settings.indentDepth)
  webLibs.addGoogleIcons(htmlFile, settings.indentDepth)
  webLibs.addMaterialize_v110_alpha(htmlFile, settings.indentDepth)
  webLibs.addGoogleFont(htmlFile, settings.indentDepth, "?family=Arima+Madurai:wght@500&display=swap")
  webLibs.addJQueryLoadingOverlay_v217(htmlFile, settings.indentDepth)

# <body>
def writeHtmlBodyContent(settings):
  htmlFile = settings.htmlOutputFile
  tabs = htmlBuilder.getEscapedTabs(settings.indentDepth)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/topNav.txt", settings.indentDepth)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/sideNav.txt", settings.indentDepth)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/topQuote.txt", settings.indentDepth)
  htmlBuilder.addNewLineToHtmlOutputFile(htmlFile, settings.indentDepth)
  htmlFile.write(tabs + "<div id=\"webContent\">\n")
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/svgCurve1.txt", settings.indentDepth + 1)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/whatThisProjectOffers.txt", settings.indentDepth + 1)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/svgCurve2.txt", settings.indentDepth + 1)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/personalRecommandation.txt", settings.indentDepth + 1)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/svgCurve3.txt", settings.indentDepth + 1)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/textBelowCurves.txt", settings.indentDepth + 1)
  htmlFile.write(tabs + "</div>\n")
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/footer.txt", settings.indentDepth)
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, settings.indentDepth, "./webPage/scripts/githubApiScripts.js")
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, settings.indentDepth, "./webPage/scripts/navigationScripts.js")
  htmlBuilder.includeFileSurroundedByHtmlTagToHtmlOutputFile(htmlFile, "./htmlIncludes/inlineJs.js",
                                                             "script", "", settings.indentDepth)


backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments()