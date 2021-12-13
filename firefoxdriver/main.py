import time
# from selenium import webdriver
from fake_useragent import UserAgent
from seleniumwire import webdriver
from proxy_auth_data import login, password

url = "https://www.vk.com/"
url_2ip = "https://2ip.ru"
url_whatis = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"

useragent = UserAgent()
# options
options = webdriver.FirefoxOptions()

# change useragent
# options.set_preference("general-useragent.override", "Hello Friends!")
options.set_preference("general-useragent.override", useragent.random)

# set proxy
# proxy = "138.128.91.65:8000"
# proxy = "75.119.157.187:3128"
#
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities["marionette"] = True
# firefox_capabilities["proxy"] = {
#     "proxyType": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy
# }

proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@138.128.91.65:8000"
    }
}
# driver = webdriver.Firefox(executable_path="geckodriver", options=options, proxy=proxy)

driver = webdriver.Firefox(executable_path="geckodriver", seleniumwire_options=proxy_options)
try:
    # driver.get(url=url_whatis)
    # driver.save_screenshot("vk.png")
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
