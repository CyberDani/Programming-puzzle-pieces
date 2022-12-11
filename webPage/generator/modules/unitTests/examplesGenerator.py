import hashlib
import json
import random

from modules import checks

def getAllExamplesByTypes(examplesDict, typeTuple):
  """ Raises exception if a type could not be found within examples.\n
Return value:\n
* examples: list containing lists of all examples"""
  checks.checkIfTuple(typeTuple)
  checks.checkIfDict(examplesDict)
  examples = []
  for typ in typeTuple:
    if typ not in examplesDict:
      raise Exception("Could not found '{}' within examples".format(str(typ)))
    typeValues = examplesDict[typ].copy()
    examples.append(typeValues)
  return examples

def getOneRandomExampleByType(examplesDict, typeTuple):
  """ Raises exception if a type could not be found within examples."""
  allValues = getAllExamplesByTypes(examplesDict, typeTuple)
  randomValues = []
  for values in allValues:
    randomValues.append(random.choice(values))
  return tuple(randomValues)

def getNRandomExamplesByType(examplesDict, typeTuple, nrOfExamples):
  """ Raises exception if a type could not be found within examples."""
  checks.checkIntIsBetween(nrOfExamples, 1, 1000)
  allValues = getAllExamplesByTypes(examplesDict, typeTuple)
  n = len(allValues)
  values = []
  for i in range(n):
    values.append([])
  randomValue = []
  randomValues = []
  while nrOfExamples > 0:
    for i in range(n):
      if not values[i]:
        values[i] = allValues[i].copy()
      value = random.choice(values[i])
      values[i].remove(value)
      randomValue.append(value)
    randomValues.append(tuple(randomValue))
    randomValue.clear()
    nrOfExamples -= 1
  return randomValues

def getNrOfLookalikeTypeTuples(examplesDict, typeTuple):
  """Calculates how many tuple combinations can be made in total by having at least one valid type in its position. \n
Raises exception if a type could not be found within examples."""
  checks.checkIfTuple(typeTuple)
  checks.checkIfDict(examplesDict)
  for typ in typeTuple:
    if typ not in examplesDict:
      raise Exception("Could not found '{}' within examples".format(str(typ)))
  if len(typeTuple) == 1:
    return 0
  x = len(examplesDict)
  xm1 = x - 1
  if len(typeTuple) == 2:
    return 2 * x - 2
  if len(typeTuple) == 3:
    return 3 * (x*x - x)
  if len(typeTuple) == 4:
    return 4*x*x*x - 6*x*x + 4*x - 2
  if len(typeTuple) == 5:
    return x*x*x*x + x*x*x*xm1 + x*x*xm1*xm1 + x*xm1*xm1*xm1 + xm1*xm1*xm1*xm1 - 1
  raise Exception("This case is not implemented!")

def getExamplesDictHash(examplesDict: dict) -> str:
  """Returns the MD5 hash of a dictionary content. \n
Order dependent: hash({'a': 1, 'b': 2) != hash({'b': 2, 'a': 1}) """
  checks.checkIfDict(examplesDict)
  dhash = hashlib.md5()
  encoded = json.dumps(str(examplesDict), ensure_ascii=True).encode()
  dhash.update(encoded)
  return dhash.hexdigest()
