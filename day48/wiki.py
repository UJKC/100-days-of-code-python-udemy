from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

arti_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(arti_count.text)
#arti_count.click()

portals = driver.find_element(By.NAME, value= "search")
portals.send_keys("Python")
portals.send_keys(Keys.ENTER)