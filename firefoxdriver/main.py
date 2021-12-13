import time
from selenium import webdriver
from fake_useragent import UserAgent

# url = "https://www.vk.com/"
url_whatis = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"

useragent = UserAgent()
# options
options = webdriver.FirefoxOptions()

# change useragent
# options.set_preference("general-useragent.override", "Hello Friends!")
options.set_preference("general-useragent.override", useragent.random)

driver = webdriver.Firefox(executable_path="geckodriver", options=options)
try:
    driver.get(url=url_whatis)
    driver.save_screenshot("vk.png")
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
