#! usr/bin/env python3

import sys 
import os
import labelers, scrapers
from datetime import datetime

def generate_record(candidate):
    # generates a candidate record by combining labels 
    return {
                "text": candidate
                ,"is_grammatical": labelers.label_grammatical(candidate)
                ,"is_unique": labelers.label_uniqueness(candidate)
                ,"is_viral": labelers.label_virality(candidate)
                ,"is_obsessional": labelers.label_obsessionality(candidate)
                ,'is_accepted': None 
                ,'source': None
                ,'earnings': None 
                ,'views': None
                ,'ad_impressions': None
                ,'answers': None
                ,'external_traffic': None
                ,'internal_traffic': None 
                ,'create_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ,'update_date': None 
                ,'build': 1.0
            }

def insert_into_db(data: dict, cred: dict):
    # Inserts in data record into MySQL location provided by table
    query =  'INSERT INTO '+ cred['table'] \
        +'('+ str(list(data.keys())).strip("[]").replace("'","") + ')' \
        + ' VALUES (' + str(list(data.values())).strip('[]') + ')'
    query = query.replace('None','NULL')
    #os.system
    #print('mysql -u {} -p{} -h {} {} -e "{}"'.format(
                #cred['u'], cred['p'], cred['h'], cred['db'], query))

  
def get_user_evaluation(q):
    # Uses CLI to collect user acceptance information
    if q["is_grammatical"] and q["is_unique"] and q["is_viral"] and q["is_obsessional"]:
        print(q['text'])
        if input() == 'y':  
            return 1 
    return 0 


def scrape_questions(LIMIT, WEBSITE, TOPIC):
    # filter scraper output for only questions
    return [post for post in dispatch_scraper(WEBSITE)(TOPIC, LIMIT) if '?' in post]
    

def dispatch_scraper(WEBSITE):
    dispatcher ={
        'reddit': scrapers.scrape_reddit
        ,'twitter': scrapers.scrape_twitter
        ,'youtube': scrapers.scrape_youtube
    }
    return dispatcher[WEBSITE]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('usage: collect.py Limit Website Topic \n (e.g. collect.py 40 reddit nlp)')
        sys.exit()

    for question in scrape_questions(int(sys.argv[1]), sys.argv[2], sys.argv[3]): 
        q = generate_record(question) 
        q["is_accepted"] = get_user_evaluation(q)
        insert_into_db(q, {'u': 'scopesdbu','p': 'mmlja5ja5ja%','h': 'mysql.queryquarry.tech',
                        'db': 'quora_query_db', 'table': 'Questions'})


   

  

