# -*- coding: utf-8 -*-

from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from auth_data import vk_password

options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0")

driver = webdriver.Chrome(executable_path="chromedriver", options=options)

try:
    driver.get("https://vk.com/")
    time.sleep(5)

    email_input = driver.find_element(by=By.XPATH, value='//*[@id="index_email"]')
    email_input.clear()
    email_input.send_keys("79832649304")
    time.sleep(5)

    pass_input = driver.find_element(by=By.XPATH, value='//*[@id="index_pass"]')
    pass_input.clear()
    pass_input.send_keys(vk_password)
    time.sleep(3)
    
    pass_input.send_keys(Keys.ENTER)

    # driver.find_element(by=By.XPATH, value='//*[@id="index_login_button"]').click()
    time.sleep(10)

    driver.find_element(by=By.XPATH, value='//*[@id="l_nwsf"]').click()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
