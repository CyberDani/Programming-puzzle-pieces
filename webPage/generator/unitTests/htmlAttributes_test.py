import sys
import unittest

sys.path.append('..')

from defTypes.filePathType import FilePathType as File

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
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("", "src")
    self.assertEqual(attributes, [])

  def test_extractDifferentValuesFromHtmlAttributesByKey_attrNotFound(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("rel=\"shortcut icon\" "
                                                             "href=\"img/favicon.ico\" type=\"image/x-icon\"", "title")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\""
                                                       "masthead_custom_styles\" is=\"custom-style\" id=\"ext-styles\" "
                                                       "nonce=\"tG2l8WDVY7XYzWdAOVtRzA\"", "style")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey(
                                                                              "src=\"jsbin/spf.vflset/spf.js\"", "alt")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"anim\"", "id")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"animated bold\"", "id")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("class=\"animated bold\" "
                                                                                "selected class=\"active-tab\"", "id")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "upgrade")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "masthead")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "dark")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "shell")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "chunked")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "e")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "disable")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "clas")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("id=\"masthead\" "
                                            "logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" "
                                            "disable-upgrade=\"true\"", "lot")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("_value=\"audi\"", "value")
    self.assertEqual(attributes, [])

  def test_extractDifferentSpaceSeparatedValuesFromHtmlAttributesByKey_attrIsNotKeyValue(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\" selected",
                                                                                         "selected")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi\" selected "
                                                                                       "class=\"myClass\"", "selected")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("selected value=\"audi\"",
                                                                                         "selected")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("selected", "selected")
    self.assertEqual(attributes, [])

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
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"   ", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value= ", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value= \n \t ", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value=\"audi'", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value='audi\"", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value \"audi\"", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value\"audi\"", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value 'audi'", "value")
    self.assertEqual(attributes, [])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("value'audi'", "value")
    self.assertEqual(attributes, [])

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
    self.assertEqual(attributes, [])

  def test_extractDifferentValuesFromHtmlAttributesByKey_valueRepeats(self):
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                                            "method=\"get\" class=\"cl1 cl1\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, ["cl1"])
    attributes = attr.extractDifferentWhiteSpaceSeparatedValuesFromHtmlAttributesByKey("action=\".\" "
                            "method=\"get\" class=\"cl1 cl1 cl2 cl1 cl3 cl2\" style=\"display:inline-block\"", "class")
    self.assertEqual(attributes, ["cl1", "cl2", "cl3"])

  def test_getListOfHtmlAttributes_nonSense(self):
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributes(12)
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributes(None)
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributes(False)
    with self.assertRaises(Exception):
      attr.getListOfHtmlAttributes([])

  def test_getListOfHtmlAttributes_onlyEmptyAndWhiteSpace(self):
    attributes = attr.getListOfHtmlAttributes("")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes(" ")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("\t")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("\n")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("  \t\t\t\t \r\r  ")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("\n      \t   \t        \n")
    self.assertEqual(attributes, [])

  def test_getListOfHtmlAttributes_corruptAttributes(self):
    attributes = attr.getListOfHtmlAttributes("selected=")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes(" \t\t selected\n = \t")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("selected = \"")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("selected = '")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("selected = \"value")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("selected = 'value")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("selected = \"value'")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("selected = 'value\"")
    self.assertEqual(attributes, [])
    attributes = attr.getListOfHtmlAttributes("class=\"example\" selected = 'value\" animated")
    self.assertEqual(attributes, [])

  def test_getListOfHtmlAttributes_oneAttribute(self):
    attributes = attr.getListOfHtmlAttributes("selected")
    self.assertEqual(attributes, ["selected"])
    attributes = attr.getListOfHtmlAttributes(" \n  \t selected \n\r \t ")
    self.assertEqual(attributes, ["selected"])
    attributes = attr.getListOfHtmlAttributes("selected \n\r \t ")
    self.assertEqual(attributes, ["selected"])
    attributes = attr.getListOfHtmlAttributes(" \n  \t selected")
    self.assertEqual(attributes, ["selected"])
    attributes = attr.getListOfHtmlAttributes("style=\"float:right;margin:11px 14px 0 0;"
                                                     "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98\"")
    self.assertEqual(attributes, ["style"])
    attributes = attr.getListOfHtmlAttributes("style='float:right;margin:11px 14px 0 0;"
                                                     "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98'")
    self.assertEqual(attributes, ["style"])
    attributes = attr.getListOfHtmlAttributes(" \n\r style\t\t\t=\n'float:right;margin:11px 14px 0 0;"
                                               "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98' \n\r ")
    self.assertEqual(attributes, ["style"])
    attributes = attr.getListOfHtmlAttributes(" \n\r style\t\t\t=\n'\t\tfloat:right;margin:11px 14px 0 0;"
                                         "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98\t\t' \n\r ")
    self.assertEqual(attributes, ["style"])
    attributes = attr.getListOfHtmlAttributes("\nproperty\n=\n\"\narticle:published_time\n\"\n")
    self.assertEqual(attributes, ["property"])
    attributes = attr.getListOfHtmlAttributes("\nproperty\n=\n\"\narticle:published_time\"")
    self.assertEqual(attributes, ["property"])
    attributes = attr.getListOfHtmlAttributes("property\n=\n\"\narticle:published_time\n\"\n")
    self.assertEqual(attributes, ["property"])

  def test_getListOfHtmlAttributes_moreAttributes(self):
    attributes = attr.getListOfHtmlAttributes("selected id=\"logo\"")
    self.assertEqual(attributes, ["selected", "id"])
    attributes = attr.getListOfHtmlAttributes("id=\"logo\" selected")
    self.assertEqual(attributes, ["id", "selected"])
    attributes = attr.getListOfHtmlAttributes("id=\"logo\" selected id=\"otherId\" selected='true'")
    self.assertEqual(attributes, ["id", "selected"])
    attributes = attr.getListOfHtmlAttributes("\tonclick\t=\t\"\tlocation.reload();\t\" style\n=\"float:right;"
          "display:inline-block;position:relative;top:15px;right:3px;margin-left:10px;font-size:13px;cursor:pointer\" "
                                                     "title='Exclude inappropriate or explicit images'")
    self.assertEqual(attributes, ["onclick", "style", "title"])
    attributes = attr.getListOfHtmlAttributes("rel=\"alternate\" type=\"application/rss+xml\" "
                     "title=\"Matematika és Informatika Kar RSS Feed\" href=\"https://www.cs.ubbcluj.ro/hu/feed/\"")
    self.assertEqual(attributes, ["rel", "type", "title", "href"])
