from enum import Enum

from defTypes import pathChecker

class DirectoryRelPathType(Enum):
  """The associated path is relative to the git root repository"""
  GIT_REPOSITORY = pathChecker.DirectoryPathChecker("", ["README.md", ".git/HEAD"])
  INDEX_HTML_LOCATION = pathChecker.DirectoryPathChecker("", ["index.html"])
  PYTHON_MAIN_GENERATOR = pathChecker.DirectoryPathChecker("webPage/generator", ["generator.py"])
  PYTHON_GENERATOR_UNIT_TESTS = pathChecker.DirectoryPathChecker("webPage/generator", ["generator.py"])
  HTML_GENERAL_INCLUDES = pathChecker.DirectoryPathChecker("webPage/generator/unitTests",
                                                           ["checks_test.py", "argumentParser_test.py"])
