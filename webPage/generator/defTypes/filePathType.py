from enum import Enum

from defTypes import dirPathType
from defTypes import filePathChecker

class FilePathType(Enum):
  HTML_INCLUDE_TOPNAV = filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.HTML_GENERAL_INCLUDES,
                                                  "topNav.txt")
  HTML_INCLUDE_SIDENAV = filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.HTML_GENERAL_INCLUDES,
                                                  "sideNav.txt")
  HTML_INCLUDE_TOPQUOTE = filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.HTML_GENERAL_INCLUDES,
                                                  "topQuote.txt")
  HTML_INCLUDE_FOOTER = filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.HTML_GENERAL_INCLUDES,
                                                  "footer.txt")
  HTML_INCLUDE_INLINEJS = filePathChecker.FilePathChecker(dirPathType.DirectoryRelPathType.HTML_GENERAL_INCLUDES,
                                                  "inlineJs.js")
