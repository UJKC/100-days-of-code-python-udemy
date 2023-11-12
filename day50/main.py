from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://tinder.onelink.me/9K8a/3d4abb81")

sleep(60)

try:
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Log in with Facebook"]'))
    )
    button.click()
except:
    print("Forced")
    div_mt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'Mt')))
    button = div_mt.find_element(By.CLASS_NAME, 'focus-outline-style')
    button.click()
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Log in with Facebook"]')))
    button.click()

sleep(10)
all_windows = driver.window_handles
new_window = [window for window in all_windows if window != driver.current_window_handle][0]
driver.switch_to.window(new_window)

username_input_email = driver.find_element(By.NAME, value= "email")
username_input_email.send_keys("")

username_input_pass = driver.find_element(By.NAME, value= "pass")
username_input_pass.send_keys("")

username_input_login = driver.find_element(By.NAME, value= "login")
username_input_login.click()