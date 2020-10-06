#all cats are yellow
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re

# Source: https://www.blackhatworld.com/seo/quora-bot-source-code.949582/


#Read File ,strip new lines ,return question list
def readFile():
    filey = "questions.txt"
    with open(filey, "r") as f:
        q = f.readlines()
    qlist = [x.strip() for x in q]
    # qlist=reversed(qlist) #Will reverse the question list if needed
    print(len(qlist), "Total Questions Loaded")
    return qlist

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

    driver.find_element_by_css_selector(email_css).send_keys(email)
    driver.find_element_by_css_selector(password_css).send_keys(passy)
    time.sleep(2)
    driver.find_element_by_css_selector(button_css).click()
    time.sleep(2)
    # LOGIN FINISHED




if __name__ == '__main__':

    #Create Question List
    qlist = readFile()

    #Create Webdriver Vroom Vroom
    driver = webdriver.Chrome('/Users/alexandergodbout/Downloads/chromedriver')

    login()

    # Iterate through qlist ask questions till no more
    for question in qlist:
        print(question)

        driver.find_element(By.CSS_SELECTOR, ".qu-color--white > .q-text").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".q-text-area").send_keys(question)
        time.sleep(2) 
        #driver.find_element(By.CSS_SELECTOR, ".q-box:nth-child(2) > .q-click-wrapper > .q-flex > .q-text > .q-text").click()
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/button/div/div/div').click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div/div[2]/div/div/div[3]/div/div[2]/button/div/div/div').click()

    
    

    

    
    comment = ''' 


        //*[@id="root"]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/button/div/div/div

   #root > div > div:nth-child(1) > div > div > div > div > div.q-flex.modal_content_inner.qu-flexDirection--column.qu-bg--white.qu-overflowY--auto.qu-borderAll.qu-alignSelf--center > div > div > div.q-flex.qu-bg--gray_ultralight.qu-borderTop > div > div.q-box.puppeteer_test_modal_primary_button > button > div > div > div
//*[@id="root"]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/button/div/div/div
/html/body/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/button/div/div/div

        <div class="q-box puppeteer_test_modal_primary_button" style="box-sizing: border-box; direction: ltr;"><button class="q-click-wrapper qu-active--textDecoration--none qu-focus--textDecoration--none base___StyledClickWrapper-lx6eke-1 kNZJaj   qu-borderRadius--pill qu-alignItems--center qu-justifyContent--center qu-whiteSpace--nowrap qu-userSelect--none qu-display--inline-flex qu-bg--blue qu-tapHighlight--white qu-textAlign--center qu-cursor--pointer qu-hover--textDecoration--none" type="button" tabindex="0" role="button" style="box-sizing: border-box; direction: ltr; font: inherit; outline: none; padding: 7px 20px; border-width: 0px; color: inherit;"><div class="q-flex qu-alignItems--center qu-justifyContent--center" style="box-sizing: border-box; direction: ltr; display: flex; max-width: 100%;"><div class="q-text qu-display--inline-flex qu-alignItems--center qu-overflow--hidden puppeteer_test_button_text qu-medium qu-color--white" style="box-sizing: border-box; direction: ltr; font-size: 14px;"><div class="q-text qu-ellipsis qu-whiteSpace--nowrap" style="box-sizing: border-box; direction: ltr;">Add new question</div></div></div></button></div>

    try: 
        driver.find_element(By.CSS_SELECTOR, ".q-box:nth-child(2) > .q-click-wrapper > .q-flex > .q-text > .q-text").click()
        time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, ".q-flex:nth-child(3) .q-box:nth-child(2) .q-text > .q-text").click()
        time.sleep(10)

    except: 
        print("Question was not already asked.")

    try: 
        driver.find_element(By.CSS_SELECTOR, ".q-box:nth-child(2) > .q-click-wrapper > .q-flex > .q-text > .q-text").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".q-flex:nth-child(3) .q-box:nth-child(2) .q-text > .q-text").click()
        time.sleep(5)
    except: 
        print("No exception given.")
    

    try: 
        driver.find_element(By.CSS_SELECTOR, ".q-box:nth-child(2) > .q-click-wrapper > .q-flex > .q-text > .q-text").click()
        driver.find_element(By.CSS_SELECTOR, ".q-flex:nth-child(3) .q-box:nth-child(1) .q-text > .q-text").click()
    except: 
        print("No changes necessary.")


    try: 
        driver.switchTo().alert().accept()
    except: 
        print("Not able to accept.")


    try: 
        driver.switchTo().alert().accept()
    except: 
        print("Not able to accept x2.")
    '''


    comment = ''' 
    try:
        print(question)
        driver.get("http://quora.com")
        soup=BeautifulSoup(driver.page_source,"lxml")

        # Find all text areas
        blox = soup.find_all("textarea")

        # Find polymorphic id string for Ask Question entry field
        for x in blox:
            try:
                placeholder = x["placeholder"]
                if placeholder.__contains__("Ask or Search Quora"): # Fix this later
                    askbar_css = "#" + x["id"]
                    print(askbar_css)
            except:
                pass


        askbutton = "#" + soup.find(class_="AskQuestionButton")["id"]# Fix this later

        # Type out Question
        driver.find_element_by_css_selector(askbar_css).send_keys(question)

        # Wait for askbutton to become clickable
        time.sleep(.2) # Fix later
        try:
            driver.find_element_by_css_selector(askbutton).click()
        except:
            #Click Failed # Fix later
            pass

        # Find the popup
        while True:
            try:
                soup = BeautifulSoup(driver.page_source, "lxml")
                popExists = soup.find(class_="Modal AskQuestionModal")
                break
            except:
                pass
        soup = BeautifulSoup(driver.page_source,"lxml")
        popup = "#" + soup.find(class_="submit_button modal_action")["id"]
        driver.find_element_by_css_selector(popup).click()

        for x in range(0,17):
            time.sleep(.1)
            try:
                soup = BeautifulSoup(driver.page_source, "lxml")
                popExists = soup.find(class_="PMsgContainer") #Found Popup

                if str(popExists).__contains__("You asked"): #big no no
                    county += 1
                    break
            except:
                pass
        print("county=>",county)
        ''' 



