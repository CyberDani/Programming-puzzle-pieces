from modules import htmlBuilder

def addFontAwesome(htmlFile, indentDepth):
  htmlBuilder.addCssLinkHrefToHtmlOutputFile(htmlFile, indentDepth, 
                    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
					"sha512-1ycn6IcaQQ40/MKBW2W4Rhis/DbILU74C1vSrLJxCq57o941Ym01SwNsOMqvEBFlcgUa6xLiPY/NS5R+E6ztJQ==",
					"anonymous", "no-referrer")
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, indentDepth, 
                    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/js/all.min.js",
					"sha512-Tn2m0TIpgVyTzzvmxLNuqbSJH3JP8jm+Cy3hvHrW7ndTDcJ1w5mBiksqDBb8GpE2ksktFvDB/ykZ0mDpsZj20w==",
					"anonymous", "no-referrer")

def addJquery(htmlFile, indentDepth):
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, indentDepth, 
                    "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js",
					"sha512-894YE6QWD5I59HgZOGReFYm4dnWc1Qt5NtvYSaNcOP+u1T9qYdvdihz0PPSiiqn/+/3e7Jo4EaG7TubfWGUrMQ==",
					"anonymous", "no-referrer")

def addMaterialize(htmlFile, indentDepth):
  htmlBuilder.addCssLinkHrefToHtmlOutputFile(htmlFile, indentDepth, 
					"https://cdn.jsdelivr.net/npm/@materializecss/materialize@1.1.0-alpha/dist/css/materialize.min.css")
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, indentDepth, 
					"https://cdn.jsdelivr.net/npm/@materializecss/materialize@1.1.0-alpha/dist/js/materialize.min.js")

def addGoogleIcons(htmlFile, indentDepth):
  htmlBuilder.addCssLinkHrefToHtmlOutputFile(htmlFile, indentDepth, "https://fonts.googleapis.com/icon?family=Material+Icons")

def addJQueryLoadingOverlay(htmlFile, indentDepth):
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, indentDepth, 
                    "https://cdn.jsdelivr.net/npm/gasparesganga-jquery-loading-overlay@2.1.7/dist/loadingoverlay.min.js")

def addGoogleFont(htmlFile, indentDepth, name):
  tabs = htmlBuilder.getIndentedTab(indentDepth)
  htmlFile.write(tabs + "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n")
  htmlFile.write(tabs + "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n")
  htmlFile.write(tabs + "<link href=\"https://fonts.googleapis.com/css2" + name +"\" rel=\"stylesheet\">\n")