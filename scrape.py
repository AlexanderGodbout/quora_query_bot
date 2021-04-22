# new file

import csv
import time 
import random 
import sys

from ques_db import ques_db, Table
import scrapers

def get_topics(WEBSITE): 
    dispatch_path = {
        'reddit':   "./data/subreddits_public_list.csv"
        ,'twitter': "./data/4000_most_frequent_words.csv"
        ,'youtube': "./data/4000_most_frequent_words.csv"
        ,'quora':   "./data/4000_most_frequent_words.csv"
    }
    with open(dispatch_path[WEBSITE], newline='\n') as file: 
        rows = csv.reader(file, delimiter=',')
        topics = []
        for row in rows:
            topics = topics + row
    return topics

def get_topics(WEBSITE): 
    dispatch_path = {
        'reddit':   "./data/subreddits_public.csv"
        ,'twitter': "./data/4000_most_frequent_words.csv"
        ,'youtube': "./data/4000_most_frequent_words.csv"
        ,'quora':   "./data/4000_most_frequent_words.csv"
    }
    with open(dispatch_path[WEBSITE], newline='\n') as file: 
        rows = csv.reader(file, delimiter=',')
        topics = []
        for row in rows:
            topics = topics + row
    return topics


def scrape_questions(WEBSITE, TOPIC):
    # dispatch scraper and output only questions 
    dispatch_scraper ={
        'reddit': scrapers.scrape_reddit
        ,'twitter': scrapers.scrape_twitter
        ,'youtube': scrapers.scrape_youtube
        ,'quora': scrapers.scrape_quora
    }
    get_limit = { #requests per minute
        'reddit': 25
        ,'youtube': 900/15 
        ,'twitter': 50000/(24*60) 
        ,'quora': 50
    }
    return [post for post in dispatch_scraper[WEBSITE](TOPIC, get_limit[WEBSITE]) if '?' in post]
    


if __name__ == "__main__":

<<<<<<< HEAD
    WEBSITE = 'quora'
=======
    website = 'reddit'
>>>>>>> f3bac17... created the bot
    db = ques_db() 
    while True: 
        records = []
        start = time.time()
        while time.time() - start <60: 
            params= {
<<<<<<< HEAD
                'topic': random.choice(get_topics(WEBSITE)) 
                ,'website': WEBSITE #random.choice(['reddit', 'youtube', 'twitter'])
=======
                'topic': random.choice(get_subreddits()) 
                ,'website': website #random.choice(['reddit', 'youtube', 'twitter'])
>>>>>>> f3bac17... created the bot
                ,'version': '0.0.0.0'
            }
            try: 
                questions = scrape_questions(params['website'], params['topic'])
                for question in questions: 
                    sys.stdout.write(question)
                    record = {**params, **{'question': question, 'timestamp':'Now()'}}
                    records.append(record)
            except: 
                print('received 404 HTTP response')
        if records: db.insert(Table('scrapes'), records) 
     
    




       
        





