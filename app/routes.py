from flask import request, render_template, redirect
from os import environ
from datetime import datetime as dt
from .models import db, User
from app import app
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://secure.tesco.ie/register/?from=http://www.tesco.ie/groceries/?&icid=GHP_Anon_1A_Sign_In")
python_button = browser.find_element_by_xpath("//*[@id='loginID']")
python_button.send_keys("donalmongey@gmail.com")
python_button = browser.find_element_by_xpath("//*[@id='password']")
python_button.send_keys(environ.get('TESCO_PASSWORD'))
python_button = browser.find_elements_by_css_selector("#signinButton > input[type=image]")[0].click()
WebDriverWait(browser,3).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fDialogue']/div[3]/input[2]")))
if browser.find_elements_by_xpath("//*[@id='fDialogue']/div[3]/input[2]"):
    python_button = browser.find_elements_by_xpath("//*[@id='fDialogue']/div[3]/input[2]")[0].click()

items = {}
@app.route('/', methods=["POST", "GET"])
def start():
    if request.method == "POST":
        items.clear()
        form_values = request.form.to_dict()
        python_button = browser.find_elements_by_xpath("//*[@id='searchBox-1']")[0]
        python_button.send_keys(form_values["item-search"])
        python_button = browser.find_elements_by_xpath("//*[@id='searchBtn']")[0].click()
        html_text = browser.page_source
        soup = BeautifulSoup(html_text, 'html.parser')
        for checkbox in soup.find_all(attrs={"name": "chkProduct"}):
            items[checkbox["value"]] = {"name": "", "image:": ""}

        for item, details in items.items():
            item_text = soup.find('a', id="h-{}".format(item))
            print(item_text)
            items[item]["name"] = item_text.text
            if item_text.img:
                items[item]["image"] = item_text.img['src']
        print(items)
        return redirect("/")
    else:
        return render_template('tescoSearch.html', items = items)

@app.route('/add_item_to_cart', methods=["POST"])
def add_item_to_cart():
    form_values = request.form.to_dict()
    python_button = browser.find_elements_by_name("add-{}".format(form_values["add-item"]))[0].click()
    
    return redirect("/")