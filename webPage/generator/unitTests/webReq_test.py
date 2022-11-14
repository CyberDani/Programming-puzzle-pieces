import os
import sys

sys.path.append('..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.paths.definitions.dirPathTypeForUT import DirectoryPathTypeForUT as Dir
from modules.paths.definitions.filePathTypeForUT import FilePathTypeForUT as File

from modules import webReq
from modules import filerw
from modules.paths import path


class WebReqTests(AutoUnitTest):

  def test_getstatusCodeEncodingAndHtmlFromUrl_nonSense(self):
    with self.assertRaises(Exception):
      webReq.getstatusCodeEncodingAndHtmlFromUrl("")
    with self.assertRaises(Exception):
      webReq.getstatusCodeEncodingAndHtmlFromUrl(None)
    with self.assertRaises(Exception):
      webReq.getstatusCodeEncodingAndHtmlFromUrl(False)
    with self.assertRaises(Exception):
      webReq.getstatusCodeEncodingAndHtmlFromUrl("123")

  def test_getstatusCodeEncodingAndHtmlFromUrl_incorrectUrl(self):
    with self.assertRaises(Exception):
      statusCode, encoding, html = webReq.getstatusCodeEncodingAndHtmlFromUrl("http://www.asdsasdsadasdas.qweqwe.com")

  def test_getstatusCodeEncodingAndHtmlFromUrl_correctUrl(self):
    statusCode, encoding, html = webReq.getstatusCodeEncodingAndHtmlFromUrl("https://www.youtube.com")
    self.assertEqual(statusCode, 200)
    self.assertEqual(encoding, "utf-8")
    self.assertTrue(len(html) > 300)

  def test_getstatusCodeEncodingAndHtmlFromUrl_404(self):
    statusCode, encoding, html = webReq.getstatusCodeEncodingAndHtmlFromUrl("https://www.google.com/asdfeogeroiyfgwieuapfbi")
    self.assertEqual(statusCode, 404)
    self.assertEqual(encoding.lower(), "utf-8")
    self.assertTrue(len(html) > 300)

  def test_downloadFromUrlToFile_nonSense(self):
    filePath = path.getAbsoluteFilePath(File.FOR_TEST_TEXTFILE1)
    tempDir = path.getAbsoluteDirPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    downloadPath = tempDir + "logo.binary"
    file = open(filePath, "wb")
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200("io", downloadPath)
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200("https://cyberdani.github.io/Programming-puzzle-pieces/webPage/images/Logo_text.png", file)
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200("https://cyberdani.github.io/Programming-puzzle-pieces/webPage/images/Logo_text.png", "")
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200("https://cyberdani.github.io/Programming-puzzle-pieces/webPage/images/Logo_text.png", None)
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200(None, downloadPath)
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200(None, None)
    self.assertFalse(filerw.fileExistsByPath(downloadPath))

  def test_downloadFromUrlToFile_incorrectUrl(self):
    tempDir = path.getAbsoluteDirPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    downloadPath = tempDir + "download.binary"
    if filerw.fileExistsByPath(downloadPath):
      os.remove(downloadPath)
    with self.assertRaises(Exception):
      statusCode, encoding, html = webReq.downloadFromUrlToFileIfStatusIs200("https://www.google.com/asdfeogeroiyfgwieuapfbi",
                                                                             downloadPath)
    self.assertFalse(filerw.fileExistsByPath(downloadPath))

  def test_downloadFromUrlToFile_404(self):
    tempDir = path.getAbsoluteDirPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    downloadPath = tempDir + "download.binary"
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200("https://www.google.com/asdfeogeroiyfgwieuapfbi", downloadPath)

  def test_downloadFromUrlToFile_correctUrl200(self):
    tempDir = path.getAbsoluteDirPath(Dir.PYTHON_GENERATOR_UNIT_TESTS_TEMP1)
    downloadPath = tempDir + "download.png"
    webReq.downloadFromUrlToFileIfStatusIs200("https://cyberdani.github.io/Programming-puzzle-pieces/webPage/images/Logo_text.png",
                                              downloadPath)
    self.assertTrue(filerw.fileExistsByPath(downloadPath))
    size1 = os.path.getsize(downloadPath) / 1024
    self.assertTrue(size1 > 15)
    self.assertTrue(size1 < 150)
    webReq.downloadFromUrlToFileIfStatusIs200("https://cyberdani.github.io/Programming-puzzle-pieces/webPage/images/Logo_text.png",
                                              downloadPath)
    self.assertTrue(filerw.fileExistsByPath(downloadPath))
    size2 = os.path.getsize(downloadPath) / 1024
    self.assertEqual(size1, size2)
    os.remove(downloadPath)
