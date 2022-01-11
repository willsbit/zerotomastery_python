from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

show_message_btn = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_btn.get_attribute('innerHTML')

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('teste')

show_message_btn.click()
output_message = chrome_browser.find_element(By.ID, 'display')

assert 'teste' in output_message.get_attribute('innerHTML')

chrome_browser.close()