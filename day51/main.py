from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

Guarenteed = 10

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://fast.com/")

sleep(100)

speed_element = driver.find_element(By.ID, value="speed-value")
if (speed_element < Guarenteed):
    print("Sign in is impossible")
else:
    print(speed_element + "Good")