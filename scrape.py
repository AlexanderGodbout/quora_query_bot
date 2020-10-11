# new file

import csv
import time 
import random 

import ques_db 
import scrapers 


def get_subreddits(): 
    # get list of all public subreddits as of 2018 
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
        'reddit': 30 
        ,'youtube': 900/15 
        ,'twitter': 50000/(24*60) 
    }
    return [post for post in dispatch_scraper[WEBSITE](get_limit[WEBSITE], TOPIC) if '?' in post]
    

if __name__ == "__main__":

    db = ques_db.ques_db() 
    while True: 
        records = []
        start = time.time()
        while time.time() - start > 60*60: 
            params= {
                'topic': random.choice(get_subreddits()) 
                ,'website': 'reddit' #random.choice(['reddit', 'youtube', 'twitter'])
                ,'version': '0.0.0.0.0'
            }
            question = scrape_questions(params['website'], params['topic'])
            records.append(params | {'question': question})
        db.insert(records, 'scrapes')
     
    




       
        





