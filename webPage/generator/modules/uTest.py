import unittest

from defTypes import appDecisionType

# Todo: unittest me
def runAndEvaluateUnitTests(stepsCounter):
  print(stepsCounter.getNextMessage('Evaluate unit tests . . .\n'))
  unitTestsResult = collectAndRunUnitTests()
  # r.testsRun, len(r.errors), len(r.failures), r.printErrors()
  if unitTestsResult.wasSuccessful():
    print('\n - ALL UNIT TESTS PASSED -\n')
    return appDecisionType.AppDecisionType.CONTINUE_RUNNING
  print('\n ======= UNIT TEST FAILED ======= ')
  print('\n [!] No operation can be done until all tests pass!')
  return appDecisionType.AppDecisionType.STOP_APP

# Todo: unittest me
def collectAndRunUnitTests():
  suites = unittest.TestSuite()
  loader = unittest.TestLoader()
  # possible arguments: sys.stdout, verbosity=2, failfast=failfast, buffer=true
  runner = unittest.TextTestRunner()
  # suites.addTest(loader.loadTestsFromName('unitTests.unitTestsRunner_test'))
  suites.addTest(loader.discover('./unitTests/', pattern='*_test.py'))
  result = runner.run(suites)
  return result
