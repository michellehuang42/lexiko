##this version has SQLite

from bs4 import BeautifulSoup 
import urllib2
import requests
import sqlite3

conn = sqlite3.connect('example.db')


response = ''

def match_class(target):
	def do_match(tag):
		classes = tag.get('class', [])
		return all(c in classes for c in target)
	return do_match

def get_html(url):
	html_content = urllib2.urlopen(url)
	return BeautifulSoup(html_content, "html.parser")

letter='A'
search_url = 'https://medlineplus.gov/ency/encyclopedia_'+letter+'.htm'
# https://medlineplus.gov/ency/encyclopedia_0-9.htm

page_url = ''
response = '['

for link in get_html(search_url).find("ul",{"id":""}).findAll("a"):
	disease_url = "https://medlineplus.gov/ency/"+link['href']
	disease = link.getText()
	opendurl = get_html(disease_url)

	summary = opendurl.find("div",{"id":"ency_summary"}).getText()
	
	causes = opendurl.findAll(if("div", {"class": "section-title"}).getText()=="Causes"):
		#print description under "causes"
	
	print response

	break

	response += '{ "name": "'+disease+'", "url": "'+disease_url+'", "summary": "'+summary+'"},'

	print response

response+= ']'

print response