from enum import Enum

from modules.paths.dirPathCheckerActionType import DirPathCheckerActionType as dirAction
from modules.paths.dirPathChecker import DirectoryPathChecker
from defTypes import pppConfig as config

class DirectoryPathTypeForProd(Enum):
  # FOR PRODUCTION CODE
  PYTHON_GENERATOR_UNIT_TESTS = DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS,
                                                     ["htmlBuilder_test.py", "argumentParser_test.py"],
                                                     dirAction.ENSURE_DIR_AND_FILES_EXIST)
  PYTHON_GENERATOR_UNIT_TESTS_TEMP1 = DirectoryPathChecker(
            config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME, [], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_TEMP2 = DirectoryPathChecker(
            config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP2_FOLDER_NAME, [], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PROJECT_ROOT = DirectoryPathChecker("", ["libs.txt"], dirAction.ENSURE_DIR_AND_FILES_EXIST)
  INDEX_HTML_LOCATION = DirectoryPathChecker("", [], dirAction.ENSURE_DIR_EXISTS_ONLY)
  HTML_BACKUP = DirectoryPathChecker("webPage/backup", [], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  HTML_SCRIPTS = DirectoryPathChecker("webPage/scripts", ["githubApiScripts.js", "navigationScripts.js"],
                                      dirAction.ENSURE_DIR_AND_FILES_EXIST)
  PYTHON_MAIN_GENERATOR = DirectoryPathChecker(config.PATH_FROM_ROOT_TO_PY_GENERATOR, ["generator.py"],
                                               dirAction.ENSURE_DIR_AND_FILES_EXIST)
  HTML_IMAGES = DirectoryPathChecker("webPage/images", ["favicon.png"], dirAction.ENSURE_DIR_AND_FILES_EXIST)
  HTML_GENERAL_INCLUDES = DirectoryPathChecker("webPage/generator/htmlIncludes",
                                               ["footer.txt", "topNav.txt", "sideNav.txt"],
                                                dirAction.ENSURE_DIR_AND_FILES_EXIST)
  HTML_PAGES_MAIN = DirectoryPathChecker("webPage/pages/mainPage", ["svgCurve1.txt", "svgCurve2.txt", "svgCurve3.txt"],
                                         dirAction.ENSURE_DIR_AND_FILES_EXIST)
  GENERATOR_CACHE = DirectoryPathChecker(config.PATH_FROM_ROOT_TO_PY_GENERATOR + "cache", [],
                                         dirAction.CREATE_DIR_IF_NOT_EXISTS)
