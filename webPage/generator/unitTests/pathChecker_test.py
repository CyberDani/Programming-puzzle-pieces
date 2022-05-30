import pathlib
import sys
import unittest

sys.path.append('..')

from defTypes import dirPathChecker

from modules import filerw
from modules import path

class PathCheckerTests(unittest.TestCase):

  def test_DirectoryPathChecker_nonSense(self):
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(None, ["file.txt"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./unitTests", None)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(True, ["file.txt"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", False)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", 34)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", "checks_test.py")
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(None, ["checks.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(12, ["checks.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("checks.py", ["checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("nonExistingFolder", ["checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(None, None)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(False, True)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker(1, 5)
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests", [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", [])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["checks_test.py", "nonExistingFile.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["nonExistingFile.py", "checks_test.py"])
    with self.assertRaises(Exception):
      dirPathChecker.DirectoryPathChecker("", ["READMENOT.md"])

  def test_DirectoryPathChecker_validExamples(self):
    file = open("./unitTests/temp/testFile.txt", "w")
    file.close()
    file = open("./unitTests/temp/testFile2.txt", "w")
    file.close()
    file = open("./unitTests/temp/testFile3.txt", "w")
    file.close()
    try:
      dirPathChecker.DirectoryPathChecker("", ["README.md"])
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp", ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/temp/", ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/temp", ["testFile.txt"])
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["temp/testFile.txt"])
      dirPathChecker.DirectoryPathChecker("webPage/generator/unitTests/", ["/temp/testFile.txt"])
      dirPathChecker.DirectoryPathChecker("webPage/generator", ["unitTests/temp/testFile.txt"])
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", ["testFile.txt", "testFile2.txt"])
      dirPathChecker.DirectoryPathChecker("./webPage/generator/unitTests/temp/", ["testFile.txt", "testFile2.txt",
                                                                               "testFile3.txt"])
    except Exception:
      self.fail("DirectoryPathChecker() raised Exception unexpectedly!")
