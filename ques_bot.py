#f

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


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