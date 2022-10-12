import sys
import unittest

sys.path.append('..')

from modules import htmlAttributes as attr

class HtmlAttributesTests(unittest.TestCase):

  def helper_getAttributeNameIdx_checkIfCorrupt(self, htmlAttributes, key):
    corrupt, keyFound, idx = attr.getAttributeNameIdx(htmlAttributes, key)
    self.assertTrue(corrupt)
    self.assertIsNone(keyFound)
    self.assertEqual(idx, -1)

  def helper_getAttributeNameIdx_checkIfNotFound(self, htmlAttributes, key):
    corrupt, keyFound, idx = attr.getAttributeNameIdx(htmlAttributes, key)
    self.assertFalse(corrupt)
    self.assertFalse(keyFound)
    self.assertEqual(idx, -1)

  def helper_getAttributeNameIdx_checkIfFoundAtIdx(self, htmlAttributes, key, foundAt):
    corrupt, keyFound, idx = attr.getAttributeNameIdx(htmlAttributes, key)
    self.assertFalse(corrupt)
    self.assertTrue(keyFound)
    self.assertEqual(idx, foundAt)

  def test_getAttributeNameIdx_nonSense(self):
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx("htmlAttribute", 12)
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx("htmlAttribute", None)
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx(None, None)
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx(12, False)
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx(None, "class")
    with self.assertRaises(Exception):
      attr.getAttributeNameIdx(False, "id")

  def test_getAttributeNameIdx_emptyString(self):
    self.helper_getAttributeNameIdx_checkIfNotFound("", "class")
    self.helper_getAttributeNameIdx_checkIfNotFound("id=\"content\" class=\"clearfix\"", "")

  def test_getAttributeNameIdx_corrupt_keyContainsHtmlDelimiter(self):
    self.helper_getAttributeNameIdx_checkIfCorrupt("selected default", " ")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='cl1 cl2'", "cl1 cl2")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='cl1 cl2'", " cl2")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='cl1 cl2'", "class=")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='myClass'", "'myClass'")

  def test_getAttributeNameIdx_corrupt(self):
    self.helper_getAttributeNameIdx_checkIfCorrupt("value='234'' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value=''234' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value='''234' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value=''''234' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value=''''234' selected'", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value='234''' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("value='234'''' selected", "selected")
    self.helper_getAttributeNameIdx_checkIfCorrupt("style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("style''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt(" 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("\t\r\n'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt(" ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("\t\t='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("\" ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'class' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class ='style myClass", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class ='style myClass'\"", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("''' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'''' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("''''' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'''''' ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("\"\" ='style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title =\t= 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = ''style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = 'style''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = ''style''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = style''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = style'''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = style''''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = '''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = ''''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = '''''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = ''''''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = ''''style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = 'style' =", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = 'style' '", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = 'style'''", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title = 'style' \"something", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'title' = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title' = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title'' = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title''' = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title\" = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("\"title\" = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title\"\" = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title\"\"\" = 'style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title='\"style'\"", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title=\"'style\"'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title=\"'hello' my 'style\"'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title=\"'hello' my 'style\"'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("title=\"'hello\" my 'style\"'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class=style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class=style'", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class=custom style red", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='custom style red", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='custom style red\"", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='style red", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class='custom style", "style")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'class my-class' class='myClass'", "class")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class'myClass' class='myClass'", "class")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'class title=\"heyo\"", "class")
    self.helper_getAttributeNameIdx_checkIfCorrupt("class' title=\"heyo\"", "class")
    self.helper_getAttributeNameIdx_checkIfCorrupt("'class' title=\"heyo\"", "class")
    self.helper_getAttributeNameIdx_checkIfCorrupt("b = 'a=\"2\"", "a")

  def test_getAttributeNameIdx_attrNotFound(self):
    self.helper_getAttributeNameIdx_checkIfNotFound("ax xa", "a")
    self.helper_getAttributeNameIdx_checkIfNotFound("aa", "a")
    self.helper_getAttributeNameIdx_checkIfNotFound("aaa", "a")
    self.helper_getAttributeNameIdx_checkIfNotFound("xacca", "a")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"'style\"selected", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"'style\" selected", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"'style\"", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"''style\"", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"''style'\"", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"''style''\"", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"'''''style\"", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('title="My \'fancy\' style"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('title="My style is \'not fancy\'"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('title="My \'fancy\' style is \'not fancy\'"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('title="My \'style\' is hardcore" id="red"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('class="style"id="red"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound('class="style"id="style"', "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("class='custom style red'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("id=\"myId\" class='custom style red'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("class='custom-style'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("class='custom-style-red'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("class='style-custom'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("class='style'", "style")
    self.helper_getAttributeNameIdx_checkIfNotFound("htmlAttribute", "class")
    self.helper_getAttributeNameIdx_checkIfNotFound("htmlAttribute no-href", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("htmlAttribute hrefx", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("htmlAttribute hrefhref", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("no-href class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("hrefx class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("hrefhref class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("selected no-href class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("selected hrefx class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("selected hrefhref class='idk'", "href")
    self.helper_getAttributeNameIdx_checkIfNotFound("b = 'a=\"2\"'", "a")

  def test_getAttributeNameIdx_attrNotFound_cornerCase(self):
    self.helper_getAttributeNameIdx_checkIfNotFound("b = 'a=\"2\"", "class")
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("b = 'a=\"2\"", "b", foundAt=0)

  def test_getAttributeNameIdx_attrNotFound_equalWithinAttributeValue(self):
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"class='myClass'\"", "class")
    self.helper_getAttributeNameIdx_checkIfNotFound("title=\"class='class='myClass''\"", "class")

  def test_getAttributeNameIdx_attrFound(self):
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("a", "a", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected", "selected", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("default='1'", "default", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("default=\"1\"", "default", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("default=\"1\"selected", "default", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("default=\"1\"selected", "selected", foundAt = 11)
    string = "value='234' selected"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "selected", foundAt = string.find("selected"))
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected class=\"className\"", "selected", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected greyed-out", "selected", foundAt = 0)
    string = "value='234' selected=\"false\""
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "selected", foundAt = string.find("selected"))
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected=\"false\" class=\"className\"", "selected", foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected=\"false\" greyed-out", "selected", foundAt = 0)
    string = "htmlAttribute no-href href"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find(" href") + 1)
    string = "htmlAttribute hrefx href=\"value\""
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find("href="))
    string = "htmlAttribute hrefhref='value2' href='value3'"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find("href='value3'"))
    string = "no-href=\"noValue\" href class='idk'"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find("href class"))
    string = "hrefx href class='idk'"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find("href class"))

  def test_getAttributeNameIdx_attrFoundMultipleTime(self):
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("selected selected='false' selected selected", "selected",
                                                      foundAt = 0)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("default='1' class=\"myClass\" default", "default", foundAt = 0)
    string = "htmlAttribute hrefhref='value2' href='value3' href href='val4'"
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx(string, "href", foundAt = string.find("href='value3'"))

  def test_getAttributeNameIdx_attrFound_equalWithinAttributeValue(self):
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("title=\"class='myClass'\"class='myClass'", "class", foundAt = 23)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("title=\"class='myClass'\" class='myClass'", "class", foundAt=24)
    self.helper_getAttributeNameIdx_checkIfFoundAtIdx("title=\"class='myClass'\"\t\t\tclass\n\t=\t\t'myClass'", "class",
                                                      foundAt = 26)

  def helper_getUniqueValuesByName_checkIfException(self, string, name):
    with self.assertRaises(Exception):
      attr.getUniqueValuesByName(string, name)

  def helper_getUniqueValuesByName_checkIfCorrupt(self, string, name):
    corrupt, nameFound, valueFound, values = attr.getUniqueValuesByName(string, name)
    self.assertTrue(corrupt)
    self.assertFalse(nameFound)
    self.assertFalse(valueFound)
    self.assertEqual(values, [])

  def helper_getUniqueValuesByName_checkIfNameNotFound(self, string, name):
    corrupt, nameFound, valueFound, values = attr.getUniqueValuesByName(string, name)
    self.assertFalse(corrupt)
    self.assertFalse(nameFound)
    self.assertFalse(valueFound)
    self.assertEqual(values, [])

  def helper_getUniqueValuesByName_checkIfValueNotFound(self, string, name):
    corrupt, nameFound, valueFound, values = attr.getUniqueValuesByName(string, name)
    self.assertFalse(corrupt)
    self.assertTrue(nameFound)
    self.assertFalse(valueFound)
    self.assertEqual(values, [])

  def helper_getUniqueValuesByName_checkIfFound(self, string, name, foundValues):
    corrupt, nameFound, valueFound, values = attr.getUniqueValuesByName(string, name)
    self.assertFalse(corrupt)
    self.assertTrue(nameFound)
    self.assertTrue(valueFound)
    self.assertEqual(values, foundValues)

  def test_getUniqueValuesByName_nonSense(self):
    self.helper_getUniqueValuesByName_checkIfException("option='audi' value='A'", 123)
    self.helper_getUniqueValuesByName_checkIfException("option='audi' value='A'", False)
    self.helper_getUniqueValuesByName_checkIfException("option='audi' value='A'", None)
    self.helper_getUniqueValuesByName_checkIfException("option='audi' value='A'", ["option"])
    self.helper_getUniqueValuesByName_checkIfException(None, "option")
    self.helper_getUniqueValuesByName_checkIfException(234, "src")
    self.helper_getUniqueValuesByName_checkIfException(123, None)
    self.helper_getUniqueValuesByName_checkIfException(None, None)
    self.helper_getUniqueValuesByName_checkIfException(0, 0)

  def test_getUniqueValuesByName_emptyName(self):
    self.helper_getUniqueValuesByName_checkIfException("option='audi' value='A'", "")

  def test_getUniqueValuesByName_emptyAttributesString(self):
    self.helper_getUniqueValuesByName_checkIfNameNotFound("", "title")
    self.helper_getUniqueValuesByName_checkIfNameNotFound("", "src")

  def test_getUniqueValuesByName_attributeNameNotFound(self):
    self.helper_getUniqueValuesByName_checkIfNameNotFound("htmlAttribute no-href", "href")
    self.helper_getUniqueValuesByName_checkIfNameNotFound("rel=\"shortcut icon\" href=\"img/favicon.ico\" "
                                                      "type=\"image/x-icon\"", "title")
    self.helper_getUniqueValuesByName_checkIfNameNotFound("class=\"masthead_custom_styles\" is=\"custom-style\" "
                                                      "id=\"ext-styles\" nonce=\"tG2l8WDVY7XYzWdAOVtRzA\"", "style")
    self.helper_getUniqueValuesByName_checkIfNameNotFound("src=\"jsbin/spf.vflset/spf.js\"", "alt")
    self.helper_getUniqueValuesByName_checkIfNameNotFound("class=\"anim\"", "id")
    self.helper_getUniqueValuesByName_checkIfNameNotFound("class=\"animated bold\"", "id")
    self.helper_getUniqueValuesByName_checkIfNameNotFound("class=\"animated bold\" selected class=\"act-tab\"", "id")
    string = "id=\"masthead\" logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" " \
             "disable-upgrade=\"true\""
    self.helper_getUniqueValuesByName_checkIfNameNotFound(string, "upgrade")
    self.helper_getUniqueValuesByName_checkIfNameNotFound(string, "masthead")
    self.helper_getUniqueValuesByName_checkIfNameNotFound(string, "dark")
    self.helper_getUniqueValuesByName_checkIfNameNotFound(string, "shell")
    self.helper_getUniqueValuesByName_checkIfNameNotFound(string, "chunked")
    self.helper_getUniqueValuesByName_checkIfNameNotFound(string, "e")
    self.helper_getUniqueValuesByName_checkIfNameNotFound(string, "disable")
    self.helper_getUniqueValuesByName_checkIfNameNotFound(string, "clas")
    self.helper_getUniqueValuesByName_checkIfNameNotFound(string, "lot")
    self.helper_getUniqueValuesByName_checkIfNameNotFound("_value=\"audi\"", "value")

  def test_getUniqueValuesByName_attrDoesNotHaveValue(self):
    self.helper_getUniqueValuesByName_checkIfValueNotFound("value=\"audi\" selected", "selected")
    self.helper_getUniqueValuesByName_checkIfValueNotFound("value=\"audi\" selected class=\"myClass\"", "selected")
    self.helper_getUniqueValuesByName_checkIfValueNotFound("selected value=\"audi\"", "selected")
    self.helper_getUniqueValuesByName_checkIfValueNotFound("selected", "selected")

  def test_getUniqueValuesByName_emptyValue(self):
    self.helper_getUniqueValuesByName_checkIfFound("value=\"\"", "value", foundValues=[])
    self.helper_getUniqueValuesByName_checkIfFound("value=\"  \"", "value", foundValues=[])
    self.helper_getUniqueValuesByName_checkIfFound("value=\"\t\"", "value", foundValues=[])
    self.helper_getUniqueValuesByName_checkIfFound("value=\" \r\n \t \"", "value", foundValues=[])

  def test_getUniqueValuesByName_corrupt_nameContainsHtmlDelimiter(self):
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", "selected class")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", "class=")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", " class")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", " class ")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", "selected ")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", "red '")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", "'custom")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", "=")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", "'")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", "\"")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", " ")
    self.helper_getUniqueValuesByName_checkIfCorrupt("selected class='custom style red'", "\t")

  def test_getUniqueValuesByName_corrupt(self):
    self.helper_getUniqueValuesByName_checkIfCorrupt("class='custom style red", "style")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value=\"", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value=\"   ", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value=", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value= ", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value= \n \t ", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value=\"audi", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value=\"audi'", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value='audi\"", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value \"audi\"", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value\"audi\"", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value 'audi'", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("value'audi'", "value")
    self.helper_getUniqueValuesByName_checkIfCorrupt("\"class'myclass' class='myclass'", "class")

  def test_getUniqueValuesByName_quotes(self):
    self.helper_getUniqueValuesByName_checkIfFound("value=\"audi\"", "value", foundValues=["audi"])
    self.helper_getUniqueValuesByName_checkIfFound("value='audi'", "value", foundValues=["audi"])
    self.helper_getUniqueValuesByName_checkIfFound("value=\"audi'A3\"", "value", foundValues=["audi'A3"])
    self.helper_getUniqueValuesByName_checkIfFound("value=\"audi'A3'\"", "value", foundValues=["audi'A3'"])
    self.helper_getUniqueValuesByName_checkIfFound("value='audi\"A3'", "value", foundValues=["audi\"A3"])
    self.helper_getUniqueValuesByName_checkIfFound("value='\"audi\"A3\"'", "value", foundValues=["\"audi\"A3\""])
    self.helper_getUniqueValuesByName_checkIfFound("class='myClass'title='titled title=\"title\"'", "title",
                                                   foundValues=["titled", "title=\"title\""])

  def test_getUniqueValuesByName_oneValueFound(self):
    self.helper_getUniqueValuesByName_checkIfFound("rel=\"shortcut icon\" href=\"img/favicon.ico\" "
                                                    "type=\"image/x-icon\"", "href", foundValues=["img/favicon.ico"])
    self.helper_getUniqueValuesByName_checkIfFound("rel=\"shortcut icon\" href=\"img/favicon.ico\" id='X' "
                                                    "type=\"image/x-icon\"", "id", foundValues=["X"])
    self.helper_getUniqueValuesByName_checkIfFound("rel=\"shortcut icon\" xhref=\"a34cd3b\" href=\"img/favicon.ico\" "
                                                   "type=\"image/x-icon\"", "href", foundValues=["img/favicon.ico"])
    self.helper_getUniqueValuesByName_checkIfFound("rel=\"shortcut icon\" no-href=\"false\" xhref=\"a34cd3b\" "
                                                    "href=\"img/favicon.ico\" type=\"image/x-icon\"", "href",
                                                   foundValues=["img/favicon.ico"])
    self.helper_getUniqueValuesByName_checkIfFound("rel=\"shortcut icon\" hrefhref=\"image\" no-href=\"false\" "
                                            "xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href",
                                                   foundValues=["img/favicon.ico"])
    self.helper_getUniqueValuesByName_checkIfFound("nonce=\"lix9PsSUHJxW7ghXrU5s0A\"", "nonce",
                                                   foundValues=["lix9PsSUHJxW7ghXrU5s0A"])
    self.helper_getUniqueValuesByName_checkIfFound("id=\"masthead\" logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\""
                                            " class=\"shell dark chunked\" disable-upgrade=\"true\"", "disable-upgrade",
                                                   foundValues=["true"])
    self.helper_getUniqueValuesByName_checkIfFound("rel=\"preload\" href="
                                "\"https://r3---sn-8vq54voxgv-vu26.googlevideo.com/generate_204\" as=\"fetch\"", "rel",
                                                   foundValues=["preload"])

  def test_getUniqueValuesByName_whitespaces(self):
    self.helper_getUniqueValuesByName_checkIfFound("rel =\"preload\" href=\"generate_204\" as=\"fetch\"", "rel",
                                                   foundValues=["preload"])
    self.helper_getUniqueValuesByName_checkIfFound("rel = \"preload\" href=\"generate_204\" as=\"fetch\"", "rel",
                                                   foundValues=["preload"])
    self.helper_getUniqueValuesByName_checkIfFound("rel= \"preload\" href=\"generate_204\" as=\"fetch\"", "rel",
                                                   foundValues=["preload"])
    self.helper_getUniqueValuesByName_checkIfFound("rel \n\r\t\t\t = \n\r\t\t\t \"preload\" "
                                                  "href=\"generate_204\" as=\"fetch\"", "rel", foundValues=["preload"])
    self.helper_getUniqueValuesByName_checkIfFound("\n\trel \n\r\t\t\t = \n\r\t\t\t \"preload\" "
                                                  "href=\"generate_204\" as=\"fetch\"", "rel", foundValues=["preload"])
    self.helper_getUniqueValuesByName_checkIfFound("\n\trel \n\r\t\t\t = \n\r\t\t\t \"\r\n\t\t preload "
                                                    "\t\t\t\n\t  \" href=\"generate_204\" as=\"fetch\"", "rel",
                                                   foundValues=["preload"])

  def test_getUniqueValuesByName_multipleValuesFound(self):
    self.helper_getUniqueValuesByName_checkIfFound("action=\".\" method=\"get\" class=\"add_search_params "
                                                    "pure-form\" style=\"display:inline-block\"", "class",
                                                   foundValues=["add_search_params", "pure-form"])
    self.helper_getUniqueValuesByName_checkIfFound("action=\".\" method=\"get\" class=\"add_search_params "
                                        "pure-form hide-xs hide-sm hide-md\" style=\"display:inline-block\"", "class",
                                       foundValues=["add_search_params", "pure-form", "hide-xs", "hide-sm", "hide-md"])
    self.helper_getUniqueValuesByName_checkIfFound("action=\".\" method=\"get\" class\n=\n\"add_search_params\t"
                                        "pure-form\r\nhide-xs     hide-sm\t\t\t\n\r   \n\r    hide-md\n\" "
                                        "style=\"display:inline-block\"", "class",
                                       foundValues=["add_search_params", "pure-form", "hide-xs", "hide-sm", "hide-md"])

  def test_getUniqueValuesByName_multipleDeclarations(self):
    self.helper_getUniqueValuesByName_checkIfFound("action=\".\" method=\"get\" class=\"add_search_params cl2 cl3\" "
                                                   "class=\"pure-form\" style=\"display:inline-block\"", "class",
                                                   foundValues=["add_search_params", "cl2", "cl3"])
    self.helper_getUniqueValuesByName_checkIfFound("action=\".\" method=\"get\" class=\"add_search_params\" "
                                                  "class=\"pure-form cl2 cl3\" style=\"display:inline-block\"", "class",
                                                   foundValues=["add_search_params"])
    self.helper_getUniqueValuesByName_checkIfValueNotFound("action=\".\" class method=\"get\" class=\"pure-form cl2 "
                                                           "cl3\" style=\"display:inline-block\"", "class")

  def test_getUniqueValuesByName_valueRepeats(self):
    self.helper_getUniqueValuesByName_checkIfFound("action=\".\" method=\"get\" class=\"cl1 cl1\" "
                                                    "style=\"display:inline-block\"", "class", foundValues=["cl1"])
    self.helper_getUniqueValuesByName_checkIfFound("action=\".\" method=\"get\" class=\"cl1 cl1 cl2 cl1 cl3 cl2\" "
                                                   "style=\"display:inline-block\"", "class",
                                                   foundValues=["cl1", "cl2", "cl3"])

  def test_getSafelyCurrentOrNextAttribute_nonSense(self):
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute("class = 'myClass'", None)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute("class = 'myClass'", False)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute("class = 'myClass'", "12")
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute("class = 'myClass'", -1)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute("class = 'myClass'", 488)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute("", 0)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute(123, 0)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute(True, 0)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute(None, 0)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute(True, False)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextAttribute(None, None)

  def helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt(self, string, startIdx):
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute(string, startIdx)
    self.assertTrue(corrupt)
    self.assertEqual(attributeName, None)
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, -1)
    self.assertEqual(endIdx, -1)

  def helper_getSafelyCurrentOrNextAttribute_checkIfNotFound(self, string, startIdx):
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute(string, startIdx)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, None)
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, -1)
    self.assertEqual(endIdx, -1)

  def helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(self, string, startIdx, foundName, startsAt, endsAt):
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute(string, startIdx)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, foundName)
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, startsAt)
    self.assertEqual(endIdx, endsAt)

  def test_getSafelyCurrentOrNextAttribute_attributeNotFound(self):
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNotFound(" ", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNotFound("\t\t", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNotFound("id='content' ", 12)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNotFound("\n  \t\t\t    \r\n", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNotFound("selected id='x'\n  \t\t\t    \r\n", 16)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNotFound("selected id='x'\n  \t\t\t    \r\n", 18)

  def test_getSafelyCurrentOrNextAttribute_corrupt(self):
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("=", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("'\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("\"'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("\"\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("''", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("\"value\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("'value'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("\"\"\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("'''", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("=value", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("='value'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("= 'value'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("\t= 'value'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class= ='myClass'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class=='myClass'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class==='myClass'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class == 'myClass'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class =  = 'myClass'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class=", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class=\t", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class =", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class\t=", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class \t \t =", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class\t=\t", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("class \t\t\t = \t\t \n", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\"   ", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\t \"   ", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\t   class='bordered'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\t \"   class='bordered'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\"audi", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\"audi\r\n", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\"audi\r\n selected", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\"audi'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\"audi' class='black-bg'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value=\"audi' selected", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value='audi\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value='audi\" selected", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value='audi\" id=\"my-id\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value \"audi\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value  \"audi\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value \t\t\t \"audi\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value\"audi\"", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value 'audi'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value\t\t'audi'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value\t\t'audi' selected", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value 'audi'\n", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value 'audi'\n selected", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value'audi'", 0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfCorrupt("value'audi' selected", 0)

  def test_getSafelyCurrentOrNextAttribute_noAttributeValue(self):
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("x", 0, foundName="x", startsAt=0, endsAt=0)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("aB", 0, foundName="aB", startsAt=0, endsAt=1)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("aB ", 0, foundName="aB", startsAt=0, endsAt=1)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("aB\t\r\n ", 0, foundName="aB", startsAt=0, endsAt=1)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("\t\r\naB\t\r\n", 0,
                                                                 foundName="aB", startsAt=3, endsAt=4)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("a b", 1, foundName="b", startsAt=2, endsAt=2)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("a b", 2, foundName="b", startsAt=2, endsAt=2)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("a b c", 1, foundName="b", startsAt=2, endsAt=2)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("a b c", 2, foundName="b", startsAt=2, endsAt=2)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("a\tb\tc", 1, foundName="b", startsAt=2, endsAt=2)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" a\r\nb\r\nc ", 2,
                                                                 foundName="b", startsAt=4, endsAt=4)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" a\r\nb\r\nc ", 3,
                                                                 foundName="b", startsAt=4, endsAt=4)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" a\r\nb\r\nc ", 4,
                                                                 foundName="b", startsAt=4, endsAt=4)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("selected", 0,
                                                                 foundName="selected", startsAt=0, endsAt=7)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" selected", 0,
                                                                 foundName="selected", startsAt=1, endsAt=8)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" selected", 1,
                                                                 foundName="selected", startsAt=1, endsAt=8)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" selected ", 0,
                                                                 foundName="selected", startsAt=1, endsAt=8)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" selected ", 1,
                                                                 foundName="selected", startsAt=1, endsAt=8)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" selected minimized", 0,
                                                                 foundName="selected", startsAt=1, endsAt=8)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" selected minimized", 1,
                                                                 foundName="selected", startsAt=1, endsAt=8)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("selected ", 0,
                                                                 foundName="selected", startsAt=0, endsAt=7)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("selected\t\n\t", 0,
                                                                 foundName="selected", startsAt=0, endsAt=7)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected", 0,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected", 1,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected", 2,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected", 4,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected", 6,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected", 7,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected", 8,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected class='abc'", 2,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("selected class=\"my-class\" no-href id='my-id'", 0,
                                                                 foundName="selected", startsAt=0, endsAt=7)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("selected class=\"my-class\" no-href id='my-id'", 25,
                                                                 foundName="no-href", startsAt=26, endsAt=32)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("selected class=\"my-class\" no-href id='my-id'", 26,
                                                                 foundName="no-href", startsAt=26, endsAt=32)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("selected  \t \n  class=\"my-class\" "
                                                                 "no-href id='my-id'", 0,
                                                                 foundName="selected", startsAt=0, endsAt=7)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound("selected\t animated\nid=\"my-id\"", 0,
                                                                 foundName="selected", startsAt=0, endsAt=7)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected\t\t\t\r\n", 0,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected\t\t\t\r\n", 1,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected\t\t\t\r\n", 6,
                                                                 foundName="selected", startsAt=8, endsAt=15)
    self.helper_getSafelyCurrentOrNextAttribute_checkIfNameFound(" \t  \r\n  selected\t\t\t\r\n", 8,
                                                                 foundName="selected", startsAt=8, endsAt=15)

    # TODO finish me
  def test_getSafelyCurrentOrNextAttribute_attributeValue(self):
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("id='my-id'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "my-id")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 9)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("id=\"my-id\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "my-id")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 9)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("id = 'my-id'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "my-id")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 11)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("id = ' my-id ' ", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " my-id ")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 13)
    string = "id \t\n= \n\t' \tmy-id '\n "
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " \tmy-id ")
    self.assertEqual(startIdx, 0)
    self.assertTrue(endIdx > startIdx)
    self.assertEqual(endIdx, string.find("'\n "))
    string = "\t\r\n id \t\n= \n\t' \tmy-id '\r\n "
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " \tmy-id ")
    self.assertEqual(startIdx, 4)
    self.assertEqual(endIdx, string.find("'\r\n "))
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("id = 'id1 id2'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "id1 id2")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 13)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("id = ' id1 id2 id3 '", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, " id1 id2 id3 ")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 19)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("\tid = '\r\n id1 id2 id3 \n\t'\t\t", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "\r\n id1 id2 id3 \n\t")
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, 24)
    string = "\tid = '\r\n id1 \t id2 \t id3 \n\t'\t\t"
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute(string, 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "\r\n id1 \t id2 \t id3 \n\t")
    self.assertEqual(startIdx, 1)
    self.assertEqual(endIdx, string.find("'\t\t"))
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("id = 'id1 id2' id=\"my-other-id\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "id")
    self.assertEqual(attributeValue, "id1 id2")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 13)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("title=\"class='myClass'\"", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "title")
    self.assertEqual(attributeValue, "class='myClass'")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 22)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("title=\"class='myClass'\""
                                                                                         "selected", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "title")
    self.assertEqual(attributeValue, "class='myClass'")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 22)

    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("title=\"===>A'B'C<===\""
                                                                                         "selected", 0)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "title")
    self.assertEqual(attributeValue, "===>A'B'C<===")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 20)

  def test_getSafelyCurrentOrNextAttribute_indexPointsWithinAttributeName(self):
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("selected", 2)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, None)
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 7)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("selected='False'", 3)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, "False")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 15)
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute("selected='False'", 7)
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "selected")
    self.assertEqual(attributeValue, "False")
    self.assertEqual(startIdx, 0)
    self.assertEqual(endIdx, 15)
    string = "\nselected\nclass\t=\t\"\tcl1\tcl2\tcl3 \" class id=\"my-id\"\n"
    corrupt, attributeName, attributeValue, startIdx, endIdx = attr.getSafelyCurrentOrNextAttribute(string, string.find("class"))
    self.assertFalse(corrupt)
    self.assertEqual(attributeName, "class")
    self.assertEqual(attributeValue, "\tcl1\tcl2\tcl3 ")
    self.assertTrue(startIdx > -1)
    self.assertTrue(endIdx > startIdx)
    self.assertEqual(startIdx, string.find("class"))
    self.assertEqual(endIdx, string.find("\" class id=\"my-id\""))

  def test_getAllAttributeNames_nonSense(self):
    with self.assertRaises(Exception):
      attr.getAllAttributeNames(12)
    with self.assertRaises(Exception):
      attr.getAllAttributeNames(None)
    with self.assertRaises(Exception):
      attr.getAllAttributeNames(False)
    with self.assertRaises(Exception):
      attr.getAllAttributeNames([])

  def test_getAllAttributeNames_onlyEmptyAndWhiteSpace(self):
    corrupt, attributes = attr.getAllAttributeNames("")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])
    corrupt, attributes = attr.getAllAttributeNames(" ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])
    corrupt, attributes = attr.getAllAttributeNames("\t")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])
    corrupt, attributes = attr.getAllAttributeNames("\n")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])
    corrupt, attributes = attr.getAllAttributeNames("  \t\t\t\t \r\r  ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])
    corrupt, attributes = attr.getAllAttributeNames("\n      \t   \t        \n")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, [])

  def helper_getAllAttributeNames_checkIfCorrupt(self, attributesString):
    corrupt, attributeNames = attr.getAllAttributeNames(attributesString)
    self.assertTrue(corrupt)
    self.assertEqual(attributeNames, [])

  def test_getAllAttributeNames_corruptAttributes(self):
    self.helper_getAllAttributeNames_checkIfCorrupt("=")
    self.helper_getAllAttributeNames_checkIfCorrupt("=12")
    self.helper_getAllAttributeNames_checkIfCorrupt("='value'")
    self.helper_getAllAttributeNames_checkIfCorrupt("'value'")
    self.helper_getAllAttributeNames_checkIfCorrupt(" = 'value'")
    self.helper_getAllAttributeNames_checkIfCorrupt("\t\t=\t\t\" value \"")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected=")
    self.helper_getAllAttributeNames_checkIfCorrupt(" \t\t selected\n = \t")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected = \"")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected = '")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected = \"value")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected = 'value")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected 'value'")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected'value'")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected=='value'")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected= ='value'")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected == 'value'")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected 'value")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected'value")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected = \"value'")
    self.helper_getAllAttributeNames_checkIfCorrupt("selected = 'value\"")
    self.helper_getAllAttributeNames_checkIfCorrupt("class=\"example\" selected = 'value\" animated")

  def test_getAllAttributeNames_oneAttribute(self):
    corrupt, attributes = attr.getAllAttributeNames("a")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["a"])
    corrupt, attributes = attr.getAllAttributeNames("selected")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["selected"])
    corrupt, attributes = attr.getAllAttributeNames(" \n  \t selected \n\r \t ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["selected"])
    corrupt, attributes = attr.getAllAttributeNames("selected \n\r \t ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["selected"])
    corrupt, attributes = attr.getAllAttributeNames(" \n  \t selected")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["selected"])
    corrupt, attributes = attr.getAllAttributeNames("style=\"float:right;margin:11px 14px 0 0;"
                                                     "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["style"])
    corrupt, attributes = attr.getAllAttributeNames("style='float:right;margin:11px 14px 0 0;"
                                                     "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98'")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["style"])
    corrupt, attributes = attr.getAllAttributeNames(" \n\r style\t\t\t=\n'float:right;margin:11px 14px 0 0;"
                                               "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98' \n\r ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["style"])
    corrupt, attributes = attr.getAllAttributeNames("style\t\t\t=\n'float:right;margin:11px 14px 0 0;"
                                               "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98' \n\r ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["style"])
    corrupt, attributes = attr.getAllAttributeNames(" \n\r style\t\t\t=\n'\t\tfloat:right;margin:11px 14px 0 0;"
                                         "border-radius:2px!important;padding:9px 12px 9px;color:#7a7e98\t\t' \n\r ")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["style"])
    corrupt, attributes = attr.getAllAttributeNames("\nproperty\n=\n\"\narticle:published_time\n\"\n")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["property"])
    corrupt, attributes = attr.getAllAttributeNames("\nproperty\n=\n\"\narticle:published_time\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["property"])
    corrupt, attributes = attr.getAllAttributeNames("property\n=\n\"\narticle:published_time\n\"\n")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["property"])
    corrupt, attributes = attr.getAllAttributeNames("title=\"class='myClass'\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["title"])
    corrupt, attributes = attr.getAllAttributeNames("title=\"<=== A'B'C ===>\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["title"])

  def test_getAllAttributeNames_moreAttributes(self):
    corrupt, attributes = attr.getAllAttributeNames("title=\"class='myClass'\"id='myId'\t\nselected")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["title", "id", "selected"])
    corrupt, attributes = attr.getAllAttributeNames("selected id=\"logo\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["selected", "id"])
    corrupt, attributes = attr.getAllAttributeNames("id=\"logo\" selected")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["id", "selected"])
    corrupt, attributes = attr.getAllAttributeNames("id=\"logo\" selected id=\"otherId\" selected='true'")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["id", "selected"])
    corrupt, attributes = attr.getAllAttributeNames("\tonclick\t=\t\"\tlocation.reload();\t\" "
          "style\n=\"float:right;"
          "display:inline-block;position:relative;top:15px;right:3px;margin-left:10px;font-size:13px;cursor:pointer\" "
          "title='Exclude inappropriate or explicit images'")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["onclick", "style", "title"])
    corrupt, attributes = attr.getAllAttributeNames("rel=\"alternate\" type=\"application/rss+xml\" "
                     "title=\"Matematika és Informatika Kar RSS Feed\" href=\"https://www.cs.ubbcluj.ro/hu/feed/\"")
    self.assertFalse(corrupt)
    self.assertEqual(attributes, ["rel", "type", "title", "href"])

  def helper_getSafelyCurrentValue_checkIfCorrupt(self, attributesString, startIdx):
    corrupt, found, firstQuoteIdx, secondQuoteIdx = attr.getSafelyCurrentValue(attributesString, startIdx)
    self.assertTrue(corrupt)
    self.assertFalse(found)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def helper_getSafelyCurrentValue_checkIfNotFound(self, attributesString, startIdx):
    corrupt, found, firstQuoteIdx, secondQuoteIdx = attr.getSafelyCurrentValue(attributesString, startIdx)
    self.assertFalse(corrupt)
    self.assertFalse(found)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def helper_getSafelyCurrentValue_checkIfFound(self, attributesString, startIdx, startsAt, endsAt):
    corrupt, found, firstQuoteIdx, secondQuoteIdx = attr.getSafelyCurrentValue(attributesString, startIdx)
    self.assertFalse(corrupt)
    self.assertTrue(found)
    self.assertEqual(firstQuoteIdx, startsAt)
    self.assertEqual(secondQuoteIdx, endsAt)

  def test_getSafelyCurrentValue_nonSense(self):
    with self.assertRaises(Exception):
      attr.getSafelyCurrentValue(None, None)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentValue(False, 0)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentValue("= 'value'", True)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentValue("= 'value'", 56)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentValue("= 'value'", -1)

  def test_getSafelyCurrentValue_emptyString(self):
    with self.assertRaises(Exception):
      attr.getSafelyCurrentValue("", 0)

  def test_getSafelyCurrentValue_spaces(self):
    self.helper_getSafelyCurrentValue_checkIfNotFound(" ", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound("\n", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound(" \t\t\n", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound(" \t\t \n ", 0)

  def test_getSafelyCurrentValue_corrupt(self):
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("==", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=========", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("= ", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("='\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=\"'", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("= \t \n", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("'", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("''", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("\"\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("'value'", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("\"value\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=value", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("= value", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("= \n\t value", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("= value ", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("\t\t\n = \n\tvalue\n\n\n", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=2", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("= 2", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=value\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=value'", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=\"value", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("='value", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=\"value'", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("='value\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("= \"value'", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("= 'value\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=   \"  value  '  ", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=  '  value  \"  ", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("\t\t=   \"  value  '  ", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("\n\n\n=  '  value  \"  ", 0)

  def test_getSafelyCurrentValue_corrupt_noAttributeNameBeforeEqual(self):
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=\"\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("='value'", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("= 'value'", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt(" = 'value'", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("='value' ", 8)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("= \"\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt(" = \"\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("\t=\t\"\"", 0)
    self.helper_getSafelyCurrentValue_checkIfCorrupt("=\t\t\t\"\"", 0)

  def test_getSafelyCurrentValue_notFound(self):
    self.helper_getSafelyCurrentValue_checkIfNotFound("X", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound("attrName", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound("multiple attribute names", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound("attrName\t", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound("\tattrName", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound("attrName\t\n", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound("\n\tattrName", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound("   \t attrName  \t\t  \t", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound("selected class='myClass'", 0)
    self.helper_getSafelyCurrentValue_checkIfNotFound("selected class='myClass'", 3)
    self.helper_getSafelyCurrentValue_checkIfNotFound("\t\tselected\n\nclass='myClass'", 0)

  def test_getSafelyCurrentValue_emptyValue(self):
    self.helper_getSafelyCurrentValue_checkIfFound("a=\"\"", 0, startsAt=2, endsAt=3)
    self.helper_getSafelyCurrentValue_checkIfFound("a=\"\"", 1, startsAt=2, endsAt=3)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \"\" ", 0, startsAt=6, endsAt=7)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \"\" ", 1, startsAt=6, endsAt=7)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \"\" ", 2, startsAt=6, endsAt=7)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \"\" ", 3, startsAt=6, endsAt=7)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \"\" ", 4, startsAt=6, endsAt=7)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \"\" ", 5, startsAt=6, endsAt=7)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \t\"\" ", 6, startsAt=7, endsAt=8)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \t\r\n\"\" ", 7, startsAt=9, endsAt=10)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \t\r\n\"\" ", 8, startsAt=9, endsAt=10)
    self.helper_getSafelyCurrentValue_checkIfFound("aabd\n\n\n=\t\t\t\"\" ", 4, startsAt=11, endsAt=12)
    self.helper_getSafelyCurrentValue_checkIfFound("a\n\n\n=\t\t\t'' ", 0, startsAt=8, endsAt=9)
    self.helper_getSafelyCurrentValue_checkIfFound("a\n\n\n=\t\t\t'' ", 1, startsAt=8, endsAt=9)
    self.helper_getSafelyCurrentValue_checkIfFound("a\n\n\n=\t\t\t''\n\t", 1, startsAt=8, endsAt=9)

  def test_getSafelyCurrentValue_whiteSpaceValue(self):
    self.helper_getSafelyCurrentValue_checkIfFound("a=\" \"", 0, startsAt=2, endsAt=4)
    self.helper_getSafelyCurrentValue_checkIfFound("a=\" \"", 1, startsAt=2, endsAt=4)
    self.helper_getSafelyCurrentValue_checkIfFound("abc=\" \"", 0, startsAt=4, endsAt=6)
    self.helper_getSafelyCurrentValue_checkIfFound("a = \"\n\" ", 1, startsAt=4, endsAt=6)
    self.helper_getSafelyCurrentValue_checkIfFound("a = \"\n\" ", 2, startsAt=4, endsAt=6)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \"\n\" ", 0, startsAt=6, endsAt=8)
    self.helper_getSafelyCurrentValue_checkIfFound("abc = \"\n\" ", 1, startsAt=6, endsAt=8)
    self.helper_getSafelyCurrentValue_checkIfFound("a\n\n\n=\t\t\t\"\t\n\t\" ", 0, startsAt=8, endsAt=12)
    self.helper_getSafelyCurrentValue_checkIfFound("a\n\n\n=\t\t\t\"\t\n\t\" ", 1, startsAt=8, endsAt=12)
    self.helper_getSafelyCurrentValue_checkIfFound("Q\n\n\n=\t\t\t'\t\n\t' ", 0, startsAt=8, endsAt=12)
    self.helper_getSafelyCurrentValue_checkIfFound("Q\n\n\n=\t\t\t'\t\n\t' ", 1, startsAt=8, endsAt=12)

  def test_getSafelyCurrentValue_nonEmptyValue(self):
    self.helper_getSafelyCurrentValue_checkIfFound("x=\"value\"", 1, startsAt=2, endsAt=8)
    self.helper_getSafelyCurrentValue_checkIfFound("a = \"value\" ", 0, startsAt=4, endsAt=10)
    self.helper_getSafelyCurrentValue_checkIfFound("a = \"value\" ", 1, startsAt=4, endsAt=10)
    self.helper_getSafelyCurrentValue_checkIfFound("a = \"value\" ", 2, startsAt=4, endsAt=10)
    self.helper_getSafelyCurrentValue_checkIfFound("a\n\n\n=\t\t\t\"value\" ", 1, startsAt=8, endsAt=14)
    self.helper_getSafelyCurrentValue_checkIfFound("a\n\n\n=\t\t\t'value' ", 1, startsAt=8, endsAt=14)
    self.helper_getSafelyCurrentValue_checkIfFound("a\n\n\n=\t\t\t'\t value\n\n' ", 1, startsAt=8, endsAt=18)
    self.helper_getSafelyCurrentValue_checkIfFound("class=\"class='myClass'\"", 5, startsAt=6, endsAt=22)
    self.helper_getSafelyCurrentValue_checkIfFound("id=\"class='myClass'\"selected", 2, startsAt=3, endsAt=19)

  def test_getSafelyCurrentValue_indexPointsToValue(self):
    self.helper_getSafelyCurrentValue_checkIfFound("x = 'value'", 4, startsAt=4, endsAt=10)
    self.helper_getSafelyCurrentValue_checkIfFound("x = 'value'", 7, startsAt=4, endsAt=10)
    self.helper_getSafelyCurrentValue_checkIfFound("x = 'value'", 9, startsAt=4, endsAt=10)
    self.helper_getSafelyCurrentValue_checkIfFound("x = 'value'", 10, startsAt=4, endsAt=10)
    self.helper_getSafelyCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 4, startsAt=4, endsAt=25)
    self.helper_getSafelyCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 5, startsAt=4, endsAt=25)
    self.helper_getSafelyCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 6, startsAt=4, endsAt=25)
    self.helper_getSafelyCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 7, startsAt=4, endsAt=25)
    self.helper_getSafelyCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 8, startsAt=4, endsAt=25)
    self.helper_getSafelyCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 9, startsAt=4, endsAt=25)
    self.helper_getSafelyCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 10, startsAt=4, endsAt=25)
    self.helper_getSafelyCurrentValue_checkIfFound("x = \" a id='myID' b value\"", 11, startsAt=4, endsAt=25)

  def helper_getCurrentValue_checkIfCorrupt(self, attributesString, startIdx):
    corrupt, found, firstQuoteIdx, secondQuoteIdx = attr.getCurrentValue(attributesString, startIdx)
    self.assertTrue(corrupt)
    self.assertFalse(found)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def helper_getCurrentValue_checkIfNotFound(self, attributesString, startIdx):
    corrupt, found, firstQuoteIdx, secondQuoteIdx = attr.getCurrentValue(attributesString, startIdx)
    self.assertFalse(corrupt)
    self.assertFalse(found)
    self.assertEqual(firstQuoteIdx, -1)
    self.assertEqual(secondQuoteIdx, -1)

  def helper_getCurrentValue_checkIfFound(self, attributesString, startIdx, startsAt, endsAt):
    corrupt, found, firstQuoteIdx, secondQuoteIdx = attr.getCurrentValue(attributesString, startIdx)
    self.assertFalse(corrupt)
    self.assertTrue(found)
    self.assertEqual(firstQuoteIdx, startsAt)
    self.assertEqual(secondQuoteIdx, endsAt)

  def test_getCurrentValue_nonSense(self):
    with self.assertRaises(Exception):
      attr.getCurrentValue(None, None)
    with self.assertRaises(Exception):
      attr.getCurrentValue(False, 0)
    with self.assertRaises(Exception):
      attr.getCurrentValue("= 'value'", True)
    with self.assertRaises(Exception):
      attr.getCurrentValue("= 'value'", 56)
    with self.assertRaises(Exception):
      attr.getCurrentValue("= 'value'", -1)

  def test_getCurrentValue_emptyString(self):
    with self.assertRaises(Exception):
      attr.getCurrentValue("", 0)

  def test_getCurrentValue_spaces(self):
    self.helper_getCurrentValue_checkIfNotFound(" ", 0)
    self.helper_getCurrentValue_checkIfNotFound("\n", 0)
    self.helper_getCurrentValue_checkIfNotFound(" \t\t\n", 0)
    self.helper_getCurrentValue_checkIfNotFound(" \t\t \n ", 0)

  def test_getCurrentValue_corrupt(self):
    self.helper_getCurrentValue_checkIfCorrupt("=", 0)
    self.helper_getCurrentValue_checkIfCorrupt("==", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=========", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= ", 0)
    self.helper_getCurrentValue_checkIfCorrupt("='\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=\"'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= \t \n", 0)
    self.helper_getCurrentValue_checkIfCorrupt("'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("''", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\"\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("'value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\"value\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=value", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= value", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= \n\t value", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= value ", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\t\t\n = \n\tvalue\n\n\n", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=2", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= 2", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=value\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=\"value", 0)
    self.helper_getCurrentValue_checkIfCorrupt("='value", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=\"value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("='value\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= \"value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= 'value\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=   \"  value  '  ", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=  '  value  \"  ", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\t\t=   \"  value  '  ", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\n\n\n=  '  value  \"  ", 0)

  def test_getCurrentValue_notCorruptBecauseOfIndexPosition(self):
    self.helper_getCurrentValue_checkIfNotFound("='value' ", 8)

  def test_getCurrentValue_corrupt_noAttributeNameBeforeEqual(self):
    self.helper_getCurrentValue_checkIfCorrupt("=\"\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("='value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= 'value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt(" = 'value'", 0)
    self.helper_getCurrentValue_checkIfCorrupt("= \"\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt(" = \"\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("\t=\t\"\"", 0)
    self.helper_getCurrentValue_checkIfCorrupt("=\t\t\t\"\"", 0)

  def test_getCurrentValue_notFound(self):
    self.helper_getCurrentValue_checkIfNotFound("X", 0)
    self.helper_getCurrentValue_checkIfNotFound("attrName", 0)
    self.helper_getCurrentValue_checkIfNotFound("multiple attribute names", 0)
    self.helper_getCurrentValue_checkIfNotFound("attrName\t", 0)
    self.helper_getCurrentValue_checkIfNotFound("\tattrName", 0)
    self.helper_getCurrentValue_checkIfNotFound("attrName\t\n", 0)
    self.helper_getCurrentValue_checkIfNotFound("\n\tattrName", 0)
    self.helper_getCurrentValue_checkIfNotFound("   \t attrName  \t\t  \t", 0)
    self.helper_getCurrentValue_checkIfNotFound("selected class='myClass'", 0)
    self.helper_getCurrentValue_checkIfNotFound("selected class='myClass'", 3)
    self.helper_getCurrentValue_checkIfNotFound("\t\tselected\n\nclass='myClass'", 0)

  def test_getCurrentValue_emptyValue(self):
    self.helper_getCurrentValue_checkIfFound("a=\"\"", 0, startsAt=2, endsAt=3)
    self.helper_getCurrentValue_checkIfFound("a=\"\"", 1, startsAt=2, endsAt=3)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 0, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 1, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 2, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 3, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("abc = \"\" ", 4, startsAt=6, endsAt=7)
    self.helper_getCurrentValue_checkIfFound("aabd\n\n\n=\t\t\t\"\" ", 4, startsAt=11, endsAt=12)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t'' ", 0, startsAt=8, endsAt=9)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t'' ", 1, startsAt=8, endsAt=9)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t''\n\t", 1, startsAt=8, endsAt=9)

  def test_getCurrentValue_whiteSpaceValue(self):
    self.helper_getCurrentValue_checkIfFound("a=\" \"", 0, startsAt=2, endsAt=4)
    self.helper_getCurrentValue_checkIfFound("a=\" \"", 1, startsAt=2, endsAt=4)
    self.helper_getCurrentValue_checkIfFound("abc=\" \"", 0, startsAt=4, endsAt=6)
    self.helper_getCurrentValue_checkIfFound("a = \"\n\" ", 1, startsAt=4, endsAt=6)
    self.helper_getCurrentValue_checkIfFound("a = \"\n\" ", 2, startsAt=4, endsAt=6)
    self.helper_getCurrentValue_checkIfFound("abc = \"\n\" ", 0, startsAt=6, endsAt=8)
    self.helper_getCurrentValue_checkIfFound("abc = \"\n\" ", 1, startsAt=6, endsAt=8)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t\"\t\n\t\" ", 0, startsAt=8, endsAt=12)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t\"\t\n\t\" ", 1, startsAt=8, endsAt=12)
    self.helper_getCurrentValue_checkIfFound("Q\n\n\n=\t\t\t'\t\n\t' ", 0, startsAt=8, endsAt=12)
    self.helper_getCurrentValue_checkIfFound("Q\n\n\n=\t\t\t'\t\n\t' ", 1, startsAt=8, endsAt=12)

  def test_getCurrentValue_nonEmptyValue(self):
    self.helper_getCurrentValue_checkIfFound("x=\"value\"", 1, startsAt=2, endsAt=8)
    self.helper_getCurrentValue_checkIfFound("a = \"value\" ", 0, startsAt=4, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("a = \"value\" ", 1, startsAt=4, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("a = \"value\" ", 2, startsAt=4, endsAt=10)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t\"value\" ", 1, startsAt=8, endsAt=14)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t'value' ", 1, startsAt=8, endsAt=14)
    self.helper_getCurrentValue_checkIfFound("a\n\n\n=\t\t\t'\t value\n\n' ", 1, startsAt=8, endsAt=18)
    self.helper_getCurrentValue_checkIfFound("class=\"class='myClass'\"", 5, startsAt=6, endsAt=22)
    self.helper_getCurrentValue_checkIfFound("id=\"class='myClass'\"selected", 2, startsAt=3, endsAt=19)

  def helper_getSafelyCurrentOrNextName_checkIfNotFound(self, string, startIdx):
    corrupt, found, attributeName, firstCharIdx, lastCharIdx = attr.getSafelyCurrentOrNextName(string, startIdx)
    self.assertFalse(corrupt)
    self.assertFalse(found)
    self.assertIsNone(attributeName, -1)
    self.assertEqual(firstCharIdx, -1)
    self.assertEqual(lastCharIdx, -1)

  def helper_getSafelyCurrentOrNextName_checkIfFound(self, string, startIdx, startsAt, endsAt):
    corrupt, found, attributeName, firstCharIdx, lastCharIdx = attr.getSafelyCurrentOrNextName(string, startIdx)
    self.assertFalse(corrupt)
    self.assertTrue(found)
    self.assertEqual(firstCharIdx, startsAt)
    self.assertEqual(lastCharIdx, endsAt)
    self.assertEqual(attributeName, string[startsAt:endsAt + 1])

  def helper_getSafelyCurrentOrNextName_checkIfCorrupt(self, string, startIdx):
    corrupt, found, attributeName, firstCharIdx, lastCharIdx = attr.getSafelyCurrentOrNextName(string, startIdx)
    self.assertTrue(corrupt)
    self.assertFalse(found)
    self.assertIsNone(attributeName, -1)
    self.assertEqual(firstCharIdx, -1)
    self.assertEqual(lastCharIdx, -1)

  def test_getSafelyCurrentOrNextName_nonSense(self):
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextName(None, None)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextName(False, 0)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextName("= 'value'", True)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextName("= 'value'", 56)
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextName("= 'value'", -1)

  def test_getSafelyCurrentOrNextName_emptyString(self):
    with self.assertRaises(Exception):
      attr.getSafelyCurrentOrNextName("", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("a='value' ", 9)

  def test_getSafelyCurrentOrNextName_spaces(self):
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound(" ", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("   ", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("   ", 1)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("     ", 2)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("\n", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound(" \t\t\n", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound(" \t\t\n", 1)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound(" \t\t\n", 2)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound(" \t\r\n", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound(" \t\t \n ", 3)

  def test_getSafelyCurrentOrNextName_corrupt(self):
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("=", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("= ", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" =", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = ", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = ", 1)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = ", 2)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = = ", 1)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = = ", 2)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = = ", 3)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("\t\t=\n\n", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("'", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("''''''''", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("' ", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" '", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" ' ", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("\t\t'\n\n", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("\"", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("\" ", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" \"", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" \" ", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("\t\t\"\n\n", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("='value'", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 1)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 2)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 3)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 4)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 11)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 12)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("=value'", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("=value'", 1)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("=value'", 2)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("=value'", 6)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("class'myClass'", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("class'myClass'", 5)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("class'myClass'", 6)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("one ' two", 0)
    self.helper_getSafelyCurrentOrNextName_checkIfCorrupt("one ' two", 4)

  def test_getSafelyCurrentOrNextName_notFound(self):
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("class ", 5)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("class \r\n", 5)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("class \r\n", 6)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' ", 21)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' \t\t", 21)
    self.helper_getSafelyCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' \t\t", 22)

  def test_getSafelyCurrentOrNextName_indexPointsAtTheFirstNameCharIdx(self):
    self.helper_getSafelyCurrentOrNextName_checkIfFound("X", 0, startsAt=0, endsAt=0)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("X=''", 0, startsAt=0, endsAt=0)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("\t\tX\t\t", 0, startsAt=2, endsAt=2)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("\t\tX\t\tY Z", 0, startsAt=2, endsAt=2)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("selected", 0, startsAt=0, endsAt=7)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("\t\tselected\n\n", 0, startsAt=2, endsAt=9)
    self.helper_getSafelyCurrentOrNextName_checkIfFound(" class='my-Class' \t selected", 0, startsAt=1, endsAt=5)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("\n\nclass\t\t=\t\n'   my-Class' \r\n\t selected", 0,
                                                        startsAt=2, endsAt=6)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("multiple words in this string", 0, startsAt=0, endsAt=7)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("title=\"class='myClass'==\"", 0, startsAt=0, endsAt=4)

  def test_getSafelyCurrentOrNextName_indexPointsWithinName(self):
    self.helper_getSafelyCurrentOrNextName_checkIfFound("selected", 3, startsAt=0, endsAt=7)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("multiple words in this string", 3, startsAt=0, endsAt=7)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("multiple words in this string", 13, startsAt=9, endsAt=13)

  def test_getSafelyCurrentOrNextName_indexPointsAroundValue(self):
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class='myClass'", 5, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class='myClass'", 6, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class='myClass'", 7, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class='myClass'", 9, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class='myClass'", 14, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 5, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 6, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 7, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 8, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 5, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 6, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 7, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 8, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 9, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 10, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 11, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("a=''", 1, startsAt=0, endsAt=0)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("a = ''", 1, startsAt=0, endsAt=0)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("a = ''", 2, startsAt=0, endsAt=0)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("a = ''", 3, startsAt=0, endsAt=0)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("title=\"class='myClass'\"", 12, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("title=\"'class'='myClass'\"", 14, startsAt=0, endsAt=4)
    self.helper_getSafelyCurrentOrNextName_checkIfFound("title=\"'class' = 'myClass'\"", 15, startsAt=0, endsAt=4)

  def helper_getCurrentOrNextName_checkIfNotFound(self, string, startIdx):
    corrupt, found, attributeName, firstCharIdx, lastCharIdx = attr.getCurrentOrNextName(string, startIdx)
    self.assertFalse(corrupt)
    self.assertFalse(found)
    self.assertIsNone(attributeName, -1)
    self.assertEqual(firstCharIdx, -1)
    self.assertEqual(lastCharIdx, -1)

  def helper_getCurrentOrNextName_checkIfFound(self, string, startIdx, startsAt, endsAt):
    corrupt, found, attributeName, firstCharIdx, lastCharIdx = attr.getCurrentOrNextName(string, startIdx)
    self.assertFalse(corrupt)
    self.assertTrue(found)
    self.assertEqual(firstCharIdx, startsAt)
    self.assertEqual(lastCharIdx, endsAt)
    self.assertEqual(attributeName, string[startsAt:endsAt + 1])

  def helper_getCurrentOrNextName_checkIfCorrupt(self, string, startIdx):
    corrupt, found, attributeName, firstCharIdx, lastCharIdx = attr.getCurrentOrNextName(string, startIdx)
    self.assertTrue(corrupt)
    self.assertFalse(found)
    self.assertIsNone(attributeName, -1)
    self.assertEqual(firstCharIdx, -1)
    self.assertEqual(lastCharIdx, -1)

  def test_getCurrentOrNextName_nonSense(self):
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName(None, None)
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName(False, 0)
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName("= 'value'", True)
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName("= 'value'", 56)
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName("= 'value'", -1)

  def test_getCurrentOrNextName_emptyString(self):
    with self.assertRaises(Exception):
      attr.getCurrentOrNextName("", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound("a='value' ", 9)

  def test_getCurrentOrNextName_spaces(self):
    self.helper_getCurrentOrNextName_checkIfNotFound(" ", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound("   ", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound("   ", 1)
    self.helper_getCurrentOrNextName_checkIfNotFound("     ", 2)
    self.helper_getCurrentOrNextName_checkIfNotFound("\n", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound(" \t\t\n", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound(" \t\t\n", 1)
    self.helper_getCurrentOrNextName_checkIfNotFound(" \t\t\n", 2)
    self.helper_getCurrentOrNextName_checkIfNotFound(" \t\r\n", 0)
    self.helper_getCurrentOrNextName_checkIfNotFound(" \t\t \n ", 3)

  def test_getCurrentOrNextName_notCorruptBecauseOfIndexPosition(self):
    self.helper_getCurrentOrNextName_checkIfNotFound(" = ", 2)
    self.helper_getCurrentOrNextName_checkIfFound(" = ' value ' ", 4, startsAt=5, endsAt=9)
    self.helper_getCurrentOrNextName_checkIfNotFound(" = ' value ' ", 12)
    self.helper_getCurrentOrNextName_checkIfFound("=value'", 1, startsAt=1, endsAt=5)
    self.helper_getCurrentOrNextName_checkIfFound("=value'", 2, startsAt=1, endsAt=5)
    self.helper_getCurrentOrNextName_checkIfFound("class'myClass'", 0, startsAt=0, endsAt=4)
    self.helper_getCurrentOrNextName_checkIfFound("class'myClass'", 6, startsAt=6, endsAt=12)
    self.helper_getCurrentOrNextName_checkIfFound("one ' two", 0, startsAt=0, endsAt=2)

  def test_getCurrentOrNextName_corrupt(self):
    self.helper_getCurrentOrNextName_checkIfCorrupt("=", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("= ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" =", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = ", 1)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = = ", 1)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = = ", 2)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = = ", 3)
    self.helper_getCurrentOrNextName_checkIfCorrupt("\t\t=\n\n", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("'", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("''''''''", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("' ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" '", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" ' ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("\t\t'\n\n", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("\"", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("\" ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" \"", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" \" ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("\t\t\"\n\n", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("='value'", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 1)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 2)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 3)
    self.helper_getCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 11)
    self.helper_getCurrentOrNextName_checkIfCorrupt("=value'", 0)
    self.helper_getCurrentOrNextName_checkIfCorrupt("=value'", 6)
    self.helper_getCurrentOrNextName_checkIfCorrupt("class'myClass'", 5)
    self.helper_getCurrentOrNextName_checkIfCorrupt("one ' two", 4)

  def test_getCurrentOrNextName_notFound(self):
    self.helper_getCurrentOrNextName_checkIfNotFound("class ", 5)
    self.helper_getCurrentOrNextName_checkIfNotFound("class \r\n", 5)
    self.helper_getCurrentOrNextName_checkIfNotFound("class \r\n", 6)
    self.helper_getCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' ", 21)
    self.helper_getCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' \t\t", 21)
    self.helper_getCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' \t\t", 22)

  def test_getCurrentOrNextName_indexPointsAtTheFirstNameCharIdx(self):
    self.helper_getCurrentOrNextName_checkIfFound("X", 0, startsAt=0, endsAt=0)
    self.helper_getCurrentOrNextName_checkIfFound("X=''", 0, startsAt=0, endsAt=0)
    self.helper_getCurrentOrNextName_checkIfFound("\t\tX\t\t", 0, startsAt=2, endsAt=2)
    self.helper_getCurrentOrNextName_checkIfFound("\t\tX\t\tY Z", 0, startsAt=2, endsAt=2)
    self.helper_getCurrentOrNextName_checkIfFound("selected", 0, startsAt=0, endsAt=7)
    self.helper_getCurrentOrNextName_checkIfFound("\t\tselected\n\n", 0, startsAt=2, endsAt=9)
    self.helper_getCurrentOrNextName_checkIfFound(" class='my-Class' \t selected", 0, startsAt=1, endsAt=5)
    self.helper_getCurrentOrNextName_checkIfFound("\n\nclass\t\t=\t\n'   my-Class' \r\n\t selected", 0,
                                                  startsAt=2, endsAt=6)
    self.helper_getCurrentOrNextName_checkIfFound("multiple words in this string", 0, startsAt=0, endsAt=7)
    self.helper_getCurrentOrNextName_checkIfFound("title=\"class='myClass'==\"", 0, startsAt=0, endsAt=4)

  def test_getCurrentOrNextName_indexPointsWithinName(self):
    self.helper_getCurrentOrNextName_checkIfFound("selected", 3, startsAt=0, endsAt=7)
    self.helper_getCurrentOrNextName_checkIfFound("multiple words in this string", 3, startsAt=0, endsAt=7)
    self.helper_getCurrentOrNextName_checkIfFound("multiple words in this string", 13, startsAt=9, endsAt=13)

  def helper_getAllAttributes_checkIfCorrupt(self, string):
    corrupt, attributes = attr.getAllAttributes(string)
    self.assertTrue(corrupt)
    self.assertEqual(attributes, {})

  def helper_getAllAttributes_checkIfNotFound(self, string):
    corrupt, attributes = attr.getAllAttributes(string)
    self.assertFalse(corrupt)
    self.assertEqual(attributes, {})

  def helper_getAllAttributes_checkIfFound(self, string, foundValues):
    corrupt, attributes = attr.getAllAttributes(string)
    self.assertFalse(corrupt)
    self.assertEqual(attributes, foundValues)

  def test_getAllAttributes_nonSense(self):
    with self.assertRaises(Exception):
      attr.getAllAttributes(None)
    with self.assertRaises(Exception):
      attr.getAllAttributes(123)
    with self.assertRaises(Exception):
      attr.getAllAttributes(False)
    with self.assertRaises(Exception):
      attr.getAllAttributes([])
    with self.assertRaises(Exception):
      attr.getAllAttributes(["hello", "generator"])
    with self.assertRaises(Exception):
      attr.getAllAttributes(-1)

  def test_getAllAttributes_emptyString(self):
    with self.assertRaises(Exception):
      attr.getAllAttributes("")

  def test_getAllAttributes_space(self):
    self.helper_getAllAttributes_checkIfNotFound(" ")
    self.helper_getAllAttributes_checkIfNotFound("  ")
    self.helper_getAllAttributes_checkIfNotFound("   ")
    self.helper_getAllAttributes_checkIfNotFound("\t")
    self.helper_getAllAttributes_checkIfNotFound("\t ")
    self.helper_getAllAttributes_checkIfNotFound(" \t")
    self.helper_getAllAttributes_checkIfNotFound("\t  \t")
    self.helper_getAllAttributes_checkIfNotFound("\r\n")
    self.helper_getAllAttributes_checkIfNotFound("\t  \n  \t\r\n")

  def test_getAllAttributes_corrupt_onlyQuotes(self):
    self.helper_getAllAttributes_checkIfCorrupt("'")
    self.helper_getAllAttributes_checkIfCorrupt("\"")
    self.helper_getAllAttributes_checkIfCorrupt("''")
    self.helper_getAllAttributes_checkIfCorrupt("'\"")
    self.helper_getAllAttributes_checkIfCorrupt("'''")
    self.helper_getAllAttributes_checkIfCorrupt("\"\"\"\"")

  def test_getAllAttributes_corrupt_other(self):
    self.helper_getAllAttributes_checkIfCorrupt("=")
    self.helper_getAllAttributes_checkIfCorrupt("= = =")
    self.helper_getAllAttributes_checkIfCorrupt("= 2")
    self.helper_getAllAttributes_checkIfCorrupt("= '")
    self.helper_getAllAttributes_checkIfCorrupt(" = '")
    self.helper_getAllAttributes_checkIfCorrupt("= \"")
    self.helper_getAllAttributes_checkIfCorrupt(" = \"")
    self.helper_getAllAttributes_checkIfCorrupt("'='")
    self.helper_getAllAttributes_checkIfCorrupt('"="')
    self.helper_getAllAttributes_checkIfCorrupt("value = 2")
    self.helper_getAllAttributes_checkIfCorrupt('value = \t')
    self.helper_getAllAttributes_checkIfCorrupt('value =')
    self.helper_getAllAttributes_checkIfCorrupt("'field' = 'value'")
    self.helper_getAllAttributes_checkIfCorrupt("'field' = \"value\"")

  def test_getAllAttributes_found_singleNameWithNoValue(self):
    self.helper_getAllAttributes_checkIfFound("b", foundValues={"b": None})
    self.helper_getAllAttributes_checkIfFound(" b", foundValues={"b": None})
    self.helper_getAllAttributes_checkIfFound("b ", foundValues={"b": None})
    self.helper_getAllAttributes_checkIfFound("\t\tb", foundValues={"b": None})
    self.helper_getAllAttributes_checkIfFound("b\n \n\n", foundValues={"b": None})
    self.helper_getAllAttributes_checkIfFound("\t \t b \r\n ", foundValues={"b": None})
    self.helper_getAllAttributes_checkIfFound("\t  Qq    ", foundValues={"Qq": None})
    self.helper_getAllAttributes_checkIfFound("\t\tabc\t", foundValues={"abc": None})
    self.helper_getAllAttributes_checkIfFound("selected", foundValues={"selected": None})

  def test_getAllAttributes_found_singleNameWithValue(self):
    self.helper_getAllAttributes_checkIfFound("b='2'", foundValues={"b": "2"})
    self.helper_getAllAttributes_checkIfFound("b=\"2\"", foundValues={"b": "2"})
    self.helper_getAllAttributes_checkIfFound("b=\"2='3'\"", foundValues={"b": "2='3'"})
    self.helper_getAllAttributes_checkIfFound("b=\"2='3's'a\"", foundValues={"b": "2='3's'a"})
    self.helper_getAllAttributes_checkIfFound("class\r\n\t\t  = \t\t' class1\tclass2 '",
                                              foundValues={"class": " class1\tclass2 "})

  def test_getAllAttributes_found_oneNameMultipleTimes(self):
    self.helper_getAllAttributes_checkIfFound("selected selected", foundValues={"selected": None})
    self.helper_getAllAttributes_checkIfFound("selected selected = 'True'", foundValues={"selected": None})
    self.helper_getAllAttributes_checkIfFound("selected = 'true' selected", foundValues={"selected": "true"})
    self.helper_getAllAttributes_checkIfFound("selected = 'false' selected = 'true'", foundValues={"selected": "false"})
    self.helper_getAllAttributes_checkIfFound("selected selected='none' selected= 'false' selected ='true'",
                                              foundValues={"selected": None})

  def test_getAllAttributes_found_multipleAttributes(self):
    self.helper_getAllAttributes_checkIfFound("b a", foundValues={"a": None, "b": None})
    self.helper_getAllAttributes_checkIfFound("b c a", foundValues={"a": None, "b": None, "c": None})
    self.helper_getAllAttributes_checkIfFound("b b c a a b c", foundValues={"a": None, "b": None, "c": None})
    self.helper_getAllAttributes_checkIfFound("\t\tclass\t\t\t\t='myClass'id\t\t\t\t= 'myId'\r\n",
                                              foundValues={"id": "myId", "class": "myClass"})
    self.helper_getAllAttributes_checkIfFound("\t\tclass\t\t\t\t='myClass cl2'id\t\t\t\t= 'myId id2'default",
                                              foundValues={"id": "myId id2", "class": "myClass cl2", "default": None})
    self.helper_getAllAttributes_checkIfFound("\t\tclass\t\t\t\t='myClass cl2'id\t\t\t\t= 'myId id2'default "
                                              "title = '2==\"2\" and option = \"check\"'",
                                              foundValues={"id": "myId id2", "class": "myClass cl2", "default": None,
                                                           "title": "2==\"2\" and option = \"check\""})

  def test_htmlDelimitedFromLeft_nonSense(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft(False, 0)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft("This is a string sample", None)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft(0, "Something")
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft("Something", -1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft("Something", 341)

  def test_htmlDelimitedFromLeft_emptyString(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromLeft("", 0)

  def test_htmlDelimitedFromLeft_indexZero(self):
    self.assertTrue(attr.htmlDelimitedFromLeft("Q", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft(" Q", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("ab", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("a b", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft(" a b ", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("abc", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("'abc'", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("a b c", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft(" a b c ", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("heyho-engineer", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft("heyho engineer", 0))
    self.assertTrue(attr.htmlDelimitedFromLeft(" heyho engineer ", 0))

  def test_htmlDelimitedFromLeft_notDelimitated(self):
    self.assertFalse(attr.htmlDelimitedFromLeft("special-table", 8))
    self.assertFalse(attr.htmlDelimitedFromLeft("XtableX", 4))
    self.assertFalse(attr.htmlDelimitedFromLeft("XtableX", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("[table]", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("[ table ]", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft(",'table','span'", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("(table)", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("-table-", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("<table>", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("<a href='img/logo.png'>", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("fa fa-btn fa-lg", 1))
    self.assertFalse(attr.htmlDelimitedFromLeft("fa fa-btn fa-lg", 6))

  def test_htmlDelimitedFromLeft_delimitated(self):
    self.assertTrue(attr.htmlDelimitedFromLeft(" my-class", 1))
    self.assertTrue(attr.htmlDelimitedFromLeft("class-1 my-class", 8))
    self.assertTrue(attr.htmlDelimitedFromLeft("class='my-class'", 7))
    self.assertTrue(attr.htmlDelimitedFromLeft('class="my-class"', 7))
    self.assertTrue(attr.htmlDelimitedFromLeft("class='my-class'", 6))
    self.assertTrue(attr.htmlDelimitedFromLeft('class="my-class"', 6))
    self.assertTrue(attr.htmlDelimitedFromLeft("=2", 1))

  def test_htmlDelimitedFromRight_nonSense(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight(False, 0)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight("This is a string sample", None)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight(0, "Something")
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight("Something", -1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight("Something", 341)

  def test_htmlDelimitedFromRight_emptyString(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFromRight("", 0)

  def test_htmlDelimitedFromRight_indexOfLastCharacter(self):
    self.assertTrue(attr.htmlDelimitedFromRight("Q", 0))
    self.assertTrue(attr.htmlDelimitedFromRight(" Q", 1))
    self.assertTrue(attr.htmlDelimitedFromRight("ab", 1))
    self.assertTrue(attr.htmlDelimitedFromRight("a b", 2))
    self.assertTrue(attr.htmlDelimitedFromRight(" a b ", 4))
    self.assertTrue(attr.htmlDelimitedFromRight("abc", 2))
    self.assertTrue(attr.htmlDelimitedFromRight("'abc'", 4))
    self.assertTrue(attr.htmlDelimitedFromRight("a b c", 4))
    self.assertTrue(attr.htmlDelimitedFromRight(" a b c ", 6))
    self.assertTrue(attr.htmlDelimitedFromRight("heyho-engineer", 13))
    self.assertTrue(attr.htmlDelimitedFromRight("heyho engineer", 13))
    self.assertTrue(attr.htmlDelimitedFromRight(" heyho engineer ", 15))

  def test_htmlDelimitedFromRight_notDelimitated(self):
    self.assertFalse(attr.htmlDelimitedFromRight("special-table", 6))
    self.assertFalse(attr.htmlDelimitedFromRight("tableX", 4))
    self.assertFalse(attr.htmlDelimitedFromRight("table_X", 1))
    self.assertFalse(attr.htmlDelimitedFromRight("table@X", 1))
    self.assertFalse(attr.htmlDelimitedFromRight("[table]", 5))
    self.assertFalse(attr.htmlDelimitedFromRight("'table','span'", 6))
    self.assertFalse(attr.htmlDelimitedFromRight("(table)", 5))
    self.assertFalse(attr.htmlDelimitedFromRight("-table-", 5))
    self.assertFalse(attr.htmlDelimitedFromRight("<table>", 5))
    self.assertFalse(attr.htmlDelimitedFromRight("<a xhref='img/logo.png'>", 3))
    self.assertFalse(attr.htmlDelimitedFromRight("fa fa-btn fa-lg", 0))
    self.assertFalse(attr.htmlDelimitedFromRight("fa fa-btn fa-lg", 4))

  def test_htmlDelimitedFromRight_delimitated(self):
    self.assertTrue(attr.htmlDelimitedFromRight("my-class ", 7))
    self.assertTrue(attr.htmlDelimitedFromRight("class-1 my-class", 6))
    self.assertTrue(attr.htmlDelimitedFromRight("class='my-class'", 4))
    self.assertTrue(attr.htmlDelimitedFromRight("class'my-class'", 4))
    self.assertTrue(attr.htmlDelimitedFromRight("class\"my-class\"", 4))
    self.assertTrue(attr.htmlDelimitedFromRight("class='my-class'", 5))
    self.assertTrue(attr.htmlDelimitedFromRight('class="my-class"', 5))
    self.assertTrue(attr.htmlDelimitedFromRight("  class='my-class'", 0))
    self.assertTrue(attr.htmlDelimitedFromRight(" 'my-class'", 0))
    self.assertTrue(attr.htmlDelimitedFromRight(" \"my-class\"", 0))
    self.assertTrue(attr.htmlDelimitedFromRight("class='my-class'", 14))
    self.assertTrue(attr.htmlDelimitedFromRight("class='my-class your-class'", 14))
    self.assertTrue(attr.htmlDelimitedFromRight('class="my-class"', 14))
    self.assertTrue(attr.htmlDelimitedFromRight("=2 ", 1))

  def test_charIsHtmlDelimiter_nonSense(self):
    with self.assertRaises(Exception):
      attr.charIsHtmlDelimiter(None)
    with self.assertRaises(Exception):
      attr.charIsHtmlDelimiter(12)
    with self.assertRaises(Exception):
      attr.charIsHtmlDelimiter(True)
    with self.assertRaises(Exception):
      attr.charIsHtmlDelimiter([])
    with self.assertRaises(Exception):
      attr.charIsHtmlDelimiter("string")

  def test_charIsHtmlDelimiter_delimiter(self):
    self.assertTrue(attr.charIsHtmlDelimiter("="))
    self.assertTrue(attr.charIsHtmlDelimiter("'"))
    self.assertTrue(attr.charIsHtmlDelimiter('"'))
    self.assertTrue(attr.charIsHtmlDelimiter(" "))
    self.assertTrue(attr.charIsHtmlDelimiter("\t"))
    self.assertTrue(attr.charIsHtmlDelimiter("\r"))
    self.assertTrue(attr.charIsHtmlDelimiter("\n"))

  def test_charIsHtmlDelimiter_notDelimiter(self):
    self.assertFalse(attr.charIsHtmlDelimiter("<"))
    self.assertFalse(attr.charIsHtmlDelimiter(">"))
    self.assertFalse(attr.charIsHtmlDelimiter("["))
    self.assertFalse(attr.charIsHtmlDelimiter("]"))
    self.assertFalse(attr.charIsHtmlDelimiter("("))
    self.assertFalse(attr.charIsHtmlDelimiter(")"))
    self.assertFalse(attr.charIsHtmlDelimiter("0"))
    self.assertFalse(attr.charIsHtmlDelimiter("a"))
    self.assertFalse(attr.charIsHtmlDelimiter("Z"))
    self.assertFalse(attr.charIsHtmlDelimiter("_"))
    self.assertFalse(attr.charIsHtmlDelimiter("-"))
    self.assertFalse(attr.charIsHtmlDelimiter("#"))
    self.assertFalse(attr.charIsHtmlDelimiter("."))

  def test_stringIsHtmlDelimited_nonSense(self):
    with self.assertRaises(Exception):
      attr.stringIsHtmlDelimited("string", 0, False)
    with self.assertRaises(Exception):
      attr.stringIsHtmlDelimited("string", True, 2)
    with self.assertRaises(Exception):
      attr.stringIsHtmlDelimited(2341, 0, 2)
    with self.assertRaises(Exception):
      attr.stringIsHtmlDelimited(False, True, False)
    with self.assertRaises(Exception):
      attr.stringIsHtmlDelimited(None, None, None)

  def test_stringIsHtmlDelimited_delimited(self):
    self.assertTrue(attr.stringIsHtmlDelimited("012345678", 0, 9))
    self.assertTrue(attr.stringIsHtmlDelimited("0", 0, 1))
    self.assertTrue(attr.stringIsHtmlDelimited("01", 0, 2))
    self.assertTrue(attr.stringIsHtmlDelimited("012", 0, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc def ghi", 0, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc def ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc def ghi", 8, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc=def=ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("=abc=def=ghi=", 5, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc'def'ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc\"def\"ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc'def\"ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc\"def'ghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc\tdef\tghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc\tdef\nghi", 4, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("abc'''def'''ghi", 6, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("'abc' 'def' 'ghi'", 7, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("'abc' =def' 'ghi'", 7, 3))
    self.assertTrue(attr.stringIsHtmlDelimited("'abc' 'def= 'ghi'", 7, 3))

  def test_stringIsHtmlDelimited_notDelimited(self):
    self.assertFalse(attr.stringIsHtmlDelimited("012345678", 1, 7))
    self.assertFalse(attr.stringIsHtmlDelimited("012345678", 1, 8))
    self.assertFalse(attr.stringIsHtmlDelimited("012345678", 0, 4))
    self.assertFalse(attr.stringIsHtmlDelimited("qwe_asd_zxc", 4, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("qwe[asd]zxc", 4, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("qwe [asd] zxc", 5, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("qwe <asd> zxc", 4, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("truth:1+1=2", 6, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("truth=1+1<3", 6, 3))
    self.assertFalse(attr.stringIsHtmlDelimited("truth: '1+1>1'", 8, 3))
    self.assertFalse(attr.stringIsHtmlDelimited('truth: "3<1+1>1"', 10, 3))

  def test_isThereNonDelimiterCharBeforeIdx_nonSense(self):
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx("text", -1)
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx("text", 123)
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx("text", 4)
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx(12, 123)
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx(False, 0)
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx(None, None)

  def test_isThereNonDelimiterCharBeforeIdx_emptyString(self):
    with self.assertRaises(Exception):
      attr.isThereNonDelimiterCharBeforeIdx("", 0)

  def test_isThereNonDelimiterCharBeforeIdx_thereIsNot(self):
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("text", 0))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("this is an another string", 0))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number=2", 7))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number='2'", 8))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number='2'", 7))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number = 2", 9))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number = '2'", 10))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx("number '2'", 8))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx('number="2"', 8))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx('number="2"', 7))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx('number = "2"', 10))
    self.assertFalse(attr.isThereNonDelimiterCharBeforeIdx('number "2"', 8))

  def test_isThereNonDelimiterCharBeforeIdx_thereIs(self):
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("text", 3))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("this is an another string", 11))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("this is an another string", 15))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("one-two-three", 4))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("one-two-three", 1))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("value = 'one'", 6))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("value= 'one'", 5))
    self.assertTrue(attr.isThereNonDelimiterCharBeforeIdx("value='one'", 5))

  def test_nextNonWhiteSpaceCharIsHtmlDelimiter_nonSense(self):
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter("string", -1)
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter("string", 523)
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter("string", 6)
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter(False, 0)
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter("string", True)
    with self.assertRaises(Exception):
      attr.nextNonWhiteSpaceCharIsHtmlDelimiter(None, [])

  def test_nextNonWhiteSpaceCharIsHtmlDelimiter_itIsNot(self):
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X ", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("     ", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(" \t \r \n ", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X     ", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X     ", 1))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X\t\r\n", 0))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("X\t\r\n", 1))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("abcdefgh", 3))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("0123456789", 9))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("one-two-three", 2))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("one two three", 2))
    self.assertFalse(attr.nextNonWhiteSpaceCharIsHtmlDelimiter("one\t\ttwo\t\t\tthree", 2))

  def test_nextNonWhiteSpaceCharIsHtmlDelimiter_itIs(self):
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(" 'value'", 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(" 'value'", 6))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(" \t 'value' ", 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(" \t 'value ' ", 9))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(' "value"', 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter(' = "value"', 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter('\t\t\r\n"value"', 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter('\t\t\r\n="value"', 0))
    self.assertTrue(attr.nextNonWhiteSpaceCharIsHtmlDelimiter('attr\t = "value"', 3))

  def test_isThereAnyQuoteChar_nonSense(self):
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", -1, 3)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", 0, 6)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", -20, 146)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", 2, True)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", "", 4)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("String", [], {})
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar(None, 0, 0)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar(None, None, None)
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar(True, False, True)

  def test_isThereAnyQuoteChar_emptyString(self):
    with self.assertRaises(Exception):
      attr.isThereAnyQuoteChar("", 0, 0)

  def test_isThereAnyQuoteChar_thereIs(self):
    self.assertTrue(attr.isThereAnyQuoteChar("'", 0, 0))
    self.assertTrue(attr.isThereAnyQuoteChar("'''''''''", 0, 8))
    self.assertTrue(attr.isThereAnyQuoteChar("\"\"\"\"'''''", 0, 8))
    self.assertTrue(attr.isThereAnyQuoteChar("\"\"\"\"'''''", 2, 5))
    self.assertTrue(attr.isThereAnyQuoteChar('"', 0, 0))
    self.assertTrue(attr.isThereAnyQuoteChar('"""""""""', 0, 8))
    self.assertTrue(attr.isThereAnyQuoteChar("1'2", 0, 2))
    self.assertTrue(attr.isThereAnyQuoteChar("0123456789'9876543210", 0, 10))
    self.assertTrue(attr.isThereAnyQuoteChar("0123456789'9876543210", 10, 20))
    self.assertTrue(attr.isThereAnyQuoteChar("0123456789'9876543210", 5, 15))
    self.assertTrue(attr.isThereAnyQuoteChar("'one' \" two \"", 0, 12))
    self.assertTrue(attr.isThereAnyQuoteChar("'one' \" two \"", 2, 9))

  def test_isThereAnyQuoteChar_thereIsNot(self):
    self.assertFalse(attr.isThereAnyQuoteChar("Q", 0, 0))
    self.assertFalse(attr.isThereAnyQuoteChar("string", 0, 5))
    self.assertFalse(attr.isThereAnyQuoteChar("string", 1, 4))
    self.assertFalse(attr.isThereAnyQuoteChar("'value'", 1, 5))
    self.assertFalse(attr.isThereAnyQuoteChar("\"value\"", 1, 5))
    self.assertFalse(attr.isThereAnyQuoteChar("'''\"\"TEXT\"''''", 5, 8))
    self.assertFalse(attr.isThereAnyQuoteChar("'''\"\"TEXT\"''''", 6, 7))
    self.assertFalse(attr.isThereAnyQuoteChar("'''\"\"TEXT\"''''", 6, 6))

  def helper_validateAdjacentCharsNearEqualChar_checkIfThrows(self, arg1, arg2):
    with self.assertRaises(Exception):
      attr.validateAdjacentCharsNearEqualChar("string", -1)

  def test_validateAdjacentCharsNearEqualChar_nonSense(self):
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("string", -1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("string", 52)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("string", True)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("string", {})
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("string", [])
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows({}, 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows(None, None)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows(True, False)

  def test_validateAdjacentCharsNearEqualChar_emptyString(self):
    self.helper_validateAdjacentCharsNearEqualChar_checkIfThrows("", 0)

  def helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt(self, htmlString, equalIndex):
    result = attr.validateAdjacentCharsNearEqualChar(htmlString, equalIndex)
    self.assertEqual(result, (True, -1))

  def test_validateAdjacentCharsNearEqualChar_equalNotFound(self):
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("Q", 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("apple", 2)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("ab_cd", 2)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("01", 1)

  def test_validateAdjacentCharsNearEqualChar_corrupt(self):
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("=", 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("= = =", 1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("= 2", 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("= '", 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt(" = '", 1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("= \"", 0)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt(" = \"", 1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("'='", 1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt('"="', 1)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("value = 2", 6)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt('value = \t', 6)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt('value =', 6)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("'field' = 'value'", 8)
    self.helper_validateAdjacentCharsNearEqualChar_checkIfCorrupt("'field' = \"value\"", 8)

  def test_validateAdjacentCharsNearEqualChar_valid(self):
    corrupt, quoteIdx = attr.validateAdjacentCharsNearEqualChar("a='", 1)
    self.assertFalse(corrupt)
    self.assertEqual(quoteIdx, 2)
    corrupt, quoteIdx = attr.validateAdjacentCharsNearEqualChar("a = '", 2)
    self.assertFalse(corrupt)
    self.assertEqual(quoteIdx, 4)
    corrupt, quoteIdx = attr.validateAdjacentCharsNearEqualChar("a\t\n=\t\t\t\"", 3)
    self.assertFalse(corrupt)
    self.assertEqual(quoteIdx, 7)

  def test_getAndValidateClosingQuote_nonSense(self):
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("clas = 'fa-lg2'", -1)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("clas = 'fa-lg2'", 15)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("clas = 'fa-lg2'", 56)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("clas = 'fa-lg2'", True)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("clas = 'fa-lg2'", "")
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote(True, 0)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote(True, True)
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote(None, None)

  def test_getAndValidateClosingQuote_emptyString(self):
    with self.assertRaises(Exception):
      attr.getAndValidateClosingQuote("", 0)

  def helper_getAndValidateClosingQuote_checkIfCorrupt(self, stringArg, indexArg):
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote(stringArg, indexArg)
    self.assertTrue(corrupt)
    self.assertEqual(closingQuoteIdx, -1)
    self.assertEqual(quoteChar, "")

  def test_getAndValidateClosingQuote_idxIsNotQuote(self):
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("Q", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("QxQ", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("Lx", 1)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("apple", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("'apple'", 1)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("'apple'", 3)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = \"apple\"", 6)

  def test_getAndValidateClosingQuote_thereIsNoClosingQuote(self):
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("'Q", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("\"Q", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'myClass yourClass", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'myClass\"", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = \"myClass yourClass", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = \"myClass'", 8)

  def test_getAndValidateClosingQuote_thereIsClosingQuoteButCorrupt(self):
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("'Q'=", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("\"Q\"=", 0)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'number = 2'=3", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'number = 2'    =   3", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'number = 2''", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'number = 2'\n\t\t\n' hello", 8)
    self.helper_getAndValidateClosingQuote_checkIfCorrupt("class = 'number = 2'\n\n' hello'", 8)

  def test_getAndValidateClosingQuote_valid(self):
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote("'apple'", 0)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 6)
    self.assertEqual(quoteChar, "'")
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('"myClass yourClass"', 0)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 18)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('" myClass yourClass "', 0)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 20)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('title = "it\'s a title"', 8)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 21)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('title = "it\'s a title" id = "specialId"', 8)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 21)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('title = "it\'s a title" id = \'specId\'', 8)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 21)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote('class = "specialClass" id = "specialId"', 28)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 38)
    self.assertEqual(quoteChar, '"')
    corrupt, closingQuoteIdx, quoteChar = attr.getAndValidateClosingQuote("integrity=\"sha512-6PM0qxuIQ==\"", 10)
    self.assertFalse(corrupt)
    self.assertEqual(closingQuoteIdx, 29)
    self.assertEqual(quoteChar, '"')

  def test_getQuoteIndexesByEqualChar_nonSense(self):
    with self.assertRaises(Exception):
      attr.getQuoteIndexesByEqualChar("string", -1)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesByEqualChar("string", 42)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesByEqualChar("string", 6)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesByEqualChar("string", "")
    with self.assertRaises(Exception):
      attr.getQuoteIndexesByEqualChar("string", True)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesByEqualChar("string", None)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesByEqualChar(True, 0)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesByEqualChar(2, 0)
    with self.assertRaises(Exception):
      attr.getQuoteIndexesByEqualChar(None, None)

  def test_getQuoteIndexesByEqualChar_emptyString(self):
    with self.assertRaises(Exception):
      attr.getQuoteIndexesByEqualChar("", 0)

  def helper_getQuoteIndexesByEqualChar_checkIfCorrupt(self, string, equalCharIdx):
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                            = attr.getQuoteIndexesByEqualChar(string, equalCharIdx)
    self.assertTrue(corrupt)
    self.assertEqual(openingQuoteCharIdx, -1)
    self.assertEqual(closingQuoteIdx, -1)
    self.assertEqual(mainQuoteChar, "")

  def test_getQuoteIndexesByEqualChar_notEqualChar(self):
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("Q", 0)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("'Q'", 1)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("apple", 4)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("class = 'myClass'", 0)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("class = \"myClass\"", 0)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("class = 'myClass'", 5)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("class = \"myClass\"", 5)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("class = 'myClass'", 7)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("class = \"myClass\"", 7)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("class = 'myClass'", 8)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("class = \"myClass\"", 8)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("class = 'myClass'", 11)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("class = \"myClass\"", 11)

  def test_getQuoteIndexesByEqualChar_noQuotes(self):
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("=", 0)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("= 2", 0)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = 2", 6)

  def test_getQuoteIndexesByEqualChar_onlyOneMainQuote(self):
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("= '2", 0)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("= \"2", 0)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("= 2'", 0)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("= 2\"", 0)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = '", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value ='", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = \"", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value =\"", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = 2'", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = 2\"", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = '2", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = \"2", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = \"2'", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = '2\"", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = '2\"\"\"", 6)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("value = \"2'''", 6)

  def test_getQuoteIndexesByEqualChar_otherInvalid(self):
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("= '2'", 0)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("\" = '2'", 2)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("\t\t\t = '2'", 4)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("\t\t\t = '2''", 4)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("\t\t\t = '''", 4)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("\t\t\t = ''''", 4)
    self.helper_getQuoteIndexesByEqualChar_checkIfCorrupt("\t\t\t = '''''", 4)

  def test_getQuoteIndexesByEqualChar_validEmptyValue(self):
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                  = attr.getQuoteIndexesByEqualChar("value=''\tdisabled='False'", 5)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (6, 7, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar("value=''", 5)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (6, 7, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar("value =''", 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (7, 8, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar("value = ''", 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 9, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                        = attr.getQuoteIndexesByEqualChar("value\n\t=\t\r\n\t''", 7)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (12, 13, "'"))

    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar('value=""', 5)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (6, 7, "\""))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar('value =""', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (7, 8, "\""))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar('value = ""', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 9, "\""))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                        = attr.getQuoteIndexesByEqualChar('value\n\t=\t\r\n\t""', 7)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (12, 13, "\""))

  def test_getQuoteIndexesByEqualChar_validNonEmptyValue(self):
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar("value=' '", 5)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (6, 8, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar('value=" "', 5)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (6, 8, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar("value =' '", 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (7, 9, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar('value =" "', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (7, 9, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar("value = ' '", 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 10, "'"))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar = attr.getQuoteIndexesByEqualChar('value = " "', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 10, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                    = attr.getQuoteIndexesByEqualChar('value = " \t "', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 12, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                    = attr.getQuoteIndexesByEqualChar('value = "test"', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 13, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                    = attr.getQuoteIndexesByEqualChar('value = "\ttest1 test2 "', 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 22, '"'))
    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                                    = attr.getQuoteIndexesByEqualChar("value = '\ttest1 test2 '", 6)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (8, 22, "'"))

    corrupt, openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar \
                                              = attr.getQuoteIndexesByEqualChar("integrity='sha512-6PM0qxuIQ=='", 9)
    self.assertFalse(corrupt)
    self.assertEqual((openingQuoteCharIdx, closingQuoteIdx, mainQuoteChar), (10, 29, "'"))

  def test_htmlDelimitedFind_nonSense(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind(None, "findThis", 0, 1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", None, 0, 1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind(0, 12, 0, 1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", None, 1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", 0, None)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", True, False)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", "", "")
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", 3, 3)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", -2, 3)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", 1, 56)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("Scan my text", "text", 10, 4)

  def test_htmlDelimitedFind_emptyStrings(self):
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("", "findThis", 0, 1)
    with self.assertRaises(Exception):
      attr.htmlDelimitedFind("find something in this string", "", 0, 1)

  def helper_htmlDelimitedFind_checkNotFound(self, stringToScan, stringToMatch, startIdx, endIdx):
    found, firstIdx = attr.htmlDelimitedFind(stringToScan, stringToMatch, startIdx, endIdx)
    self.assertFalse(found)
    self.assertEqual(firstIdx, -1)

  def test_htmlDelimitedFind_stringNotFoundAtAll(self):
    self.helper_htmlDelimitedFind_checkNotFound("a", "b", 0, 1)
    self.helper_htmlDelimitedFind_checkNotFound("this is my string", "findMe", 0, 17)
    self.helper_htmlDelimitedFind_checkNotFound("this is my lovely little string", "this", 1, 31)
    self.helper_htmlDelimitedFind_checkNotFound("this is my lovely little string", "string", 0, 27)
    self.helper_htmlDelimitedFind_checkNotFound("this is my lovely little string", "my", 11, 24)
    self.helper_htmlDelimitedFind_checkNotFound("this is my lovely little string", "string", 11, 24)

  def test_htmlDelimitedFind_foundStringIsNotHtmlDelimited(self):
    self.helper_htmlDelimitedFind_checkNotFound("pineapple", "pine", 0, 9)
    self.helper_htmlDelimitedFind_checkNotFound("pineapple", "apple", 0, 9)
    self.helper_htmlDelimitedFind_checkNotFound("pineapple", "neapple", 0, 9)
    self.helper_htmlDelimitedFind_checkNotFound("one-two-three", "one", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one-two-three", "two", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one-two-three", "three", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one;two;three", "one", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one;two;three", "two", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one;two;three", "three", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one,two,three", "one", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one,two,three", "two", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one,two,three", "three", 0, 13)
    self.helper_htmlDelimitedFind_checkNotFound("one, two, three.", "one", 0, 16)
    self.helper_htmlDelimitedFind_checkNotFound("one, two, three.", "two", 0, 16)
    self.helper_htmlDelimitedFind_checkNotFound("one, two, three.", "three", 0, 16)

  def test_htmlDelimitedFind_stringFound(self):
    found, firstIdx = attr.htmlDelimitedFind("one two three", "one", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 0)
    found, firstIdx = attr.htmlDelimitedFind("one two three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one two three", "three", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 8)
    found, firstIdx = attr.htmlDelimitedFind("one=two=three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one'two'three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one\"two\"three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one'two\"three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one\"two'three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("one=two'three", "two", 0, 13)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 4)
    found, firstIdx = attr.htmlDelimitedFind("'one'two=three", "two", 0, 14)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 5)
    found, firstIdx = attr.htmlDelimitedFind("a", "a", 0, 1)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 0)
    found, firstIdx = attr.htmlDelimitedFind("abc", "abc", 0, 3)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 0)
    found, firstIdx = attr.htmlDelimitedFind("value=2", "2", 2, 7)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 6)
    found, firstIdx = attr.htmlDelimitedFind("value=2", "value", 0, 7)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 0)
    found, firstIdx = attr.htmlDelimitedFind("hrefx='2' href", "href", 0, 14)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 10)
    found, firstIdx = attr.htmlDelimitedFind("hrefx='2' rel='xhref' href", "href", 0, 26)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 22)
    found, firstIdx = attr.htmlDelimitedFind("hrefx='2' rel='xhref' hrefhrefhref href", "href", 0, 39)
    self.assertTrue(found)
    self.assertEqual(firstIdx, 35)

  def test_indexIsWithinHtmlAttributeValue_nonSense(self):
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue("text", "")
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue(0, 0)
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue(None, None)
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue([], True)
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue("this is a text", -1)
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue("this is a text", 341)
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue("this is a text", 14)

  def test_indexIsWithinHtmlAttributeValue_emptyString(self):
    with self.assertRaises(Exception):
      attr.indexIsWithinHtmlAttributeValue("", 0)

  def helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt(self, string, index):
    corrupt, isAttributeValue = attr.indexIsWithinHtmlAttributeValue(string, index)
    self.assertTrue(corrupt)
    self.assertIsNone(isAttributeValue)

  def helper_indexIsWithinHtmlAttributeValue_checkIfNotValue(self, string, index):
    corrupt, isAttributeValue = attr.indexIsWithinHtmlAttributeValue(string, index)
    self.assertFalse(corrupt)
    self.assertFalse(isAttributeValue)

  def helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue(self, string, index):
    corrupt, isAttributeValue = attr.indexIsWithinHtmlAttributeValue(string, index)
    self.assertFalse(corrupt)
    self.assertTrue(isAttributeValue)

  def test_indexIsWithinHtmlAttributeValue_corrupt_quoteCharButNotEqualFound(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("''", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'''", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("''''", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("''''", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("''''", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("''", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"\"", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"\"", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'apple", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'apple", 4)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("apple'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("apple'", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("apple'", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("ap'ple", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("ap'ple", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"apple\"", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"apple\"", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'apple'", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'carrot' 'apple'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'carrot apple'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'carrot apple'", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'carrot apple'", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot'apple", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot'apple", 6)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot'apple", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot''''''apple", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot''''''apple", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot' 'apple", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot\" 'apple", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot' \"apple", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("carrot\" \"apple", 7)

  def test_indexIsWithinHtmlAttributeValue_corrupt_equalButNotQuoteFound(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("=", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= ", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= ", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= 2", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= 2", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= 2", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 234", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 17)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 20)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 21)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 22)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value1 = text value2 = anotherText", 28)

  def test_indexIsWithinHtmlAttributeValue_corrupt_quotesAreNotCorrect(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = '2\"", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = \"2'", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = \"2", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = '2", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = '''2", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = '''2'", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = ''''2", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2'", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2''", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2'''", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2\"", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2\"'", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2\"\"'", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2\"''", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2'\"", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2'\"\"", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("value = 2''\"", 8)

  def test_indexIsWithinHtmlAttributeValue_corrupt_noAttributeValue(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= 'two'", 4)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\t\t\t=\t'two'", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt(" = 'two'", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("= \"two\"", 4)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt(" = \"two\"", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'number' = 'two'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("'number' = \"two\"", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("\"number\" = 'two'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("' = 'two'", 7)

  def test_indexIsWithinHtmlAttributeValue_corrupt_tooMuchQuotes(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = 'two''", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = 'two'''", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = ''two'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = ''two''", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = '''two'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = '''two''", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = '''two'''", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = ''two'''", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = 'two'''", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = 'two''", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = 'two''", 11)

  def test_indexIsWithinHtmlAttributeValue_corrupt_tooMuchEqual(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number == 'two'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number = = 'two'", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number ='two'=", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number =\t'two'\t=", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number =\t'two'\t==", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfCorrupt("number =\t'two'\t= '2'", 11)

  def test_indexIsWithinHtmlAttributeValue_attributeName(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue(" ", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("a", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("ab", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("ab", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 1)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 3)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("one two three", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 0)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 2)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 4)

  def test_indexIsWithinHtmlAttributeValue_attributeValue(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' '", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = \" \"", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' 'notEmpty=\"value\"", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' 'notEmpty='value'", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' 'notEmpty='value'", 21)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = \" \" class = 'myClass'", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' ' class = 'myClass'", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("empty = ' ' class = 'myClass'", 24)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("id\t\t\t=\n\n'mainContent\t\n\tanyContent'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("id\t\t\t=\n\n'mainContent\t\n\tanyContent'", 20)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("id\t\t\t=\n\n'mainContent\t\n\tanyContent'", 21)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("id\t\t\t=\n\n'mainContent\t\n\tanyContent'", 22)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("id\t\t\t=\n\n'mainContent\t\n\tanyContent'", 25)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class = 'cl1 cl2'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class = 'cl1\"cl2'", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class = \"cl1 cl2\"", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class = \"cl1'cl2\"", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class='cl1 cl2'", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class='cl1\"cl2'", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class=\"cl1 cl2\"", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("class=\"cl1'cl2\"", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the title'\"", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the title'\"", 15)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the title'\"", 16)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the title'\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the title'\"", 25)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the'title'\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the'title'\"", 25)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the=title'\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is 'the=title'\"", 25)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is =the=title=\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"this is =the=title=\"", 25)

  def test_indexIsWithinHtmlAttributeValue_equalInAttributeValue(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title='='", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title='==='", 7)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title='==='", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title='==='", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=two\"", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=two\"", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=two\"", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number='two'\"", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number='two'\"", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number='two'\"", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number='two'\"", 16)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 10)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 15)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 16)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"number=='two'\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 15)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 17)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 18)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 21)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 22)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"==number=='two'==\"", 23)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input=number=two\"", 8)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input=number=two\"", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input=number=two\"", 15)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input=number=two\"", 19)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input=number=two\"", 20)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 11)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 12)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 13)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 20)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 21)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 22)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 25)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"input='number='two''\"", 26)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"class='myClass'\"class='myClass'", 30)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"class='myClass'\"class='myClass'", 9)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfAttributeValue("title=\"class='myClass'\"class='myClass'", 16)

  def test_indexIsWithinHtmlAttributeValue_equalMainCharAndBetween(self):
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 6)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class='myClass'", 14)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class = 'myClass'", 5)
    self.helper_indexIsWithinHtmlAttributeValue_checkIfNotValue("class = 'myClass'", 7)

  def test_stringContainsHtmlDelimiter_nonSense(self):
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", 0, 67)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", 0, 7)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", 0, None)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", 0, True)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", -1, 4)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", 5, 2)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", None, 2)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter("string", None, None)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter(None, 0, 2)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter(0, 0, 0)
    with self.assertRaises(Exception):
      attr.stringContainsHtmlDelimiter(None, None, None)

  def test_stringContainsHtmlDelimiter_true(self):
    result = attr.stringContainsHtmlDelimiter(" ", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("=", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("'", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("\"", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("\t", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("\n", 0, 1)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter(" '='= \"\" ", 0, 9)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("hello world!", 0, 12)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("hello world!", 5, 12)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("hello world!", 0, 6)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("hello world!", 2, 8)
    self.assertTrue(result)
    result = attr.stringContainsHtmlDelimiter("class='myClass'", 0, 15)
    self.assertTrue(result)

  def test_stringContainsHtmlDelimiter_false(self):
    result = attr.stringContainsHtmlDelimiter("Q", 0, 1)
    self.assertFalse(result)
    result = attr.stringContainsHtmlDelimiter("apple", 0, 5)
    self.assertFalse(result)
    result = attr.stringContainsHtmlDelimiter("'apple'", 1, 6)
    self.assertFalse(result)
    result = attr.stringContainsHtmlDelimiter("true != false", 0, 4)
    self.assertFalse(result)
    result = attr.stringContainsHtmlDelimiter("true != false", 8, 13)
    self.assertFalse(result)

  def helper_getFirstHtmlDelimiter_exceptionRaised(self, string, inclusiveStartIdx, exclusiveEndIdx):
    with self.assertRaises(Exception):
      attr.getFirstHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)

  def helper_getFirstHtmlDelimiter_notFound(self, string, inclusiveStartIdx, exclusiveEndIdx):
    found, idx = attr.getFirstHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertFalse(found)
    self.assertEqual(idx, -1)

  def helper_getFirstHtmlDelimiter_found(self, string, inclusiveStartIdx, exclusiveEndIdx, foundAt):
    found, idx = attr.getFirstHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertTrue(found)
    self.assertEqual(idx, foundAt)

  def test_getFirstHtmlDelimiter_nonSense(self):
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, 345)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, 7)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, None)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, True)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, [])
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 0, "")
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", -1, 2)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", -1, 45)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 5, 3)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", None, 3)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", True, 3)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", True, False)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", None, None)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", "", "")
    self.helper_getFirstHtmlDelimiter_exceptionRaised("string", 2, 2)
    self.helper_getFirstHtmlDelimiter_exceptionRaised(None, 0, 3)
    self.helper_getFirstHtmlDelimiter_exceptionRaised([], 0, 3)
    self.helper_getFirstHtmlDelimiter_exceptionRaised(None, None, None)
    self.helper_getFirstHtmlDelimiter_exceptionRaised(0, 0, 0)

  def test_getFirstHtmlDelimiter_emptyString(self):
    self.helper_getFirstHtmlDelimiter_exceptionRaised("", 0, 0)
    self.helper_getFirstHtmlDelimiter_exceptionRaised("", 0, 1)

  def test_getFirstHtmlDelimiter_notFound(self):
    self.helper_getFirstHtmlDelimiter_notFound("Q", 0, 1)
    self.helper_getFirstHtmlDelimiter_notFound("one-two-three", 0, 13)
    self.helper_getFirstHtmlDelimiter_notFound("=Hello=", 1, 6)
    self.helper_getFirstHtmlDelimiter_notFound("\n'greeting'\t= \"Hello\" ", 2, 10)
    self.helper_getFirstHtmlDelimiter_notFound("\n'greeting'\t= \"Hello\" ", 15, 20)

  def test_getFirstHtmlDelimiter_found(self):
    self.helper_getFirstHtmlDelimiter_found(" ", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("\t", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("\n", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("'", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("\"", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("=", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("'=='", 0, 1, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("key = 'value'", 0, 11, foundAt = 3)
    self.helper_getFirstHtmlDelimiter_found("key='value'", 0, 11, foundAt = 3)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 0, 17, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 0, 4, foundAt = 0)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 1, 17, foundAt = 1)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 1, 3, foundAt = 1)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 2, 17, foundAt = 5)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 5, 17, foundAt = 5)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 6, 17, foundAt = 6)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 8, 17, foundAt = 8)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 11, 17, foundAt = 16)
    self.helper_getFirstHtmlDelimiter_found("\n'key'\t\t= \"value\"", 3, 11, foundAt = 5)

  def helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised(self, string, inclusiveStartIdx, exclusiveEndIdx):
    with self.assertRaises(Exception):
      attr.getFirstHtmlDelimiterThenSkipWhiteSpaces(string, inclusiveStartIdx, exclusiveEndIdx)

  def helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound(self, string, inclusiveStartIdx, exclusiveEndIdx):
    found, idx = attr.getFirstHtmlDelimiterThenSkipWhiteSpaces(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertFalse(found)
    self.assertEqual(idx, -1)

  def helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound(self, string, inclusiveStartIdx,
                                                                   exclusiveEndIdx, foundAt):
    found, idx = attr.getFirstHtmlDelimiterThenSkipWhiteSpaces(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertTrue(found)
    self.assertEqual(idx, foundAt)

  def test_getFirstHtmlDelimiterThenSkipWhiteSpaces_nonSense(self):
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, 345)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, 7)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, None)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, True)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, [])
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 0, "")
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", -1, 2)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", -1, 45)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 5, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", None, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", True, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", True, False)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", None, None)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", "", "")
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("string", 2, 2)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised(None, 0, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised([], 0, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised(None, None, None)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised(0, 0, 0)

  def test_getFirstHtmlDelimiterThenSkipWhiteSpaces_emptyString(self):
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_exceptionRaised("", 0, 1)

  def test_getFirstHtmlDelimiterThenSkipWhiteSpaces_notFound(self):
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("Q", 0, 1)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound(" ", 0, 1)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("string", 0, 6)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two three", 0, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two three", 4, 7)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two three", 8, 13)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("<one-two-three>", 0, 15)

  def test_getFirstHtmlDelimiterThenSkipWhiteSpaces_LastIdxIsWhiteSpace(self):
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two three", 0, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one\ttwo three", 0, 3)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two three", 4, 8)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfNotFound("one two\nthree", 4, 8)

  def test_getFirstHtmlDelimiterThenSkipWhiteSpaces_found(self):
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("=", 0, 1, foundAt=0)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("'", 0, 1, foundAt=0)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("\"", 0, 1, foundAt=0)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("one two three", 0, 13, foundAt=4)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("one two three", 4, 13, foundAt=8)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("one two=three", 4, 13, foundAt=7)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("key\r\n\t = value", 1, 14, foundAt=7)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("key\r\n\t 'value'", 1, 14, foundAt=7)
    self.helper_getFirstHtmlDelimiterThenSkipWhiteSpaces_checkIfFound("key\r\n\t \"value\"", 1, 14, foundAt=7)

  def helper_getLastValueByFoundEquals_exceptionRaised(self, string, inclStartIdx, inclEndIdx):
    with self.assertRaises(Exception):
      attr.getLastValueByFoundEquals(string, inclStartIdx, inclEndIdx)

  def helper_getLastValueByFoundEquals_checkIfCorrupt(self, string, inclStartIdx, inclEndIdx):
    corrupt, found, equalIdx, openingQuoteIdx, ClosingQuoteIdx \
                                                      = attr.getLastValueByFoundEquals(string, inclStartIdx, inclEndIdx)
    self.assertTrue(corrupt)
    self.assertFalse(found)
    self.assertEqual(equalIdx, -1)
    self.assertEqual(openingQuoteIdx, -1)
    self.assertEqual(ClosingQuoteIdx, -1)

  def helper_getLastValueByFoundEquals_checkIfNotFound(self, string, inclStartIdx, inclEndIdx):
    corrupt, found, equalIdx, openingQuoteIdx, ClosingQuoteIdx \
                                                      = attr.getLastValueByFoundEquals(string, inclStartIdx, inclEndIdx)
    self.assertFalse(corrupt)
    self.assertFalse(found)
    self.assertEqual(equalIdx, -1)
    self.assertEqual(openingQuoteIdx, -1)
    self.assertEqual(ClosingQuoteIdx, -1)

  def helper_getLastValueByFoundEquals_checkIfFound(self, string, inclStartIdx, inclEndIdx, equalIdxAt,
                                                    openingQuoteIdxAt, closingQuoteIdxAt):
    corrupt, found, equalIdx, openingQuoteIdx, closingQuoteIdx \
                                                      = attr.getLastValueByFoundEquals(string, inclStartIdx, inclEndIdx)
    self.assertFalse(corrupt)
    self.assertTrue(found)
    self.assertEqual(equalIdx, equalIdxAt)
    self.assertEqual(openingQuoteIdx, openingQuoteIdxAt)
    self.assertEqual(closingQuoteIdx, closingQuoteIdxAt)

  def test_getLastValueByFoundEquals_nonSense(self):
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", -1, 2)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 6, 8)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 36, 75)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 5, 2)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 1, None)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 1, "")
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", 1, True)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", None, 4)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", "", 4)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", True, 4)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", True, True)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", None, None)
    self.helper_getLastValueByFoundEquals_exceptionRaised("string", "string", "string")
    self.helper_getLastValueByFoundEquals_exceptionRaised([], 0, 0)
    self.helper_getLastValueByFoundEquals_exceptionRaised(True, True, True)
    self.helper_getLastValueByFoundEquals_exceptionRaised(None, None, None)

  def test_getLastValueByFoundEquals_emptyString(self):
    self.helper_getLastValueByFoundEquals_exceptionRaised("", 0, 0)

  def test_getLastValueByFoundEquals_corrupt_onlyEqual(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("=", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= ", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = ", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = ", 0, 2)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = ", 1, 2)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = ", 1, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = ", 1, 2)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = = ", 1, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" == ", 1, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 0, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 0, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 1, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 1, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 2, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n=\t\t", 2, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\r\n = \t \t", 0, 7)

  def test_getLastValueByFoundEquals_corrupt_onlyQuotes(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\"", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("''", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("''", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("''", 1, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt('""', 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt('""', 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" ' ", 0, 2)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\n\t'\t\n", 0, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("''''", 0, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'\"'\"", 0, 3)

  def test_getLastValueByFoundEquals_corrupt_noQuotes(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("=2", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("=2", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= 2", 0, 2)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("=\t\t2", 0, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2", 0, 5)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2", 1, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2", 1, 5)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a = 4", 0, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number = one two", 0, 14)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number = one two", 0, 10)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number = one two", 0, 7)

  def test_getLastValueByFoundEquals_corrupt_noEqual(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'myClass'", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'myClass' id = 'myId'", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number 'one' two", 0, 9)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'number one two'", 0, 9)

  def test_getLastValueByFoundEquals_corrupt_mixedQuotes(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t '2", 0, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t \"2", 1, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2'", 0, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2'", 1, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2\"", 0, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t 2\"", 1, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t '2\"", 0, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t=\t\t \"2'", 0, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a\t=\t\t \"0'", 0, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a = \"0'", 0, 6)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a = \"0''", 0, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a = \"0'''", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("a = \"0' selected", 0, 15)

  def test_getLastValueByFoundEquals_corrupt_noAttributeName(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= ''", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= ''", 0, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = 'myClass'", 0, 11)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t\r\n = 'myClass'", 0, 14)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\t\r\n = 'myClass'", 3, 14)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt(" = '' selected", 0, 10)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= '' selected", 0, 9)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("='' selected", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("=''selected", 0, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= 'a=\"2\"'", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= 'a=\"2\"'", 3, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("= ' back a=\"2\" href'", 9, 17)

  def test_getLastValueByFoundEquals_corrupt_other(self):
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'number one two", 0, 9)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'number one two\"", 0, 9)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("'number one two\"", 1, 4)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("\"number one two\"", 0, 9)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number one two'", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number one two\"", 0, 8)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number 'one two", 0, 14)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("number \"one two", 0, 14)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("b = 'a=\"2\"", 3, 7)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("b = 'a=\"2\"", 1, 3)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("b = ' checked a=\"2\" selected", 14, 25)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("b = ' checked a=\"2\" selected", 24, 25)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("class='myClass' b = ' checked a=\"2\" selected", 16, 42)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("class='myClass' b = ' checked a=\"2\" selected", 24, 42)
    self.helper_getLastValueByFoundEquals_checkIfCorrupt("class='myClass' b = ' checked a=\"2\" selected", 36, 43)

# TODO review tests below
  def test_getLastValueByFoundEquals_valueNotFound(self):
    self.helper_getLastValueByFoundEquals_checkIfNotFound(" ", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\t", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\r", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\n", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\r\n", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("Q", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("ab", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("abc", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("abc", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("abc", 0, 2)
    self.helper_getLastValueByFoundEquals_checkIfNotFound(" a ", 0, 2)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("a\t=\t\t \"0'", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\none\ttwo three\r\n", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\none\ttwo three\r\n", 0, 1)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\none\ttwo three\r\n", 0, 6)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("\none\ttwo three\r\n", 0, 15)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("selected number='two'", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("selected number='two'", 0, 4)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("a ='2'", 0, 0)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("b = 'a=\"2\"'", 3, 7)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'checked a=\"2\"' selected'", 21, 42)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'checked a=\"2\"' selected'", 32, 42)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'checked a=\"2\"' selected'", 36, 42)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 36, 38)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 28, 38)
    self.helper_getLastValueByFoundEquals_checkIfNotFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 32, 38)

  def test_getLastValueByFoundEquals_valueFound(self):
    self.helper_getLastValueByFoundEquals_checkIfFound("a\t=\t\t '0'", 0, 2, equalIdxAt=2,
                                                       openingQuoteIdxAt=6, closingQuoteIdxAt=8)
    self.helper_getLastValueByFoundEquals_checkIfFound("a = '' selected", 0, 11, equalIdxAt=2,
                                                       openingQuoteIdxAt=4, closingQuoteIdxAt=5)
    self.helper_getLastValueByFoundEquals_checkIfFound("a = '' selected", 0, 7, equalIdxAt=2,
                                                       openingQuoteIdxAt=4, closingQuoteIdxAt=5)
    self.helper_getLastValueByFoundEquals_checkIfFound("a = '' selected", 0, 14, equalIdxAt=2,
                                                       openingQuoteIdxAt=4, closingQuoteIdxAt=5)
    self.helper_getLastValueByFoundEquals_checkIfFound("a = \"\" selected", 0, 14, equalIdxAt=2,
                                                       openingQuoteIdxAt=4, closingQuoteIdxAt=5)
    self.helper_getLastValueByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 42,
                                                       equalIdxAt=24, openingQuoteIdxAt=29, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 33,
                                                       equalIdxAt=24, openingQuoteIdxAt=29, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 30,
                                                       equalIdxAt=24, openingQuoteIdxAt=29, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 29,
                                                       equalIdxAt=24, openingQuoteIdxAt=29, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n \" myClass \" selected", 0, 29,
                                                       equalIdxAt=24, openingQuoteIdxAt=29, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("title = \"class='myClass'\"", 0, 18,
                                                       equalIdxAt=6, openingQuoteIdxAt=8, closingQuoteIdxAt=24)
    self.helper_getLastValueByFoundEquals_checkIfFound("title = \"=class='myClass'=\"", 0, 19,
                                                       equalIdxAt=6, openingQuoteIdxAt=8, closingQuoteIdxAt=26)
    self.helper_getLastValueByFoundEquals_checkIfFound("title\t=\n\"===class='myClass'===\"", 0, 21,
                                                       equalIdxAt=6, openingQuoteIdxAt=8, closingQuoteIdxAt=30)
    self.helper_getLastValueByFoundEquals_checkIfFound("id='myId'title\t=\n\"===class='myClass'===\"", 0, 30,
                                                       equalIdxAt=15, openingQuoteIdxAt=17, closingQuoteIdxAt=39)
    self.helper_getLastValueByFoundEquals_checkIfFound("id='myId' title\t=\n\"===class='myClass'===\"", 0, 31,
                                                       equalIdxAt=16, openingQuoteIdxAt=18, closingQuoteIdxAt=40)

    self.helper_getLastValueByFoundEquals_checkIfFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel' checked", 8, 38,
                                                       equalIdxAt=18, openingQuoteIdxAt=20, closingQuoteIdxAt=38)

  def helper_getLastHtmlDelimiter_exceptionRaised(self, string, inclusiveStartIdx, exclusiveEndIdx):
    with self.assertRaises(Exception):
      attr.getLastHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)

  def helper_getLastHtmlDelimiter_notFound(self, string, inclusiveStartIdx, exclusiveEndIdx):
    found, idx = attr.getLastHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertFalse(found)
    self.assertEqual(idx, -1)

  def helper_getLastHtmlDelimiter_found(self, string, inclusiveStartIdx, exclusiveEndIdx, foundAt):
    found, idx = attr.getLastHtmlDelimiter(string, inclusiveStartIdx, exclusiveEndIdx)
    self.assertTrue(found)
    self.assertEqual(idx, foundAt)

  def test_getLastHtmlDelimiter_nonSense(self):
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, 345)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, 7)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, None)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, True)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, [])
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 0, "")
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", -1, 2)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", -1, 45)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", 5, 3)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", None, 3)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", True, 3)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", True, False)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", None, None)
    self.helper_getLastHtmlDelimiter_exceptionRaised("string", "", "")
    self.helper_getLastHtmlDelimiter_exceptionRaised(None, 0, 3)
    self.helper_getLastHtmlDelimiter_exceptionRaised([], 0, 3)
    self.helper_getLastHtmlDelimiter_exceptionRaised(None, None, None)
    self.helper_getLastHtmlDelimiter_exceptionRaised(0, 0, 0)

  def test_getLastHtmlDelimiter_emptyString(self):
    self.helper_getLastHtmlDelimiter_exceptionRaised("", 0, 0)
    self.helper_getLastHtmlDelimiter_exceptionRaised("", 0, 1)

  def test_getLastHtmlDelimiter_notFound(self):
    self.helper_getLastHtmlDelimiter_notFound("Q", 0, 0)
    self.helper_getLastHtmlDelimiter_notFound("one-two-three", 0, 12)
    self.helper_getLastHtmlDelimiter_notFound("=Hello=", 1, 5)
    self.helper_getLastHtmlDelimiter_notFound("\n'greeting'\t= \"Hello\" ", 2, 9)
    self.helper_getLastHtmlDelimiter_notFound("\n'greeting'\t= \"Hello\" ", 15, 19)

  def test_getLastHtmlDelimiter_found(self):
    self.helper_getLastHtmlDelimiter_found(" ", 0, 0, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("\t", 0, 0, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("\n", 0, 0, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("'", 0, 0, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("\"", 0, 0, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("=", 0, 0, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("'=='", 0, 0, foundAt = 0)
    self.helper_getLastHtmlDelimiter_found("key = 'value'", 0, 10, foundAt = 6)
    self.helper_getLastHtmlDelimiter_found("key='value'", 0, 10, foundAt = 10)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 0, 16, foundAt = 16)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 0, 3, foundAt = 1)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 1, 15, foundAt = 10)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 1, 2, foundAt = 1)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 6, 16, foundAt = 16)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 11, 16, foundAt = 16)
    self.helper_getLastHtmlDelimiter_found("\n'key'\t\t= \"value\"", 3, 8, foundAt = 8)

  def helper_getValuesSafelyByFoundEquals_exceptionRaised(self, attributeString, inclusiveStartIdx, inclusiveEndIdx):
    with self.assertRaises(Exception):
      attr.getValuesSafelyByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)

  def helper_getValuesSafelyByFoundEquals_corrupt(self, attributeString, inclusiveStartIdx, inclusiveEndIdx):
    corrupt, values = attr.getValuesSafelyByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)
    self.assertTrue(corrupt)
    self.assertEqual(values, [])

  def helper_getValuesSafelyByFoundEquals_notFound(self, attributeString, inclusiveStartIdx, inclusiveEndIdx):
    corrupt, values = attr.getValuesSafelyByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)
    self.assertFalse(corrupt)
    self.assertEqual(values, [])

  def helper_getValuesSafelyByFoundEquals_checkIfFound(self, attributeString, inclusiveStartIdx, inclusiveEndIdx,
                                                       foundValues):
    corrupt, values = attr.getValuesSafelyByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)
    self.assertFalse(corrupt)
    self.assertEqual(values, foundValues)

  def test_getValuesSafelyByFoundEquals_nonSense(self):
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", -1, 2)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", 6, 8)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", 36, 75)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", 5, 2)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", 1, None)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", 1, "")
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", 1, True)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", None, 4)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", "", 4)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", True, 4)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", True, True)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", None, None)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("string", "string", "string")
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised([], 0, 0)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised(True, True, True)
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised(None, None, None)

  def test_getValuesSafelyByFoundEquals_emptyString(self):
    self.helper_getValuesSafelyByFoundEquals_exceptionRaised("", 0, 0)

  def test_getValuesSafelyByFoundEquals_corrupt_onlyEqual(self):
    self.helper_getValuesSafelyByFoundEquals_corrupt("=", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_corrupt("= ", 0, 1)
    self.helper_getValuesSafelyByFoundEquals_corrupt(" = ", 0, 1)
    self.helper_getValuesSafelyByFoundEquals_corrupt(" = ", 0, 2)
    self.helper_getValuesSafelyByFoundEquals_corrupt(" = ", 1, 2)
    self.helper_getValuesSafelyByFoundEquals_corrupt(" = ", 1, 1)
    self.helper_getValuesSafelyByFoundEquals_corrupt(" = ", 1, 2)
    self.helper_getValuesSafelyByFoundEquals_corrupt(" = = ", 1, 4)
    self.helper_getValuesSafelyByFoundEquals_corrupt(" == ", 1, 3)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\r\n=\t\t", 0, 4)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\r\n=\t\t", 0, 3)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\r\n=\t\t", 1, 3)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\r\n=\t\t", 1, 4)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\r\n=\t\t", 2, 4)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\r\n=\t\t", 2, 3)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\r\n = \t \t", 0, 7)

  def test_getValuesSafelyByFoundEquals_corrupt_onlyQuotes(self):
    self.helper_getValuesSafelyByFoundEquals_corrupt("'", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\"", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_corrupt("''", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_corrupt("''", 0, 1)
    self.helper_getValuesSafelyByFoundEquals_corrupt("''", 1, 1)
    self.helper_getValuesSafelyByFoundEquals_corrupt('""', 0, 0)
    self.helper_getValuesSafelyByFoundEquals_corrupt('""', 0, 1)
    self.helper_getValuesSafelyByFoundEquals_corrupt(" ' ", 0, 2)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\n\t'\t\n", 0, 4)
    self.helper_getValuesSafelyByFoundEquals_corrupt("''''", 0, 3)
    self.helper_getValuesSafelyByFoundEquals_corrupt("'\"'\"", 0, 3)

  def test_getValuesSafelyByFoundEquals_corrupt_noQuotes(self):
    self.helper_getValuesSafelyByFoundEquals_corrupt("=2", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_corrupt("=2", 0, 1)
    self.helper_getValuesSafelyByFoundEquals_corrupt("= 2", 0, 2)
    self.helper_getValuesSafelyByFoundEquals_corrupt("=\t\t2", 0, 3)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t 2", 0, 5)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t 2", 1, 4)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t 2", 1, 5)
    self.helper_getValuesSafelyByFoundEquals_corrupt("a = 4", 0, 4)
    self.helper_getValuesSafelyByFoundEquals_corrupt("number = one two", 0, 14)
    self.helper_getValuesSafelyByFoundEquals_corrupt("number = one two", 0, 10)
    self.helper_getValuesSafelyByFoundEquals_corrupt("number = one two", 0, 7)

  def test_getValuesSafelyByFoundEquals_corrupt_noEqual(self):
    self.helper_getValuesSafelyByFoundEquals_corrupt("'myClass'", 0, 8)
    self.helper_getValuesSafelyByFoundEquals_corrupt("'myClass' id = 'myId'", 0, 8)
    self.helper_getValuesSafelyByFoundEquals_corrupt("number 'one' two", 0, 9)
    self.helper_getValuesSafelyByFoundEquals_corrupt("'number one two'", 0, 9)
    self.helper_getValuesSafelyByFoundEquals_corrupt("'number one two", 0, 9)
    self.helper_getValuesSafelyByFoundEquals_corrupt("'number one two\"", 0, 9)
    self.helper_getValuesSafelyByFoundEquals_corrupt("'number one two\"", 1, 4)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\"number one two\"", 0, 9)
    self.helper_getValuesSafelyByFoundEquals_corrupt("number one two'", 0, 8)
    self.helper_getValuesSafelyByFoundEquals_corrupt("number one two\"", 0, 8)
    self.helper_getValuesSafelyByFoundEquals_corrupt("number 'one two", 0, 14)
    self.helper_getValuesSafelyByFoundEquals_corrupt("number ' one two", 0, 14)
    self.helper_getValuesSafelyByFoundEquals_corrupt("number \"one two", 0, 14)

  def test_getValuesSafelyByFoundEquals_corrupt_mixedQuotes(self):
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t '2", 0, 6)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t \"2", 1, 6)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t 2'", 0, 6)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t 2'", 1, 6)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t 2\"", 0, 6)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t 2\"", 1, 6)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t '2\"", 0, 7)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t=\t\t \"2'", 0, 7)
    self.helper_getValuesSafelyByFoundEquals_corrupt("a\t=\t\t \"0'", 0, 7)
    self.helper_getValuesSafelyByFoundEquals_corrupt("a = \"0'", 0, 6)
    self.helper_getValuesSafelyByFoundEquals_corrupt("a = \"0''", 0, 7)
    self.helper_getValuesSafelyByFoundEquals_corrupt("a = \"0'''", 0, 8)
    self.helper_getValuesSafelyByFoundEquals_corrupt("a = \"0' selected", 0, 15)

  def test_getValuesSafelyByFoundEquals_corrupt_noAttributeName(self):
    self.helper_getValuesSafelyByFoundEquals_corrupt("= ''", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_corrupt("= ''", 0, 3)
    self.helper_getValuesSafelyByFoundEquals_corrupt(" = 'myClass'", 0, 11)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t\r\n = 'myClass'", 0, 14)
    self.helper_getValuesSafelyByFoundEquals_corrupt("\t\r\n = 'myClass'", 3, 14)
    self.helper_getValuesSafelyByFoundEquals_corrupt(" = '' selected", 0, 10)
    self.helper_getValuesSafelyByFoundEquals_corrupt("= '' selected", 0, 9)
    self.helper_getValuesSafelyByFoundEquals_corrupt("='' selected", 0, 8)
    self.helper_getValuesSafelyByFoundEquals_corrupt("=''selected", 0, 7)
    self.helper_getValuesSafelyByFoundEquals_corrupt("= 'a=\"2\"'", 0, 8)
    self.helper_getValuesSafelyByFoundEquals_corrupt("= 'a=\"2\"'", 3, 8)
    self.helper_getValuesSafelyByFoundEquals_corrupt("= ' back a=\"2\" href'", 9, 17)

  def test_getValuesSafelyByFoundEquals_corrupt_other(self):
    self.helper_getValuesSafelyByFoundEquals_corrupt("b = 'a=\"2\"", 3, 7)
    self.helper_getValuesSafelyByFoundEquals_corrupt("b = 'a=\"2\"", 1, 3)
    self.helper_getValuesSafelyByFoundEquals_corrupt("b = ' checked a=\"2\" selected", 14, 25)
    self.helper_getValuesSafelyByFoundEquals_corrupt("b = ' checked a=\"2\" selected", 24, 25)
    self.helper_getValuesSafelyByFoundEquals_corrupt("class='myClass' b = ' checked a=\"2\" selected", 16, 42)
    self.helper_getValuesSafelyByFoundEquals_corrupt("class='myClass' b = ' checked a=\"2\" selected", 24, 42)
    self.helper_getValuesSafelyByFoundEquals_corrupt("class='myClass' b = ' checked a=\"2\" selected", 36, 43)

  def test_getValuesSafelyByFoundEquals_valueNotFound(self):
    self.helper_getValuesSafelyByFoundEquals_notFound(" ", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("\t", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("\r", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("\n", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("\r\n", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("Q", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("ab", 0, 1)
    self.helper_getValuesSafelyByFoundEquals_notFound("abc", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("abc", 0, 1)
    self.helper_getValuesSafelyByFoundEquals_notFound("abc", 0, 2)
    self.helper_getValuesSafelyByFoundEquals_notFound(" a ", 0, 2)
    self.helper_getValuesSafelyByFoundEquals_notFound("a\t=\t\t \"0'", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("\none\ttwo three\r\n", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("\none\ttwo three\r\n", 0, 1)
    self.helper_getValuesSafelyByFoundEquals_notFound("\none\ttwo three\r\n", 0, 6)
    self.helper_getValuesSafelyByFoundEquals_notFound("\none\ttwo three\r\n", 0, 15)
    self.helper_getValuesSafelyByFoundEquals_notFound("selected number='two'", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("selected number='two'", 0, 4)
    self.helper_getValuesSafelyByFoundEquals_notFound("a ='2'", 0, 0)
    self.helper_getValuesSafelyByFoundEquals_notFound("b = 'a=\"2\"'", 3, 7)
    self.helper_getValuesSafelyByFoundEquals_notFound("class='myClass' b = 'checked a=\"2\"' selected'", 21, 42)
    self.helper_getValuesSafelyByFoundEquals_notFound("class='myClass' b = 'checked a=\"2\"' selected'", 32, 42)
    self.helper_getValuesSafelyByFoundEquals_notFound("class='myClass' b = 'checked a=\"2\"' selected'", 36, 42)
    self.helper_getValuesSafelyByFoundEquals_notFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 36, 38)
    self.helper_getValuesSafelyByFoundEquals_notFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 28, 38)
    self.helper_getValuesSafelyByFoundEquals_notFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 32, 38)

  # TODO review these tests
  def test_getValuesSafelyByFoundEquals_valueFound(self):
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("a\t=\t\t '0'", 0, 2, foundValues = [(2, 6, 8)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("a = '' selected", 0, 11, foundValues = [(2, 4, 5)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("a = '' selected", 0, 7, foundValues = [(2, 4, 5)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("a = '' selected", 0, 14, foundValues = [(2, 4, 5)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("a = \"\" selected", 0, 14, foundValues = [(2, 4, 5)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 42,
                                                          foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 2, 33,
                                                          foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 4, 26,
                                                          foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 6, 24,
                                                          foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 7, 24,
                                                          foundValues=[(24, 29, 39)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 2, 23,
                                                          foundValues=[(6, 8, 16)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n \" myClass \" selected", 0, 29,
                                                          foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("title = \"class='myClass'\"", 0, 18, foundValues=[(6, 8, 24)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("title = \"=class='myClass'=\"", 0, 19, foundValues=[(6, 8, 26)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("title\t=\n\"===class='myClass'===\"", 0, 21,
                                                          foundValues=[(6, 8, 30)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("id='myId'title\t=\n\"===class='myClass'===\"", 0, 30,
                                                          foundValues=[(2, 3, 8), (15, 17, 39)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("id='myId' title\t=\n\"===class='myClass'===\"", 0, 31,
                                                          foundValues=[(2, 3, 8), (16, 18, 40)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel' checked", 18, 38,
                                                          foundValues=[(18, 20, 38)])
    self.helper_getValuesSafelyByFoundEquals_checkIfFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel' checked", 5, 18,
                                                          foundValues=[(5, 6, 14), (18, 20, 38)])

  def helper_getValuesByFoundEquals_exceptionRaised(self, attributeString, inclusiveStartIdx, inclusiveEndIdx):
    with self.assertRaises(Exception):
      attr.getValuesByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)

  def helper_getValuesByFoundEquals_corrupt(self, attributeString, inclusiveStartIdx, inclusiveEndIdx):
    corrupt, values = attr.getValuesByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)
    self.assertTrue(corrupt)
    self.assertEqual(values, [])

  def helper_getValuesByFoundEquals_notFound(self, attributeString, inclusiveStartIdx, inclusiveEndIdx):
    corrupt, values = attr.getValuesByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)
    self.assertFalse(corrupt)
    self.assertEqual(values, [])

  def helper_getValuesByFoundEquals_checkIfFound(self, attributeString, inclusiveStartIdx, inclusiveEndIdx,
                                                    foundValues):
    corrupt, values = attr.getValuesByFoundEquals(attributeString, inclusiveStartIdx, inclusiveEndIdx)
    self.assertFalse(corrupt)
    self.assertEqual(values, foundValues)

  def test_getValuesByFoundEquals_nonSense(self):
    self.helper_getValuesByFoundEquals_exceptionRaised("string", -1, 2)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", 6, 8)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", 36, 75)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", 5, 2)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", 1, None)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", 1, "")
    self.helper_getValuesByFoundEquals_exceptionRaised("string", 1, True)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", None, 4)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", "", 4)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", True, 4)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", True, True)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", None, None)
    self.helper_getValuesByFoundEquals_exceptionRaised("string", "string", "string")
    self.helper_getValuesByFoundEquals_exceptionRaised([], 0, 0)
    self.helper_getValuesByFoundEquals_exceptionRaised(True, True, True)
    self.helper_getValuesByFoundEquals_exceptionRaised(None, None, None)

  def test_getValuesByFoundEquals_emptyString(self):
    self.helper_getValuesByFoundEquals_exceptionRaised("", 0, 0)

  def test_getValuesByFoundEquals_corrupt_onlyEqual(self):
    self.helper_getValuesByFoundEquals_corrupt("=", 0, 0)
    self.helper_getValuesByFoundEquals_corrupt("= ", 0, 1)
    self.helper_getValuesByFoundEquals_corrupt(" = ", 0, 1)
    self.helper_getValuesByFoundEquals_corrupt(" = ", 0, 2)
    self.helper_getValuesByFoundEquals_corrupt(" = ", 1, 2)
    self.helper_getValuesByFoundEquals_corrupt(" = ", 1, 1)
    self.helper_getValuesByFoundEquals_corrupt(" = ", 1, 2)
    self.helper_getValuesByFoundEquals_corrupt(" = = ", 1, 4)
    self.helper_getValuesByFoundEquals_corrupt(" == ", 1, 3)
    self.helper_getValuesByFoundEquals_corrupt("\r\n=\t\t", 0, 4)
    self.helper_getValuesByFoundEquals_corrupt("\r\n=\t\t", 0, 3)
    self.helper_getValuesByFoundEquals_corrupt("\r\n=\t\t", 1, 3)
    self.helper_getValuesByFoundEquals_corrupt("\r\n=\t\t", 1, 4)
    self.helper_getValuesByFoundEquals_corrupt("\r\n=\t\t", 2, 4)
    self.helper_getValuesByFoundEquals_corrupt("\r\n=\t\t", 2, 3)
    self.helper_getValuesByFoundEquals_corrupt("\r\n = \t \t", 0, 7)

  def test_getValuesByFoundEquals_corrupt_noQuotes(self):
    self.helper_getValuesByFoundEquals_corrupt("=2", 0, 0)
    self.helper_getValuesByFoundEquals_corrupt("=2", 0, 1)
    self.helper_getValuesByFoundEquals_corrupt("= 2", 0, 2)
    self.helper_getValuesByFoundEquals_corrupt("=\t\t2", 0, 3)
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t 2", 0, 5)
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t 2", 1, 4)
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t 2", 1, 5)
    self.helper_getValuesByFoundEquals_corrupt("a = 4", 0, 4)
    self.helper_getValuesByFoundEquals_corrupt("number = one two", 0, 14)
    self.helper_getValuesByFoundEquals_corrupt("number = one two", 0, 10)
    self.helper_getValuesByFoundEquals_corrupt("number = one two", 0, 7)

  def test_getValuesByFoundEquals_corrupt_mixedQuotes(self):
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t '2", 0, 6)
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t \"2", 1, 6)
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t 2'", 0, 6)
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t 2'", 1, 6)
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t 2\"", 0, 6)
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t 2\"", 1, 6)
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t '2\"", 0, 7)
    self.helper_getValuesByFoundEquals_corrupt("\t=\t\t \"2'", 0, 7)
    self.helper_getValuesByFoundEquals_corrupt("a\t=\t\t \"0'", 0, 7)
    self.helper_getValuesByFoundEquals_corrupt("a = \"0'", 0, 6)
    self.helper_getValuesByFoundEquals_corrupt("a = \"0''", 0, 7)
    self.helper_getValuesByFoundEquals_corrupt("a = \"0'''", 0, 8)
    self.helper_getValuesByFoundEquals_corrupt("a = \"0' selected", 0, 15)

  def test_getValuesByFoundEquals_corrupt_noAttributeName(self):
    self.helper_getValuesByFoundEquals_corrupt("= ''", 0, 0)
    self.helper_getValuesByFoundEquals_corrupt("= ''", 0, 3)
    self.helper_getValuesByFoundEquals_corrupt(" = 'myClass'", 0, 11)
    self.helper_getValuesByFoundEquals_corrupt("\t\r\n = 'myClass'", 0, 14)
    self.helper_getValuesByFoundEquals_corrupt("\t\r\n = 'myClass'", 3, 14)
    self.helper_getValuesByFoundEquals_corrupt(" = '' selected", 0, 10)
    self.helper_getValuesByFoundEquals_corrupt("= '' selected", 0, 9)
    self.helper_getValuesByFoundEquals_corrupt("='' selected", 0, 8)
    self.helper_getValuesByFoundEquals_corrupt("=''selected", 0, 7)
    self.helper_getValuesByFoundEquals_corrupt("= 'a=\"2\"'", 0, 8)
    self.helper_getValuesByFoundEquals_corrupt("= 'a=\"2\"'", 3, 8)

  def test_getValuesByFoundEquals_corrupt_other(self):
    self.helper_getValuesByFoundEquals_corrupt("b = 'a=\"2\"", 1, 3)
    self.helper_getValuesByFoundEquals_corrupt("class='myClass' b = ' checked a=\"2\" selected", 16, 42)

  def test_getValuesByFoundEquals_valueNotFound(self):
    self.helper_getValuesByFoundEquals_notFound(" ", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("\t", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("\r", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("\n", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("\r\n", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("Q", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("ab", 0, 1)
    self.helper_getValuesByFoundEquals_notFound("abc", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("abc", 0, 1)
    self.helper_getValuesByFoundEquals_notFound("abc", 0, 2)
    self.helper_getValuesByFoundEquals_notFound(" a ", 0, 2)
    self.helper_getValuesByFoundEquals_notFound("a\t=\t\t \"0'", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("\none\ttwo three\r\n", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("\none\ttwo three\r\n", 0, 1)
    self.helper_getValuesByFoundEquals_notFound("\none\ttwo three\r\n", 0, 6)
    self.helper_getValuesByFoundEquals_notFound("\none\ttwo three\r\n", 0, 15)
    self.helper_getValuesByFoundEquals_notFound("selected number='two'", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("selected number='two'", 0, 4)
    self.helper_getValuesByFoundEquals_notFound("a ='2'", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("class='myClass' b = 'checked a=\"2\"' selected'", 32, 42)
    self.helper_getValuesByFoundEquals_notFound("class='myClass' b = 'checked a=\"2\"' selected'", 36, 42)
    self.helper_getValuesByFoundEquals_notFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 36, 38)
    self.helper_getValuesByFoundEquals_notFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 32, 38)

  def test_getValuesByFoundEquals_cornerCase_onlyQuotes(self):
    self.helper_getValuesByFoundEquals_notFound("'", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("\"", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("''", 0, 0)
    self.helper_getValuesByFoundEquals_notFound("''", 0, 1)
    self.helper_getValuesByFoundEquals_notFound("''", 1, 1)
    self.helper_getValuesByFoundEquals_notFound('""', 0, 0)
    self.helper_getValuesByFoundEquals_notFound('""', 0, 1)
    self.helper_getValuesByFoundEquals_notFound(" ' ", 0, 2)
    self.helper_getValuesByFoundEquals_notFound("\n\t'\t\n", 0, 4)
    self.helper_getValuesByFoundEquals_notFound("''''", 0, 3)
    self.helper_getValuesByFoundEquals_notFound("'\"'\"", 0, 3)

  def test_getValuesByFoundEquals_notFound_cornerCase_noEqual(self):
    self.helper_getValuesByFoundEquals_notFound("'myClass'", 0, 8)
    self.helper_getValuesByFoundEquals_notFound("'myClass' id = 'myId'", 0, 8)
    self.helper_getValuesByFoundEquals_notFound("number 'one' two", 0, 9)
    self.helper_getValuesByFoundEquals_notFound("'number one two'", 0, 9)
    self.helper_getValuesByFoundEquals_notFound("'number one two", 0, 9)
    self.helper_getValuesByFoundEquals_notFound("'number one two\"", 0, 9)
    self.helper_getValuesByFoundEquals_notFound("'number one two\"", 1, 4)
    self.helper_getValuesByFoundEquals_notFound("\"number one two\"", 0, 9)
    self.helper_getValuesByFoundEquals_notFound("number one two'", 0, 8)
    self.helper_getValuesByFoundEquals_notFound("number one two\"", 0, 8)
    self.helper_getValuesByFoundEquals_notFound("number 'one two", 0, 14)
    self.helper_getValuesByFoundEquals_notFound("number ' one two", 0, 14)
    self.helper_getValuesByFoundEquals_notFound("number \"one two", 0, 14)

  def test_getValuesByFoundEquals_cornerCases(self):
    self.helper_getValuesByFoundEquals_notFound("b = ' checked a=\"2\" selected", 24, 25)
    self.helper_getValuesByFoundEquals_checkIfFound("= ' back a=\"2\" href'", 9, 17, foundValues = [(10, 11, 13)])
    self.helper_getValuesByFoundEquals_checkIfFound("b = 'a=\"2\"", 3, 7, foundValues = [(6, 7, 9)])
    self.helper_getValuesByFoundEquals_checkIfFound("b = ' checked a=\"2\" selected", 14, 25,
                                                    foundValues = [(15, 16, 18)])
    self.helper_getValuesByFoundEquals_corrupt("b = 'a=\"2\"'", 3, 7)
    self.helper_getValuesByFoundEquals_checkIfFound("class='myClass' b = ' checked a=\"2\" selected", 24, 42,
                                                    foundValues=[(31, 32, 34)])
    self.helper_getValuesByFoundEquals_notFound("class='myClass' b = ' checked a=\"2\" selected", 36, 43)
    self.helper_getValuesByFoundEquals_corrupt("class='myClass' b = 'checked a=\"2\"' selected'", 21, 42)
    self.helper_getValuesByFoundEquals_checkIfFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel'", 28, 38,
                                                    foundValues=[(30, 31, 33)])

  # TODO review these tests
  def test_getValuesByFoundEquals_valueFound(self):
    self.helper_getValuesByFoundEquals_checkIfFound("a\t=\t\t '0'", 0, 2, foundValues = [(2, 6, 8)])
    self.helper_getValuesByFoundEquals_checkIfFound("a = '' selected", 0, 11, foundValues = [(2, 4, 5)])
    self.helper_getValuesByFoundEquals_checkIfFound("a = '' selected", 0, 7, foundValues = [(2, 4, 5)])
    self.helper_getValuesByFoundEquals_checkIfFound("a = '' selected", 0, 14, foundValues = [(2, 4, 5)])
    self.helper_getValuesByFoundEquals_checkIfFound("a = \"\" selected", 0, 14, foundValues = [(2, 4, 5)])
    self.helper_getValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 0, 42,
                                                       foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 2, 33,
                                                       foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 4, 26,
                                                       foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 6, 24,
                                                       foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 7, 24,
                                                       foundValues=[(24, 29, 39)])
    self.helper_getValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n ' myClass ' selected", 2, 23,
                                                       foundValues=[(6, 8, 16)])
    self.helper_getValuesByFoundEquals_checkIfFound("\nhref = 'img.png' class =\t\r\n \" myClass \" selected", 0, 29,
                                                       foundValues=[(6, 8, 16), (24, 29, 39)])
    self.helper_getValuesByFoundEquals_checkIfFound("title = \"class='myClass'\"", 0, 18, foundValues=[(6, 8, 24)])
    self.helper_getValuesByFoundEquals_checkIfFound("title = \"=class='myClass'=\"", 0, 19, foundValues=[(6, 8, 26)])
    self.helper_getValuesByFoundEquals_checkIfFound("title\t=\n\"===class='myClass'===\"", 0, 21,
                                                       foundValues=[(6, 8, 30)])
    self.helper_getValuesByFoundEquals_checkIfFound("id='myId'title\t=\n\"===class='myClass'===\"", 0, 30,
                                                       foundValues=[(2, 3, 8), (15, 17, 39)])
    self.helper_getValuesByFoundEquals_checkIfFound("id='myId' title\t=\n\"===class='myClass'===\"", 0, 31,
                                                       foundValues=[(2, 3, 8), (16, 18, 40)])
    self.helper_getValuesByFoundEquals_checkIfFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel' checked", 18, 38,
                                                       foundValues=[(18, 20, 38)])
    self.helper_getValuesByFoundEquals_checkIfFound("class='myClass' b = 'c a=\"2\" b=\"3\" sel' checked", 5, 18,
                                                       foundValues=[(5, 6, 14), (18, 20, 38)])

  def test_charIsQuote_exception(self):
    with self.assertRaises(Exception):
      attr.charIsQuote(2)
    with self.assertRaises(Exception):
      attr.charIsQuote([])
    with self.assertRaises(Exception):
      attr.charIsQuote(None)
    with self.assertRaises(Exception):
      attr.charIsQuote(False)
    with self.assertRaises(Exception):
      attr.charIsQuote("string")
    with self.assertRaises(Exception):
      attr.charIsQuote("ab")

  def test_charIsQuote_isQuote(self):
    self.assertTrue(attr.charIsQuote("'"))
    self.assertTrue(attr.charIsQuote("\""))

  def test_charIsQuote_isNotQuote(self):
    self.assertFalse(attr.charIsQuote("="))
    self.assertFalse(attr.charIsQuote(" "))
    self.assertFalse(attr.charIsQuote("\t"))
    self.assertFalse(attr.charIsQuote("\r"))
    self.assertFalse(attr.charIsQuote("\n"))
    self.assertFalse(attr.charIsQuote(" "))
    self.assertFalse(attr.charIsQuote("A"))
    self.assertFalse(attr.charIsQuote("0"))
    self.assertFalse(attr.charIsQuote("c"))
    self.assertFalse(attr.charIsQuote("#"))
    self.assertFalse(attr.charIsQuote("!"))
    self.assertFalse(attr.charIsQuote(","))
    self.assertFalse(attr.charIsQuote("<"))
    self.assertFalse(attr.charIsQuote("?"))
    self.assertFalse(attr.charIsQuote(">"))
    self.assertFalse(attr.charIsQuote("["))
    self.assertFalse(attr.charIsQuote("]"))
    self.assertFalse(attr.charIsQuote("\\"))
    self.assertFalse(attr.charIsQuote("/"))

  def helper_getPossibleValuesByFoundEquals_checkException(self, string, startIdx, endIdx):
    with self.assertRaises(Exception):
      attr.getPossibleValuesByFoundEquals(string, startIdx, endIdx)

  def helper_getPossibleValuesByFoundEquals_checkIfNotFound(self, string, startIdx, endIdx):
    possibleValues = attr.getPossibleValuesByFoundEquals(string, startIdx, endIdx)
    self.assertEqual(possibleValues, [])

  def test_getPossibleValuesByFoundEquals_exception(self):
    self.helper_getPossibleValuesByFoundEquals_checkException("string", 0, 234)
    self.helper_getPossibleValuesByFoundEquals_checkException("string", 0, 6)
    self.helper_getPossibleValuesByFoundEquals_checkException("string", -1, 3)
    self.helper_getPossibleValuesByFoundEquals_checkException("string", 5, 2)
    self.helper_getPossibleValuesByFoundEquals_checkException("string", 0, None)
    self.helper_getPossibleValuesByFoundEquals_checkException("string", None, None)
    self.helper_getPossibleValuesByFoundEquals_checkException("string", False, 0)
    self.helper_getPossibleValuesByFoundEquals_checkException("string", None, 0)
    self.helper_getPossibleValuesByFoundEquals_checkException("string", True, True)
    self.helper_getPossibleValuesByFoundEquals_checkException("string", "0", "0")
    self.helper_getPossibleValuesByFoundEquals_checkException([], 0, 0)
    self.helper_getPossibleValuesByFoundEquals_checkException([1], 0, 0)
    self.helper_getPossibleValuesByFoundEquals_checkException(0, 0, 0)
    self.helper_getPossibleValuesByFoundEquals_checkException(None, None, None)
    self.helper_getPossibleValuesByFoundEquals_checkException(True, False, False)
    self.helper_getPossibleValuesByFoundEquals_checkException(0, True, True)

  def test_getPossibleValuesByFoundEquals_emptyString(self):
    self.helper_getPossibleValuesByFoundEquals_checkException("", 0, 0)

  def test_getPossibleValuesByFoundEquals_notFound(self):
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound(" ", 0, 0)
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound("'", 0, 0)
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound("\"", 0, 0)
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound("\t", 0, 0)
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound("\r", 0, 0)
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound("\n", 0, 0)
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound("Q", 0, 0)
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound("(-> {this} <- [is] *my* _#1_ 'string')", 0, 37)
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound("'value'", 0, 6)
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound("key 'value'", 0, 10)
    self.helper_getPossibleValuesByFoundEquals_checkIfNotFound("key = 'value'", 5, 12)

  def test_getPossibleValuesByFoundEquals_found(self):
    possibleValues = attr.getPossibleValuesByFoundEquals("=", 0, 0)
    self.assertEqual(possibleValues, [(0, True, -1, -1)])
    possibleValues = attr.getPossibleValuesByFoundEquals(" = ", 0, 2)
    self.assertEqual(possibleValues, [(1, True, -1, -1)])
    possibleValues = attr.getPossibleValuesByFoundEquals("===", 1, 1)
    self.assertEqual(possibleValues, [(1, True, -1, -1)])
    possibleValues = attr.getPossibleValuesByFoundEquals("===", 1, 2)
    self.assertEqual(possibleValues, [(1, True, -1, -1), (2, True, -1, -1)])
    possibleValues = attr.getPossibleValuesByFoundEquals("key = 'value'", 0, 12)
    self.assertEqual(possibleValues, [(4, False, 6, 12)])
    possibleValues = attr.getPossibleValuesByFoundEquals("key = 'value'", 4, 4)
    self.assertEqual(possibleValues, [(4, False, 6, 12)])
    possibleValues = attr.getPossibleValuesByFoundEquals("key = \"title='hello'\"", 1, 20)
    self.assertEqual(possibleValues, [(4, False, 6, 20), (12, True, -1, -1)])
    possibleValues = attr.getPossibleValuesByFoundEquals("key = \"title='hello' selected\"", 1, 20)
    self.assertEqual(possibleValues, [(4, False, 6, 29), (12, False, 13, 19)])
    possibleValues = attr.getPossibleValuesByFoundEquals("key = \"=title='hello' selected=\"", 1, 31)
    self.assertEqual(possibleValues, [(4, False, 6, 31), (7, True, -1, -1), (13, False, 14, 20), (30, True, -1, -1)])

  def helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(self, string, idx):
    corrupt, found, firstCharIdx = attr.jumpSafelyToFirstIdxOfCurrentOrNextName(string, idx)
    self.assertTrue(corrupt)
    self.assertFalse(found)
    self.assertEqual(firstCharIdx, -1)

  def helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound(self, string, idx):
    corrupt, found, firstCharIdx = attr.jumpSafelyToFirstIdxOfCurrentOrNextName(string, idx)
    self.assertFalse(corrupt)
    self.assertFalse(found)
    self.assertEqual(firstCharIdx, -1)

  def helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound(self, string, idx, foundAt):
    corrupt, found, firstCharIdx = attr.jumpSafelyToFirstIdxOfCurrentOrNextName(string, idx)
    self.assertFalse(corrupt)
    self.assertTrue(found)
    self.assertEqual(firstCharIdx, foundAt)

  def test_jumpSafelyToFirstIdxOfCurrentOrNextName_nonSense(self):
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName("string", -1)
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName("string", 345)
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName("string", 6)
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName("string", True)
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName("string", [])
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName("string", "")
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName("string", "string")
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName(0, 0)
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName([], 0)
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName(["1", "2"], 0)
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName(None, None)

  def test_jumpSafelyToFirstIdxOfCurrentOrNextName_emptyString(self):
    with self.assertRaises(Exception):
      attr.jumpSafelyToFirstIdxOfCurrentOrNextName("", 0)

  def test_jumpSafelyToFirstIdxOfCurrentOrNextName_spaces(self):
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound(" ", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound("   ", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound("   ", 1)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound("     ", 2)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound("\n", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound(" \t\t\n", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound(" \t\t\n", 1)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound(" \t\t\n", 2)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound(" \t\r\n", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound(" \t\t \n ", 3)

  def test_jumpSafelyToFirstIdxOfCurrentOrNextName_corrupt(self):
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("=", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("= ", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" =", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ", 1)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ", 2)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = = ", 1)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = = ", 2)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = = ", 3)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("\t\t=\n\n", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("'", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("''''''''", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("' ", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" '", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" ' ", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("\t\t'\n\n", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("\"", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("\" ", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" \"", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" \" ", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("\t\t\"\n\n", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("='value'", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 1)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 2)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 3)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 4)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 11)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 12)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("=value'", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("=value'", 1)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("=value'", 2)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("=value'", 6)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("class'myClass'", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("class'myClass'", 5)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("class'myClass'", 6)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("one ' two", 0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfCorrupt("one ' two", 4)

  def test_jumpSafelyToFirstIdxOfCurrentOrNextName_notFound(self):
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound("class ", 5)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound("class \r\n", 5)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound("class \r\n", 6)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' ", 21)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' \t\t", 21)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' \t\t", 22)

  def test_jumpSafelyToFirstIdxOfCurrentOrNextName_indexPointsAtTheFirstNameCharIdx(self):
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("X", 0, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("X=''", 0, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("\t\tX\t\t", 0, foundAt=2)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("\t\tX\t\tY Z", 0, foundAt=2)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("selected", 0, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("\t\tselected\n\n", 0, foundAt=2)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound(" class='my-Class' \t selected", 0, foundAt=1)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("\n\nclass\t\t=\t\n'   my-Class' \r\n\t selected",
                                                                     0, foundAt=2)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("multiple words in this string", 0, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("title=\"class='myClass'==\"", 0, foundAt=0)

  def test_jumpSafelyToFirstIdxOfCurrentOrNextName_indexPointsWithinName(self):
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("selected", 3, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("multiple words in this string", 3, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("multiple words in this string", 13, foundAt=9)

  def test_jumpSafelyToFirstIdxOfCurrentOrNextName_indexPointsAroundValue(self):
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class='myClass'", 5, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class='myClass'", 6, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class='myClass'", 7, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class='myClass'", 9, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class='myClass'", 14, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 5, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 6, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 7, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\t=\n'myClass'", 8, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 5, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 6, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 7, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 8, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 9, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 10, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("class\n\t =\n\r\n'myClass'", 11, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("a=''", 1, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("a = ''", 1, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("a = ''", 2, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("a = ''", 3, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("title=\"class='myClass'\"", 12, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("title=\"'class'='myClass'\"", 14, foundAt=0)
    self.helper_jumpSafelyToFirstIdxOfCurrentOrNextName_checkIfFound("title=\"'class' = 'myClass'\"", 15, foundAt=0)

  def helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(self, string, idx):
    corrupt, found, firstCharIdx = attr.jumpToFirstIdxOfCurrentOrNextName(string, idx)
    self.assertTrue(corrupt)
    self.assertFalse(found)
    self.assertEqual(firstCharIdx, -1)

  def helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound(self, string, idx):
    corrupt, found, firstCharIdx = attr.jumpToFirstIdxOfCurrentOrNextName(string, idx)
    self.assertFalse(corrupt)
    self.assertFalse(found)
    self.assertEqual(firstCharIdx, -1)

  def helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound(self, string, idx, foundAt):
    corrupt, found, firstCharIdx = attr.jumpToFirstIdxOfCurrentOrNextName(string, idx)
    self.assertFalse(corrupt)
    self.assertTrue(found)
    self.assertEqual(firstCharIdx, foundAt)

  def test_jumpToFirstIdxOfCurrentOrNextName_nonSense(self):
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName("string", -1)
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName("string", 345)
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName("string", 6)
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName("string", True)
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName("string", [])
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName("string", "")
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName("string", "string")
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName(0, 0)
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName([], 0)
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName(["1", "2"], 0)
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName(None, None)

  def test_jumpToFirstIdxOfCurrentOrNextName_emptyString(self):
    with self.assertRaises(Exception):
      attr.jumpToFirstIdxOfCurrentOrNextName("", 0)

  def test_jumpToFirstIdxOfCurrentOrNextName_spaces(self):
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound(" ", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound("   ", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound("   ", 1)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound("     ", 2)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound("\n", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound(" \t\t\n", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound(" \t\t\n", 1)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound(" \t\t\n", 2)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound(" \t\r\n", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound(" \t\t \n ", 3)

  def test_jumpToFirstIdxOfCurrentOrNextName_corrupt(self):
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("=", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("= ", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" =", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ", 1)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = = ", 1)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = = ", 2)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = = ", 3)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("\t\t=\n\n", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("'", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("''''''''", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("' ", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" '", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" ' ", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("\t\t'\n\n", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("\"", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("\" ", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" \"", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" \" ", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("\t\t\"\n\n", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("='value'", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 1)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 2)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 3)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt(" = ' value ' ", 11)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("=value'", 0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("=value'", 6)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("class'myClass'", 5)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfCorrupt("one ' two", 4)

  def test_jumpToFirstIdxOfCurrentOrNextName_notCorruptBecauseOfIndexPosition(self):
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound(" = ", 2)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound(" = ' value ' ", 12)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound(" = ' value ' ", 4, foundAt=5)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("=value'", 1, foundAt=1)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("=value'", 2, foundAt=1)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("class'myClass'", 0, foundAt=0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("class'myClass'", 6, foundAt=6)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("one ' two", 0, foundAt=0)

  def test_jumpToFirstIdxOfCurrentOrNextName_notFound(self):
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound("class ", 5)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound("class \r\n", 5)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound("class \r\n", 6)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' ", 21)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' \t\t", 21)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfNotFound("class  =  ' myClass ' \t\t", 22)

  def test_jumpToFirstIdxOfCurrentOrNextName_indexPointsAtTheFirstNameCharIdx(self):
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("X", 0, foundAt=0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("X=''", 0, foundAt=0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("\t\tX\t\t", 0, foundAt=2)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("\t\tX\t\tY Z", 0, foundAt=2)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("selected", 0, foundAt=0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("\t\tselected\n\n", 0, foundAt=2)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound(" class='my-Class' \t selected", 0, foundAt=1)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("\n\nclass\t\t=\t\n'   my-Class' \r\n\t selected", 0,
                                                               foundAt=2)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("multiple words in this string", 0, foundAt=0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("title=\"class='myClass'==\"", 0, foundAt=0)

  def test_jumpToFirstIdxOfCurrentOrNextName_indexPointsWithinName(self):
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("selected", 3, foundAt=0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("multiple words in this string", 3, foundAt=0)
    self.helper_jumpToFirstIdxOfCurrentOrNextName_checkIfFound("multiple words in this string", 13, foundAt=9)

  def helper_getValueByName_checkIfException(self, string, name):
    with self.assertRaises(Exception):
      attr.getValueByName(string, name)

  def helper_getValueByName_checkIfCorrupt(self, string, name):
    corrupt, nameFound, valueFound, value = attr.getValueByName(string, name)
    self.assertTrue(corrupt)
    self.assertFalse(nameFound)
    self.assertFalse(valueFound)
    self.assertEqual(value, "")

  def helper_getValueByName_checkIfNameNotFound(self, string, name):
    corrupt, nameFound, valueFound, value = attr.getValueByName(string, name)
    self.assertFalse(corrupt)
    self.assertFalse(nameFound)
    self.assertFalse(valueFound)
    self.assertEqual(value, "")

  def helper_getValueByName_checkIfValueNotFound(self, string, name):
    corrupt, nameFound, valueFound, value = attr.getValueByName(string, name)
    self.assertFalse(corrupt)
    self.assertTrue(nameFound)
    self.assertFalse(valueFound)
    self.assertEqual(value, "")

  def helper_getValueByName_checkIfValueFound(self, string, name, foundValue):
    corrupt, nameFound, valueFound, value = attr.getValueByName(string, name)
    self.assertFalse(corrupt)
    self.assertTrue(nameFound)
    self.assertTrue(valueFound)
    self.assertEqual(value, foundValue)

  def test_getValueByName_nonSense(self):
    self.helper_getValueByName_checkIfException("option='audi' value='A'", 123)
    self.helper_getValueByName_checkIfException("option='audi' value='A'", False)
    self.helper_getValueByName_checkIfException("option='audi' value='A'", None)
    self.helper_getValueByName_checkIfException("option='audi' value='A'", ["option"])
    self.helper_getValueByName_checkIfException(None, "option")
    self.helper_getValueByName_checkIfException(234, "src")
    self.helper_getValueByName_checkIfException(123, None)
    self.helper_getValueByName_checkIfException(None, None)
    self.helper_getValueByName_checkIfException(0, 0)

  def test_getValueByName_emptyName(self):
    self.helper_getValueByName_checkIfException("option='audi' value='A'", "")

  def test_getValueByName_emptyAttributesString(self):
    self.helper_getValueByName_checkIfNameNotFound("", "title")
    self.helper_getValueByName_checkIfNameNotFound("", "src")

  def test_getValueByName_attributeNameNotFound(self):
    self.helper_getValueByName_checkIfNameNotFound("htmlAttribute no-href", "href")
    self.helper_getValueByName_checkIfNameNotFound("rel=\"shortcut icon\" href=\"img/favicon.ico\" "
                                                   "type=\"image/x-icon\"", "title")
    self.helper_getValueByName_checkIfNameNotFound("class=\"masthead_custom_styles\" is=\"custom-style\" "
                                                   "id=\"ext-styles\" nonce=\"tG2l8WDVY7XYzWdAOVtRzA\"", "style")
    self.helper_getValueByName_checkIfNameNotFound("src=\"jsbin/spf.vflset/spf.js\"", "alt")
    self.helper_getValueByName_checkIfNameNotFound("class=\"anim\"", "id")
    self.helper_getValueByName_checkIfNameNotFound("class=\"animated bold\"", "id")
    self.helper_getValueByName_checkIfNameNotFound("class=\"animated bold\" selected class=\"act-tab\"", "id")
    string = "id=\"masthead\" logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\" class=\"shell dark chunked\" " \
             "disable-upgrade=\"true\""
    self.helper_getValueByName_checkIfNameNotFound(string, "upgrade")
    self.helper_getValueByName_checkIfNameNotFound(string, "masthead")
    self.helper_getValueByName_checkIfNameNotFound(string, "dark")
    self.helper_getValueByName_checkIfNameNotFound(string, "shell")
    self.helper_getValueByName_checkIfNameNotFound(string, "chunked")
    self.helper_getValueByName_checkIfNameNotFound(string, "e")
    self.helper_getValueByName_checkIfNameNotFound(string, "disable")
    self.helper_getValueByName_checkIfNameNotFound(string, "clas")
    self.helper_getValueByName_checkIfNameNotFound(string, "lot")
    self.helper_getValueByName_checkIfNameNotFound("_value=\"audi\"", "value")

  def test_getValueByName_attrDoesNotHaveValue(self):
    self.helper_getValueByName_checkIfValueNotFound("selected value=\"audi\" selected='True'", "selected")
    self.helper_getValueByName_checkIfValueNotFound("value=\"audi\" selected", "selected")
    self.helper_getValueByName_checkIfValueNotFound("value=\"audi\" selected class=\"myClass\"", "selected")
    self.helper_getValueByName_checkIfValueNotFound("selected value=\"audi\"", "selected")
    self.helper_getValueByName_checkIfValueNotFound("selected", "selected")

  def test_getValueByName_emptyValue(self):
    self.helper_getValueByName_checkIfValueFound("value=\"\"", "value", foundValue="")
    self.helper_getValueByName_checkIfValueFound("value=\"  \"", "value", foundValue="  ")
    self.helper_getValueByName_checkIfValueFound("value=\"\t\"", "value", foundValue="\t")
    self.helper_getValueByName_checkIfValueFound("value=\" \r\n \t \"", "value", foundValue=" \r\n \t ")

  def test_getValueByName_corrupt_nameContainsHtmlDelimiter(self):
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", "selected class")
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", "class=")
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", " class")
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", "selected ")
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", "red '")
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", "'custom")
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", "=")
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", "'")
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", "\"")
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", " ")
    self.helper_getValueByName_checkIfCorrupt("selected class='custom style red'", "\t")

  def test_getValueByName_corrupt(self):
    self.helper_getValueByName_checkIfCorrupt("class='custom style red", "style")
    self.helper_getValueByName_checkIfCorrupt("value=\"", "value")
    self.helper_getValueByName_checkIfCorrupt("value=\"   ", "value")
    self.helper_getValueByName_checkIfCorrupt("value=", "value")
    self.helper_getValueByName_checkIfCorrupt("value= ", "value")
    self.helper_getValueByName_checkIfCorrupt("value= \n \t ", "value")
    self.helper_getValueByName_checkIfCorrupt("value=\"audi", "value")
    self.helper_getValueByName_checkIfCorrupt("value=\"audi'", "value")
    self.helper_getValueByName_checkIfCorrupt("value='audi\"", "value")
    self.helper_getValueByName_checkIfCorrupt("value \"audi\"", "value")
    self.helper_getValueByName_checkIfCorrupt("value\"audi\"", "value")
    self.helper_getValueByName_checkIfCorrupt("value 'audi'", "value")
    self.helper_getValueByName_checkIfCorrupt("value'audi'", "value")
    self.helper_getValueByName_checkIfCorrupt("\"class'myclass' class='myclass'", "class")

  def test_getValueByName_quotes(self):
    self.helper_getValueByName_checkIfValueFound("value=\"audi\"", "value", foundValue="audi")
    self.helper_getValueByName_checkIfValueFound("value='audi'", "value", foundValue="audi")
    self.helper_getValueByName_checkIfValueFound("value=\"audi'A3\"", "value", foundValue="audi'A3")
    self.helper_getValueByName_checkIfValueFound("value=\"audi'A3'\"", "value", foundValue="audi'A3'")
    self.helper_getValueByName_checkIfValueFound("value='audi\"A3'", "value", foundValue="audi\"A3")
    self.helper_getValueByName_checkIfValueFound("value='\"audi\"A3\"'", "value", foundValue="\"audi\"A3\"")
    self.helper_getValueByName_checkIfValueFound("class='myClass'title='titled title=\"title\"'", "title",
                                                  foundValue="titled title=\"title\"")

  def test_getValueByName_oneValueFound(self):
    self.helper_getValueByName_checkIfValueFound("rel=\"shortcut icon\" href=\"img/favicon.ico\" "
                                                  "type=\"image/x-icon\"", "href", foundValue="img/favicon.ico")
    self.helper_getValueByName_checkIfValueFound("rel=\"shortcut icon\" href=\"img/favicon.ico\" id='X' "
                                                  "type=\"image/x-icon\"", "id", foundValue="X")
    self.helper_getValueByName_checkIfValueFound("rel=\"shortcut icon\" xhref=\"a34cd3b\" href=\"img/favicon.ico\" "
                                                 "type=\"image/x-icon\"", "href", foundValue="img/favicon.ico")
    self.helper_getValueByName_checkIfValueFound("rel=\"shortcut icon\" no-href=\"false\" xhref=\"a34cd3b\" "
                                                  "href=\"img/favicon.ico\" type=\"image/x-icon\"", "href",
                                                  foundValue="img/favicon.ico")
    self.helper_getValueByName_checkIfValueFound("rel=\"shortcut icon\" hrefhref=\"image\" no-href=\"false\" "
                                            "xhref=\"a34cd3b\" href=\"img/favicon.ico\" type=\"image/x-icon\"", "href",
                                              foundValue="img/favicon.ico")
    self.helper_getValueByName_checkIfValueFound("nonce=\"lix9PsSUHJxW7ghXrU5s0A\"", "nonce",
                                                 foundValue="lix9PsSUHJxW7ghXrU5s0A")
    self.helper_getValueByName_checkIfValueFound("id=\"masthead\" logo-type=\"YOUTUBE_LOGO\" slot=\"masthead\""
                                            " class=\"shell dark chunked\" disable-upgrade=\"true\"", "disable-upgrade",
                                                  foundValue="true")
    self.helper_getValueByName_checkIfValueFound("rel=\"preload\" href="
                                "\"https://r3---sn-8vq54voxgv-vu26.googlevideo.com/generate_204\" as=\"fetch\"", "rel",
                                                  foundValue="preload")

  def test_getValueByName_whitespaces(self):
    self.helper_getValueByName_checkIfValueFound("rel =\"preload\" href=\"generate_204\" as=\"fetch\"", "rel",
                                                  foundValue="preload")
    self.helper_getValueByName_checkIfValueFound("rel = \"preload\" href=\"generate_204\" as=\"fetch\"", "rel",
                                                  foundValue="preload")
    self.helper_getValueByName_checkIfValueFound("rel= \"preload\" href=\"generate_204\" as=\"fetch\"", "rel",
                                                  foundValue="preload")
    self.helper_getValueByName_checkIfValueFound("rel \n\r\t\t\t = \n\r\t\t\t \"preload\" href=\"generate_204\" "
                                                 "as=\"fetch\"", "rel", foundValue="preload")
    self.helper_getValueByName_checkIfValueFound("\n\trel \n\r\t\t\t = \n\r\t\t\t \"preload\" href=\"generate_204\" "
                                                 "as=\"fetch\"", "rel", foundValue="preload")
    self.helper_getValueByName_checkIfValueFound("\n\trel \n\r\t\t\t = \n\r\t\t\t \"\r\n\t\t preload \t\t\t\n\t  \" "
                                                 "href=\"generate_204\" as=\"fetch\"", "rel",
                                                  foundValue="\r\n\t\t preload \t\t\t\n\t  ")

  def test_getValueByName_multipleValuesFound(self):
    self.helper_getValueByName_checkIfValueFound("action=\".\" method=\"get\" class=\"add_search_params pure-form\" "
                                                 "style=\"display:inline-block\"", "class",
                                                  foundValue="add_search_params pure-form")
    self.helper_getValueByName_checkIfValueFound("action=\".\" method=\"get\" class=\"add_search_params pure-form "
                                                 "hide-xs hide-sm hide-md\" style=\"display:inline-block\"", "class",
                                                  foundValue="add_search_params pure-form hide-xs hide-sm hide-md")
    self.helper_getValueByName_checkIfValueFound("action=\".\" method=\"get\" class\n=\n\"add_search_params\t"
                                        "pure-form\r\nhide-xs     hide-sm\t\t\t\n\r   \n\r    hide-md\n\" "
                                        "style=\"display:inline-block\"", "class",
                        foundValue="add_search_params\tpure-form\r\nhide-xs     hide-sm\t\t\t\n\r   \n\r    hide-md\n")

  def test_getValueByName_multipleDeclarations(self):
    self.helper_getValueByName_checkIfValueFound("action=\".\" method=\"get\" class=\"add_search_params cl2 cl3\" "
                                                 "class=\"pure-form\" style=\"display:inline-block\"", "class",
                                                  foundValue="add_search_params cl2 cl3")
    self.helper_getValueByName_checkIfValueFound("action=\".\" method=\"get\" class=\"add_search_params\" "
                                                  "class=\"pure-form cl2 cl3\" style=\"display:inline-block\"", "class",
                                                  foundValue="add_search_params")
    self.helper_getValueByName_checkIfValueNotFound("action=\".\" class method=\"get\" class=\"pure-form cl2 cl3\" "
                                                    "style=\"display:inline-block\"", "class")

  def test_getValueByName_valueRepeats(self):
    self.helper_getValueByName_checkIfValueFound("action=\".\" method=\"get\" class=\"cl1 cl1\" "
                                                  "style=\"display:inline-block\"", "class",
                                                  foundValue="cl1 cl1")
    self.helper_getValueByName_checkIfValueFound("action=\".\" method=\"get\" class=\"cl1 cl1 cl2 cl1 cl3 cl2\" "
                                                  "style=\"display:inline-block\"", "class",
                                                  foundValue="cl1 cl1 cl2 cl1 cl3 cl2")
