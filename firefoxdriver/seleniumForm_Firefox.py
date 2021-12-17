# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from auth_data import instagram_password

options = webdriver.FirefoxOptions()

options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) "
                                                     "Gecko/20100101 Firefox/95.0")

driver = webdriver.Firefox(executable_path="geckodriver", options=options)

try:
    driver.get("https://instagram.com/")
    time.sleep(10)

    username_input = driver.find_element(by=By.XPATH,
                                         value="//input[@aria-label='Телефон, имя пользователя или эл. адрес']")
    username_input.clear()
    username_input.send_keys("firstvirpil")
    time.sleep(5)

    password_input = driver.find_element(by=By.XPATH, value="//input[@aria-label='Пароль']")
    password_input.clear()
    password_input.send_keys(instagram_password)
    time.sleep(5)
    password_input.send_keys(Keys.ENTER)
    time.sleep(6)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
