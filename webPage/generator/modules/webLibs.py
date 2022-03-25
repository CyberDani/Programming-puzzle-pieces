from modules import htmlBuilder

def addFontAwesome_v611(htmlFile, indentDepth):
  htmlBuilder.addCssLinkHrefToHtmlOutputFile(htmlFile, indentDepth, 
                    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
					"sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==",
					"anonymous", "no-referrer")
  htmlBuilder.addJsScriptSrcToHtmlOutputFile(htmlFile, indentDepth, 
                    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/js/all.min.js",
					"sha512-6PM0qYu5KExuNcKt5bURAoT6KCThUmHRewN3zUFNaoI6Di7XJPTMoT6K0nsagZKk2OB4L7E3q1uQKHNHd4stIQ==",
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