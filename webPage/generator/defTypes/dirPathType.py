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
  PYTHON_GENERATOR_UNIT_TESTS_TEMP1 = dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/temp", [],
                                                            dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_GENERATOR_UNIT_TESTS_TEMP2 = dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/temp2", [],
                                                                          dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  NON_EXISTING_DIRECTORY = dirPathChecker.DirectoryPathChecker("webPage/generator/nonExistingFolder", [],
                                                                          dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS = dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests4unitTests",
                                                                       ["fail_x_group1.py", "pass_x_group1.py",
                                                                        "pass_x_group2.py", "test_tempDir.py"],
                                                                        dirAction.ENSURE_PATH_AND_FILES_EXIST)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR = dirPathChecker.DirectoryPathChecker(
                                                                      "webPage/generator/unitTests4unitTests/tempDir",
                                                                      [], dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR1 = dirPathChecker.DirectoryPathChecker(
                                                                      "webPage/generator/unitTests4unitTests/tempDir1",
                                                                      [], dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR2 = dirPathChecker.DirectoryPathChecker(
                                                                      "webPage/generator/unitTests4unitTests/tempDir2",
                                                                      [], dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  PYTHON_UNIT_TESTS_4_UNIT_TESTS_TEMPDIR34 = dirPathChecker.DirectoryPathChecker(
                                                                      "webPage/generator/unitTests4unitTests/tempDir34",
                                                                      [], dirAction.DO_NOT_CHECK_PATH_EXISTENCE)
  HTML_GENERAL_INCLUDES = dirPathChecker.DirectoryPathChecker("webPage/generator/htmlIncludes",
                                                           ["footer.txt", "topNav.txt", "sideNav.txt"],
                                                            dirAction.ENSURE_PATH_AND_FILES_EXIST)
