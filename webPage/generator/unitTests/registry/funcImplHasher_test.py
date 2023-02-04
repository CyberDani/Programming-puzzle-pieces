import inspect
import sys

sys.path.append('../..')

from modules.unitTests.autoUnitTest import AutoUnitTest

from modules.checks import checks
from modules.registry import funcionImpllHasher as funcImplHash
from unitTests4unitTests import similarFunctions as func

class FunctionImplementationHasherTests(AutoUnitTest):

  def setUp(self):
    self.hash = funcImplHash.getHash(func.simpleFunc)

  def test_getFunctionDeclarationIndexes_wrongType(self):
    self.assertRaises(Exception, funcImplHash.getFunctionDeclarationIndexes, print)
    self.assertRaises(Exception, funcImplHash.getFunctionDeclarationIndexes, None)
    self.assertRaises(Exception, funcImplHash.getFunctionDeclarationIndexes, [])
    self.assertRaises(Exception, funcImplHash.getFunctionDeclarationIndexes, sys.path.copy)
    self.assertRaises(Exception, funcImplHash.getFunctionDeclarationIndexes, AutoUnitTest)

  def test_getFunctionDeclarationIndexes_examples(self):
    source = inspect.getsource(func.simpleFunc)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc")
    self.assertEqual(source[signatureIdx:colIdx], "()")
    source = inspect.getsource(func.simpleFunc2)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc2)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def \\\n    \\\n        ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc2 \\\n                \\\n                ")
    self.assertEqual(source[signatureIdx:colIdx], "(\n\n        )\\\n        \\\n        ")
    self.assertEqual(source[colIdx], ':')
    source = inspect.getsource(func.simpleFunc3)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc3)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def \\\n    \\\n        ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc3 \\\n                \\\n                ")
    self.assertEqual(source[signatureIdx:colIdx], "(\n\n        )\\\n        \\\n        ")
    self.assertEqual(source[colIdx], ':')
    source = inspect.getsource(func.simpleFunc4)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc4)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def \\\n        ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc4 \\\n                ")
    self.assertEqual(source[signatureIdx:colIdx], "(\n        )\\\n        ")
    self.assertEqual(source[colIdx], ':')
    source = inspect.getsource(func.simpleFunc5)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc5)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def \\\n        ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc5 \\\n                ")
    self.assertEqual(source[signatureIdx:colIdx], "( arg\n        )\\\n        ")
    self.assertEqual(source[colIdx], ':')
    source = inspect.getsource(func.simpleFunc6)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc6)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def \\\n        ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc6 \\\n                ")
    self.assertEqual(source[signatureIdx:colIdx], "( arg\n        )\\\n        ")
    self.assertEqual(source[colIdx], ':')
    source = inspect.getsource(func.simpleFunc7)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc7)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def \\\n        ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc7 \\\n                ")
    self.assertEqual(source[signatureIdx:colIdx], "( arg\n        )\\\n        ")
    self.assertEqual(source[colIdx], ':')
    source = inspect.getsource(func.simpleFunc8)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc8)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def \\\n        ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc8 \\\n                ")
    self.assertEqual(source[signatureIdx:colIdx], "( arg\n        )\\\n        ")
    self.assertEqual(source[colIdx], ':')
    source = inspect.getsource(func.simpleFunc9)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc9)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def \\\n        ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc9 \\\n                ")
    self.assertEqual(source[signatureIdx:colIdx], "( arg\n        )\\\n        ")
    self.assertEqual(source[colIdx], ':')
    source = inspect.getsource(func.simpleFunc10)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc10)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def \\\n        ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc10 \\\n                ")
    self.assertEqual(source[signatureIdx:colIdx], "( arg\n        )\\\n        ")
    self.assertEqual(source[colIdx], ':')
    source = inspect.getsource(func.simpleFunc11)
    defIdx, nameIdx, signatureIdx, colIdx = funcImplHash.getFunctionDeclarationIndexes(func.simpleFunc11)
    self.assertTrue(defIdx < nameIdx < signatureIdx < colIdx)
    self.assertEqual(source[defIdx:nameIdx], "def \\\n        ")
    self.assertEqual(source[nameIdx:signatureIdx], "simpleFunc11 \\\n                ")
    self.assertEqual(source[signatureIdx:colIdx], "( arg\n        )\\\n        ")
    self.assertEqual(source[colIdx], ':')

  def test_getHash_wrongType(self):
    self.assertRaises(Exception, funcImplHash.getHash, print)
    self.assertRaises(Exception, funcImplHash.getHash, None)
    self.assertRaises(Exception, funcImplHash.getHash, [])
    self.assertRaises(Exception, funcImplHash.getHash, sys.path.copy)
    self.assertRaises(Exception, funcImplHash.getHash, AutoUnitTest)

  def test_getHash_functionHashEqualsWithItself(self):
    hash1 = funcImplHash.getHash(func.simpleFunc)
    hash2 = funcImplHash.getHash(func.simpleFunc)
    self.assertEqual(hash1, hash2)
    self.assertEqual(self.hash, hash1)
    self.assertEqual(self.hash, hash2)

  def test_getHash_differentFunctionName(self):
    hash1 = funcImplHash.getHash(func.simpleFunc)
    hash2 = funcImplHash.getHash(func.simpleFunc_sameImpl)
    # self.assertEqual(hash1, hash2)
