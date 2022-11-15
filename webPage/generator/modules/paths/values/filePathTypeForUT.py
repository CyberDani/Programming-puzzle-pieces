from enum import Enum

from modules.paths.values.dirPathTypeForUT import DirectoryPathTypeForUT as UtDir
from modules.paths.filePathCheckerActionType import FilePathCheckerActionType as fileAction
from modules.paths.filePathChecker import FilePathChecker

class FilePathTypeForUT(Enum):
  FOR_TEST_TEXTFILE1 = FilePathChecker(UtDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1, "test1.txt",
                                       fileAction.DONT_CHECK_FILE_EXISTENCE)
  FOR_TEST_TEXTFILE2 = FilePathChecker(UtDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1, "test2.txt",
                                       fileAction.DONT_CHECK_FILE_EXISTENCE)
  FOR_TEST_TEXTFILE3 = FilePathChecker(UtDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1, "test3.txt",
                                       fileAction.DONT_CHECK_FILE_EXISTENCE)
  FOR_TEST_NON_EXISTING_TEXTFILE1 = FilePathChecker(UtDir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1, "fbweifb1.sda",
                                                    fileAction.DONT_CHECK_FILE_EXISTENCE)
