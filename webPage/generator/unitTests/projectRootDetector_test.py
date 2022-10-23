import os
import pathlib
import shutil
import sys
import unittest

sys.path.append('..')

from modules.paths import projectRootDetector as projRoot


class ProjectRootDetectorTests(unittest.TestCase):

  def test_getGitRepoAbsolutePath_ifFound_renameGitDir_retest_renameBack(self):
    repoFound, gitRepoPath = projRoot.getGitRepoAbsolutePath()
    if not repoFound:
      self.assertEqual(gitRepoPath, "")
      return
    self.assertEqual(gitRepoPath[-1], "/")
    self.assertTrue(os.path.isdir(gitRepoPath + ".git"))
    self.assertTrue(os.path.isfile(gitRepoPath + ".git/HEAD"))
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(gitRepoPath))
    shutil.move(gitRepoPath + ".git", gitRepoPath + ".gitX")
    repoFound, newGitRepoPath = projRoot.getGitRepoAbsolutePath()
    if not repoFound:
      self.assertEqual(newGitRepoPath, "")
      shutil.move(gitRepoPath + ".gitX", gitRepoPath + ".git")
      return
    self.assertTrue(gitRepoPath.startswith(newGitRepoPath))
    self.assertTrue(len(gitRepoPath) > len(newGitRepoPath))
    shutil.move(gitRepoPath + ".gitX", gitRepoPath + ".git")

  def test_getProjectRootAbsolutePath_ifFound_renameRootDir_retest_renameBack(self):
    rootFound, rootPath = projRoot.getProjectRootAbsolutePath()
    if not rootFound:
      self.assertEqual(rootPath, "")
      return
    self.assertEqual(rootPath[-1], "/")
    self.assertTrue(os.path.isdir(rootPath + ".projRoot"))
    self.assertTrue(os.path.isfile(rootPath + ".projRoot/prog_puzzle_pieces.txt"))
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(rootPath))
    shutil.move(rootPath + ".projRoot", rootPath + ".projRootX")
    rootFound, newRootPath = projRoot.getProjectRootAbsolutePath()
    if not rootFound:
      self.assertEqual(newRootPath, "")
      shutil.move(rootPath + ".projRootX", rootPath + ".projRoot")
      return
    self.assertTrue(rootPath.startswith(newRootPath))
    self.assertTrue(len(rootPath) > len(newRootPath))
    shutil.move(rootPath + ".projRootX", rootPath + ".projRoot")

  def test_getRootAbsolutePathBySpecificFileNames_ifFound_renameSth_retest_renameBack(self):
    rootFound, rootPath = projRoot.getRootAbsolutePathBySpecificFileNames()
    if not rootFound:
      self.assertEqual(rootPath, "")
      return
    self.assertEqual(rootPath[-1], "/")
    originalFileName = "libs.txt"
    modifiedFileName = "libsX.txt"
    self.assertTrue(os.path.isdir(rootPath + "webPage"))
    self.assertTrue(os.path.isfile(rootPath + originalFileName))
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(rootPath))
    # rename -> retest -> rename back
    os.rename(rootPath + originalFileName, rootPath + modifiedFileName)
    rootFound, newRootPath = projRoot.getRootAbsolutePathBySpecificFileNames()
    if not rootFound:
      self.assertEqual(newRootPath, "")
      os.rename(rootPath + modifiedFileName, rootPath + originalFileName)
      return
    self.assertTrue(rootPath.startswith(newRootPath))
    self.assertTrue(len(rootPath) > len(newRootPath))
    os.rename(rootPath + modifiedFileName, rootPath + originalFileName)

  def test_getRootAbsolutePathByNumberOfParentsFromGithub(self):
    found, rootPath = projRoot.getRootAbsolutePathByNumberOfParentsFromGithub()
    if not found:
      self.assertEqual(rootPath, "")
      return
    self.assertEqual(rootPath[-1], "/")
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(rootPath))

  def test_getRootAbsolutePathByNameOfParentsFromGithub(self):
    found, rootPath = projRoot.getRootAbsolutePathByNameOfParentsFromGithub()
    if not found:
      self.assertEqual(rootPath, "")
      return
    self.assertEqual(rootPath[-1], "/")
    currentPath = pathlib.Path(__file__).parent.resolve().as_posix()
    self.assertTrue(currentPath.startswith(rootPath))
