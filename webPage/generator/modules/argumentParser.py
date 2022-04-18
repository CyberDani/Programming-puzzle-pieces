import sys

from modules import buildType
from modules import checks

# args excludes the name of the script
def parseArguments(args):
  checks.checkIfPureListOfStrings(args)
  argsSize = len(args)
  invalidUsage = True
  runUnitTests = False
  buildOption = buildType.buildType.DO_NOT_BUILD
  if argsSize == 0 or argsSize > 1:
    return invalidUsage, runUnitTests, buildOption
  firstArg = args[0]
  if firstArg == "-u":
    invalidUsage = False
    runUnitTests = True
    return invalidUsage, runUnitTests, buildOption
  if firstArg == "-b":
    invalidUsage = False
    runUnitTests = True
    buildOption = buildType.buildType.BUILD
    return invalidUsage, runUnitTests, buildOption
  if firstArg == "-rb":
    invalidUsage = False
    runUnitTests = True
    buildOption = buildType.buildType.REBUILD
    return invalidUsage, runUnitTests, buildOption
  return invalidUsage, runUnitTests, buildOption

def getCommandLineArgs():
  #skip the first argument which contains the name of the script
  return sys.argv[1:]

def displayScriptUsage():
  print("  Script usage: \n")
  print("{0} -u \t Run only the unit tests, nothing else happens".format(sys.argv[0]))
  print("{0} -b \t If all unit tests pass, backup current files and generate the necessary files".format(sys.argv[0]))
  print("{0} -rb \t If all unit tests pass, backup current files and rebuild all files".format(sys.argv[0]))
