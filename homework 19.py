from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.set_window_position(2000, 600)

driver.maximize_window()

url = "https://test.mensa.no"

driver.get(url)

age1850_xpath = '//button[contains(@class,"ageselect_1850")]'
age1850_xpath_button = driver.find_element(By.XPATH, age1850_xpath)
age1850_xpath_button.click()
time.sleep(3)

start_id = 'startTest'
start_id_button = driver.find_element(By.ID, start_id)
start_id_button.click()
time.sleep(3)

ex1_a_xpath = '//div[@id="question_0"]/div/div/div[@data-answerid="0"]'
ex1_a_button = driver.find_element(By.XPATH, ex1_a_xpath)
ex1_a_button.click()
time.sleep(3)

ex2_b_xpath = '//div[@id="question_1"]/div/div/div[@data-answerid="1"]'
ex2_b_button = driver.find_element(By.XPATH, ex2_b_xpath)
ex2_b_button.click()
time.sleep(3)

ex3_c_xpath = '//div[@id="question_2"]/div/div/div[@data-answerid="2"]'
ex3_c_button = driver.find_element(By.XPATH, ex3_c_xpath)
ex3_c_button.click()
time.sleep(3)

ex4_d_xpath = '//div[@id="question_3"]/div/div/div[@data-answerid="3"]'
ex4_d_button = driver.find_element(By.XPATH, ex4_d_xpath)
ex4_d_button.click()
time.sleep(3)

ex5_e_xpath = '//div[@id="question_4"]/div/div/div[@data-answerid="4"]'
ex5_e_button = driver.find_element(By.XPATH, ex5_e_xpath)
ex5_e_button.click()
time.sleep(3)

ex6_f_xpath = '//div[@id="question_5"]/div/div/div[@data-answerid="5"]'
ex6_f_button = driver.find_element(By.XPATH, ex6_f_xpath)
ex6_f_button.click()
time.sleep(3)

ex7_a_xpath = '//div[@id="question_6"]/div/div/div[@data-answerid="0"]'
ex7_a_button = driver.find_element(By.XPATH, ex7_a_xpath)
ex7_a_button.click()
time.sleep(3)

ex8_b_xpath = '//div[@id="question_7"]/div/div/div[@data-answerid="1"]'
ex8_b_button = driver.find_element(By.XPATH, ex8_b_xpath)
ex8_b_button.click()
time.sleep(3)

ex9_c_xpath = '//div[@id="question_8"]/div/div/div[@data-answerid="2"]'
ex9_c_button = driver.find_element(By.XPATH, ex9_c_xpath)
ex9_c_button.click()
time.sleep(3)

ex10_d_xpath = '//div[@id="question_9"]/div/div/div[@data-answerid="3"]'
ex10_d_button = driver.find_element(By.XPATH, ex10_d_xpath)
ex10_d_button.click()
time.sleep(3)

ex11_e_xpath = '//div[@id="question_10"]/div/div/div[@data-answerid="4"]'
ex11_e_button = driver.find_element(By.XPATH, ex11_e_xpath)
ex11_e_button.click()
time.sleep(3)

ex12_f_xpath = '//div[@id="question_11"]/div/div/div[@data-answerid="5"]'
ex12_f_button = driver.find_element(By.XPATH, ex12_f_xpath)
ex12_f_button.click()
time.sleep(3)

ex13_a_xpath = '//div[@id="question_12"]/div/div/div[@data-answerid="0"]'
ex13_a_button = driver.find_element(By.XPATH, ex13_a_xpath)
ex13_a_button.click()
time.sleep(3)

ex14_b_xpath = '//div[@id="question_13"]/div/div/div[@data-answerid="1"]'
ex14_b_button = driver.find_element(By.XPATH, ex14_b_xpath)
ex14_b_button.click()
time.sleep(3)

ex15_c_xpath = '//div[@id="question_14"]/div/div/div[@data-answerid="2"]'
ex15_c_button = driver.find_element(By.XPATH, ex15_c_xpath)
ex15_c_button.click()
time.sleep(3)

ex16_d_xpath = '//div[@id="question_15"]/div/div/div[@data-answerid="3"]'
ex16_d_button = driver.find_element(By.XPATH, ex16_d_xpath)
ex16_d_button.click()
time.sleep(3)

ex17_e_xpath = '//div[@id="question_16"]/div/div/div[@data-answerid="4"]'
ex17_e_button = driver.find_element(By.XPATH, ex17_e_xpath)
ex17_e_button.click()
time.sleep(3)

