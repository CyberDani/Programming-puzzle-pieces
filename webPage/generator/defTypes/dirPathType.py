from enum import Enum

from defTypes.dirPathCheckerActionType import DirPathCheckerActionType as dirAction
from defTypes import dirPathChecker

class DirectoryPathType(Enum):
  GIT_REPOSITORY = dirPathChecker.DirectoryPathChecker("", ["README.md", ".git/HEAD"],
                                                       dirAction.ENSURE_PATH_AND_FILES_EXIST)
  INDEX_HTML_LOCATION = dirPathChecker.DirectoryPathChecker("", [], dirAction.ENSURE_PATH_EXISTS_ONLY)
  HTML_BACKUP = dirPathChecker.DirectoryPathChecker("webPage/backup", [], dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_MAIN_GENERATOR = dirPathChecker.DirectoryPathChecker("webPage/generator", ["generator.py"],
                                                              dirAction.ENSURE_PATH_AND_FILES_EXIST)
  PYTHON_GENERATOR_UNIT_TESTS = dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests",
                                                           ["checks_test.py", "argumentParser_test.py"],
                                                            dirAction.ENSURE_PATH_AND_FILES_EXIST)
  HTML_GENERAL_INCLUDES = dirPathChecker.DirectoryPathChecker("webPage/generator/htmlIncludes",
                                                           ["footer.txt", "topNav.txt", "sideNav.txt"],
                                                            dirAction.ENSURE_PATH_AND_FILES_EXIST)
