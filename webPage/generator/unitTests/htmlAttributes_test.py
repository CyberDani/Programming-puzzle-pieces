import sys
import unittest

sys.path.append('..')

from modules import htmlAttributes as attr

class HtmlAttributesTests(unittest.TestCase):

  def test_getAttributeIdx_nonSense(self):
    with self.assertRaises(Exception):
      attr.getAttributeIdx("htmlAttribute", 12)
    with self.assertRaises(Exception):
      attr.getAttributeIdx("htmlAttribute", None)
    with self.assertRaises(Exception):
      attr.getAttributeIdx(None, None)
    with self.assertRaises(Exception):
      attr.getAttributeIdx(12, False)
    with self.assertRaises(Exception):
      attr.getAttributeIdx(None, "class")
    with self.assertRaises(Exception):
      attr.getAttributeIdx(False, "id")

  def test_getAttributeIdx_emptyString(self):
    idx = attr.getAttributeIdx("", "class")
    self.assertEqual(idx, -1)
    idx = attr.getAttributeIdx("id=\"content\" class=\"clearfix\"", "")
    self.assertEqual(idx, -1)

  def test_getAttributeIdx_attrNotFound(self):
    idx = attr.getAttributeIdx("htmlAttribute", "class")
    self.assertEqual(idx, -1)
    idx = attr.getAttributeIdx("htmlAttribute no-href", "href")
    self.assertEqual(idx, -1)
    idx = attr.getAttributeIdx("htmlAttribute hrefx", "href")
    self.assertEqual(idx, -1)
    idx = attr.getAttributeIdx("htmlAttribute hrefhref", "href")
    self.assertEqual(idx, -1)
    idx = attr.getAttributeIdx("no-href class='idk'", "href")
    self.assertEqual(idx, -1)
    idx = attr.getAttributeIdx("hrefx class='idk'", "href")
    self.assertEqual(idx, -1)
    idx = attr.getAttributeIdx("hrefhref class='idk'", "href")
    self.assertEqual(idx, -1)
    idx = attr.getAttributeIdx("selected no-href class='idk'", "href")
    self.assertEqual(idx, -1)
    idx = attr.getAttributeIdx("selected hrefx class='idk'", "href")
    self.assertEqual(idx, -1)
    idx = attr.getAttributeIdx("selected hrefhref class='idk'", "href")
    self.assertEqual(idx, -1)

  def test_getAttributeIdx_attrFound(self):
    idx = attr.getAttributeIdx("selected", "selected")
    self.assertEqual(idx, 0)
    idx = attr.getAttributeIdx("default='1'", "default")
    self.assertEqual(idx, 0)
    idx = attr.getAttributeIdx("default=\"1\"", "default")
    self.assertEqual(idx, 0)
    string = "value='234' selected"
    idx = attr.getAttributeIdx(string, "selected")
    self.assertEqual(idx, string.find("selected"))
    idx = attr.getAttributeIdx("selected class=\"className\"", "selected")
    self.assertEqual(idx, 0)
    idx = attr.getAttributeIdx("selected greyed-out", "selected")
    self.assertEqual(idx, 0)
    string = "value='234' selected=\"false\""
    idx = attr.getAttributeIdx(string, "selected")
    self.assertEqual(idx, string.find("selected"))
    idx = attr.getAttributeIdx("selected=\"false\" class=\"className\"", "selected")
    self.assertEqual(idx, 0)
    idx = attr.getAttributeIdx("selected=\"false\" greyed-out", "selected")
    self.assertEqual(idx, 0)
    string = "htmlAttribute no-href href"
    idx = attr.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find(" href") + 1)
    string = "htmlAttribute hrefx href=\"value\""
    idx = attr.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find("href="))
    string = "htmlAttribute hrefhref='value2' href='value3'"
    idx = attr.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find("href='value3'"))
    string = "no-href=\"noValue\" href class='idk'"
    idx = attr.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find("href class"))
    string = "hrefx href class='idk'"
    idx = attr.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find("href class"))

  def test_getAttributeIdx_attrFoundMultipleTime(self):
    idx = attr.getAttributeIdx("selected selected='false' selected selected", "selected")
    self.assertEqual(idx, 0)
    idx = attr.getAttributeIdx("default='1' class=\"myClass\" default", "default")
    self.assertEqual(idx, 0)
    string = "htmlAttribute hrefhref='value2' href='value3' href href='val4'"
    idx = attr.getAttributeIdx(string, "href")
    self.assertEqual(idx, string.find("href='value3'"))

  def test_extractDifferentValuesFromHtmlAttributesByKey_nonSense(self):
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", "")
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", 123)
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", False)
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", None)
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("option='audi' value='A'", ["option"])
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(None, "option")
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(234, "src")
    with self.assertRaises(Exception):
      attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(123, None)

  def test_extractDifferentValuesFromHtmlAttributesByKey_emptyAttributes(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("", "title")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("", "src")
    self.assertEqual(attributes, None)

  def test_extractDifferentValuesFromHtmlAttributesByKey_attrNotFound(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                                             "href=\"img/favicon.ico\" type=\"image/x-icon\"", "title")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\""
                                                       "masthead_custom_styles\" is=\"custom-style\" id=\"ext-styles\" "
                                                       "nonce=\"tG2l8WDVY7XYzWdAOVtRzA\"", "style")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                                              "src=\"jsbin/spf.vflset/spf.js\"", "alt")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"anim\"", "id")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"animated bold\"", "id")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"animated bold\" "
                                                                                "selected class=\"active-tab\"", "id")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "upgrade")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "masthead")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "dark")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "shell")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "chunked")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "e")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "disable")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "clas")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "lot")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("_value=\"audi\"", "value")
    self.assertEqual(attributes, None)

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_attrIsNotKeyValue(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\" selected",
                                                                                         "selected")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\" selected "
                                                                                       "class=\"myClass\"", "selected")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("selected value=\"audi\"",
                                                                                         "selected")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("selected", "selected")
    self.assertEqual(attributes, None)

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_emptyValue(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"\"", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"  \"", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"\t\"", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\" \r\n \t \"", "value")
    self.assertEqual(attributes, [])

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_corrupt(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"   ", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value= ", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value= \n \t ", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi'", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='audi\"", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value \"audi\"", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value\"audi\"", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value 'audi'", "value")
    self.assertEqual(attributes, None)
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value'audi'", "value")
    self.assertEqual(attributes, None)

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_quotes(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\"", "value")
    self.assertEqual(attributes, ["audi"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='audi'", "value")
    self.assertEqual(attributes, ["audi"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi'A3\"", "value")
    self.assertEqual(attributes, ["audi'A3"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi'A3'\"", "value")
    self.assertEqual(attributes, ["audi'A3'"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='audi\"A3'", "value")
    self.assertEqual(attributes, ["audi\"A3"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='\"audi\"A3\"'", "value")
    self.assertEqual(attributes, ["\"audi\"A3\""])

  def test_extractDifferentValuesFromHtmlAttributesByKey_oneValueFound(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                                             "href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, ["img/favicon.ico"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                                   "href=\"img/favicon.ico\" id='X' type=\"image/x-icon\"", "id")
    self.assertEqual(attributes, ["X"])
    # I have found these tricky examples while implementing beforeWhitespaceDelimitedFind as an effort to minimize
    # code length
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                            "xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, ["img/favicon.ico"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                          "no-href=\"false\" xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, ["img/favicon.ico"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
        "hrefhref=\"image\" no-href=\"false\" xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href")
    self.assertEqual(attributes, ["img/favicon.ico"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                                            "nonce=\"lix9PsSUHJxW7ghXrU5s0A\"", "nonce")
    self.assertEqual(attributes, ["lix9PsSUHJxW7ghXrU5s0A"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "disable-upgrade")
    self.assertEqual(attributes, ["true"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"preload\" href="
                                "\"https://r3---sn-8vq54voxgv-vu26.googlevideo.com/generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])

  def test_extractDifferentValuesFromHtmlAttributesByKey_whitespaces(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                         "rel =\"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                          "rel = \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                          "rel= \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                    "rel \n\r\t\t\t = \n\r\t\t\t \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                "\n\trel \n\r\t\t\t = \n\r\t\t\t \"preload\" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
          "\n\trel \n\r\t\t\t = \n\r\t\t\t \"\r\n\t\t preload \t\t\t\n\t  \" href=\"generate_204\" as=\"fetch\"", "rel")
    self.assertEqual(attributes, ["preload"])

  def test_extractDifferentValuesFromHtmlAttributesByKey_multipleValuesFound(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                "method=\"get\" class=\"add_search_params pure-form\" style=\"display:inline-block\"",
                                "class")
    self.assertEqual(attributes, ["add_search_params", "pure-form"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                "method=\"get\" class=\"add_search_params pure-form hide-xs hide-sm hide-md\" "
                                "style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, ["add_search_params", "pure-form", "hide-xs", "hide-sm", "hide-md"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                "method=\"get\" class\n=\n\"add_search_params\tpure-form\r\nhide-xs     hide-sm"
                                "\t\t\t\n\r   \n\r    hide-md\n\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, ["add_search_params", "pure-form", "hide-xs", "hide-sm", "hide-md"])

  def test_extractDifferentValuesFromHtmlAttributesByKey_multipleDeclarations(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
              "method=\"get\" class=\"add_search_params cl2 cl3\" class=\"pure-form\" style=\"display:inline-block\"",
              "class")
    self.assertEqual(attributes, ["add_search_params", "cl2", "cl3"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
              "method=\"get\" class=\"add_search_params\" class=\"pure-form cl2 cl3\" style=\"display:inline-block\"",
              "class")
    self.assertEqual(attributes, ["add_search_params"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" class "
                              "method=\"get\" class=\"pure-form cl2 cl3\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, None)

  def test_extractDifferentValuesFromHtmlAttributesByKey_valueRepeats(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                            "method=\"get\" class=\"cl1 cl1\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, ["cl1"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                            "method=\"get\" class=\"cl1 cl1 cl2 cl1 cl3 cl2\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, ["cl1", "cl2", "cl3"])

  def test_getNextHtmlAttribute_nonSense(self):
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("class = 'myClass'", None)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("class = 'myClass'", False)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("class = 'myClass'", "12")
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("class = 'myClass'", -1)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("class = 'myClass'", 488)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute("", 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute(123, 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute(True, 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute(None, 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute(True, False)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttribute(None, None)

  def helper_getNextHtmlAttribute_testInvalidOutput(self, attributeName, attributeValue, startIdx, endIdx):
    self.assertEqual(attributeName, None)
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, -1)
    self.assertEqual(endIdx, -1)

  def test_getNextHtmlAttribute_attributeNotFound(self):
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" ", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id='content' ", 12)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("\n  \t\t\t    \r\n", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected id='x'\n  \t\t\t    \r\n", 16)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected id='x'\n  \t\t\t    \r\n", 18)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)

  def test_getNextHtmlAttribute_corrupt(self):
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("=", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("'\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("\"'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("\"\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("''", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("\"value\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("'value'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("\"\"\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("'''", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("=value", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("='value'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("= 'value'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("\t= 'value'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class= ='myClass'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class=='myClass'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class==='myClass'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class == 'myClass'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class =  = 'myClass'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class=", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class=\t", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class =", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class\t=", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class \t \t =", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class\t=\t", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("class \t\t\t = \t\t \n", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value=\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value=\"   ", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value=\t \"   ", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value=\t \"   class='bordered'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value=\"audi", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value=\"audi\r\n", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value=\"audi\r\n selected", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value=\"audi'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value=\"audi' class='black-bg'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value=\"audi' selected", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value='audi\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value='audi\" selected", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value='audi\" id=\"my-id\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value \"audi\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value  \"audi\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value \t\t\t \"audi\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value\"audi\"", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value 'audi'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value\t\t'audi'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value\t\t'audi' selected", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value 'audi'\n", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value 'audi'\n selected", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value'audi'", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("value'audi' selected", 0)
    self.helper_getNextHtmlAttribute_testInvalidOutput(attributeName, attributeValue, startIdx, endIdx)

  def test_getNextHtmlAttribute_noAttributeValue(self):
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("x", 0)
    self.assertEqual(attributeName, "x")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 0)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected class=\"my-class\" "
                                                                                "no-href id='my-id'", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected  \t \n  class=\"my-class\" "
                                                                                "no-href id='my-id'", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected ", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected\t\n\t", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected\t animated\nid=\"my-id\"", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" selected", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, 8)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" selected minimized", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, 8)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" \t  \r\n  selected", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 8)
    self.assertEqual(endIdx, 15)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" \t  \r\n  selected class='abc'", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 8)
    self.assertEqual(endIdx, 15)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(" selected ", 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, 8)
    string = " \t  \r\n  selected\t\t\t\r\n"
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(string, 0)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 8)
    self.assertEqual(endIdx, string.find("d\t\t"))

  def test_getNextHtmlAttribute_attributeValue(self):
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id='my-id'", 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "my-id")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 9)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id=\"my-id\"", 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "my-id")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 9)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id = 'my-id'", 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "my-id")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 11)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id = ' my-id ' ", 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " my-id ")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 13)
    string = "id \t\n= \n\t' \tmy-id '\n "
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(string, 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " \tmy-id ")
    self.assertEqual(startIdx, 0)
    self.assertTrue(endIdx > startIdx)
    self.assertEqual(endIdx, string.find("'\n "))
    string = "\t\r\n id \t\n= \n\t' \tmy-id '\r\n "
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(string, 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " \tmy-id ")
    self.assertEqual(startIdx, 4)
    self.assertEqual(endIdx, string.find("'\r\n "))
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id = 'id1 id2'", 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "id1 id2")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 13)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id = ' id1 id2 id3 '", 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " id1 id2 id3 ")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 19)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("\tid = '\r\n id1 id2 id3 \n\t'\t\t", 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "\r\n id1 id2 id3 \n\t")
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, 24)
    string = "\tid = '\r\n id1 \t id2 \t id3 \n\t'\t\t"
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(string, 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "\r\n id1 \t id2 \t id3 \n\t")
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, string.find("'\t\t"))
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("id = 'id1 id2' id=\"my-other-id\"", 0)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "id1 id2")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 13)

  def test_getNextHtmlAttribute_startIdxGreaterThan1(self):
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected", 2)
    self.assertEqual(attributeName, "lected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 2)
    self.assertEqual(endIdx, 7)
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute("selected='False'", 3)
    self.assertEqual(attributeName, "ected")
    self.assertEqual(attributeValue, "False")
    self.assertEqual(startIdx, 3)
    self.assertEqual(endIdx, 15)
    string = "\nselected\nclass\t=\t\"\tcl1\tcl2\tcl3 \" class id=\"my-id\"\n"
    attributeName, attributeValue, startIdx, endIdx = attr.getNextHtmlAttribute(string, string.find("class"))
    self.assertEqual(attributeName, "class")
    self.assertEqual(attributeValue, "\tcl1\tcl2\tcl3 ")
    self.assertTrue(startIdx > -1)
    self.assertTrue(endIdx > startIdx)
    self.assertEqual(startIdx, string.find("class"))
    self.assertEqual(endIdx, string.find("\" class id=\"my-id\""))

  def test_getListOfHtmlAttributeNames_nonSense(self):
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributeNames(12)
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributeNames(None)
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributeNames(False)
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributeNames([])

  def test_getListOfHtmlAttributeNames_onlyEmptyAndWhiteSpace(self):
    attributes = attr.getListOfHtmlAttributeNames("")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames(" ")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("\t")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("\n")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("  \t\t\t\t \r\r  ")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("\n      \t   \t        \n")
    self.assertEqual(attributes, [])

  def test_getListOfHtmlAttributeNames_corruptAttributes(self):
    attributes = attr.getListOfHtmlAttributeNames("=")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("=12")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("='value'")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("'value'")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames(" = 'value'")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("\t\t=\t\t\" value \"")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected=")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames(" \t\t selected\n = \t")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected = \"")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected = '")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected = \"value")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected = 'value")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected 'value'")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected'value'")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected=='value'")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected= ='value'")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected == 'value'")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected 'value")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected'value")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected = \"value'")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("selected = 'value\"")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributeNames("class=\"example\" selected = 'value\" animated")
    self.assertEqual(attributes, [])

  def test_getListOfHtmlAttributeNames_oneAttribute(self):
    attributes = attr.getListOfHtmlAttributeNames("a")
    self.assertEqual(attributes, ["a"])
    attributes = attr.getListOfHtmlAttributeNames("selected")
    self.assertEqual(attributes, ["selected"])
    attributes = attr.getListOfHtmlAttributeNames(" \n  \t selected \n\r \t ")
    self.assertEqual(attributes, ["selected"])
    attributes = attr.getListOfHtmlAttributeNames("selected \n\r \t ")
    self.assertEqual(attributes, ["selected"])
    attributes = attr.getListOfHtmlAttributeNames(" \n  \t selected")
    self.assertEqual(attributes, ["selected"])
    attributes = attr.getListOfHtmlAttributeNames("style=\"float:right;margin:11px 14px 0 0;"
                                                     "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98\"")
    self.assertEqual(attributes, ["style"])
    attributes = attr.getListOfHtmlAttributeNames("style='float:right;margin:11px 14px 0 0;"
                                                     "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98'")
    self.assertEqual(attributes, ["style"])
    attributes = attr.getListOfHtmlAttributeNames(" \n\r style\t\t\t=\n'float:right;margin:11px 14px 0 0;"
                                               "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98' \n\r ")
    self.assertEqual(attributes, ["style"])
    attributes = attr.getListOfHtmlAttributeNames("style\t\t\t=\n'float:right;margin:11px 14px 0 0;"
                                               "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98' \n\r ")
    self.assertEqual(attributes, ["style"])
    attributes = attr.getListOfHtmlAttributeNames(" \n\r style\t\t\t=\n'\t\tfloat:right;margin:11px 14px 0 0;"
                                         "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98\t\t' \n\r ")
    self.assertEqual(attributes, ["style"])
    attributes = attr.getListOfHtmlAttributeNames("\nproperty\n=\n\"\narticle:published_time\n\"\n")
    self.assertEqual(attributes, ["property"])
    attributes = attr.getListOfHtmlAttributeNames("\nproperty\n=\n\"\narticle:published_time\"")
    self.assertEqual(attributes, ["property"])
    attributes = attr.getListOfHtmlAttributeNames("property\n=\n\"\narticle:published_time\n\"\n")
    self.assertEqual(attributes, ["property"])

  def test_getListOfHtmlAttributeNames_moreAttributes(self):
    attributes = attr.getListOfHtmlAttributeNames("selected id=\"logo\"")
    self.assertEqual(attributes, ["selected", "id"])
    attributes = attr.getListOfHtmlAttributeNames("id=\"logo\" selected")
    self.assertEqual(attributes, ["id", "selected"])
    attributes = attr.getListOfHtmlAttributeNames("id=\"logo\" selected id=\"otherId\" selected='true'")
    self.assertEqual(attributes, ["id", "selected"])
    attributes = attr.getListOfHtmlAttributeNames("\tonclick\t=\t\"\tlocation.reload();\t\" style\n=\"float:right;"
          "display:inline-block;position:relative;top:15px;right:3px;margin-left:10px;font-size:13px;cursor:pointer\" "
                                                     "title='Exclude inappropriate or explicit images'")
    self.assertEqual(attributes, ["onclick", "style", "title"])
    attributes = attr.getListOfHtmlAttributeNames("rel=\"alternate\" type=\"application/rss+xml\" "
                     "title=\"Matematika és Informatika Kar RSS Feed\" href=\"https://www.cs.ubbcluj.ro/hu/feed/\"")
    self.assertEqual(attributes, ["rel", "type", "title", "href"])

  def test_getNextHtmlAttributeValueIfExists_nonSense(self):
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists(None, None)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists(False, 0)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists("= 'value'", True)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists("= 'value'", 56)
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists("= 'value'", -1)

  def test_getNextHtmlAttributeValueIfExists_emptyString(self):
    with self.assertRaises(Exception):
      attr.getNextHtmlAttributeValueIfExists("", 0)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("='value' ", 8)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def test_getNextHtmlAttributeValueIfExists_spaces(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" \t\t\n", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" \t\t \n ", 3)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(self, corrupt, firstQuoteIdx, secondQuoteIdx):
    self.assertTrue(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(self, corrupt, firstQuoteIdx, secondQuoteIdx):
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def test_getNextHtmlAttributeValueIfExists_corrupt(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("==", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=========", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("''", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\"\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("'value'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\"value\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("='\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\"'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= \t \n", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= \n\t value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= value ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\t\t\n = \n\tvalue\n\n\n", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=2", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= 2", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=value\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=value'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\"value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("='value", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\"value'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("='value\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= \"value'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("= 'value\"", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=   \"  value  '  ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=  '  value  \"  ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\t\t=   \"  value  '  ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=  '  value  \"  ", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfCorrupt(corrupt, firstQuoteIdx, secondQuoteIdx)

  def test_getNextHtmlAttributeValueIfExists_noValue(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("X", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("attrName", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("multiple attribute names", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("attrName\t", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\tattrName", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("attrName\t\n", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\tattrName", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("   \t attrName  \t\t  \t", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("selected class='myClass'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(
                                                                                  "\t\tselected\n\nclass='myClass'", 0)
    self.helper_getNextHtmlAttributeValueIfExists_checkIfNoValue(corrupt, firstQuoteIdx, secondQuoteIdx)

  def test_getNextHtmlAttributeValueIfExists_emptyValue(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\"\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 1)
    self.assertEqual(secondQuoteIdx, 2)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" = \"\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 3)
    self.assertEqual(secondQuoteIdx, 4)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t\"\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 8)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t'' ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 8)

  def test_getNextHtmlAttributeValueIfExists_whiteSpaceValue(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\" \"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 1)
    self.assertEqual(secondQuoteIdx, 3)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" = \"\n\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 3)
    self.assertEqual(secondQuoteIdx, 5)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t\"\t\n\t\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 11)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t'\t\n\t' ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 11)

  def test_getNextHtmlAttributeValueIfExists_nonEmptyValue(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("=\"value\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 1)
    self.assertEqual(secondQuoteIdx, 7)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" = \"value\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 3)
    self.assertEqual(secondQuoteIdx, 9)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t\"value\" ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 13)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t'value' ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 13)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t'\t value\n\n' ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 17)

  def test_getNextHtmlAttributeValueIfExists_nonZeroStartIdx(self):
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t'\t value\n\n' ", 2)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 17)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t\"\t\n\t\" ", 3)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 7)
    self.assertEqual(secondQuoteIdx, 11)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists("\n\n\n=\t\t\t\"\t\n\t\" ", 4)
    self.assertTrue(corrupt)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)
    corrupt, firstQuoteIdx, secondQuoteIdx = attr.getNextHtmlAttributeValueIfExists(" = \"\" ", 1)
    self.assertFalse(corrupt)
    self.assertEqual(firstQuoteIdx, 3)
    self.assertEqual(secondQuoteIdx, 4)

