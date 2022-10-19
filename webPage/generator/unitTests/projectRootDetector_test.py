import os
import pathlib
import shutil
import sys
import unittest

sys.path.append('..')

from modules.paths import projectRootDetector as projRoot


class ProjectRootDetectorTests(unittest.TestCase):

  def test_getGitRepoAbsolutePathEndingWithSlash_ifFound_RenameGitDir_Retest_RenameBack(self):
    repoFound, gitRepoPath = projRoot.getGitRepoAbsolutePathEndingWithSlash()
    if not repoFound:
      self.assertEqual(gitRepoPath, "")
      return
    self.assertEqual(gitRepoPath[-1], "/")
    self.assertTrue(os.path.isdir(gitRepoPath + ".git"))
    self.assertTrue(os.path.isfile(gitRepoPath + ".git/HEAD"))
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(gitRepoPath))
    shutil.move(gitRepoPath + ".git", gitRepoPath + ".gitX")
    repoFound, newGitRepoPath = projRoot.getGitRepoAbsolutePathEndingWithSlash()
    if not repoFound:
      self.assertEqual(newGitRepoPath, "")
      shutil.move(gitRepoPath + ".gitX", gitRepoPath + ".git")
      return
    self.assertTrue(gitRepoPath.startswith(newGitRepoPath))
    self.assertTrue(len(gitRepoPath) > len(newGitRepoPath))
    shutil.move(gitRepoPath + ".gitX", gitRepoPath + ".git")

  def test_getProjectRootAbsolutePathEndingWithSlash_ifFound_RenameRootDir_Retest_RenameBack(self):
    rootFound, rootPath = projRoot.getProjectRootAbsolutePathEndingWithSlash()
    if not rootFound:
      self.assertEqual(rootPath, "")
      return
    self.assertEqual(rootPath[-1], "/")
    self.assertTrue(os.path.isdir(rootPath + ".projRoot"))
    self.assertTrue(os.path.isfile(rootPath + ".projRoot/prog_puzzle_pieces.txt"))
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(rootPath))
    shutil.move(rootPath + ".projRoot", rootPath + ".projRootX")
    rootFound, newRootPath = projRoot.getProjectRootAbsolutePathEndingWithSlash()
    if not rootFound:
      self.assertEqual(newRootPath, "")
      shutil.move(rootPath + ".projRootX", rootPath + ".projRoot")
      return
    self.assertTrue(rootPath.startswith(newRootPath))
    self.assertTrue(len(rootPath) > len(newRootPath))
    shutil.move(rootPath + ".projRootX", rootPath + ".projRoot")
