from enum import Enum

from defTypes import dirPathChecker

class DirectoryRelPathType(Enum):
  """The associated path is relative to the git root repository"""
  GIT_REPOSITORY = dirPathChecker.DirectoryPathChecker("", ["README.md", ".git/HEAD"])
  INDEX_HTML_LOCATION = dirPathChecker.DirectoryPathChecker("", ["index.html"])
  PYTHON_MAIN_GENERATOR = dirPathChecker.DirectoryPathChecker("webPage/generator", ["generator.py"])
  PYTHON_GENERATOR_UNIT_TESTS = dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests",
                                                           ["checks_test.py", "argumentParser_test.py"])
  HTML_GENERAL_INCLUDES = dirPathChecker.DirectoryPathChecker("webPage/generator/htmlIncludes",
                                                           ["footer.txt", "topNav.txt", "sideNav.txt"])
