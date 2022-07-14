from enum import Enum

from defTypes.dirPathCheckerActionType import DirPathCheckerActionType as dirAction
from defTypes.dirPathChecker import DirectoryPathChecker
from defTypes import pppConfig as config


class DirectoryPathType(Enum):
  GIT_REPOSITORY = DirectoryPathChecker("", ["README.md", ".git/HEAD"], dirAction.ENSURE_PATH_AND_FILES_EXIST)
  INDEX_HTML_LOCATION = DirectoryPathChecker("", [], dirAction.ENSURE_PATH_EXISTS_ONLY)
  HTML_BACKUP = DirectoryPathChecker("webPage/backup", [], dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  HTML_SCRIPTS = DirectoryPathChecker("webPage/scripts", ["githubApiScripts.js", "navigationScripts.js"],
                                      dirAction.ENSURE_PATH_AND_FILES_EXIST)
  PYTHON_MAIN_GENERATOR = DirectoryPathChecker(config.PATH_FROM_REPO_TO_PY_GENERATOR, ["generator.py"],
                                               dirAction.ENSURE_PATH_AND_FILES_EXIST)
  PYTHON_GENERATOR_UNIT_TESTS = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UNIT_TESTS,
                                                     ["checks_test.py", "argumentParser_test.py"],
                                                     dirAction.ENSURE_PATH_AND_FILES_EXIST)
  PYTHON_GENERATOR_UNIT_TESTS_TEMP1 = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME,
                                                           [], dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_TEMP2 = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UNIT_TESTS + config.UT_TEMP2_FOLDER_NAME,
                                                           [], dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_TEST1 = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UNIT_TESTS + "testDir1", [],
                                                           dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2 = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UNIT_TESTS
                                                                  + "nestedTest11/nestedTest12",
                                                               [], dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  NON_EXISTING_DIRECTORY = DirectoryPathChecker("webPage/generator/nonExistingFolder", [],
                                                dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS = DirectoryPathChecker("webPage/generator/unitTests4unitTests",
                                                         ["fail_x_group1.py", "pass_x_group1.py",
                                                          "pass_x_group2.py", "test_tempDir.py"],
                                                          dirAction.ENSURE_PATH_AND_FILES_EXIST)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR = DirectoryPathChecker("webPage/generator/unitTests4unitTests/tempDir", [],
                                                                dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1 = DirectoryPathChecker("webPage/generator/unitTests4unitTests/tempDir1", [],
                                                                 dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2 = DirectoryPathChecker("webPage/generator/unitTests4unitTests/tempDir2", [],
                                                                 dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34 = DirectoryPathChecker("webPage/generator/unitTests4unitTests/tempDir34", [],
                                                                  dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  HTML_IMAGES = DirectoryPathChecker("webPage/images", ["favicon.png"], dirAction.ENSURE_PATH_AND_FILES_EXIST)
  HTML_GENERAL_INCLUDES = DirectoryPathChecker("webPage/generator/htmlIncludes",
                                               ["footer.txt", "topNav.txt", "sideNav.txt"],
                                                dirAction.ENSURE_PATH_AND_FILES_EXIST)
  HTML_PAGES_MAIN = DirectoryPathChecker("webPage/pages/mainPage", ["svgCurve1.txt", "svgCurve2.txt", "svgCurve3.txt"],
                                         dirAction.ENSURE_PATH_AND_FILES_EXIST)
