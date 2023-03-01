import dis
import inspect
import builtins as builtin

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
    """Signature string is normalized by deleting extra and adding missing white space characters. Simple quotes will
be used unless it does not make sense to use the double ones.\n
  Example: (arg1: int, arg2='default', arg3="hello 'world'") -> bool"""
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
      checks.checkIfTrue(found, "'def' not found for function '{}'".format(self.functionName))
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
    sourceIdx, signatureIdx, colonIdx = self.signatureIndex, 0, 0
    signatureLen = len(self.signature)
    while signatureIdx < signatureLen:
      found, sourceIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(self.source, sourceIdx, self.sourceLen - 1)
      if not found: raise Exception("Failed to find colon idx for function '{}'".format(self.functionName))
      found, signatureIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(self.signature, signatureIdx, signatureLen - 1)
      if self.source[sourceIdx] == self.signature[signatureIdx] or \
            (self.source[sourceIdx] == '"' and self.signature[signatureIdx] == "'"):
        sourceIdx += 1
        signatureIdx += 1
        continue
      if self.source[sourceIdx] == "#":
        found, sourceIdx = stringUtil.getFirstNewLineCharIdx(self.source, sourceIdx, self.sourceLen - 1)
        if not found: raise Exception("Failed to find colon idx for function '{}'".format(self.functionName))
        continue
      if self.source[sourceIdx:sourceIdx + 2] == '\\"' and self.signature[signatureIdx] == '"':
        sourceIdx += 2
        signatureIdx += 1
        continue
      raise Exception("Failed to find colon idx for function '{}'".format(self.functionName))
    found, sourceIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(self.source, sourceIdx, self.sourceLen - 1)
    if not found: raise Exception("Failed to find colon idx for function '{}'".format(self.functionName))
    while self.source[sourceIdx] == "\\":
      found, sourceIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(self.source, sourceIdx + 1, self.sourceLen - 1)
      if not found: raise Exception("Failed to find colon idx for function '{}'".format(self.functionName))
    if self.source[sourceIdx] == ":":
      self.colonIndex = sourceIdx
    return self.colonIndex

  def getImplementationIndex(self):
    """Raises exception if not valid (should not happen). \n
Returns the index of the first line at where the implementation begins skipping all possible comments"""
    if self.implementationIndex is not None:
      return self.implementationIndex
    if self.colonIndex is None:
      self.getColonIndex()
    idx = self.colonIndex + 1
    while True:
      found, idx = stringUtil.getFirstNewLineCharIdx(self.source, idx, self.sourceLen - 1)
      if not found: raise Exception("Failed to find implementation for function '{}'".format(self.functionName))
      # skip newlines
      found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(self.source, idx, self.sourceLen - 1)
      if not found: raise Exception("Failed to find implementation for function '{}'".format(self.functionName))
      if self.source[idx:].startswith('"""'):
        found, idx = stringUtil.find(self.source, '"""', idx + 3, self.sourceLen - 1, -1)
        if not found: raise Exception("Incorrect doc found in function '{}'".format(self.functionName))
        found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(self.source, idx + 3, self.sourceLen - 1)
        if not found: raise Exception("Failed to find implementation for function '{}'".format(self.functionName))
      if self.source[idx] == "#": continue
      found, self.implementationIndex = stringUtil.getLastNewLineCharIdx(self.source, self.colonIndex, idx)
      if not found: raise Exception("Failed to find implementation for function '{}'".format(self.functionName))
      break
    self.implementationIndex += 1
    if self.implementationIndex >= self.sourceLen - 1:
      raise Exception("Failed to find implementation for function '{}'".format(self.functionName))
    return self.implementationIndex

  def getImplementationCode(self):
    """Get raw implementation code as if it were alone itself, which means: \n
* Remove first indentation
* Remove empty lines
* Remove comments
* Replace 'return' with 'returnValue ='\n
There is no source code normalization applied."""
    startIdx = self.getImplementationIndex()
    lines = self.source[startIdx:].splitlines()
    found, nrOfCharsUsedForIndentation = stringUtil.getFirstNonWhiteSpaceCharIdx(lines[0], 0, len(lines[0]) - 1)
    if not found:
      raise Exception("Failed to get implementation code for function '{}'".format(self.functionName))
    answer = ""
    for line in lines:
      if not line:
        continue
      # TODO stringUtil.stringHasOnlyWhitespaceChars
      found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(line, 0, len(line) - 1)
      if not found:
        continue
      while True:
        if not line:
          break
        found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(line, 0, len(line) - 1)
        if not found:
          break
        commentFound, commentIdx = stringUtil.find(line, "#", idx, len(line) - 1, -1)
        if not commentFound:
          break
        notString = stringUtil.indexIsOutsideOfPythonStringConstant(line, commentIdx)
        if notString:
          line = line[:commentIdx]
        else:
          continue
      found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(line, 0, len(line) - 1)
      if not found:
        continue
      line = line.rstrip()
      while True:
        returnFound, returnIdx = stringUtil.find(line, "return", idx, len(line) - 1, -1)
        if not returnFound:
          break
        if line[returnIdx - 1] != ":" and not line[returnIdx - 1].isspace():
          idx = returnIdx + 1
          continue
        if returnIdx + 6 < len(line) and not line[returnIdx + 6].isspace():
          idx = returnIdx + 1
          continue
        notString = stringUtil.indexIsOutsideOfPythonStringConstant(line, returnIdx)
        if notString:
          line = line[:returnIdx] + "returnValue =" + line[returnIdx + 6:]
        else:
          idx = returnIdx + 1
          continue
      answer += line[nrOfCharsUsedForIndentation:] + "\n"
    return answer[:-1]

  # Source (slightly modified):
  # https://stackoverflow.com/questions/51901676/get-the-lists-of-functions-used-called-within-a-function-in-python
  def getFunctionCallNames(self, built_ins=False):
    """Ignore function names which can be methods of a built-in type (e.g. find). Because of the duck-typing mechanism
it seems impossible to deduce if that method is applied on a string for example. To not be excluded better autocheck
that functions has unique names.\n
**Does not work with decorated functions** (it will return empty lists)\n
Return:\n
* functionNames: list of names ordered alphabetically
* methodNames: list of names ordered alphabetically"""
    # function definition will not work, e.g. self.source[self.defIndex] - will found nothing
    implCode = self.getImplementationCode()
    code = compile(implCode,
                   filename="compiled",
                   mode="exec")
    instructions = list(dis.get_instructions(code))[::-1]
    # use dict for unique check
    functions, methods = {}, {}
    for i, inst in list(enumerate(instructions))[::-1]:
        if inst.opname[:11] == "LOAD_METHOD":
          name = str(inst.argval)
          if not hasattr(str, name) and not hasattr(tuple, name) and not hasattr(dict, name):
            methods[name] = True
          continue
        if inst.opname[:13] == "CALL_FUNCTION":
            # function takes ins[i].arg number of arguments
            ep = i + inst.arg + (2 if inst.opname[13:16] == "_KW" else 1)
            # parse argument list (Python2)
            if inst.arg == 257:
                k = i+1
                while k < len(instructions) and instructions[k].opname != "BUILD_LIST":
                    k += 1
                ep = k-1
            entry = instructions[ep]
            name = str(entry.argval)
            if "." not in name and (entry.opname == "LOAD_GLOBAL" or entry.opname == "LOAD_NAME") and \
                    (built_ins or not hasattr(builtin, name)):
                functions[name] = True
            # reduce this CALL_FUNCTION and all its parameters to one entry
            instructions = instructions[:i] + [entry] + instructions[ep + 1:]
    return sorted(list(functions.keys())), sorted(list(methods.keys()))
