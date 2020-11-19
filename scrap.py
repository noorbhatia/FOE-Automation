from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options = options)

driver.get("http://deifoe.org/my/")
print(driver.title)
username = driver.find_element_by_id("username")
username.click()
username.send_keys("ENTER YOUR USERNAME")

password = driver.find_element_by_id("password")
password.click()
password.send_keys("ENTER YOUR PASSWORD")

#search2.send_keys(Keys.RETURN)
login_button = driver.find_element_by_id("loginbtn")
login_button.click()



calender = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "inst13840")))
contents = calender.find_elements_by_class_name('content')

for events in contents:
    event = events.find_elements_by_class_name("event")
if not event:
    print("Nothing to DO!!!!")
else:
    for course in event:
        print(course.text)

time.sleep(5)
driver.quit()
