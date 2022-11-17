import random

from modules import checks

def getAllExamplesByTypes(examplesDict, typeTuple):
  """ Raises exception if a type could not be found within examples.\n
Return value:\n
* examples: list containing lists of all examples"""
  checks.checkIfTuple(typeTuple)
  checks.checkIfType(examplesDict, dict)
  examples = []
  for typ in typeTuple:
    if typ not in examplesDict:
      raise Exception("Could not found '{}' within examples".format(str(typ)))
    typeValues = examplesDict[typ]
    examples.append(typeValues)
  return examples

def getRandomTupleByType(examplesDict, typeTuple):
  """ Raises exception if a type could not be found within examples."""
  checks.checkIfTuple(typeTuple)
  checks.checkIfType(examplesDict, dict)
  allValues = getAllExamplesByTypes(examplesDict, typeTuple)
  randomValues = []
  for values in allValues:
    randomValues.append(random.choice(values))
  return tuple(randomValues)
