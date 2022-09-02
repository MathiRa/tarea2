import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("http://localhost:8116")
user = driver.find_element(By.ID, "user")
user.clear()
user.send_keys("root")
password = driver.find_element(By.NAME, "pass")
password.clear()
password.send_keys("password")
password.submit()
driver.get("http://localhost:8116")
driver.execute_script('document.querySelector("#CreateTicketInQueue > div.create-wide > input").click()')
subject = driver.find_element(By.NAME, "Subject")
subject.clear()
subject.send_keys("Mathias Rodriguez")
subject.submit()
time.sleep(20)
driver.close()
