'''
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
browser.save_screenshot("dom.png")
time.sleep(10)
browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
time.sleep(3)
browser.refresh()'''

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
import time

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

'''
paragraphs = browser.find_elements(By.TAG_NAME, "p")

for paragraph in paragraphs:
    print(paragraph.text)
    input()'''

hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

print(hatnotes)
hatnotes = random.choice(hatnotes)
link = hatnotes.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)