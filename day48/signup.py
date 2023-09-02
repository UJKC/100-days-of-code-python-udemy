from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

portals_f = driver.find_element(By.NAME, value= "fName")
portals_f.send_keys("Ujwal")

portals_l = driver.find_element(By.NAME, value= "lName")
portals_l.send_keys("KC")

portals_e = driver.find_element(By.NAME, value= "email")
portals_e.send_keys("ujwalkcsps@gmail.com")

portals = driver.find_element(By.CSS_SELECTOR, value= ".form-signin button")
portals.click()