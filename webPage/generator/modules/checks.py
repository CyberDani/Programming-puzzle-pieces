import io

def checkIfPureListOfStrings(var):
  checkIfList(var)
  for val in var:
    if (type(val) != str):
      raise Exception("The list has a non-string element: '{0}'".format(str(val)))

def checkIfList(var):
  if (type(var) != list):
    raise Exception("Not a list type")

def checkIfFile(file):
  if not isinstance(file, io.TextIOBase):
    raise Exception("The file is not a TextIOWrapper type argument")

def checkIntIsBetween(var, minValue, maxValue):
  if (type(minValue) != int):
    raise Exception("minValue not an int type")
  if (type(maxValue) != int):
    raise Exception("maxValue not an int type")
  if (type(var) != int):
    raise Exception("Not an int type for argument " + str(var))
  if (maxValue < minValue):
    raise Exception("max [{0}] < min[{1}]".format(maxValue, minValue))
  if (var < minValue):
    raise Exception("int < " + minValue + " for argument " + str(var))
  if (var > maxValue):
    raise Exception("Do you really need that int to be {0}?".format(var))