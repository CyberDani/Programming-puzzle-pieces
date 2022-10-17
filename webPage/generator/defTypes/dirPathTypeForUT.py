from enum import Enum

from defTypes.dirPathCheckerActionType import DirPathCheckerActionType as dirAction
from defTypes.dirPathChecker import DirectoryPathChecker
from defTypes import pppConfig as config

class DirectoryPathTypeForUT(Enum):
  # FOR UNIT TESTS
  PYTHON_GENERATOR_UNIT_TESTS = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UNIT_TESTS,
                                                     ["checks_test.py", "argumentParser_test.py"],
                                                     dirAction.ENSURE_DIR_AND_FILES_EXIST)
  PYTHON_GENERATOR_UNIT_TESTS_TEMP1 = DirectoryPathChecker(
                                                      config.PATH_FROM_REPO_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME,
                                                      [], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_TEMP2 = DirectoryPathChecker(
                                                      config.PATH_FROM_REPO_TO_UNIT_TESTS + config.UT_TEMP2_FOLDER_NAME,
                                                      [], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_TEST1 = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UNIT_TESTS + "testDir1", [],
                                                           dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2 = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UNIT_TESTS
                                                               + "nestedTest11/nestedTest12",
                                                               [], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UT4UT,
                                                        ["fail_x_group1.py", "pass_x_group1.py",
                                                         "pass_x_group2.py", "test_tempDir.py"],
                                                        dirAction.ENSURE_DIR_AND_FILES_EXIST)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UT4UT + "tempDir", [],
                                                                dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1 = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UT4UT + "tempDir1", [],
                                                                 dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2 = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UT4UT + "tempDir2", [],
                                                                 dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34 = DirectoryPathChecker(config.PATH_FROM_REPO_TO_UT4UT + "tempDir34", [],
                                                                  dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  NON_EXISTING_DIRECTORY = DirectoryPathChecker("webPage/generator/nonExistingFolder", [],
                                                dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  # FOR PRODUCTION CODE
  GIT_REPOSITORY = DirectoryPathChecker("", ["README.md", ".git/HEAD"], dirAction.ENSURE_DIR_AND_FILES_EXIST)
  INDEX_HTML_LOCATION = DirectoryPathChecker("", [], dirAction.ENSURE_DIR_EXISTS_ONLY)
  HTML_BACKUP = DirectoryPathChecker("webPage/backup", [], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  HTML_SCRIPTS = DirectoryPathChecker("webPage/scripts", ["githubApiScripts.js", "navigationScripts.js"],
                                      dirAction.ENSURE_DIR_AND_FILES_EXIST)
  PYTHON_MAIN_GENERATOR = DirectoryPathChecker(config.PATH_FROM_REPO_TO_PY_GENERATOR, ["generator.py"],
                                               dirAction.ENSURE_DIR_AND_FILES_EXIST)
  HTML_IMAGES = DirectoryPathChecker("webPage/images", ["favicon.png"], dirAction.ENSURE_DIR_AND_FILES_EXIST)
