import sys
import unittest

from defTypes import appDecisionType

from modules import checks

# Todo: unittest me
def runAndEvaluateUnitTests(stepsCounter):
  print(stepsCounter.getNextMessage('Evaluate unit tests . . .\n'))
  unitTestsResult = collectAndRunUnitTestsByFilePattern('./unitTests/', '*_test.py')
  # r.testsRun, len(r.errors), len(r.failures), r.printErrors()
  if unitTestsResult.wasSuccessful():
    print(' - ALL UNIT TESTS PASSED -\n')
    return appDecisionType.AppDecisionType.CONTINUE_RUNNING
  print('\n ======= UNIT TEST FAILED ======= ')
  print('\n [!] No operation can be done until all tests pass!')
  return appDecisionType.AppDecisionType.STOP_APP

def collectAndRunUnitTestsByFilePattern(relativeDirPath, filePattern, outputStream = None):
  checks.checkIfString(relativeDirPath, 2, 300)
  checks.checkIfString(filePattern, 1, 300)
  suites = unittest.TestSuite()
  loader = unittest.TestLoader()
  runner = unittest.TextTestRunner(stream = outputStream, verbosity = 0)
  # suites.addTest(loader.loadTestsFromName('unitTests.unitTestsRunner_test'))
  suites.addTest(loader.discover(relativeDirPath, pattern = filePattern))
  result = runner.run(suites)
  return result
