from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()
sites = ["https://www.netflix.com/ua-ru/",
         "https://www.hotspot.school/",
        "https://en.wikipedia.org/wiki/Main_Page"
         ]
for url in sites:
    driver.get(url)
    if url == "https://www.netflix.com/ua-ru/":
        sign_in_button = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[1]/header/div/div/div[2]/div/div/div[2]/div/a")
        sign_in_button.click()
        time.sleep(6)
    elif url == "https://en.wikipedia.org/wiki/Main_Page":
        log_in_button = driver.find_element("xpath", "/html/body/div[1]/header/div[2]/nav/div[1]/div[4]/div/ul/li[2]/a/span")
        log_in_button.click()
        time.sleep(6)
    elif url ==  "https://www.hotspot.school/":
        contacts_button = driver.find_element("xpath", "/html/body/div/nav/div/div[2]/ul/li[5]/a")
        contacts_button.click()
        time.sleep(6)
    else:
        print("Something went wrong")
