import os

# this is the main function being run
def backupAndGenerateNewHtmlOutputFile():
  backupIndexHtml()
  generateHtmlOutputFile()

def backupIndexHtml():
  os.replace("../../index.html", "./backup/index.html")

def generateHtmlOutputFile():
  htmlOutputFilePath = "../../index.html"
  htmlFile = open(htmlOutputFilePath, "w")
  writeHtmlContentToFile(htmlFile)

def writeHtmlContentToFile(htmlFile):
  htmlFile.write("<html>\n")
  htmlFile.write("\t<head>\n")
  writeHtmlHeadContent(htmlFile, 2)
  htmlFile.write("\t</head>\n")
  htmlFile.write("\t<body>\n")
  writeHtmlBodyContent(htmlFile, 2)
  htmlFile.write("\t</body>\n")
  htmlFile.write("</html>\n")

# <head>
def writeHtmlHeadContent(htmlFile, indentDepth):
  tabs = getIndentedTab(indentDepth)
  # TODO: see what is worth to add as a configuration
  htmlFile.write(tabs + "<title>Programming puzzle-pieces</title>\n")
  htmlFile.write(tabs + "<link rel=\"icon\" href=\"./webPage/images/favicon.png\">\n")
  # website is optimized for mobile
  htmlFile.write(tabs + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"/>\n")
  htmlFile.write(tabs + "<style>\n")
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/inlineCssStyle.css", indentDepth + 1)
  htmlFile.write(tabs + "</style>\n")
  addFontAwesome(htmlFile, indentDepth)
  addJquery(htmlFile, indentDepth)
  addGoogleIcons(htmlFile, indentDepth)
  addMaterialize(htmlFile, indentDepth)
  addGoogleFont(htmlFile, indentDepth, "?family=Arima+Madurai:wght@500&display=swap")
  addJQueryLoadingOverlay(htmlFile, indentDepth)

# <body>
def writeHtmlBodyContent(htmlFile, indentDepth):
  tabs = getIndentedTab(indentDepth)
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/topNav.txt", indentDepth)
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/sideNav.txt", indentDepth)
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/topQuote.txt", indentDepth)
  addNewLineToHtmlOutputFile(htmlFile, indentDepth)
  htmlFile.write(tabs + "<div id=\"webContent\">\n")
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/svgCurve1.txt", indentDepth + 1)
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/whatThisProjectOffers.txt", indentDepth + 1)
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/svgCurve2.txt", indentDepth + 1)
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/personalRecommandation.txt", indentDepth + 1)
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/svgCurve3.txt", indentDepth + 1)
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/textBelowCurves.txt", indentDepth + 1)
  htmlFile.write(tabs + "</div>\n")
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/footer.txt", indentDepth)
  addJsFileAsLink(htmlFile, indentDepth, "./webPage/scripts/githubApiScripts.js")
  htmlFile.write(tabs + "<script>\n")
  includeFileToHtmlOutputFile(htmlFile, "./htmlIncludes/inlineJs.js", indentDepth + 1)
  htmlFile.write(tabs + "</script>\n")

def addFontAwesome(htmlFile, indentDepth):
  addCssFileAsLink(htmlFile, indentDepth, "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
					"sha512-1ycn6IcaQQ40/MKBW2W4Rhis/DbILU74C1vSrLJxCq57o941Ym01SwNsOMqvEBFlcgUa6xLiPY/NS5R+E6ztJQ==",
					"anonymous", "no-referrer")
  addJsFileAsLink(htmlFile, indentDepth, "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/js/all.min.js",
					"sha512-Tn2m0TIpgVyTzzvmxLNuqbSJH3JP8jm+Cy3hvHrW7ndTDcJ1w5mBiksqDBb8GpE2ksktFvDB/ykZ0mDpsZj20w==",
					"anonymous", "no-referrer")

def addJquery(htmlFile, indentDepth):
  addJsFileAsLink(htmlFile, indentDepth, "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js",
					"sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==",
					"anonymous", "no-referrer")

