import io
import json

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

def checkIfStringIsAlphaNumerical(string):
  if type(string) != str:
    raise Exception("Not a string type: '{0}'".format(str(string)))
  if not string.isalnum():
    raise Exception("String {} is not alphanumerical!".format(string))

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

def checkIfList(var):
  if type(var) != list:
    raise Exception("Not a list type")

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
    raise Exception("int < " + minValue + " for argument " + str(var))
  if var > maxValue:
    raise Exception("Do you really need that int to be {0}?".format(var))
