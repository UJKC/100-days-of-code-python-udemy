from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.python.org/")

event = {}

event_dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
for event_num in range(len(event_dates)):
    event[event_num] = {
        "time": event_dates[event_num].text,
        "name": events[event_num].text,
    }

print(event)

driver.close()
driver.quit()