import os
import sys
import unittest

sys.path.append('..')
from modules import webReq
from modules import filerw

class WebReqTests(unittest.TestCase):

  def test_getstatusCodeEncodingAndHtmlFromUrl_nonSense(self):
    with self.assertRaises(Exception):
      webReq.getstatusCodeEncodingAndHtmlFromUrl("")
    with self.assertRaises(Exception):
      webReq.getstatusCodeEncodingAndHtmlFromUrl()
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
    statusCode, encoding, html = webReq.getstatusCodeEncodingAndHtmlFromUrl("https://www.youtube.com/q1w2e3r4t5")
    self.assertEqual(statusCode, 404)
    self.assertEqual(encoding, "utf-8")
    self.assertTrue(len(html) > 300)

  def test_downloadFromUrlToFile_nonSense(self):
    file = open("./unitTests/temp/test.txt", "wb")
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200("io", "./unitTests/temp/logo.binary")
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200("https://cyberdani.github.io/Programming-puzzle-pieces/webPage/images/Logo_text.png", file)
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200("https://cyberdani.github.io/Programming-puzzle-pieces/webPage/images/Logo_text.png", "")
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200("https://cyberdani.github.io/Programming-puzzle-pieces/webPage/images/Logo_text.png", None)
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200(None, "./unitTests/temp/logo.binary")
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200(None, None)
    self.assertFalse(filerw.fileExists("./unitTests/temp/logo.binary"))

  def test_downloadFromUrlToFile_incorrectUrl(self):
    with self.assertRaises(Exception):
      statusCode, encoding, html = webReq.downloadFromUrlToFileIfStatusIs200("http://www.asdsasdsadasdas.qweqwe.com", "./unitTests/temp/download.binary")
    self.assertFalse(filerw.fileExists("./unitTests/temp/download.binary"))

  def test_downloadFromUrlToFile_404(self):
    with self.assertRaises(Exception):
      webReq.downloadFromUrlToFileIfStatusIs200("https://www.youtube.com/q1w2e3r4t5", "./unitTests/temp/download.binary")

  def test_downloadFromUrlToFile_correctUrl200(self):
    webReq.downloadFromUrlToFileIfStatusIs200("https://cyberdani.github.io/Programming-puzzle-pieces/webPage/images/Logo_text.png", "./unitTests/temp/download.png")
    self.assertTrue(filerw.fileExists("./unitTests/temp/download.png"))
    size1 = os.path.getsize("./unitTests/temp/download.png") / 1024
    self.assertTrue(size1 > 15)
    self.assertTrue(size1 < 150)
    webReq.downloadFromUrlToFileIfStatusIs200("https://cyberdani.github.io/Programming-puzzle-pieces/webPage/images/Logo_text.png", "./unitTests/temp/download.png")
    self.assertTrue(filerw.fileExists("./unitTests/temp/download.png"))
    size2 = os.path.getsize("./unitTests/temp/download.png") / 1024
    self.assertEqual(size1, size2)
    os.remove("./unitTests/temp/download.png")