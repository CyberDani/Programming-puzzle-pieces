import subprocess

from modules import checks

def getOutputFromCommand(command):
  checks.checkIfString(command, 1, 800)
  result = subprocess.run(command, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
  return result
