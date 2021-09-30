from bs4 import BeautifulSoup
import requests 
from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://www.economictimes.indiatimes.com/markets/stocks/news")

news_titles = {}
news_titles_count = 0

tag_dup = []

page_break = -10

while len(tag_dup)<=2508 and len(tag_dup)>=page_break:
    source = driver.page_source
    soup = BeautifulSoup(source,'html.parser')
    tags = soup.find_all('div',{'class':'eachStory'})
    try:
        new_tags = set(tags).difference(tag_dup)
    except:
        new_tags = tags

    tag_dup = []

    for tag_du in tags:
        tag_dup.append(tag_du)

    page_break+=1

    for tag in new_tags:
        title = tag.find('h3').text
        address = tag.find('a').get('href')
        link = f'https://www.economictimes.indiatimes.com{address}'
        news_titles_count+=1
        news_titles[news_titles_count] = [title,link]
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    next_page = driver.find_elements_by_class_name('autoload_continue')
    driver.execute_script("$(arguments[0]).click();", next_page)
    time.sleep(0.5)
    print('\n\n-----\n')
    print(len(tag_dup))
    print('\n\n-----\n')

title_df = pd.DataFrame.from_dict(news_titles,orient='index',columns=['Title','Link'])
print(len(title_df))
title_df.drop_duplicates(subset ="Link", keep = False, inplace = True)
print(len(title_df))

links = '\n'.join(list(title_df['Link']))

f = open("links.txt", "w")
f.write(links)
f.close()
    
