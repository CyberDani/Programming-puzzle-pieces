import sys

# args excludes the name of the script
def parseArguments(args):
  argsSize = len(args)
  invalidUsage = True
  runUnitTests = False
  backupAndGenerate = False
  if argsSize == 0 or argsSize > 1:
    return invalidUsage, runUnitTests, backupAndGenerate
  firstArg = args[0]
  if firstArg == "-u":
    invalidUsage = False
    runUnitTests = True
    return invalidUsage, runUnitTests, backupAndGenerate
  if firstArg == "-a":
    invalidUsage = False
    runUnitTests = True
    backupAndGenerate = True
    return invalidUsage, runUnitTests, backupAndGenerate  
  return invalidUsage, runUnitTests, backupAndGenerate

def getCommandLineArgs():
  #skip the first argument which contains the name of the script
  return sys.argv[1:]

def displayScriptUsage():
  print("  Script usage: \n")
  print("{0} -u \t Run only the unit tests, nothing else happens".format(sys.argv[0]))
  print("{0} -a \t If all unit tests pass, backup current files and generate new ones".format(sys.argv[0]))
