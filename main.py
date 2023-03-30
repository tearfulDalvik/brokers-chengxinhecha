from selenium import webdriver
from win10toast import ToastNotifier
from subprocess import Popen
from selenium.webdriver.common.by import By
import time

toaster = ToastNotifier()

browser = webdriver.Chrome()

url_4090 = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-4090-24gb-gddr6x-graphics-card-titanium-and-black/6521430.p?skuId=6521430'



def start():
    browser.get(url_4090)
    print("select country")
    time.sleep(3)
    if browser.find_element(By.CSS_SELECTOR, '.add-to-cart-button').text == "Sold Out":
        print("out of stock.")
        print(time.time())
        print("\nrestarting")
   
start()