import inspect

from modules import stringUtil
from modules.checks import checks

class FunctionInspector:
  def __init__(self, func):
    checks.checkIfUserDefinedFunction(func)
    self.func = func
    self.source = inspect.getsource(func)
    self.sourceLen = len(self.source)
    self.functionName = func.__name__
    self.signature = str(inspect.signature(func))
    self.isDecorated = False
    self.decoratorIndex, self.defIndex, \
      self.nameIndex, self.signatureIndex, \
      self.colonIndex, self.implementationIndex = None, None, None, None, None, None

  def getFunctionName(self):
    return self.functionName

  def getFunctionSignature(self):
    """Signature string is normalized by deleting extra and adding missing white space characters. \n
  Example: (arg1: int, arg2: str) -> bool"""
    return self.signature

  def getArgumentVariableNames(self):
    """Keeps the original order"""
    args = inspect.getfullargspec(self.func).args
    answer = ""
    for arg in args:
      answer += arg + ","
    if answer:
      answer = answer[:-1]
    return answer

  def getFullSource(self):
    """Original source code containing every part of the function, not normalized"""
    return self.source

  def isDecorator(self):
    return self.source.startswith("@decorator\n")

  def getDecorationIndex(self):
    """Returns:\n
* found: True | False
* decoratorIndex: the index of the first '@' character (even for multiple decorators), -1 if not found"""
    if self.decoratorIndex is not None:
      return self.isDecorated, self.decoratorIndex
    if self.defIndex is None:
      self.getDefIndex()
    found, idx = stringUtil.find(self.source, "@", 0, self.defIndex, -1)
    if not found:
      return False, -1
    self.decoratorIndex = idx
    self.isDecorated = True
    return True, self.decoratorIndex

  def getDefIndex(self):
    """Raises exception if not valid (should not happen). \n
Returns the position of the 'def' keyword"""
    if self.defIndex is not None:
      return self.defIndex
    startIdx = 0
    aroundFound, aroundIdx = stringUtil.find(self.source, '@', 0, self.sourceLen - 1, -1)
    firstOpenParenthesisFound, firstOpenParenthesisIdx = stringUtil.find(self.source, '(', 0, self.sourceLen - 1, -1)
    while True:
      found, self.defIndex = stringUtil.whitespaceDelimitedFind(self.source, "def", startIdx, self.sourceLen - 1)
      if not found:
        raise Exception("'def' not found for function '{}'".format(self.functionName))
      if aroundFound < self.defIndex and firstOpenParenthesisFound and firstOpenParenthesisIdx < self.defIndex:
        found, idx = stringUtil.getLastNonWhiteSpaceCharIdx(self.source, 0, self.defIndex - 1)
        if not found:
          raise Exception("Strange unexpected error")
        newLineFound, newLineIdx = stringUtil.find(self.source, "\n", idx, self.defIndex, -1)
        if (not newLineFound and self.source[idx] == ")") or self.source[idx] != ")":
          startIdx = self.defIndex + 1
          continue
      break
    return self.defIndex

  def getNameIndex(self):
    """Raises exception if not valid (should not happen). \n
Returns the index of the first character from the function name"""
    if self.nameIndex is not None:
      return self.nameIndex
    if self.defIndex is None:
      self.getDefIndex()
    found, self.nameIndex = stringUtil.getFirstNonWhiteSpaceCharIdx(self.source, self.defIndex + 3, self.sourceLen - 1)
    while found and self.source[self.nameIndex] == '\\':
      startIdx = self.nameIndex + 1
      found, self.nameIndex = stringUtil.getFirstNonWhiteSpaceCharIdx(self.source, startIdx, self.sourceLen - 1)
    if not found or self.source[self.nameIndex: self.nameIndex + len(self.functionName)] != self.functionName:
      raise Exception("Function name not found for function '{}'".format(self.functionName))
    return self.nameIndex

  def getSignatureIndex(self):
    """Raises exception if not valid (should not happen). \n
Returns the index of the first '(' character of the function signature"""
    if self.signatureIndex is not None:
      return self.signatureIndex
    if self.nameIndex is None:
      self.getNameIndex()
    found, self.signatureIndex = stringUtil.getFirstNonWhiteSpaceCharIdx(self.source, self.nameIndex
                                                                         + len(self.functionName), self.sourceLen - 1)
    while found and self.source[self.signatureIndex] == '\\':
      startIdx = self.signatureIndex + 1
      found, self.signatureIndex = stringUtil.getFirstNonWhiteSpaceCharIdx(self.source, startIdx, self.sourceLen - 1)
    if not found or self.source[self.signatureIndex] != "(":
      raise Exception("Failed to find signature for function '{}'".format(self.functionName))
    return self.signatureIndex

  def getColonIndex(self):
    """Raises exception if not valid (should not happen). \n
Returns the position of the first ':' after the signature"""
    if self.colonIndex is not None:
      return self.colonIndex
    if self.signatureIndex is None:
      self.getSignatureIndex()
    nrOfColons = self.signature.count(":")
    found, self.colonIndex = stringUtil.findNthOccurrence(self.source, ":", nrOfColons + 1,
                                                          self.signatureIndex, self.sourceLen - 1)
    if not found:
      raise Exception("Failed to find the colon at the end of the '{}' function declaration".format(self.functionName))
    return self.colonIndex

  def getImplementationIndex(self):
    """Raises exception if not valid (should not happen). \n
Returns the index of the first line at where the implementation begins"""
    if self.implementationIndex is not None:
      return self.implementationIndex
    if self.colonIndex is None:
      self.getColonIndex()
    found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(self.source, self.colonIndex + 1, self.sourceLen - 1)
    if not found:
      raise Exception("Failed to find implementation for function '{}'".format(self.functionName))
    found, self.implementationIndex = stringUtil.getLastNewLineCharIdx(self.source, self.colonIndex, idx)
    if not found:
      raise Exception("Failed to find implementation for function '{}'".format(self.functionName))
    self.implementationIndex += 1
    if self.implementationIndex >= self.sourceLen - 1:
      raise Exception("Failed to find implementation for function '{}'".format(self.functionName))
    return self.implementationIndex
