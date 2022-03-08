import os
import sys
import unittest

import argumentParser
import htmlBuilder
import webLibs

def backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments():
  args = argumentParser.getCommandLineArgs()
  invalidUsage, runUnitTests, backupAndGenerate = argumentParser.parseArguments(args)
  if invalidUsage:
    print(" [!] Invalid command")
    argumentParser.displayScriptUsage()
    return
  if runUnitTests:
    print('[1]. Validate unit tests . . .\n')
    unitTestsResult = collectAndRunUnitTests()
    # r.testsRun, len(r.errors), len(r.failures), r.printErrors()
    if not unitTestsResult.wasSuccessful():
      print('\n ======= UNIT TEST FAILED ======= ')
      print('\n [!] No operation can be done until all tests pass!')
    else:
      print('\n - ALL UNIT TESTS PASSED -\n')
  if backupAndGenerate:
    backupAndGenerateNewHtmlOutputFile()
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
def backupAndGenerateNewHtmlOutputFile():
  print('[2]. Backup all files before generating new ones . . .')
  backupIndexHtml()
  print('[3]. Generate HTML files . . .')
  generateHtmlOutputFile()

def backupIndexHtml():
  os.replace("../../index.html", "./backup/index.html")

def generateHtmlOutputFile():
  htmlOutputFilePath = "../../index.html"
  htmlFile = open(htmlOutputFilePath, "w")
  writeHtmlContentToFile(htmlFile)

def writeHtmlContentToFile(htmlFile):
  htmlFile.write("<html>\n")
  htmlFile.write("\t<head>\n")
  writeHtmlHeadContent(htmlFile, 2)
  htmlFile.write("\t</head>\n")
  htmlFile.write("\t<body>\n")
  writeHtmlBodyContent(htmlFile, 2)
  htmlFile.write("\t</body>\n")
  htmlFile.write("</html>\n")

# <head>
def writeHtmlHeadContent(htmlFile, indentDepth):
  tabs = htmlBuilder.getIndentedTab(indentDepth)
  # TODO: see what is worth to add as a configuration
  htmlFile.write(tabs + "<title>Programming puzzle-pieces</title>\n")
  htmlFile.write(tabs + "<link rel=\"icon\" href=\"./webPage/images/favicon.png\">\n")
  # website is optimized for mobile
  htmlFile.write(tabs + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>\n")
  htmlFile.write(tabs + "<style>\n")
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/inlineCssStyle.css", indentDepth + 1)
  htmlFile.write(tabs + "</style>\n")
  webLibs.addFontAwesome(htmlFile, indentDepth)
  webLibs.addJquery(htmlFile, indentDepth)
  webLibs.addGoogleIcons(htmlFile, indentDepth)
  webLibs.addMaterialize(htmlFile, indentDepth)
  webLibs.addGoogleFont(htmlFile, indentDepth, "?family=Arima+Madurai:wght@500&display=swap")
  webLibs.addJQueryLoadingOverlay(htmlFile, indentDepth)

# <body>
def writeHtmlBodyContent(htmlFile, indentDepth):
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
  htmlBuilder.addJsFileAsLink(htmlFile, indentDepth, "./webPage/scripts/githubApiScripts.js")
  htmlBuilder.addJsFileAsLink(htmlFile, indentDepth, "./webPage/scripts/navigationScripts.js")
  htmlFile.write(tabs + "<script>\n")
  htmlBuilder.includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/inlineJs.js", indentDepth + 1)
  htmlFile.write(tabs + "</script>\n")


backupAndGenerateNewHtmlOutputFileIfAllUnitTestsPassDrivenByArguments()