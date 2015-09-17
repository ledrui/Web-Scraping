form urlib.request import urlopen 
html = urlopen("https://www.facebook.com/faceiliass")
print html.read()