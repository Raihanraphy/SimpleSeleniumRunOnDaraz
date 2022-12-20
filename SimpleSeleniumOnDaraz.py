from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

 
driver = webdriver.Chrome(r'C:\Users\TigerIT\Downloads\chromedriver_win32./chromedriver.exe')
driver.get('https://www.daraz.com.bd/')
driver.maximize_window()
m = driver.find_element(By.ID, "q")
m.send_keys("Mouse")
time.sleep(3)

m2=driver.find_element(By.XPATH, '//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button')
m2.click()

time.sleep(2)
driver.find_element(By.XPATH, '//body/div[@id="root"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]').click()
driver.find_element(By.XPATH, '//div[contains(text(),"Price high to low")]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//body/div[@id="root"]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]').click()
time.sleep(2)
print(driver.find_element(By.XPATH, '//body/div[@id="container"]/div[@id="root"]/div[@id="block-F4KXhLDUKR"]/div[@id="block-w3Jz3V-dNP"]/div[@id="block-nmb82fpO-P"]/div[@id="block-sWqtrZRyI2"]/div[@id="module_product_price_1"]/div[1]/div[1]/span[1]').text)
time.sleep(30)