def addMaterialize(htmlFile, indentDepth):
  addCssFileAsLink(htmlFile, indentDepth, 
					"https://cdn.jsdelivr.net/npm/@materializecss/materialize@1.1.0-alpha/dist/css/materialize.min.css")
  addJsFileAsLink(htmlFile, indentDepth, 
					"https://cdn.jsdelivr.net/npm/@materializecss/materialize@1.1.0-alpha/dist/js/materialize.min.js")

def addGoogleIcons(htmlFile, indentDepth):
  addCssFileAsLink(htmlFile, indentDepth, "https://fonts.googleapis.com/icon?family=Material+Icons")

def addJQueryLoadingOverlay(htmlFile, indentDepth):
    addJsFileAsLink(htmlFile, indentDepth, 
                        "https://cdn.jsdelivr.net/npm/gasparesganga-jquery-loading-overlay@2.1.7/dist/loadingoverlay.min.js")

# include
def includeFileToHtmlOutputFile(htmlFile, includeFilePath, indentDepth):
  lines = getLinesFromFile(includeFilePath)
  tabs = getIndentedTab(indentDepth)
  for line in lines:
    if (line and line != "\n"):
      htmlFile.write(tabs + line)
    else:
      htmlFile.write("\n")
  htmlFile.write("\n")

def getLinesFromFile(filePath):
  f = open(filePath, "r")
  return f.readlines()

# <br \>
def addNewLineToHtmlOutputFile(htmlFile, indentDepth):
  tabs = getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<br \>\n")

# <script src=".js" />
def addJsFileAsLink(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  tabs = getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<script src=\"" + url + "\"")
  if (integrity is None or crossorigin is None or referrerpolicy is None):
    if (integrity is not None or crossorigin is not None or referrerpolicy is not None):
      raise Exception("integrity, crossorigin and referrerpolicy must be all set or None")
    htmlFile.write("></script>\n")
    return
  tabs += "\t"
  htmlFile.write("\n" + tabs + "integrity=\"" + integrity + "\"\n")
  htmlFile.write(tabs + "crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\"></script>\n")

# <link href=".css" />
def addCssFileAsLink(htmlFile, indentDepth, url, integrity=None, crossorigin=None, referrerpolicy=None):
  tabs = getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<link href=\"" + url + "\"")
  if (integrity is None or crossorigin is None or referrerpolicy is None):
    if (integrity is not None or crossorigin is not None or referrerpolicy is not None):
      raise Exception("integrity, crossorigin and referrerpolicy must be all set or None")
    if len(url) > 95:
      htmlFile.write("\n" + tabs + "\t")
    else:
      htmlFile.write(" ")
    htmlFile.write("rel=\"stylesheet\" />\n")
    return
  tabs += "\t"
  htmlFile.write("\n" + tabs + "integrity=\"" + integrity + "\"\n")
  htmlFile.write(tabs + "rel=\"stylesheet\" crossorigin=\"" + crossorigin + "\" referrerpolicy=\"" + referrerpolicy + "\" />\n")

def addGoogleFont(htmlFile, indentDepth, name):
  tabs = getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n")
  htmlFile.write(tabs + "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n")
  htmlFile.write(tabs + "<link href=\"https://fonts.googleapis.com/css2" + name +"\" rel=\"stylesheet\">\n")
	
def getIndentedTab(indentDepth):
  if (type(indentDepth) != int):
    raise Exception("indentDepth is not an int type for argument " + str(indentDepth))
  if (indentDepth < 0):
    raise Exception("indentDepth < 0 for argument " + str(indentDepth))
  if (indentDepth == 0):
    raise Exception("I do not really think you want indentDepth == 0")
  if (indentDepth > 50):
    raise Exception("Do you really need that much indentation?")
  ans=""; 
  for i in range(indentDepth):
    ans += "\t"
  return ans;

backupAndGenerateNewHtmlOutputFile()