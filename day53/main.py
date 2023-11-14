from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
import requests
from bs4 import BeautifulSoup

url = "https://appbrewery.github.io/Zillow-Clone/"

# Send a GET request to the URL
response = requests.get(url)
cleaned_prices = []

sleep(20)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize arrays to store information
    links = []
    addresses = []
    prices = []

    # Find all div elements with class "StyledPropertyCardDataWrapper"
    property_cards = soup.find_all('div', class_='StyledPropertyCardDataWrapper')

    # Extract and store information for each property card
    for card in property_cards:
        # Extract link
        link_element = card.find('a', {'data-test': 'property-card-link'})
        link = link_element['href'] if link_element else None

        # Extract address
        address_element = card.find('address', {'data-test': 'property-card-addr'})
        address = address_element.get_text(strip=True) if address_element else None

        # Extract price
        price_element = card.find('span', {'data-test': 'property-card-price'})
        price = price_element.get_text(strip=True) if price_element else None

        # Remove unwanted text from the price
        unwanted_text = ["1 bd", "/mo", "+/mo", "+", "+ 1bd", "1bd", " 1bd"]
        for text in unwanted_text:
            price = price.replace(text, "").strip() if price else None

        # Check if all information is present
        if link and address and price:
            links.append(link)
            addresses.append(address)
            prices.append(price)

    # Print or use the arrays as needed
    print("Links:", links)
    print("Addresses:", addresses)
    print("Prices:", prices)
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

print(len(prices))
print(len(addresses))
print(len(links))

sleep(20)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(addresses)):
    # Open the Google Form for the current item
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdKaCuGqTgt_xD2SIm4ll7uYTlMElwN3zDnWkiSxNboEd1t9Q/viewform")
    sleep(5)
    wait = WebDriverWait(driver, 10)

    # Find the input fields by their aria-labelledby attribute
    address_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="i1"]')))
    price_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="i5"]')))
    link_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="i9"]')))

    # Input data into the form
    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])

    # Add a small delay to simulate human interaction
    sleep(1)

    # Find and click the submit button
    submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.uArJ5e')))
    submit_button.click()

    sleep(1)