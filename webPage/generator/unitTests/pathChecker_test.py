import pathlib
import sys
import unittest

sys.path.append('..')

from defTypes import pathChecker

from modules import filerw
from modules import path

class PathCheckerTests(unittest.TestCase):

  def test_DirectoryPathChecker_nonSense(self):
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker(None, ["file.txt"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./unitTests", None)
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker(True, ["file.txt"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests", False)
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests", 34)
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests", "checks_test.py")
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker(None, ["checks.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker(12, ["checks.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("checks.py", ["checks_test.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("nonExistingFolder", ["checks_test.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker(None, None)
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker(False, True)
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker(1, 5)
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests", [])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", [])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests", [])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests/", [])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      pathChecker.DirectoryPathChecker("", ["READMENOT.md"])

  def test_DirectoryPathChecker_validExamples(self):
    file = open("./unitTests/temp/testFile.txt", "w")
    file.close()
    file = open("./unitTests/temp/testFile2.txt", "w")
    file.close()
    file = open("./unitTests/temp/testFile3.txt", "w")
    file.close()
    try:
      pathChecker.DirectoryPathChecker("", ["README.md"])
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", ["testFile.txt"])
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp", ["testFile.txt"])
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests/temp/", ["testFile.txt"])
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests/temp", ["testFile.txt"])
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["temp/testFile.txt"])
      pathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["/temp/testFile.txt"])
      pathChecker.DirectoryPathChecker("webPage/generator", ["unitTests/temp/testFile.txt"])
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", ["testFile.txt", "testFile2.txt"])
      pathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", ["testFile.txt", "testFile2.txt",
                                                                               "testFile3.txt"])
    except Exception:
      self.fail("DirectoryPathChecker() raised Exception unexpectedly!")
