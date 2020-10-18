# new file

import csv
import time 
import random 

from ques_db import ques_db, Table
import scrapers


def get_subreddits(): 
    # get public subreddits (source: https://www.kaggle.com/rayraegah/subreddits/data)
    with open('./data/subreddits_public.csv', newline='\n') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        subreddits = []
        for row in rows: 
            if len(row)==5: subreddits.append(row[3])
    return subreddits 


def scrape_questions(WEBSITE, TOPIC):
    # dispatch scraper and output only questions 
    dispatch_scraper ={
        'reddit': scrapers.scrape_reddit
        ,'twitter': scrapers.scrape_twitter
        ,'youtube': scrapers.scrape_youtube
    }
    get_limit = { #requests per minute
        'reddit': 25
        ,'youtube': 900/15 
        ,'twitter': 50000/(24*60) 
    }
    return [post for post in dispatch_scraper[WEBSITE](TOPIC, get_limit[WEBSITE]) if '?' in post]
    

if __name__ == "__main__":

    db = ques_db() 
    while True: 
        records = []
        start = time.time()
        while time.time() - start <60: 
            params= {
                'topic': random.choice(get_subreddits()) 
                ,'website': 'reddit' #random.choice(['reddit', 'youtube', 'twitter'])
                ,'version': '0.0.0.0.0'
            }
            try: 
                questions = scrape_questions(params['website'], params['topic'])
                for question in questions: 
                    print(question)
                    record = {**params, **{'question': question, 'timestamp':'Now()'}}
                    records.append(record)
            except: 
                print('received 404 HTTP response')
        db.insert(Table('scrapes'), records) 
     
    




       
        





