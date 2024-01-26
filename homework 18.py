from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html"
driver.get(url)

# 1 - 8
q1_field = driver.find_element(By.NAME, "q1")
q1_field.send_keys('a')
time.sleep(2)

q2_field = driver.find_element(By.NAME, "q2")
q2_field.send_keys('1')
time.sleep(2)

q3_field = driver.find_element(By.NAME, "q3")
q3_field.send_keys('1')
time.sleep(2)

q4_field = driver.find_element(By.NAME, "q4")
q4_field.send_keys('21')
time.sleep(2)

q5_field = driver.find_element(By.NAME, "q5")
q5_field.send_keys('8')
time.sleep(2)

q6_field = driver.find_element(By.NAME, "q6")
q6_field.send_keys('256')
time.sleep(2)

q7_field = driver.find_element(By.NAME, "q7")
q7_field.send_keys('1')
time.sleep(2)

q8_field = driver.find_element(By.NAME, "q8")
q8_field.send_keys('63')
time.sleep(2)

# 9 - 18
q9_radio = driver.find_element(By.XPATH, '//input[@name="q9" and @value="b"]')
q9_radio.click()
time.sleep(2)

q10_radio = driver.find_element(By.XPATH, '//input[@name="q10" and @value="b"]')
q10_radio.click()
time.sleep(2)

q11_radio = driver.find_element(By.XPATH, '//input[@name="q11" and @value="b"]')
q11_radio.click()
time.sleep(2)

q12_radio = driver.find_element(By.XPATH, '//input[@name="q12" and @value="c"]')
q12_radio.click()
time.sleep(2)

q13_radio = driver.find_element(By.XPATH, '//input[@name="q13" and @value="b"]')
q13_radio.click()
time.sleep(2)

q14_radio = driver.find_element(By.XPATH, '//input[@name="q14" and @value="a"]')
q14_radio.click()
time.sleep(2)

q15_radio = driver.find_element(By.XPATH, '//input[@name="q15" and @value="b"]')
q15_radio.click()
time.sleep(2)

q16_radio = driver.find_element(By.XPATH, '//input[@name="q16" and @value="d"]')
q16_radio.click()
time.sleep(2)

q17_radio = driver.find_element(By.XPATH, '//input[@name="q17" and @value="b"]')
q17_radio.click()
time.sleep(2)

q18_radio = driver.find_element(By.XPATH, '//input[@name="q18" and @value="a"]')
q18_radio.click()
time.sleep(2)

# 19 - 22

q19_checkbox_button = driver.find_element(By.XPATH, '//input[@name="q19" and @value="b"]')
q19_checkbox_button.click()
time.sleep(2)

q20_checkbox_button = driver.find_element(By.XPATH, '//input[@name="q20" and @value="c"]')
q20_checkbox_button.click()
time.sleep(2)

q21_checkbox_button = driver.find_element(By.XPATH, '//input[@name="q21" and @value="b"]')
q21_checkbox_button.click()
time.sleep(2)

q22_checkbox_button = driver.find_element(By.XPATH, '//input[@name="q22" and @value="b"]')
q22_checkbox_button.click()
time.sleep(2)

# 23 - 26

q23_radio = driver.find_element(By.XPATH, '//input[@name="q23" and @value="a"]')
q23_radio.click()
time.sleep(2)

q24_radio = driver.find_element(By.XPATH, '//input[@name="q24" and @value="b"]')
q24_radio.click()
time.sleep(2)

q25_radio = driver.find_element(By.XPATH, '//input[@name="q25" and @value="a"]')
q25_radio.click()
time.sleep(2)

q26_radio = driver.find_element(By.XPATH, '//input[@name="q26" and @value="d"]')
q26_radio.click()
time.sleep(2)

# 27 - 33

q27_radio = driver.find_element(By.XPATH, '//input[@name="q27" and @value="d"]')
q27_radio.click()
time.sleep(2)

q28_radio = driver.find_element(By.XPATH, '//input[@name="q28" and @value="d"]')
q28_radio.click()
time.sleep(2)

q29_radio = driver.find_element(By.XPATH, '//input[@name="q29" and @value="d"]')
q29_radio.click()
time.sleep(2)

q30_radio = driver.find_element(By.XPATH, '//input[@name="q30" and @value="d"]')
q30_radio.click()
time.sleep(2)

q31_radio = driver.find_element(By.XPATH, '//input[@name="q31" and @value="d"]')
q31_radio.click()
time.sleep(2)

q32_radio = driver.find_element(By.XPATH, '//input[@name="q32" and @value="d"]')
q32_radio.click()
time.sleep(2)

q33_radio = driver.find_element(By.XPATH, '//input[@name="q33" and @value="d"]')
q33_radio.click()
time.sleep(2)

finish_button = driver.find_element(By.XPATH, '//input[@value="FINISHED" and @type="BUTTON"]')
finish_button.click()
time.sleep(10)