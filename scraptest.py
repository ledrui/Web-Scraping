#!scrapEnv/bin/python3
from urllib.request import urlopen 
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		print('HTTPError')
		return None

	try:
		bsObj = BeautifulSoup(html.read()) 
		title = bsObj.body.h1
	except AttributError as e:
		print('AttributError')
		return None

	return title

title = getTitle("http://unfoldingmaps.org/exhibition/index.html")

if title == None:
	print("Title could not be found")
else:
	print(title)