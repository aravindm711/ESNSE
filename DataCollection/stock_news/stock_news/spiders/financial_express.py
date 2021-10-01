import bs4
from bs4 import BeautifulSoup as soup
import urllib.request as urllib2
import re
import json

def pageOpener(url):
    response = urllib2.urlopen(url)
    page_html = response.read()
    return soup(page_html,"html.parser")

def contentScraper(url):
    page_soup = pageOpener(url)
    content = ""
    div_content = page_soup.find('div', {"class":"post-summary"})
    for data in div_content.find_all('p'):
        content += re.sub(' +', " ",data.text.strip())
    return content

if __name__ == "__main__":
    next_page = "https://www.financialexpress.com/market/"
    f = open("financialexpress.json", "a")

    while next_page != None:
        page_soup = pageOpener(next_page)
        rows = page_soup.find_all('div',{"class" : "listitembx"})    
        f.write('[\n')
        for row in rows:
            f.write(json.dumps({
                "title": row.h3.text,
                "link" : row.h3.a['href'],
                "date" : row.find('span',{"class" : "minsago"}).text,
                "gist" : row.h4.text,
                "content" : contentScraper(row.h3.a['href']),
            })+",\n")
        try:
            next_page = page_soup.find('a', {"class" : "next page-numbers"})['href']
        except:
            next_page = None
        print(next_page)
    f.write(']')  
    f.close() 
