import json
import requests
import logging
import time
import schedule
from bs4 import BeautifulSoup
from datetime import datetime


class Index:
    def __init__(self, index_fl): 
        self.index_fl = index_fl
        self.index_content = self.read()

    def save(self):
        with open(self.index_fl, "w") as fh:  
            json.dump(self.index_content, fh)

    def read(self):
        try:
            with open(self.index_fl, 'r') as fh:  
                return json.load(fh) 
        except FileNotFoundError: 
            logging.warning('Index file does not exist. Will proceed with empty index')  
            return {} 
    
    def add(self, val):
        if val in self.index_content:  
            return False
        
        self.index_content[val] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        return True


def run():
    
    url = 'https://novini.bg'
    index = Index('scraper_index.json') 

    logging.info('Start of downloading!') 
    download_fl_name = 'articles_download_{date}.json'.format(date=datetime.now().strftime("%Y%m%d%H%M%S"))

    request = requests.get(url) 
    soup = BeautifulSoup(request.text, 'html.parser')
    articles = soup.find_all('article', class_= 'g-grid__item js-content')
    art = []

    for article in articles:
        article_link = article.a.get('href')
        article_title = article.find('h2', {'class', 'g-grid__item-title'}).text
        
        
        if not index.add(article_link):  

            logging.info('This link has already been downloaded. Skipping!')
            continue

        art.append({
            'Headline': article_title,
            'Link': article_link,
        })

    if not art:   
        logging.info('No new article was found.')
        return
    
    with open(f'/Users/gginchev/Downloads/Desktop - 21-10-2022/downloaded_news/{download_fl_name}', 'w') as fh: 
        json.dump(art, fh)
    
    index.save() 
    logging.info('End of downloading!') 
    
schedule.every().day.at("11:44").do(run)


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG) 
    while True:
        schedule.run_pending()
        time.sleep(10)