import inspect
import hashlib

from modules import stringUtil
from modules.checks import checks
from modules.sourceInspector import functionInspector


def getHash(func):
  checks.checkIfUserDefinedFunction(func)
  implementation = inspect.getsource(func)
  return hashlib.sha512(bytes(implementation, encoding='utf-8')).hexdigest()

def getFunctionDeclarationIndexes(func):
  """Raises exception if not valid. \n
Full implementation source: inspect.getsource(func) \n
Return: \n
* defIdx: position of the 'def' keyword
* functionNameIdx: position of the function name
* signatureIdx: position of the opening parenthesis of the signature
* colIdx: position of the ':' after the signature"""
  inspector = functionInspector.FunctionInspector(func)
  defIdx = inspector.getDefIndex()
  functionNameIdx = inspector.getNameIndex()
  signatureIdx = inspector.getSignatureIndex()
  funcColIdx = inspector.getColonIndex()
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
