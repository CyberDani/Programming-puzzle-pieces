from enum import Enum

from modules.paths.dirPathCheckerActionType import DirPathCheckerActionType as dirAction
from modules.paths.dirPathChecker import DirectoryPathChecker
from defTypes import pppConfig as config

class DirectoryPathTypeForUT(Enum):
  PYTHON_GENERATOR_UNIT_TESTS_TEMP1 = DirectoryPathChecker(
    config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP1_FOLDER_NAME,
                                                      [], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_TEMP2 = DirectoryPathChecker(
    config.PATH_FROM_ROOT_TO_UNIT_TESTS + config.UT_TEMP2_FOLDER_NAME,
                                                      [], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_TEST1 = DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS + "testDir1", [],
                                                           dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_NESTED_X2 = DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UNIT_TESTS
                                                               + "nestedTest11/nestedTest12",
                                                               [], dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS = DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UT4UT,
                                                        ["fail_x_group1.py", "pass_x_group1.py",
                                                         "pass_x_group2.py", "test_tempDir.py"],
                                                        dirAction.ENSURE_DIR_AND_FILES_EXIST)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR = DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UT4UT + "tempDir", [],
                                                                dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1 = DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UT4UT + "tempDir1", [],
                                                                 dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2 = DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UT4UT + "tempDir2", [],
                                                                 dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34 = DirectoryPathChecker(config.PATH_FROM_ROOT_TO_UT4UT + "tempDir34", [],
                                                                  dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
  NON_EXISTING_DIRECTORY = DirectoryPathChecker("webPage/generator/nonExistingFolder", [],
                                                dirAction.DO_NOT_CHECK_DIR_EXISTENCE)
