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
	return (page_soup)