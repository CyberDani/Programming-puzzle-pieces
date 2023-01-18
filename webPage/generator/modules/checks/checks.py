import io
import json
import os
import pathlib

def checkIfValidJsonFile(file):
  checkIfFile(file)
  try:
    return json.load(file)
  except ValueError as e:
    raise Exception('Invalid json: {0}'.format(e))

def checkIfValidJsonFileByFilePath(filePath):
  checkIfString(filePath, 2, 300)
  f = open(filePath, "r")
  return checkIfValidJsonFile(f)

def checkIfStringDoesNotContainAnySubstringFromList(string, minLength, maxLength, listOfExceptionChars):
  checkIfString(string, minLength, maxLength)
  checkIfPureListOfStrings(listOfExceptionChars)
  for stringToMatch in listOfExceptionChars:
    if stringToMatch in string:
      raise Exception("String '{}' should not contain '{}' in itself".format(string, stringToMatch))

def checkIfStringIsAlphaNumerical(string):
  if type(string) != str:
    raise Exception("Not a string type: '{0}'".format(str(string)))
  if not string.isalnum():
    raise Exception("String {} is not alphanumerical!".format(string))

def checkIfFilePathExists(filePath):
  checkIfString(filePath, 2, 300)
  if not os.path.isfile(filePath):
    raise Exception("Could not found file path '{}'!".format(filePath))

def checkIfDirectoryPathExists(dirPath):
  checkIfString(dirPath, 1, 300)
  resolvedPath = pathlib.Path(dirPath).resolve()
  if not resolvedPath.is_dir():
    raise Exception("Could not validate as a directory path '{}'!".format(resolvedPath))

def checkIfCallable(arg):
  if not callable(arg):
    raise Exception("'{}' having type '{}' is not a callable object!".format(str(arg), str(type(arg))))

def checkIfTuple(arg):
  if type(arg) != tuple:
    raise Exception("'{}' having type '{}' is not a tuple!".format(str(arg), str(type(arg))))

def checkIfDict(arg):
  if type(arg) != dict:
    raise Exception("'{}' having type '{}' is not a dictionary!".format(str(arg), str(type(arg))))

def checkIfType(value, compareType):
  if type(value) != compareType:
    raise Exception("Type missmatch '{}' with '{}'!".format(str(type(value)), str(compareType)))

def checkIfAnyType(value, compareTypeList):
  checkIfList(compareTypeList)
  for compareType in compareTypeList:
    if type(value) == compareType:
      return
  raise Exception("Type missmatch using '{}'!".format(str(type(value))))

def checkIfAllNoneOrString(listVar, minStringLength, maxStringLength):
  checkIfList(listVar)
  if len(listVar) == 0:
    raise Exception("List must not be empty")
  allNone = True
  for val in listVar:
    if val is not None:
      allNone = False
      break
  if allNone:
    return
  for val in listVar:
    checkIfString(val, minStringLength, maxStringLength)

def checkIfChar(var):
  if type(var) != str:
    raise Exception("Not a string type: '{0}'!".format(str(var)))
  if len(var) != 1:
    raise Exception("The length of '{0}' is not 1 to be char!".format(str(var)))

def checkIfString(var, minLength, maxLength):
  if type(var) != str:
    raise Exception("Not a string type: '{0}'".format(str(var)))
  if type(minLength) != int:
    raise Exception("minLength not an int type")
  if type(maxLength) != int:
    raise Exception("maxLength not an int type")
  if minLength < 0:
    raise Exception("minLength cannot be a negative number")
  if maxLength < minLength:
    raise Exception("maxLength [{0}] < minLength [{1}]".format(maxLength, minLength))
  if len(var) < minLength:
    raise Exception("String is too short")
  if len(var) > maxLength:
    raise Exception("String is too long")

def checkIfPureListOfStrings(var):
  checkIfList(var)
  for val in var:
    if type(val) != str:
      raise Exception("The list has a non-string element: '{0}'".format(str(val)))

def checkIfPureListOfNonEmptyStrings(var):
  checkIfPureListOfStrings(var)
  for string in var:
    if not string:
      raise Exception("Empty string found in list: '{0}'".format(str(var)))

def checkIfPureListOfStringsDoesNotContainWhitespaceCharacter(var):
  checkIfPureListOfStrings(var)
  for string in var:
    for char in string:
      if char.isspace():
        raise Exception("Whitespace character found in string: '{0}'".format(str(string)))

def checkIfPureListOfNonEmptyStringsDoesNotContainWhitespaceCharacter(var):
  checkIfPureListOfNonEmptyStrings(var)
  for string in var:
    for char in string:
      if char.isspace():
        raise Exception("Whitespace character found in string: '{0}'".format(str(string)))

def checkIfTwoNonEmptyStringsAreDifferent(string1, string2):
  checkIfString(string1, 1, 5000)
  checkIfString(string2, 1, 5000)
  if string1 == string2:
    raise Exception("String '{}' is equal with '{}'".format(string1, string2))

def checkIfNonEmptyPureListOfStrings(var):
  checkIfList(var)
  if len(var) == 0:
    raise Exception("The list must contain at least one string!")
  for val in var:
    if type(val) != str:
      raise Exception("The list has a non-string element: '{0}'".format(str(val)))

def checkIfList(var):
  if type(var) != list:
    raise Exception("Not a list type")

def checkIfEmptyList(var):
  if type(var) != list:
    raise Exception("Not a list type")
  if len(var) > 0:
    raise Exception("The list must be empty")

def checkIfNonEmptyList(var):
  if type(var) != list:
    raise Exception("Not a list type")
  if len(var) == 0:
    raise Exception("The list must contain at least one element")

def checkIfNonEmptyPureListOfType(var, compareType):
  checkIfNonEmptyList(var)
  for element in var:
    checkIfType(element, compareType)

def checkIfFile(file):
  if not isinstance(file, io.TextIOBase):
    raise Exception("The file is not a TextIOWrapper type argument")

def checkIntIsBetween(var, minValue, maxValue):
  if type(minValue) != int:
    raise Exception("minValue not an int type")
  if type(maxValue) != int:
    raise Exception("maxValue not an int type")
  if type(var) != int:
    raise Exception("Not an int type for argument " + str(var))
  if maxValue < minValue:
    raise Exception("max [{0}] < min[{1}]".format(maxValue, minValue))
  if var < minValue:
    raise Exception("var({}) < minValue({})?".format(var, minValue))
  if var > maxValue:
    raise Exception("var({}) > maxValue({})?".format(var, maxValue))
