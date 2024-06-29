# Include necessary imports
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def search_ebay(product_name):
    # Path to Chrome driver executable
    chrome_driver_path = r'C:\Tools\chromedriver.exe'

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode

    # Create a WebDriver instance with headless mode
    driver = webdriver.Chrome(service=Service(chrome_driver_path))

    # Open Amazon website
    driver.get("https://www.ebay.com/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type= 'text']")))
    # Find the search input field and enter the product name
    search_input = driver.find_element("xpath", "//input[@type= 'text']")
    search_input.send_keys(product_name)
    search_input.send_keys(Keys.RETURN)

    # Wait for search results to load
    driver.implicitly_wait(10)

    # Find the first product in the search results
    first_product = driver.find_element(By.XPATH, '//li[@class="s-item s-item__pl-on-bottom"][2]')
    product_name = driver.find_element(By.XPATH,"//body/div[5]/div[4]/div[2]/div[1]/div[2]/ul[1]/li/div[1]/div[2]/a[1]").text
    product_price = driver.find_element(By.XPATH, "//body/div[5]/div[4]/div[2]/div[1]/div[2]/ul[1]/li/div[1]/div[2]/div[2]/div[1]/span[1]").text
    product_link = driver.find_element(By.XPATH, "//body/div[5]/div[4]/div[2]/div[1]/div[2]/ul[1]/li/div[1]/div[2]/a[1]").get_attribute("href")
    driver.quit()
    # Print product details
    ebay_results = [
        {'name': product_name,'price': product_price, 'link' :product_link}
    ]

    return ebay_results
    # Close the browser

def search_alibaba(product):
    driver = webdriver.Chrome()  # You may need to adjust the path to your Chrome driver

    # Open Alibaba website
    driver.get("https://www.alibaba.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='search-bar-placeholder util-ellipsis']")))
    # Find the search box and enter the product name
    search_box = driver.find_element("xpath", "//div[@class='search-bar-placeholder util-ellipsis']")
    search_box.send_keys(product)
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(2)

    # Find the top search result
    top_result = driver.find_element("xpath","//body/div[@class='container']/div[@id='root']/div[@class='app-organic-search l-main-wrap J-p4p-container']/div[@class='app-organic-search__main-body']/div[@class='app-organic-search__content']/div[@class='app-organic-search__content-main']/div[@class='offer-list-wrapper']/div[@class='organic-list organic-list_G app-organic-search__list organic-list-gallery-wrapper']/div[1]")

    # Extract product name, price, and link
    product_name = driver.find_element("xpath", "//body[1]/div[4]/div[1]/div[1]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]/a[1]/span[1]").text
    product_price = driver.find_element("xpath", "//*[@class='search-card-e-price-main'][1]").text
    product_link = driver.find_element("xpath","//body[1]/div[4]/div[1]/div[1]/div[5]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h2[1]/a[1]/span[1]").get_attribute("href")

    # Close the WebDriver
    driver.quit()

    return {
        'name': product_name,
        'price': product_price,
        'link': product_link
    }

def search_walmart(product):
    driver = webdriver.Chrome()  # You may need to adjust the path to your Chrome driver

    # Open Alibaba website
    driver.get("https://www.walmart.com/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//header/form[1]/div[1]/input[1]")))

    # Find the search box and enter the product name
    search_box = driver.find_element("xpath", "//header/form[1]/div[1]/input[1]")
    search_box.send_keys(product)
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(2)

    # Find the top search result
    top_result = driver.find_element("xpath",
                                     "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]")

    top_result.click()
    time.sleep(3)


    # Extract product name, price, and link
    product_name = driver.find_element("xpath", "//h1[@id='main-title']").text
    product_price = driver.find_element("xpath", "//span[@itemprop='price']").text
    product_link = driver.find_element("xpath",
                                           "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]").get_attribute(
        "href")

    # Close the WebDriver
    driver.quit()

    return {
        'name': product_name,
        'price': product_price,
        'link': product_link
    }


