from bs4 import BeautifulSoup 
import string
import requests

# Input: url to get html of
# Output: html
def get_html(url):
    html = requests.get(url).text
    return BeautifulSoup(html, "html.parser")

ROOT_ENCYCLOPEDIA_URL = 'https://medlineplus.gov/ency/encyclopedia_{}.htm'
def scrape_encyclopedia_pages():
    # Let's iterate over all the letters in the alphabet
    for letter in string.ascii_uppercase:
        # Let's get the HTML for the page
        encyclopedia_page_url = ROOT_ENCYCLOPEDIA_URL.format(letter)
        encyclopedia_page_soup = get_html(encyclopedia_page_url)

        # Let's get every single link in "index"
        for(soup.find_all("section .item"))


if __name__ == '__main__':
    scrape_encyclopedia_pages()