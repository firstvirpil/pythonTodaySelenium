import time

from selenium import webdriver


url = "https://www.instagram.com/"
driver = webdriver.Chrome(executable_path="chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)
    # driver.get("https://stackoverflow.com/")
    # time.sleep(5)

    # driver.refresh()
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
