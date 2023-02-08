def getTrue():
  return True

def getFalseIfNotTrue():
  return not getTrue()

class OtherClass:
  def saySomething(self):
    if getTrue():
      print("something true")
    else:
      print("Something else")
