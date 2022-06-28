from enum import Enum

from defTypes import dirPathType
from defTypes.filePathCheckerActionType import FilePathCheckerActionType as fileAction
from defTypes import filePathChecker

class FilePathType(Enum):
  FOR_TEST_TEXTFILE1 = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS_TEMP1,
                                                    "test1.txt", fileAction.DONT_CHECK_FILE_EXISTENCE)
  FOR_TEST_TEXTFILE2 = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS_TEMP1,
                                                    "test2.txt", fileAction.DONT_CHECK_FILE_EXISTENCE)
  FOR_TEST_TEXTFILE3 = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.PYTHON_GENERATOR_UNIT_TESTS_TEMP1,
                                                    "test3.txt", fileAction.DONT_CHECK_FILE_EXISTENCE)
  HTML_INCLUDE_TOPNAV = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES,
                                                    "topNav.txt", fileAction.ENSURE_FILE_EXISTS)
  HTML_INCLUDE_SIDENAV = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES,
                                                    "sideNav.txt", fileAction.ENSURE_FILE_EXISTS)
  HTML_INCLUDE_TOPQUOTE = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES,
                                                    "topQuote.txt", fileAction.ENSURE_FILE_EXISTS)
  HTML_INCLUDE_FOOTER = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES,
                                                    "footer.txt", fileAction.ENSURE_FILE_EXISTS)
  HTML_INCLUDE_INLINEJS = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.HTML_GENERAL_INCLUDES,
                                                    "inlineJs.js", fileAction.ENSURE_FILE_EXISTS)
  INDEX_HTML_MAIN = filePathChecker.FilePathChecker(dirPathType.DirectoryPathType.INDEX_HTML_LOCATION,
                                                    "index.html", fileAction.DONT_CHECK_FILE_EXISTENCE)
