import requests

from modules import checks

def getstatusCodeEncodingAndHtmlFromUrl(url):
  checks.checkIfString(url, 9, 500)
  r = requests.get(url)
  return r.status_code, r.encoding, r.text