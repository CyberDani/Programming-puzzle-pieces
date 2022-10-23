import string
import sys
import unittest

sys.path.append('..')
from defTypes.dbBranchType import DbBranchType
from modules import githubApi

class GithubApiTests(unittest.TestCase):

  def test_getTreeSha_nonSense(self):
    with self.assertRaises(Exception):
      githubApi.getTreeSha("devel")
    with self.assertRaises(Exception):
      githubApi.getTreeSha(DbBranchType.MASTER)
    with self.assertRaises(Exception):
      githubApi.getTreeSha(None)
    with self.assertRaises(Exception):
      githubApi.getTreeSha(12)
    with self.assertRaises(Exception):
      githubApi.getTreeSha(False)
    with self.assertRaises(Exception):
      githubApi.getTreeSha(["master"])
    with self.assertRaises(Exception):
      githubApi.getTreeSha({})

  def test_getTreeSha_wrongParameters(self):
    originalGithubUser = githubApi.githubUser
    nonExistingGithubUser = "afoibfvbwqipfv"
    githubApi.githubUser = nonExistingGithubUser
    found, treeSha = githubApi.getTreeSha(githubApi.RepoBranchType.MASTER)
    if not found:
      self.assertEqual(treeSha, "")
    found, treeSha = githubApi.getTreeSha(githubApi.RepoBranchType.DEVEL)
    if not found:
      self.assertEqual(treeSha, "")
    githubApi.githubUser = originalGithubUser

  # turn off the internet to test
  def test_getTreeSha_noInternet(self):
    found, treeSha = githubApi.getTreeSha(githubApi.RepoBranchType.MASTER)
    if not found:
      self.assertEqual(treeSha, "")

  def test_getTreeSha_validResponse(self):
    found, treeSha = githubApi.getTreeSha(githubApi.RepoBranchType.MASTER)
    if not found:
      return
    self.assertTrue(found)
    self.assertTrue(len(treeSha) > 0)
    allHexDigits = all(c in string.hexdigits for c in treeSha)
    self.assertTrue(allHexDigits)
    found, treeSha = githubApi.getTreeSha(githubApi.RepoBranchType.MASTER)
    if not found:
      return
    self.assertTrue(found)
    self.assertTrue(len(treeSha) > 0)
    allHexDigits = all(c in string.hexdigits for c in treeSha)
    self.assertTrue(allHexDigits)

  def test_getAllBlobs_nonSense(self):
    with self.assertRaises(Exception):
      githubApi.getAllBlobs("devel")
    with self.assertRaises(Exception):
      githubApi.getAllBlobs(DbBranchType.MASTER)
    with self.assertRaises(Exception):
      githubApi.getAllBlobs(None)
    with self.assertRaises(Exception):
      githubApi.getAllBlobs(12)
    with self.assertRaises(Exception):
      githubApi.getAllBlobs(False)
    with self.assertRaises(Exception):
      githubApi.getAllBlobs(["master"])
    with self.assertRaises(Exception):
      githubApi.getAllBlobs({})

  def test_getAllBlobs_wrongParameters(self):
    originalGithubUser = githubApi.githubUser
    nonExistingGithubUser = "afoibfvbwqipfv"
    githubApi.githubUser = nonExistingGithubUser
    found, files = githubApi.getAllBlobs(githubApi.RepoBranchType.MASTER)
    if not found:
      self.assertEqual(files, [])
    found, files = githubApi.getAllBlobs(githubApi.RepoBranchType.DEVEL)
    if not found:
      self.assertEqual(files, [])
    githubApi.githubUser = originalGithubUser

  # turn off the internet connection to test
  def test_getAllBlobs_noInternet(self):
    found, files = githubApi.getAllBlobs(githubApi.RepoBranchType.MASTER)
    if not found:
      self.assertEqual(files, [])

  def test_getAllBlobs_validResponse(self):
    found, files = githubApi.getAllBlobs(githubApi.RepoBranchType.MASTER)
    if not found:
      return
    self.assertTrue(found)
    self.assertTrue(len(files) > 0)
    found, files = githubApi.getAllBlobs(githubApi.RepoBranchType.MASTER)
    if not found:
      return
    self.assertTrue(found)
    self.assertTrue(len(files) > 0)

  def helper_getGithubBlobFromJsonObject_checkIfCorrupt(self, jsonDict):
    corrupt, blob = githubApi.getGithubBlobFromJsonObject(jsonDict)
    self.assertTrue(corrupt)
    self.assertIsNone(blob)

  def test_getGithubBlobFromJsonObject_nonSense(self):
    with self.assertRaises(Exception):
      githubApi.getGithubBlobFromJsonObject("devel")
    with self.assertRaises(Exception):
      githubApi.getGithubBlobFromJsonObject(DbBranchType.MASTER)
    with self.assertRaises(Exception):
      githubApi.getGithubBlobFromJsonObject(None)
    with self.assertRaises(Exception):
      githubApi.getGithubBlobFromJsonObject(12)
    with self.assertRaises(Exception):
      githubApi.getGithubBlobFromJsonObject(False)
    with self.assertRaises(Exception):
      githubApi.getGithubBlobFromJsonObject(["master"])
    with self.assertRaises(Exception):
      githubApi.getGithubBlobFromJsonObject(githubApi.RepoBranchType.MASTER)
    with self.assertRaises(Exception):
      githubApi.getGithubBlobFromJsonObject('"path": "x","mode": "x","type": "blob","sha": "x","size": 0,"url": "Q.io"')

  def test_getGithubBlobFromJsonObject_corruptExamples(self):
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt({})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt({"something": "random"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt({"something": "random", "sth2": "rand2"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt({"something": "random", "sth2": "rand2", "k3": "v3"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt({"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt({"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4", "k5": "v5"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt({"1": "v", "2": "v", "3": "v", "4": "v", "5": "v", "6": "v"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt(
                                      {"pathX": "x", "mode": 123, "type": "blob", "sha": "x", "size": 0, "url": "Q.io"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt(
                                      {"path": "x", "Xmode": 123, "type": "blob", "sha": "x", "size": 0, "url": "Q.io"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt(
                                      {"path": "x", "mode": 123, "typeX": "blob", "sha": "x", "size": 0, "url": "Q.io"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt(
                                      {"path": "x", "mode": 123, "type": "blob", "sh_a": "x", "size": 0, "url": "Q.io"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt(
                                      {"path": "x", "mode": 123, "type": "blob", "sha": "x", "Size": 0, "url": "Q.io"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt(
                                      {"path": "x", "mode": 123, "type": "blob", "sha": "x", "size": 0, "uRl": "Q.io"})
    self.helper_getGithubBlobFromJsonObject_checkIfCorrupt(
                                                  {"path": "x", "mode": 123, "type": "blob", "sha": "x", "url": "q.io"})

  def test_getGithubBlobFromJsonObject_validExamples(self):
    corrupt, blob = githubApi.getGithubBlobFromJsonObject(
                                  {"path": "x", "mode": 123, "type": "blob", "sha": "x", "size": 234, "url": "q.io"})
    self.assertFalse(corrupt)
    self.assertEqual(blob, githubApi.GithubBlob("x", 123, githubApi.GitBlobType.BLOB, "x", 234, "q.io"))
    corrupt, blob = githubApi.getGithubBlobFromJsonObject(
                                  {"path": ".file", "mode": 333, "type": "tree", "sha": "12c6", "url": "site.com"})
    self.assertFalse(corrupt)
    self.assertEqual(blob, githubApi.GithubBlob(".file", 333, githubApi.GitBlobType.TREE, "12c6", -1, "site.com"))

  def test_getBlobsByFileName_nonSense(self):
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(githubApi.RepoBranchType.MASTER, "")
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(githubApi.RepoBranchType.DEVEL, [])
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(githubApi.RepoBranchType.MASTER, ["file"])
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(githubApi.RepoBranchType.DEVEL, 2)
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(githubApi.RepoBranchType.MASTER, {})
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(githubApi.RepoBranchType.DEVEL, None)
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(githubApi.RepoBranchType.MASTER, {"file"})
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(githubApi.RepoBranchType.DEVEL, {"file", "txt"})
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName("master", "file.txt")
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(DbBranchType.MASTER, "file.txt")
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(None, "file.txt")
    with self.assertRaises(Exception):
      githubApi.getBlobsByFileName(None, None)

  def test_getBlobsByFileName_surelyNotExistingFile(self):
    found, blobs = githubApi.getBlobsByFileName(githubApi.RepoBranchType.MASTER, "ionviubi31gqwgs.pwgq")
    self.assertFalse(found)
    self.assertEqual(blobs, [])
    found, blobs = githubApi.getBlobsByFileName(githubApi.RepoBranchType.DEVEL, "og42hiy2ewfwuib.ewivy")
    self.assertFalse(found)
    self.assertEqual(blobs, [])

  def test_getBlobsByFileName_getUniqueFileName(self):
    fileName = "uniqueFileName.unique"
    found, blobs = githubApi.getBlobsByFileName(githubApi.RepoBranchType.DEVEL, fileName)
    if not found:
      return
    self.assertTrue(found)
    self.assertEqual(len(blobs), 1)
    blob = blobs[0]
    self.assertTrue(blob.size >= 0)
    self.assertEqual(blob.type, githubApi.GitBlobType.BLOB)
    self.assertTrue(blob.relPath.endswith("/" + fileName))

  def test_getBlobsByFileName_getNonUniqueFileName(self):
    fileName = "notUniqeFileName.nunique"
    found, blobs = githubApi.getBlobsByFileName(githubApi.RepoBranchType.DEVEL, fileName)
    if not found:
      return
    self.assertTrue(found)
    self.assertEqual(len(blobs), 3)
    blob1 = blobs[0]
    blob2 = blobs[1]
    blob3 = blobs[2]
    self.assertTrue(blob1.size >= 0)
    self.assertTrue(blob2.size >= 0)
    self.assertTrue(blob3.size >= 0)
    self.assertEqual(blob1.type, githubApi.GitBlobType.BLOB)
    self.assertEqual(blob2.type, githubApi.GitBlobType.BLOB)
    self.assertEqual(blob3.type, githubApi.GitBlobType.BLOB)
    self.assertTrue(blob1.relPath.endswith("/" + fileName))
    self.assertTrue(blob2.relPath.endswith("/" + fileName))
    self.assertTrue(blob3.relPath.endswith("/" + fileName))
