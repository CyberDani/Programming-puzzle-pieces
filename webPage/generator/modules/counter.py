from modules import checks

class SimpleCounter:
  def __init__(self, startCounter):
    checks.checkIntIsBetween(startCounter, 0, 1000000)
    self.counter = startCounter
  
  def getNextInt(self):
    counterCp = self.counter
    self.counter += 1
    return counterCp

  def getNextMessage(self, string):
    checks.checkIfString(string, 0, 500)
    ans = "[{0}] {1}".format(self.counter, string)
    self.counter += 1
    return ans
