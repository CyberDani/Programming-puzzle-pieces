import os
import unittest

from defTypes import buildType
from defTypes import dbBranchType
from modules import argumentParser
from modules import counter
from modules import htmlBuilder
from modules import webLibs

def backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments():
  args = argumentParser.getCommandLineArgs()
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
    backupAndGenerateNewHtmlOutputFile(stepsCounter, buildOption, dbBranch)
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

# this is the main function being run
def backupAndGenerateNewHtmlOutputFile(stepsCounter, buildOption, dbBranch):
  print(stepsCounter.getNextMessage('Backup all HTML files . . .'))
  backupIndexHtml()
  print(stepsCounter.getNextMessage('Generate HTML files . . .'))
  generateHtmlOutputFile(buildOption, dbBranch)

def backupIndexHtml():
  os.replace("../../index.html", "./backup/index.html")

def generateHtmlOutputFile(buildOption, dbBranch):
  htmlOutputFilePath = "../../index.html"
  htmlFile = open(htmlOutputFilePath, "w")
  writeHtmlContentToFile(htmlFile, buildOption, dbBranch)

def writeHtmlContentToFile(htmlFile, buildOption, dbBranch):
  htmlFile.write("<html>\n")
  htmlFile.write("\t<head>\n")
  writeHtmlHeadContent(htmlFile, buildOption, dbBranch, 2)
  htmlFile.write("\t</head>\n")
  htmlFile.write("\t<body>\n")
  writeHtmlBodyContent(htmlFile, buildOption, dbBranch, 2)
  htmlFile.write("\t</body>\n")
  htmlFile.write("</html>\n")

# <head>
def writeHtmlHeadContent(htmlFile, buildOption, dbBranch, indentDepth):
  tabs = htmlBuilder.getIndentedTab(indentDepth)
  # TODO: see what is worth to add as a configuration
  htmlFile.write(tabs + "<title>Programming puzzle-pieces</title>\n")
  htmlFile.write(tabs + "<link rel=\"icon\" href=\"./webPage/images/favicon.png\">\n")
  # website is optimized for mobile
  htmlFile.write(tabs + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>\n")
  htmlFile.write(tabs + "<style>\n")
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/inlineCssStyle.css", indentDepth + 1)
  htmlFile.write(tabs + "</style>\n")
  webLibs.addFontAwesome_v611(htmlFile, indentDepth)
  webLibs.addJquery_v360(htmlFile, indentDepth)
  webLibs.addGoogleIcons(htmlFile, indentDepth)
  webLibs.addMaterialize_v110_alpha(htmlFile, indentDepth)
  webLibs.addGoogleFont(htmlFile, indentDepth, "?family=Arima+Madurai:wght@500&display=swap")
  webLibs.addJQueryLoadingOverlay_v217(htmlFile, indentDepth)

# <body>
def writeHtmlBodyContent(htmlFile, buildOption, dbBranch, indentDepth):
  tabs = htmlBuilder.getIndentedTab(indentDepth)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/topNav.txt", indentDepth)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/sideNav.txt", indentDepth)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/topQuote.txt", indentDepth)
  htmlBuilder.addNewLineToHtmlOutputFile(htmlFile, indentDepth)
  htmlFile.write(tabs + "<div id=\"webContent\">\n")
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/svgCurve1.txt", indentDepth + 1)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/whatThisProjectOffers.txt", indentDepth + 1)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/svgCurve2.txt", indentDepth + 1)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/personalRecommandation.txt", indentDepth + 1)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/svgCurve3.txt", indentDepth + 1)
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "../pages/mainPage/textBelowCurves.txt", indentDepth + 1)
  htmlFile.write(tabs + "</div>\n")
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/footer.txt", indentDepth)
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, indentDepth, "./webPage/scripts/githubApiScripts.js")
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, indentDepth, "./webPage/scripts/navigationScripts.js")
  htmlFile.write(tabs + "<script>\n")
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/inlineJs.js", indentDepth + 1)
  htmlFile.write(tabs + "</script>\n")


backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments()