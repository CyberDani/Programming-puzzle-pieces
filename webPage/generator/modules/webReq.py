import requests

from modules import checks

def getstatusCodeEncodingAndHtmlFromUrl(url):
  checks.checkIfString(url, 9, 500)
  r = requests.get(url)
  return r.status_code, r.encoding, r.text

def downloadFromUrlToFileIfStatusIs200(url, filePath):
  checks.checkIfString(url, 9, 500)
  checks.checkIfString(filePath, 3, 300)
  r = requests.get(url, stream=True)
  if r.status_code != 200:
    raise Exception('Status Code {0} returned, download prevented!'.format(r.status_code))
  with open(filePath, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=512000): # 500 kb chunks
      fd.write(chunk)