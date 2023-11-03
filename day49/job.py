from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

username_input = driver.find_element(By.ID, value= "username")
username_input.send_keys("logaxot532@mainmile.com")

password_input = driver.find_element(By.ID, value= "password")
password_input.send_keys("Kncgreat1!")

search_input = driver.find_element(By.ID, value= "search-global-typeahead__input")
search_input.send_keys("Kncgreat1!")

sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()