ex18_f_xpath = '//div[@id="question_17"]/div/div/div[@data-answerid="5"]'
ex18_f_button = driver.find_element(By.XPATH, ex18_f_xpath)
ex18_f_button.click()
time.sleep(3)

ex19_a_xpath = '//div[@id="question_18"]/div/div/div[@data-answerid="0"]'
ex19_a_button = driver.find_element(By.XPATH, ex19_a_xpath)
ex19_a_button.click()
time.sleep(3)

ex20_b_xpath = '//div[@id="question_19"]/div/div/div[@data-answerid="1"]'
ex20_b_button = driver.find_element(By.XPATH, ex20_b_xpath)
ex20_b_button.click()
time.sleep(3)

ex21_c_xpath = '//div[@id="question_20"]/div/div/div[@data-answerid="2"]'
ex21_c_button = driver.find_element(By.XPATH, ex21_c_xpath)
ex21_c_button.click()
time.sleep(3)

ex22_d_xpath = '//div[@id="question_21"]/div/div/div[@data-answerid="3"]'
ex22_d_button = driver.find_element(By.XPATH, ex22_d_xpath)
ex22_d_button.click()
time.sleep(3)

ex23_e_xpath = '//div[@id="question_22"]/div/div/div[@data-answerid="4"]'
ex23_e_button = driver.find_element(By.XPATH, ex23_e_xpath)
ex23_e_button.click()
time.sleep(3)

ex24_f_xpath = '//div[@id="question_23"]/div/div/div[@data-answerid="5"]'
ex24_f_button = driver.find_element(By.XPATH, ex24_f_xpath)
ex24_f_button.click()
time.sleep(3)

ex25_a_xpath = '//div[@id="question_24"]/div/div/div[@data-answerid="0"]'
ex25_a_button = driver.find_element(By.XPATH, ex25_a_xpath)
ex25_a_button.click()
time.sleep(3)

ex26_b_xpath = '//div[@id="question_25"]/div/div/div[@data-answerid="1"]'
ex26_b_button = driver.find_element(By.XPATH, ex26_b_xpath)
ex26_b_button.click()
time.sleep(3)

ex27_c_xpath = '//div[@id="question_26"]/div/div/div[@data-answerid="2"]'
ex27_c_button = driver.find_element(By.XPATH, ex27_c_xpath)
ex27_c_button.click()
time.sleep(3)

ex28_d_xpath = '//div[@id="question_27"]/div/div/div[@data-answerid="3"]'
ex28_d_button = driver.find_element(By.XPATH, ex28_d_xpath)
ex28_d_button.click()
time.sleep(3)

ex29_e_xpath = '//div[@id="question_28"]/div/div/div[@data-answerid="4"]'
ex29_e_button = driver.find_element(By.XPATH, ex29_e_xpath)
ex29_e_button.click()
time.sleep(3)

ex30_f_xpath = '//div[@id="question_29"]/div/div/div[@data-answerid="5"]'
ex30_f_button = driver.find_element(By.XPATH, ex30_f_xpath)
ex30_f_button.click()
time.sleep(3)

ex31_a_xpath = '//div[@id="question_30"]/div/div/div[@data-answerid="0"]'
ex31_a_button = driver.find_element(By.XPATH, ex31_a_xpath)
ex31_a_button.click()
time.sleep(3)

ex32_b_xpath = '//div[@id="question_31"]/div/div/div[@data-answerid="1"]'
ex32_b_button = driver.find_element(By.XPATH, ex32_b_xpath)
ex32_b_button.click()
time.sleep(3)

ex33_c_xpath = '//div[@id="question_32"]/div/div/div[@data-answerid="2"]'
ex33_c_button = driver.find_element(By.XPATH, ex33_c_xpath)
ex33_c_button.click()
time.sleep(3)

ex34_d_xpath = '//div[@id="question_33"]/div/div/div[@data-answerid="3"]'
ex34_d_button = driver.find_element(By.XPATH, ex34_d_xpath)
ex34_d_button.click()
time.sleep(3)

ex35_e_xpath = '//div[@id="question_34"]/div/div/div[@data-answerid="4"]'
ex35_e_button = driver.find_element(By.XPATH, ex35_e_xpath)
ex35_e_button.click()
time.sleep(3)

finish_xpath = '//div[@id="question_34"]/div/div/button[contains(@class,"questionFinish")]'
finish_button = driver.find_element(By.XPATH, finish_xpath)
finish_button.click()
time.sleep(3)

done_already_xpath = '//div[@id="endTestDialog"]/div/div/div/button[contains(@class, "btn-danger")]'
done_already_button = driver.find_element(By.XPATH, done_already_xpath)
done_already_button.click()
time.sleep(3)

time.sleep(3000)
