from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

Guaranteed = 10

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/")

# Wait for the login button to be clickable (assuming it takes time to load)
try:
    login_button = WebDriverWait(driver, Guaranteed).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._acan._acao._acas._aj1-._ap30'))
    )
    login_button.click()

    username_input_email = driver.find_element(By.NAME, value= "email")
    username_input_email.send_keys("ukc0756@gmail.com")

    username_input_pass = driver.find_element(By.NAME, value= "pass")
    username_input_pass.send_keys("9448906153")

    username_input_login = driver.find_element(By.NAME, value= "login")
    username_input_login.click()

    sleep(20)

    not_now_button = WebDriverWait(driver, Guaranteed).until(
        EC.element_to_be_clickable((By.CLASS_NAME, '_a9--'))
    )
    not_now_button.click()

    new_url = "https://www.instagram.com/books_or_songs/following/"
    driver.get(new_url)

    sleep(20)

    #try:
        #elements_to_click = WebDriverWait(driver, Guaranteed).until(
        #    EC.presence_of_all_elements_located((By.CLASS_NAME, '_acan'))
        #)

        # Click on each element
        #for element in elements_to_click:
        #    follow_button = element.find_element(By.CLASS_NAME, '_ap3a')
        #    driver.execute_script("arguments[0].scrollIntoView();", follow_button)
        #    follow_button.click()
    #except Exception as e:
    #    print(f"Error clicking elements: {e}")

except Exception as e:
    print(f"Error clicking login button: {e}")
