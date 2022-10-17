import io
import unittest

from defTypes import appDecisionType
from defTypes import possibleDirPathTypes
from defTypes.dirPathType import DirectoryPathType as Dir

from modules import checks
from modules import filerw
from modules import path

def runAndEvaluateUnitTestsUsingMultipleTempFolderPathsByType(dirPathTypeContainingTests, filePattern,
                                                              tempFolderPathTypes, outputStream = None):
  checks.checkIfAnyType(dirPathTypeContainingTests, possibleDirPathTypes.dirPathTypes)

  # TODO checkIfNonEmptyPureListOfAnyType
  checks.checkIfNonEmptyList(tempFolderPathTypes)
  #checks.checkIfNonEmptyPureListOfType(tempFolderPathTypes, Dir)

  testPath = path.getAbsoluteDirPathEndingWithSlash(dirPathTypeContainingTests)
  tempFolderPaths = []
  for tempDirType in tempFolderPathTypes:
    dirPath = path.getAbsoluteDirPathEndingWithSlash(tempDirType)
    tempFolderPaths.append(dirPath)
  return runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(testPath, filePattern, tempFolderPaths, outputStream)

def runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(dirPathContainingTests, filePattern,
                                                        tempFolderPaths, outputStream = None):
  checks.checkIfNonEmptyPureListOfStrings(tempFolderPaths)
  checks.checkIfString(dirPathContainingTests, 0, 300)
  checks.checkIfString(filePattern, 1, 300)
  checks.checkIfDirectoryPathExists(dirPathContainingTests)
  if outputStream is not None:
    checks.checkIfType(outputStream, io.TextIOWrapper)
  if dirPathContainingTests[-1] != "/":
    dirPathContainingTests += "/"
  for pathToTempFolder in tempFolderPaths:
    filerw.createDirectoryWithParentsByPathIfNotExists(pathToTempFolder)
  lines = []
  result = appDecisionType.AppDecisionType.STOP_APP
  try:
    result, lines = runAndEvaluateUnitTests(dirPathContainingTests, filePattern, outputStream)
  except Exception as e:
    raise e
  finally:
    for pathToTempFolder in tempFolderPaths:
      filerw.deleteNonEmptyDirectoryByPathIfExists(pathToTempFolder)
  return result, lines

def runAndEvaluateUnitTestsUsingSingleTempFolderPath(dirPathContainingTests, filePattern,
                                                     tempFolderPath, outputStream = None):
  return runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(dirPathContainingTests, filePattern,
                                                             [tempFolderPath], outputStream)

def runAndEvaluateUnitTestsUsingMultipleTempFolderNames(dirPathContainingTests, filePattern,
                                                        tempFolderNames, outputStream = None):
  checks.checkIfNonEmptyPureListOfStrings(tempFolderNames)
  for tempFolderName in tempFolderNames:
    checks.checkIfStringDoesNotContainAnySubstringFromList(tempFolderName, 1, 200, ['/'])
  checks.checkIfString(dirPathContainingTests, 0, 300)
  if dirPathContainingTests[-1] != "/":
    dirPathContainingTests += "/"
  tempFolderPaths = []
  for tempFolderName in tempFolderNames:
    pathToTempFolder = dirPathContainingTests + tempFolderName
    tempFolderPaths.append(pathToTempFolder)
  return runAndEvaluateUnitTestsUsingMultipleTempFolderPaths(dirPathContainingTests, filePattern,
                                                             tempFolderPaths, outputStream)

def runAndEvaluateUnitTestsUsingSingleTempFolderName(dirPathContainingTests, filePattern,
                                                     tempFolderName, outputStream = None):
  return runAndEvaluateUnitTestsUsingMultipleTempFolderNames(dirPathContainingTests, filePattern,
                                                             [tempFolderName], outputStream)

def runAndEvaluateUnitTests(dirPath, filePattern, outputStream = None):
  lines = []
  unitTestsResult = collectAndRunUnitTestsByFilePattern(dirPath, filePattern, outputStream)
  if unitTestsResult.wasSuccessful():
    lines.append(' - ALL UNIT TESTS PASSED -\n')
    return appDecisionType.AppDecisionType.CONTINUE_RUNNING, lines
  lines.append('\n ======= UNIT TEST FAILED ======= ')
  lines.append('\n [!] No operation can be done until all tests pass!')
  return appDecisionType.AppDecisionType.STOP_APP, lines

def collectAndRunUnitTestsByFilePattern(dirPath, filePattern, outputStream = None):
  checks.checkIfString(dirPath, 2, 300)
  checks.checkIfString(filePattern, 1, 300)
  if outputStream is not None:
    checks.checkIfType(outputStream, io.TextIOWrapper)
  suites = unittest.TestSuite()
  loader = unittest.TestLoader()
  runner = unittest.TextTestRunner(stream = outputStream, verbosity = 0)
  # suites.addTest(loader.loadTestsFromName('unitTests.unitTestsRunner_test'))
  suites.addTest(loader.discover(dirPath, pattern = filePattern))
  result = runner.run(suites)
  if result.testsRun == 0:
    raise Exception('No tests found to run!')
  return result
