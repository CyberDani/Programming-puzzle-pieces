import sys
import unittest

sys.path.append('..')
from modules import webReq

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