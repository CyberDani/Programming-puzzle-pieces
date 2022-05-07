import sys

from defTypes import buildType
from defTypes import dbBranchType
from modules import checks
from modules import db

# args excludes the name of the script
def parseArguments(args):
  checks.checkIfPureListOfStrings(args)
  argsSize = len(args)
  invalidUsage = True
  runUnitTests = False
  backup = False
  buildOption = buildType.BuildType.DO_NOT_BUILD
  dbBranch = db.getCurrentDbBranch()
  if argsSize == 0 or argsSize > 2:
    return invalidUsage, runUnitTests, backup, buildOption, dbBranch
  if argsSize == 2:
    secondArg = args[1]
    if secondArg != "db:master" and secondArg != "db:devel":
      return invalidUsage, runUnitTests, backup, buildOption, dbBranch
    if secondArg == "db:master":
      dbBranch = dbBranchType.DbBranchType.MASTER
    elif secondArg == "db:devel":
      dbBranch = dbBranchType.DbBranchType.DEVEL
  firstArg = args[0]
  if firstArg == "-u":
    invalidUsage = False
    runUnitTests = True
    backup = False
    return invalidUsage, runUnitTests, backup, buildOption, dbBranch
  if firstArg == "-b":
    invalidUsage = False
    runUnitTests = True
    backup = True
    buildOption = buildType.BuildType.BUILD
    return invalidUsage, runUnitTests, backup, buildOption, dbBranch
  if firstArg == "-rb":
    invalidUsage = False
    runUnitTests = True
    backup = True
    buildOption = buildType.BuildType.REBUILD
    return invalidUsage, runUnitTests, backup, buildOption, dbBranch
  return invalidUsage, runUnitTests, backup, buildOption, dbBranch

def getCommandLineArgs():
  #skip the first argument which contains the name of the script
  return sys.argv[1:]

def getScriptUsageLines():
  lines = ["  Usage: {0} [command] [db-branch] \n".format(sys.argv[0]),
           "Commands:",
           "\t -u \t Run unit tests, nothing else happens",
           "\t -b \t If all unit tests pass, backup current files and regenerate necessary files",
           "\t -rb \t If all unit tests pass, backup current files and rebuild all files",
           "",
           "DB branch:",
           " [!] Note: if not given it uses db:master for git:master and db:devel otherwise",
           "",
           "\t db:master \t Use the master branch on dbhub.io",
           "\t db:devel \t Use the devel branch on dbhub.io"]
  return lines
