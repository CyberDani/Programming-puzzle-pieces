import sys
import unittest

sys.path.append('..')
from modules import filerw
from modules import webLibs

class WebLibsTests(unittest.TestCase):

  def test_addFontAwesome_v611_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      webLibs.addFontAwesome_v611(file, None)
    with self.assertRaises(Exception):
      webLibs.addFontAwesome_v611(file, -1)
    with self.assertRaises(Exception):
      webLibs.addFontAwesome_v611(file, 150)
    with self.assertRaises(Exception):
      webLibs.addFontAwesome_v611("index.html", 2)
    with self.assertRaises(Exception):
      webLibs.addFontAwesome_v611(None, 3)

  def test_addFontAwesome_v611_normalCase(self):
    file = open("./unitTests/temp/test.txt", "w")
    webLibs.addFontAwesome_v611(file, 2)
    file.close()
    lines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 6)
    self.assertEqual(lines[0], "\t\t<link href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css\"\n")
    self.assertEqual(lines[1], "\t\t\tintegrity=\"sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==\"\n")
    self.assertEqual(lines[2], "\t\t\trel=\"stylesheet\" crossorigin=\"anonymous\" referrerpolicy=\"no-referrer\" />\n")
    self.assertEqual(lines[3], "\t\t<script src=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/js/all.min.js\"\n")
    self.assertEqual(lines[4], "\t\t\tintegrity=\"sha512-6PM0qYu5KExuNcKt5bURAoT6KCThUmHRewN3zUFNaoI6Di7XJPTMoT6K0nsagZKk2OB4L7E3q1uQKHNHd4stIQ==\"\n")
    self.assertEqual(lines[5], "\t\t\tcrossorigin=\"anonymous\" referrerpolicy=\"no-referrer\"></script>\n")

  def test_addJquery_v360_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      webLibs.addJquery_v360(file, None)
    with self.assertRaises(Exception):
      webLibs.addJquery_v360(file, -1)
    with self.assertRaises(Exception):
      webLibs.addJquery_v360(file, 150)
    with self.assertRaises(Exception):
      webLibs.addJquery_v360("index.html", 2)
    with self.assertRaises(Exception):
      webLibs.addJquery_v360(None, 3)

  def test_addJquery_v360_normalCase(self):
    file = open("./unitTests/temp/test.txt", "w")
    webLibs.addJquery_v360(file, 3)
    file.close()
    lines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "\t\t\t<script src=\"https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js\"\n")
    self.assertEqual(lines[1], "\t\t\t\tintegrity=\"sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==\"\n")
    self.assertEqual(lines[2], "\t\t\t\tcrossorigin=\"anonymous\" referrerpolicy=\"no-referrer\"></script>\n")

  def test_addMaterialize_v110_alpha_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      webLibs.addMaterialize_v110_alpha(file, None)
    with self.assertRaises(Exception):
      webLibs.addMaterialize_v110_alpha(file, -1)
    with self.assertRaises(Exception):
      webLibs.addMaterialize_v110_alpha(file, 150)
    with self.assertRaises(Exception):
      webLibs.addMaterialize_v110_alpha("index.html", 2)
    with self.assertRaises(Exception):
      webLibs.addMaterialize_v110_alpha(None, 3)

  def test_addMaterialize_v110_alpha_normalCase(self):
    file = open("./unitTests/temp/test.txt", "w")
    webLibs.addMaterialize_v110_alpha(file, 1)
    file.close()
    lines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "\t<link href=\"https://cdn.jsdelivr.net/npm/@materializecss/materialize@1.1.0-alpha/dist/css/materialize.min.css\"\n")
    self.assertEqual(lines[1], "\t\trel=\"stylesheet\" />\n")
    self.assertEqual(lines[2], "\t<script src=\"https://cdn.jsdelivr.net/npm/@materializecss/materialize@1.1.0-alpha/dist/js/materialize.min.js\"></script>\n")

  def test_addGoogleIcons_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      webLibs.addGoogleIcons(file, None)
    with self.assertRaises(Exception):
      webLibs.addGoogleIcons(file, -1)
    with self.assertRaises(Exception):
      webLibs.addGoogleIcons(file, 150)
    with self.assertRaises(Exception):
      webLibs.addGoogleIcons("index.html", 2)
    with self.assertRaises(Exception):
      webLibs.addGoogleIcons(None, 3)

  def test_addGoogleIcons_normalCase(self):
    file = open("./unitTests/temp/test.txt", "w")
    webLibs.addGoogleIcons(file, 4)
    file.close()
    lines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 1)
    self.assertEqual(lines[0], "\t\t\t\t<link href=\"https://fonts.googleapis.com/icon?family=Material+Icons\" rel=\"stylesheet\" />\n")

  def test_addJQueryLoadingOverlay_v217_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      webLibs.addJQueryLoadingOverlay_v217(file, None)
    with self.assertRaises(Exception):
      webLibs.addJQueryLoadingOverlay_v217(file, -1)
    with self.assertRaises(Exception):
      webLibs.addJQueryLoadingOverlay_v217(file, 150)
    with self.assertRaises(Exception):
      webLibs.addJQueryLoadingOverlay_v217("index.html", 2)
    with self.assertRaises(Exception):
      webLibs.addJQueryLoadingOverlay_v217(None, 3)

  def test_addJQueryLoadingOverlay_v217_normalCase(self):
    file = open("./unitTests/temp/test.txt", "w")
    webLibs.addJQueryLoadingOverlay_v217(file, 5)
    file.close()
    lines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 1)
    self.assertEqual(lines[0], "\t\t\t\t\t<script src=\"https://cdn.jsdelivr.net/npm/gasparesganga-jquery-loading-overlay@2.1.7/dist/loadingoverlay.min.js\"></script>\n")

  def test_addGoogleFont_nonSense(self):
    file = open("./unitTests/temp/test.txt", "w")
    with self.assertRaises(Exception):
      webLibs.addGoogleFont(file, None, "Dani Sans")
    with self.assertRaises(Exception):
      webLibs.addGoogleFont(file, -1, "Dani Sans")
    with self.assertRaises(Exception):
      webLibs.addGoogleFont(file, 150, "Dani Sans")
    with self.assertRaises(Exception):
      webLibs.addGoogleFont("index.html", 2, "Dani Sans")
    with self.assertRaises(Exception):
      webLibs.addGoogleFont(None, 3, "Dani Sans")
    with self.assertRaises(Exception):
      webLibs.addGoogleFont(file, 3, 24)

  def test_addGoogleFont_normalCase(self):
    file = open("./unitTests/temp/test.txt", "w")
    webLibs.addGoogleFont(file, 6, "?family=Heyho+Joe:wght@500&display=something")
    file.close()
    lines = filerw.getLinesByFilePathWithEndingNewLine("./unitTests/temp/test.txt")
    self.assertEqual(len(lines), 3)
    self.assertEqual(lines[0], "\t\t\t\t\t\t<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n")
    self.assertEqual(lines[1], "\t\t\t\t\t\t<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n")
    self.assertEqual(lines[2], "\t\t\t\t\t\t<link href=\"https://fonts.googleapis.com/css2?family=Heyho+Joe:wght@500&display=something\" rel=\"stylesheet\">\n")
