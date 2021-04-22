
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time
import sys
import re
import csv 
from datetime import datetime

import secrets 

#from ques_db import ques_db, Table 


#Login to Quora
def login(params):
    email = params['account'] 
    passy = params['password'] 
    print("Logging in...")
    driver.get("http://quora.com")

    email_css = "#email" 
    password_css = "#password"
    button_css = "button[type='button']"

    driver.find_element_by_css_selector(email_css).send_keys(email)
    driver.find_element_by_css_selector(password_css).send_keys(passy)
    time.sleep(2)
    driver.find_element_by_css_selector(button_css).click()
    time.sleep(2)
    # LOGIN FINISHED


def get_texts(web_element): 
    # return text from web_element, or, if empty, return None 
    return ([e.text for e in web_element] or [None])

def extract_date(ask_date):
    if not re.search('[0-9]{4}', ask_date):
        ask_date += ', ' + str(datetime.now().year)
    return datetime.strptime(ask_date, 'Asked %b %d, %Y').strftime('%Y-%m-%d')

def scrape_questions(scrolls, keyword):

    search_box = driver.find_element(By.CSS_SELECTOR, ".q-input")
    
    for _ in range(25): search_box.send_keys(Keys.BACK_SPACE)
    time.sleep(1)
    search_box.send_keys(keyword)
    time.sleep(1)
    search_box.send_keys(Keys.ENTER)

    body = driver.find_element_by_css_selector('body')
    for _ in range(scrolls): 
        try: 
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        except: 
            print('scrolling failed')
            break 
        
    questions = []
    for listing in driver.find_elements(By.CSS_SELECTOR, 'span[style*="background: none;"]'):
        questions.append(listing.text)
    return questions

def quora_scraper(TOPIC, LIMIT):
    # scrape quora for TOPIC related questions
    driver = webdriver.Chrome(ChromeDriverManager().install())
    params = secrets.quora_accounts['ggunthy']
    login(params)
    search_term = "topic:" + TOPIC 
    scrapes = scrape_questions(LIMIT, search_term)
    return scrapes 



if __name__ == '__main__':

<<<<<<< HEAD

    driver = webdriver.Chrome(ChromeDriverManager().install())
    params = secrets.quora_accounts['ggunthy']
    login(params)
    #scrolls, keyword = int(sys.argv[1]), sys.argv[2]
    keywords = []
    with open("data/4000_most_frequent_words.csv", "r") as file: 
=======
    accounts = {
        'alexgodbout':
            {'account':     'alexgodbout@gmail.com'
            ,'password':    'Mmlja5ja5ja%'}
        ,'ggunthy':
            {'account': 'ggunthy@gmail.com '
            ,'password': 'Zcaaddaa55'}
    } #TODO create permissions file and add to git.ignore
    #secrets.quora_accounts['ggunthy']
    driver = webdriver.Chrome(ChromeDriverManager().install())
    params = accounts['ggunthy']
    login(params)
    #scrolls, keyword = int(sys.argv[1]), sys.argv[2]

    keywords = []
    with open("4000_most_frequent_words.csv", "r") as file: 
>>>>>>> f3bac17... created the bot
        spamreader = csv.reader(file, delimiter=' ', quotechar='|')
        for row in spamreader:
            keywords = keywords + row

<<<<<<< HEAD
    counter = 0
    for keyword in keywords:
        print(keyword)     
        counter += 1
        if counter < 3090: continue
        topic = "topic:" + keyword   
        scrapes = scrape_questions(100, topic)
        with open("quora_scrape_2.txt", "a+") as file: 
=======
    for keyword in keywords:
        print(keyword)     
        topic = "topic:" + keyword   
        scrapes = scrape_questions(100, topic)
        with open("quora_scrape_1.txt", "a+") as file: 
>>>>>>> f3bac17... created the bot
            for scrape in scrapes: 
                file.write(scrape + '\n')



    #db = ques_db()
    #db.insert(Table('benchmarks'), stats)


