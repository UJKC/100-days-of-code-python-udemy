import requests
from bs4 import BeautifulSoup

# Function to get the price of an Amazon product by its URL
def get_amazon_product_price(url):
    try:
        # Send a GET request to the Amazon product page
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the price element using its class
            price_element = soup.find('span', class_ = "a-offscreen")

            # Check if the price element was found
            if price_element:
                # Extract the price text
                price = price_element.text.strip()
                return price

        # If the request was not successful or price not found
        return "Price not available"

    except Exception as e:
        return str(e)

# Example usage:
product_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
product_price = get_amazon_product_price(product_url)
print("Product Price:", product_price)
