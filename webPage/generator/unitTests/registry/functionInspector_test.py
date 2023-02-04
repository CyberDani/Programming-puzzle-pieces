import sys

sys.path.append('../..')

from modules.unitTests.autoUnitTest import AutoUnitTest
from modules.registry.functionInspector import FunctionInspector
from unitTests4unitTests import similarFunctions as func

class FunctionInspectorTests(AutoUnitTest):

  def setUp(self):
    self.hash = 2

  def test_ctor_wrongType(self):
    self.assertRaises(Exception, FunctionInspector, print)
    self.assertRaises(Exception, FunctionInspector, None)
    self.assertRaises(Exception, FunctionInspector, [])
    self.assertRaises(Exception, FunctionInspector, {})
    self.assertRaises(Exception, FunctionInspector, 2)
    self.assertRaises(Exception, FunctionInspector, sys.path.copy)
    self.assertRaises(Exception, FunctionInspector, AutoUnitTest)

  def test_getFunctionName_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc")
    inspector = FunctionInspector(func.simpleFunc2)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc2")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc_sameImpl_differentSignature")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc_sameImpl_differentSignature_decorated")
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc")
    inspector = FunctionInspector(func.simpleFunc10)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc10")
    inspector = FunctionInspector(func.simpleFunc11)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc11")
    inspector = FunctionInspector(func.simpleFunc12)
    self.assertEqual(inspector.getFunctionName(), "simpleFunc12")

  def test_getFunctionSignature_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getFunctionSignature(), "()")
    inspector = FunctionInspector(func.simpleFunc2)
    self.assertEqual(inspector.getFunctionSignature(), "()")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature)
    self.assertEqual(inspector.getFunctionSignature(), "(arg1, arg2)")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated)
    self.assertEqual(inspector.getFunctionSignature(), "(arg1, arg2)")
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    self.assertEqual(inspector.getFunctionSignature(), "(self)")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated_annotated)
    self.assertEqual(inspector.getFunctionSignature(), "(arg1: int, arg2: str) -> bool")

  def test_getFullSource_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    self.assertEqual(inspector.getFullSource(), "def simpleFunc():\n  a = 2\n  b = 3\n"
                                                "  return ((a + b) * 10) % 2 == 0\n")
    inspector = FunctionInspector(func.simpleFunc2)
    self.assertEqual(inspector.getFullSource(), "def \\\n    \\\n        simpleFunc2 \\\n                \\\n"
                                                "                (\n\n        )\\\n        \\\n        :\n"
                                                "  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n")
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature)
    self.assertEqual(inspector.getFullSource(), 'def simpleFunc_sameImpl_differentSignature(\n                       '
                                                '                    arg1 ,\n                                        '
                                                '   arg2\n                                          )     :\n'
                                                '  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated)
    self.assertEqual(inspector.getFullSource(), '@invertBool\ndef simpleFunc_sameImpl_differentSignature_decorated(\n'
                                                '                                           arg1 ,\n                 '
                                                '                          arg2\n                                    '
                                                '      )     :\n  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    self.assertEqual(inspector.getFullSource(), '  def simpleFunc( self ) \\\n          :\n'
                                                '    a = 2\n    b = 3\n    return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc_sameImpl_differentSignature_decorated_annotated)
    self.assertEqual(inspector.getFullSource(), '@invertBool\n'
                                                'def simpleFunc_sameImpl_differentSignature_decorated_annotated (\n'
                                                '                                           arg1   :    int,\n'
                                                '                                           arg2   :    str\n'
                                                '                                          )       ->   bool \\\n'
                                                '    :\n  a = 2\n  b = 3\n  return ((a + b) * 10) % 2 == 0\n')
    inspector = FunctionInspector(func.simpleFunc12)
    self.assertEqual(inspector.getFullSource(), '@\\\ndefdef \\\n  (arg = " @defdef(dec) \\\n def simpleFunc12(): ")\n'
                                    'def \\\n        simpleFunc12 \\\n                ( str = "2:1",\n                '
                                    '  d = {"one": 1}\n        )\\\n        :\n  a = len(d)\n  b = len(str)\n'
                                    '  return ((a + b) * 10) % 2 == 0\n')

  def test_getDefIndex_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def simpleFunc():\n"))
    inspector = FunctionInspector(func.simpleFunc2)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n    \\\n        simpleFunc2 "
                                               "\\\n                \\\n                (\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc3)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n    \\\n        simpleFunc3 "
                                               "\\\n                \\\n                (\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc4)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc4 \\\n                "
                                               "(\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc5)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc5 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc6)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc6 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc7)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc7 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc8)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc8 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc9)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc9 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc10)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc10 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc11)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def \\\n        simpleFunc11 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    source = inspector.getFullSource()
    defIdx = inspector.getDefIndex()
    self.assertTrue(source[defIdx:].startswith("def simpleFunc( self ) \\\n"))

  def test_getNameIndex_examples(self):
    inspector = FunctionInspector(func.SimpleClass.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc( self ) \\\n"))
    inspector = FunctionInspector(func.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc():\n"))
    inspector = FunctionInspector(func.simpleFunc2)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc2 \\\n                \\\n                (\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc3)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc3 \\\n                \\\n                (\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc4)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc4 \\\n                (\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc5)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc5 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc6)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc6 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc7)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc7 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc8)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc8 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc9)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc9 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc10)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc10 \\\n                ( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc11)
    source = inspector.getFullSource()
    idx = inspector.getNameIndex()
    self.assertTrue(source[idx:].startswith("simpleFunc11 \\\n                ( arg\n        )\\\n        :"))

  def test_getSignatureIndex_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("():\n"))
    inspector = FunctionInspector(func.simpleFunc2)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("(\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc3)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("(\n\n        )\\\n"))
    inspector = FunctionInspector(func.simpleFunc4)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("(\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc5)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc6)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc7)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc8)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc9)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc10)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc11)
    source = inspector.getFullSource()
    idx = inspector.getSignatureIndex()
    self.assertTrue(source[idx:].startswith("( arg\n        )\\\n        :"))

  def test_getColonIndex_examples(self):
    inspector = FunctionInspector(func.simpleFunc)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def simpleFunc():"))
    inspector = FunctionInspector(func.simpleFunc2)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n    \\\n        simpleFunc2 \\\n                \\\n"
                                              "                (\n\n        )\\\n        \\\n        :"))
    inspector = FunctionInspector(func.simpleFunc3)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n    \\\n        simpleFunc3 \\\n                \\\n"
                                              "                (\n\n        )\\\n        \\\n        :"))
    inspector = FunctionInspector(func.simpleFunc4)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc4 \\\n                "
                                               "(\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc5)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc5 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc6)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc6 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc7)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc7 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc8)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc8 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc9)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc9 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc10)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc10 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc11)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc11 \\\n                "
                                               "( arg\n        )\\\n        :"))
    inspector = FunctionInspector(func.simpleFunc12)
    source = inspector.getFullSource()
    idx = inspector.getColonIndex()
    self.assertTrue(source[:idx + 1].endswith("def \\\n        simpleFunc12 \\\n                ( str = \"2:1\","
                                              "\n                  d = {\"one\": 1}\n        )\\\n        :"))