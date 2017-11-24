##this version has SQLite

from bs4 import BeautifulSoup as soup
import urllib2
import requests
import sqlite3

# Let's connect SQLite and initialize json
conn = sqlite3.connect('example.db')
# result = '['

# opening up connection, grabs page
my_url = 'https://medlineplus.gov/all_healthtopics.html'
uClient = urllib2.urlopen(my_url)
page_html = uClient.read()
uClient.close()

#HTML parsing
page_soup = soup(page_html, "html.parser")

#Grabs each section
sections = page_soup.findAll("div", {"class": "section"})

filename = "medline_diseases.csv"
f = open(filename, "w")

headers = "disease, disease_url, summary\n"

f.write(headers)

#Grabs each name and link under each section
for section in sections:
	topics = section.findAll("a")
	for topic in topics:
		disease = topic.text
		disease_url = topic['href']
		# or write a function for getting the soup of the disease_url
		disClient = urllib2.urlopen(disease_url)
		dis_html = disClient.read()
		disClient.close()
		dis_soup = soup(dis_html, "html.parser")
		summary_container = dis_soup.findAll("div", {"id": "topic-summary"})
		summary = summary_container[0].p.text

	# print("disease: " + disease)
	# print("disease_url: " + disease_url)
	# print("summary: " + summary)

	f.write(disease + "," + disease_url + "," + summary.replace(",", ";") + "\n")

f.close()

#Add into json file

# 	Function for getting soup of second URL
# 	def get_html(url):
# 	page_html = urllib2.urlopen(url)
# 	return BeautifulSoup(html_content, "html.parser")

# 	response += '{ "name": "'+disease+'", "url": "'+disease_url+'", "summary": "'+summary+'"},'

# response+= ']'

# print response 