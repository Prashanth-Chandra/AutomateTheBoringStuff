from selenium import webdriver
import warnings
from selenium.webdriver.common.keys import Keys
browser=webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
html=browser.find_element_by_tag_name('html')
while True:
    html.send_keys(Keys.UP)
    html.send_keys(Keys.RIGHT)
    html.send_keys(Keys.DOWN)
    html.send_keys(Keys.LEFT)


