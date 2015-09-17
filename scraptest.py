from urllib.request import urlopen 
from bs4 import BeautifulSoup

html = urlopen("http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world")
bsObj = BeautifulSoup(html.read())
print (bsObj.h1)