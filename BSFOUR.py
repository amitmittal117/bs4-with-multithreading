import bs4
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def retriever_data(my_url,tag_name,tag_var,tag_value):
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	data = page_soup.findAll(tag_name,{tag_var:tag_value})
	return (data)

def retriever_soup(my_url):
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")
	# print(page_soup)
	return (page_soup)

# print(retriever_soup("http://www.google.com"))

print (retriever_data("http://s4.bitdownload.ir/Game/PC.Game/","table","id","list")) #good Gaming Site