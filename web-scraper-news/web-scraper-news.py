import json
import requests
import pandas as pd
import time
import schedule
from bs4 import BeautifulSoup
import csv

def news_info():
    url = 'https://novini.bg'
    request = requests.get('https://novini.bg')
    soup = BeautifulSoup(request.text, 'html.parser')
    articles = soup.find_all('article', class_= 'g-grid__item js-content')
    art = []
    for article in articles:
        article_link = article.a.get('href')
        article_title = article.find('h2', {'class', 'g-grid__item-title'}).text
        article_date = article.find('p', class_ = 'g-grid__item--time')
        article_date = article_date.text if article_date else None

        art.append({
            'Headline': article_title,
            'Link': article_link,
            'Date Published': article_date
        })
    df = pd.DataFrame(art)
    df.to_csv('News_Bulgaria.csv', index=False)


    csvfile = open('News_Bulgaria.csv', 'r')
    jsonfile = open('file.json', 'w')

    fieldnames = ("Headline","Link","Date Posted")
    reader = csv.DictReader( csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

news_info()

schedule.every().day.at("10:30").do(news_info)

while True:
    schedule.run_pending()
    time.sleep(1)


