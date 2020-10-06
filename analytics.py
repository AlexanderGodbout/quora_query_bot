# get Q stats 



from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re


#Login to Quora
def login():
    email="alexgodbout@gmail.com"
    passy="Mmlja5ja5ja%"
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

    time.sleep(2)
    driver.find_element_by_css_selector(email_css).send_keys(email)
    driver.find_element_by_css_selector(password_css).send_keys(passy)
    time.sleep(2)
    driver.find_element_by_css_selector(button_css).click()
    time.sleep(2)
    # LOGIN FINISHED


driver = webdriver.Chrome('/Users/alexandergodbout/Downloads/chromedriver')

login()
driver.find_element(By.CSS_SELECTOR, ".q-relative > .q-inlineFlex .q-box:nth-child(3)").click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/a[1]').click()

body = driver.find_element_by_css_selector('body')
while True: 
    try: 
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
    except: 
        break 

    comment = '''                                       
    if "NCBI BLAST algorithm" in driver.find_element_by_tag_name('div').text: 
        print("the End")
        break 

    for element in driver.find_elements(By.CSS_SELECTOR, ".ui_qtext_rendered_qtext"): 
        if "NCBI BLAST algorithm" in element.text: 
            print("The Very End")
            break 
    '''



try: 
    earnings = driver.find_elements(By.CSS_SELECTOR, ".earnings_amount")
    print('earnings')
    print([earn.text for earn in earnings])
except: 
    pass 

try: 
    questions = driver.find_elements(By.CSS_SELECTOR, ".ui_qtext_rendered_qtext")
    print('questions')
    print([ques.text for ques in questions])
except:  
    pass 

try: 
    ask_dates = driver.find_elements(By.CSS_SELECTOR, ".ask_date")
    print('ask_dates')
    print([ask.text for ask in ask_dates]) 
except: 
    pass

try: 
    answer_count = driver.find_elements(By.CSS_SELECTOR, ".answer_count")
    print('answer_count') 
    print([ans.text for ans in answer_count])
except: 
    pass 

try: 
    request_count = driver.find_elements(By.XPATH, "//*[contains(@id,'total_request_count')]")
    print('request_count') 
    print([req.text for req in request_count])
except: 
    pass 


try: 
    labels = driver.find_elements(By.CSS_SELECTOR, ".label")
    print('labels') 
    print([lab.text for lab in labels])
except: 
    pass 

try: 
    infos = driver.find_elements(By.CSS_SELECTOR, ".info")
    print('infos') 
    print([info.text for info in infos])
except: 
    pass 
