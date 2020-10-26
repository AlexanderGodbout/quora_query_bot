# get Q stats 



from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time
import re



#Login to Quora
def login(params):
    email = params['account'] 
    passy = params['password'] 
    print("Logging in...")
    driver.get("http://quora.com")

    # Create Soup Object and find all form_column classes
    forms = BeautifulSoup(driver.page_source, "lxml").find_all(class_="form_column")

    # Iterate through forms
    # Find polymorphic id string,append a hashtag(#) to create css_selector
    for form in forms:
        try:
            # This is for email/password entry box
            data = form.find("input")["name"]
            if data == "email":
                email_css = "#" + form.find("input")["id"]
            if data == "password":
                password_css = "#" + form.find("input")["id"]
        except:
            pass

        try:
            # This is for the Login Button
            data = form.find("input")["value"]
            if data == "Login":
                button_css = "#" + form.find("input")["id"]
        except:
            pass

    driver.find_element_by_css_selector(email_css).send_keys(email)
    driver.find_element_by_css_selector(password_css).send_keys(passy)
    time.sleep(2)
    driver.find_element_by_css_selector(button_css).click()
    time.sleep(2)
    # LOGIN FINISHED


def get_texts(web_element): 
    return [e.text for e in web_element]


def scrape_stats(scrolls): 

    driver.find_element(By.CSS_SELECTOR, ".q-relative > .q-inlineFlex .q-box:nth-child(3)").click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/a[1]').click()

    body = driver.find_element_by_css_selector('body')
    for _ in range(scrolls): 
        try: 
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        except: 
            print('scrolling failed')
            break 

    topic_lists = []
    try: 
        for element in driver.find_elements(By.CSS_SELECTOR, ".TopicList"):
            topic_list = get_texts(element.find_elements(By.CSS_SELECTOR, ".TopicName"))
            topic_lists.append(topic_list)

    except: 
        print('scraping failed')


    try: 
        earnings = get_texts(driver.find_elements(By.CSS_SELECTOR, ".earnings_amount"))
        questions = get_texts(driver.find_elements(By.CSS_SELECTOR, ".ui_qtext_rendered_qtext"))
        ask_dates = get_texts(driver.find_elements(By.CSS_SELECTOR, ".ask_date"))
        answer_counts = get_texts(driver.find_elements(By.CSS_SELECTOR, ".answer_count"))
        request_counts = get_texts(driver.find_elements(By.XPATH, "//*[contains(@id,'total_request_count')]"))
        labels = get_texts(driver.find_elements(By.CSS_SELECTOR, ".label"))
        infos = get_texts(driver.find_elements(By.CSS_SELECTOR, ".info"))
    except: 
        print('scraping failed')
    

    extra_stats  = {
        'FOLLOWER': []
        ,'VIEWS': []
        ,'AD IMPRESSIONS': []
        ,'TRAFFIC SOURCES': []
        ,'QUESTION EARNINGS': []
        ,'REQUEST EARNINGS': []
    }


    for label, info in zip(labels[5:], infos[1:]): 
        print(label, info)
        if label in extra_stats: extra_stats[label].append(info)
        

    stats = []
    print(topic_lists)

    min_len = min([len(L) for L in [earnings, questions, ask_dates, answer_counts, request_counts]])
    for i in range(min_len):
        stat = {
            'earning': earnings[i]
            ,'question': questions[i]
            ,'ask_date': ask_dates[i]
            ,'topics': str(topic_lists[i])
            ,'answer_count': answer_counts[i]
            ,'request_count': request_counts[i]
            ,'followers': extra_stats['FOLLOWER'][i]
            ,'views': extra_stats['VIEWS'][i]
            ,'ad_impressions': extra_stats['AD IMPRESSIONS'][i]
            ,'traffic_sources': extra_stats['TRAFFIC SOURCES'][i]
            ,'question_earnings': extra_stats['QUESTION EARNINGS'][i]
            ,'request_earnings': extra_stats['REQUEST EARNINGS'][i]
        }


        stats.append(stat)
    return stats 



if __name__ == '__main__':

    accounts = {
        'alexgodbout':
            {'account':     'alexgodbout@gmail.com'
            ,'password':    'Mmlja5ja5ja%'}
        ,'ggunthy':
            {'account': 'ggunth@gmail.com'
            ,'password': 'zcaaddaadd'}
    } #TODO create permissions file and add to git.ignore

    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    params = accounts['alexgodbout']
    login(params)
    stats = scrape_stats(10)
    print(stats)

    

    for stat in stats: 
        pass 


        comment = ''' 

        if table == 'benchmarks': 
            self.desc =  {
                'id':               'INT NOT NULL'
                ,'topics':          'VARCHAR(255)'
                ,'answers':         'INT'
                ,'followers':       'INT'
                ,'views':           'INT'
                ,'ad_impressions':  'INT'
                ,'ques_earn':       'DECIMAL(12, 2)'
                ,'req_earn':        'DECIMAL(12, 2)'
                ,'tot_earn':        'DECIMAL(12, 2)'
                ,'version':         'VARCHAR(255)'
                ,'timestamp':       'TIMESTAMP DEFAULT CURRENT_TIMESTAMP'
            }


            'earning': earnings[i]
            ,'question': questions[i]
            ,'ask_date': ask_dates[i]
            ,'answer_count': answer_counts[i]
            ,'request_count': request_counts[i]
            ,'followers': extra_stats['FOLLOWER'][i]
            ,'views': extra_stats['VIEWS'][i]
            ,'ad_impressions': extra_stats['AD IMPRESSIONS'][i]
            ,'traffic_sources': extra_stats['TRAFFIC SOURCES'][i]
            ,'question_earnings': extra_stats['QUESTION EARNINGS'][i]
            ,'request_earnings': extra_stats['REQUEST EARNINGS'][i]



            scrape_id
            post_id 
            

            ''' 