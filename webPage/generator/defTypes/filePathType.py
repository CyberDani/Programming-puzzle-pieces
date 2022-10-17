from enum import Enum

from defTypes.dirPathType import DirectoryPathType as Dir
from defTypes.filePathCheckerActionType import FilePathCheckerActionType as fileAction
from defTypes.filePathChecker import FilePathChecker

class FilePathType(Enum):
  # FOR PRODUCTION CODE
  HTML_FAVICON = FilePathChecker(Dir.HTML_IMAGES, "favicon.png", fileAction.ENSURE_FILE_EXISTS)
  HTML_INCLUDE_TOPNAV = FilePathChecker(Dir.HTML_GENERAL_INCLUDES, "topNav.txt", fileAction.ENSURE_FILE_EXISTS)
  HTML_INCLUDE_SIDENAV = FilePathChecker(Dir.HTML_GENERAL_INCLUDES, "sideNav.txt", fileAction.ENSURE_FILE_EXISTS)
  HTML_INCLUDE_TOPQUOTE = FilePathChecker(Dir.HTML_GENERAL_INCLUDES, "topQuote.txt", fileAction.ENSURE_FILE_EXISTS)
  HTML_INCLUDE_FOOTER = FilePathChecker(Dir.HTML_GENERAL_INCLUDES, "footer.txt", fileAction.ENSURE_FILE_EXISTS)
  HTML_INCLUDE_INLINEJS = FilePathChecker(Dir.HTML_GENERAL_INCLUDES, "inlineJs.js", fileAction.ENSURE_FILE_EXISTS)
  HTML_INCLUDE_INLINECSS = FilePathChecker(Dir.HTML_GENERAL_INCLUDES, "inlineCssStyle.css",
                                           fileAction.ENSURE_FILE_EXISTS)
  INDEX_HTML_MAIN = FilePathChecker(Dir.INDEX_HTML_LOCATION, "index.html", fileAction.DONT_CHECK_FILE_EXISTENCE)
  MAIN_PAGE_SVG_CURVE1 = FilePathChecker(Dir.HTML_PAGES_MAIN, "svgCurve1.txt", fileAction.ENSURE_FILE_EXISTS)
  MAIN_PAGE_SVG_CURVE2 = FilePathChecker(Dir.HTML_PAGES_MAIN, "svgCurve2.txt", fileAction.ENSURE_FILE_EXISTS)
  MAIN_PAGE_SVG_CURVE3 = FilePathChecker(Dir.HTML_PAGES_MAIN, "svgCurve3.txt", fileAction.ENSURE_FILE_EXISTS)
  MAIN_PAGE_WHAT_PROJECT_OFFERS = FilePathChecker(Dir.HTML_PAGES_MAIN, "whatThisProjectOffers.txt",
                                                  fileAction.ENSURE_FILE_EXISTS)
  MAIN_PAGE_PERSONAL_RECOMMENDATION = FilePathChecker(Dir.HTML_PAGES_MAIN, "personalRecommendation.txt",
                                                      fileAction.ENSURE_FILE_EXISTS)
  MAIN_PAGE_BELOW_CURVE3 = FilePathChecker(Dir.HTML_PAGES_MAIN, "textBelowCurves.txt", fileAction.ENSURE_FILE_EXISTS)
  SCRIPT_GITHUB_API = FilePathChecker(Dir.HTML_SCRIPTS, "githubApiScripts.js", fileAction.ENSURE_FILE_EXISTS)
  SCRIPT_NAVIGATION = FilePathChecker(Dir.HTML_SCRIPTS, "navigationScripts.js", fileAction.ENSURE_FILE_EXISTS)
