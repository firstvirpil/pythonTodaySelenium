# from selenium import webdriver
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent

# url = "https://www.instagram.com/"
# url_whatis = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
url_2ip = "https://2ip.ru"

user_agent_list = [
    "best_of_the_best",
    "life_is_life",
    "oo_java_agent"
]

# change useragent
useragent = UserAgent()

# options
options = webdriver.ChromeOptions()

# выбор агента произвольный из списка
# options.add_argument(f"user-agent={random.choice(user_agent_list)}")

options.add_argument(f"user-agent={useragent.random}")

# set proxy
options.add_argument("--proxy-server=138.128.91.65:8000")

# driver = webdriver.Chrome(executable_path="chromedriver", options=options)
driver = webdriver.Chrome(executable_path="chromedriver", options=options)
try:
    # driver.get(url=url_whatis)
    # time.sleep(5)
    # driver.get("https://stackoverflow.com/")
    # time.sleep(5)

    # driver.refresh()
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)
    driver.get(url=url_2ip)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
