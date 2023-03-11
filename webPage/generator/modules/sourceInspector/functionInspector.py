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

  # TODO test
  def __getFirstIndexAfterSignature(self):
    self.getSignatureIndex()
    sourceIdx, signatureIdx, signatureLen = self.signatureIndex, 0, len(self.signature)
    while signatureIdx < signatureLen:
      sourceIdx = stringUtil.getFirstNonWhiteSpaceCharIdxOrThrow(self.source, sourceIdx, self.sourceLen - 1)
      found, signatureIdx = stringUtil.getFirstNonWhiteSpaceCharIdx(self.signature, signatureIdx, signatureLen - 1)
      if self.source[sourceIdx] == self.signature[signatureIdx] or \
              (self.source[sourceIdx] == '"' and self.signature[signatureIdx] == "'"):
        sourceIdx += 1
        signatureIdx += 1
        continue
      if self.source[sourceIdx] == "#":
        sourceIdx = stringUtil.getFirstNewLineCharIdxOrThrow(self.source, sourceIdx, self.sourceLen - 1)
        continue
      if self.source[sourceIdx:sourceIdx + 2] == '\\"' and self.signature[signatureIdx] == '"':
        sourceIdx += 2
        signatureIdx += 1
        continue
      raise Exception("Failed to find colon idx for function '{}'".format(self.functionName))
    return sourceIdx

  # TODO test
  # TODO move to stringUtil
  def __whiteSpaceString(self, string):
    if not string:
      return True
    found, idx = stringUtil.getFirstNonWhiteSpaceCharIdx(string, 0, len(string) - 1)
    return not found

  # TODO test
  def __removeWhiteSpaceLines(self, lines):
    answer = []
    for line in lines:
      if self.__whiteSpaceString(line):
        continue
      answer.append(line)
    return answer

  # TODO test
  def __removeCommentsFromCodeLines(self, lines):
    """Empty and whitespace lines must be removed before"""
    answer = []
    for line in lines:
      commentIdx = -1
      while True:
        commentFound, commentIdx = stringUtil.find(line, "#", commentIdx + 1, len(line) - 1, -1)
        if not commentFound:
          break
        notString = stringUtil.indexIsOutsideOfPythonStringConstant(line, commentIdx)
        if notString:
          line = line[:commentIdx].rstrip()
          break
      if not self.__whiteSpaceString(line):
        answer.append(line)
    return answer

  # TODO test
  def __removeExtraIndentationFromCodeLines(self, lines):
    """Whitespace lines and comments must be removed before"""
    nrOfCharsUsedForIndentation = stringUtil.getFirstNonWhiteSpaceCharIdxOrThrow(lines[0], 0, len(lines[0]) - 1)
    answer = []
    for line in lines:
      answer.append(line[nrOfCharsUsedForIndentation:])
    return answer

  # TODO test
  def __returnIsDelimited(self, line, returnIdx):
    """returnIdx must point to "return" """
    if returnIdx > 0 and line[returnIdx - 1] != ":" and not line[returnIdx - 1].isspace():
      return False
    if returnIdx + 6 < len(line) and not line[returnIdx + 6].isspace():
      return False
    return True

  # TODO test
  def __findReturnInLine(self, line):
    returnIdx = 0
    while True:
      returnFound, returnIdx = stringUtil.find(line, "return", returnIdx, len(line) - 1, -1)
      if not returnFound:
        return False, -1
      if not self.__returnIsDelimited(line, returnIdx) \
              or not stringUtil.indexIsOutsideOfPythonStringConstant(line, returnIdx):
        returnIdx += 1
        continue
      break
    return True, returnIdx

  # TODO test
  def __rewriteReturnToAssignmentIfFound(self, line, variable, defaultValue):
    returnFound, returnIdx = self.__findReturnInLine(line)
    if not returnFound:
      return line
    line = line[:returnIdx] + variable + " =" + line[returnIdx + 6:]
    if returnIdx + 13 == len(line):
      line += " " + defaultValue
    return line

  # TODO test
  def __rewriteReturnsToAssignmentsInCodeLines(self, lines):
    answer = []
    for line in lines:
      line = self.__rewriteReturnToAssignmentIfFound(line, "returnValue", '"exitFunction"')
      answer.append(line)
    return answer

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
      # TODO add throwing alternative
      found, self.defIndex = stringUtil.whitespaceDelimitedFind(self.source, "def", startIdx, self.sourceLen - 1)
      checks.checkIfTrue(found, "'def' not found for function '{}'".format(self.functionName))
      if aroundFound < self.defIndex and firstOpenParenthesisFound and firstOpenParenthesisIdx < self.defIndex:
        idx = stringUtil.getLastNonWhiteSpaceCharIdxOrThrow(self.source, 0, self.defIndex - 1)
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
    self.nameIndex = stringUtil.getFirstNonWhiteSpaceCharIdxOrThrow(self.source, self.defIndex + 3, self.sourceLen - 1)
    while self.source[self.nameIndex] == '\\':
      startIdx = self.nameIndex + 1
      self.nameIndex = stringUtil.getFirstNonWhiteSpaceCharIdxOrThrow(self.source, startIdx, self.sourceLen - 1)
    if self.source[self.nameIndex: self.nameIndex + len(self.functionName)] != self.functionName:
      raise Exception("Function name missmatch for '{}'".format(self.functionName))
    return self.nameIndex

  def getSignatureIndex(self):
    """Raises exception if not valid (should not happen). \n
Returns the index of the first '(' character of the function signature"""
    if self.signatureIndex is not None:
      return self.signatureIndex
    if self.nameIndex is None:
      self.getNameIndex()
    self.signatureIndex = stringUtil.getFirstNonWhiteSpaceCharIdxOrThrow(self.source, self.nameIndex
                                                                         + len(self.functionName), self.sourceLen - 1)
    while self.source[self.signatureIndex] == '\\':
      startIdx = self.signatureIndex + 1
      self.signatureIndex = stringUtil.getFirstNonWhiteSpaceCharIdxOrThrow(self.source, startIdx, self.sourceLen - 1)
    openParenthesesFound = self.source[self.signatureIndex] == "("
    checks.checkIfTrue(openParenthesesFound, "Failed to find signature for function '{}'".format(self.functionName))
    return self.signatureIndex

  def getColonIndex(self):
    """Raises exception if not valid (should not happen). \n
Returns the position of the first ':' after the signature"""
    if self.colonIndex is not None:
      return self.colonIndex
    sourceIdx = self.__getFirstIndexAfterSignature()
    sourceIdx = stringUtil.getFirstNonWhiteSpaceCharIdxOrThrow(self.source, sourceIdx, self.sourceLen - 1)
    while self.source[sourceIdx] == "\\":
      sourceIdx = stringUtil.getFirstNonWhiteSpaceCharIdxOrThrow(self.source, sourceIdx + 1, self.sourceLen - 1)
    checks.checkIfTrue(self.source[sourceIdx] == ":", "Colon char not found")
    self.colonIndex = sourceIdx
    return self.colonIndex

  def getImplementationIndex(self):
    """Raises exception if not valid (should not happen). \n
Returns the index of the first line at where the implementation begins skipping all comments"""
    if self.implementationIndex is not None:
      return self.implementationIndex
    if self.colonIndex is None:
      self.getColonIndex()
    idx = self.colonIndex + 1
    while True:
      idx = stringUtil.getFirstNewLineCharIdxOrThrow(self.source, idx, self.sourceLen - 1)
      idx = stringUtil.getFirstNonWhiteSpaceCharIdxOrThrow(self.source, idx, self.sourceLen - 1)
      if self.source[idx:].startswith('"""'):
        idx = stringUtil.findOrThrow(self.source, '"""', idx + 3, self.sourceLen - 1)
        idx = stringUtil.getFirstNonWhiteSpaceCharIdxOrThrow(self.source, idx + 3, self.sourceLen - 1)
      if self.source[idx] == "#": continue
      self.implementationIndex = stringUtil.getLastNewLineCharIdxOrThrow(self.source, self.colonIndex, idx)
      break
    self.implementationIndex += 1
    if self.implementationIndex >= self.sourceLen - 1:
      raise Exception("Failed to find implementation for function '{}'".format(self.functionName))
    return self.implementationIndex

  def getImplementationCode(self):
    """Get raw implementation code as if it would not be a function: \n
* Remove first indentation
* Remove empty lines
* Remove comments
* Replace 'return' with 'returnValue =' if there is a value
* Replace non-value 'return' with 'returnValue = "exitFunction"' \n
There is no source code normalization applied."""
    startIdx = self.getImplementationIndex()
    lines = self.source[startIdx:].splitlines()
    lines = self.__removeWhiteSpaceLines(lines)
    lines = self.__removeCommentsFromCodeLines(lines)
    lines = self.__removeExtraIndentationFromCodeLines(lines)
    lines = self.__rewriteReturnsToAssignmentsInCodeLines(lines)
    ans = stringUtil.stringListToString(lines, "", "", "\n")
    return ans

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
            methodName = name
            methodParentName = ""
            methodParent = instructions[i+1]
            if methodParent.opname[:9] == "LOAD_NAME":
              methodParentName = methodParent.argrepr
            if methodParentName:
              methods[(methodParentName, methodName)] = True
            else:
              methods[methodName] = True
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
