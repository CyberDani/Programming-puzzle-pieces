import inspect
import hashlib

from modules import stringUtil
from modules.checks import checks

def getHash(func):
  checks.checkIfUserDefinedFunction(func)
  implementation = inspect.getsource(func)
  return hashlib.sha512(bytes(implementation, encoding='utf-8')).hexdigest()

def getFunctionSignature(func):
  """Signature string is normalized by deleting extra and adding missing white space characters. \n
Example: (arg1: int, arg2: str) -> bool"""
  checks.checkIfUserDefinedFunction(func)
  return str(inspect.signature(func))

def getFunctionName(func):
  checks.checkIfUserDefinedFunction(func)
  return func.__name__

def getDefIndex(func):
  """Raises exception if not valid (should not happen). \n
Full implementation source: inspect.getsource(func) \n
Return: \n
* defIdx: position of the 'def' keyword"""
  checks.checkIfUserDefinedFunction(func)
  source = inspect.getsource(func)
  startIdx, defIdx = 0, -1
  aroundFound, aroundIdx = stringUtil.find(source, '@', 0, len(source) - 1, -1)
  firstOpenParenthesisFound, firstOpenParenthesisIdx = stringUtil.find(source, '(', 0, len(source) - 1, -1)
  while True:
    found, defIdx = stringUtil.whitespaceDelimitedFind(source, "def", startIdx, len(source) - 1)
    if not found:
      raise Exception("'def' not found for function '{}'".format(func.__name__))
    if aroundFound < defIdx and firstOpenParenthesisFound and firstOpenParenthesisIdx < defIdx:
      found, idx = stringUtil.getLastNonWhiteSpaceCharIdx(source, 0, defIdx - 1)
      if not found:
        raise Exception("Strange unexpected error")
      newLineFound, newLineIdx = stringUtil.find(source, "\n", idx, defIdx, -1)
      if (not newLineFound and source[idx] == ")") or source[idx] != ")":
        startIdx = defIdx + 1
        continue
    break
  return defIdx

def getNameIndex(func):
  """Raises exception if not valid (should not happen). \n
Full implementation source: inspect.getsource(func) \n
Return: \n
* functionNameIdx: points to the first character of the function name"""
  defIdx = getDefIndex(func)
  source = inspect.getsource(func)
  found, functionNameIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(source, defIdx + 3, len(source) - 1)
  while found and source[functionNameIdx] == '\\':
    startIdx = functionNameIdx + 1
    found, functionNameIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(source, startIdx, len(source) - 1)
  if not found or source[functionNameIdx: functionNameIdx + len(func.__name__)] != func.__name__:
    raise Exception("Function name not found for function '{}'".format(func.__name__))
  return functionNameIdx

def getSignatureIndex(func):
  """Raises exception if not valid (should not happen). \n
Full implementation source: inspect.getsource(func) \n
Return: \n
* signatureIdx: points to the '(' character of the signature"""
  functionNameIdx = getNameIndex(func)
  source = inspect.getsource(func)
  found, signatureIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(source, functionNameIdx + len(func.__name__),
                                                                len(source) - 1)
  while found and source[signatureIdx] == '\\':
    startIdx = signatureIdx + 1
    found, signatureIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(source, startIdx, len(source) - 1)
  if not found or source[signatureIdx] != "(":
    raise Exception("Failed to find signature for function '{}'".format(func.__name__))
  return signatureIdx

def getFunctionDeclarationIndexes(func):
  """Raises exception if not valid. \n
Full implementation source: inspect.getsource(func) \n
Return: \n
* defIdx: position of the 'def' keyword
* functionNameIdx: position of the function name
* signatureIdx: position of the opening parenthesis of the signature
* colIdx: position of the ':' after the signature"""
  functionName = getFunctionName(func)
  source = inspect.getsource(func)
  startIdx = 0
  defIdx = getDefIndex(func)
  functionNameIdx = getNameIndex(func)
  signatureIdx = getSignatureIndex(func)
  sig = getFunctionSignature(func)
  nrOfColons = sig.count(":")
  found, funcColIdx = stringUtil.findNthOccurrence(source, ":", nrOfColons + 1, signatureIdx, len(source) - 1)
  if not found:
    raise Exception("Failed to find the colon at the end of the function declaration")
  return defIdx, functionNameIdx, signatureIdx, funcColIdx

# TODO not tested
def getOnlyImplementation(func):
  source = inspect.getsource(func)
  functionName = getFunctionName(func)
  startIdx = 0
  functionNameIdx = -1
  while True:
    found, idx = stringUtil.whitespaceDelimitedFind(source, "def", startIdx, len(source) - 1)
    if not found:
      raise Exception("Definition not found for function '{}'".format(functionName))
    found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(source, idx + 3, len(source) - 1)
    if not found:
      raise Exception("Function name '{}' not found in its source code".format(functionName))
    if source[idx: idx + len(functionName)] == functionName:
      functionNameIdx = idx
      break
  sig = getFunctionName(func)
  nrOfColons = sig.count(":")
  found, funcColIdx = stringUtil.findNthOccurrence(source, ":", nrOfColons + 1, functionNameIdx, len(source) - 1)
  if not found:
    raise Exception("Failed to find the colon at the end of the function declaration")
