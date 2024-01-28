from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from csv import writer
from time import sleep

driver = webdriver.Chrome('C:/Users/Asus/Downloads/chromedriver_win32')

driver.get("https://bazarstore.az/456-vanilqabartma-tozu")

with open('vanilqabartmatozu.csv', 'w', encoding = 'utf-8') as vanilqabartmatozu_csv:
    csv_writer = writer(vanilqabartmatozu_csv)
    csv_writer.writerow(['product', 'price'])

    products = driver.find_elements(By.CLASS_NAME, 'bs-product-row')
    for product in products:
        product = product.find_element(By.CLASS_NAME, 'product-title').text  

    for product in products:
        price = product.find_element(By.CLASS_NAME, 'pp_price_with_text').text

        csv_writer.writerow([product, price])

        driver.quit()