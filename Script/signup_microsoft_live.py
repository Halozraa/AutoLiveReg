from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import random

#yg dibawan inin untuk menggunakan explisty wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://signup.live.com/signup?mkt=EN-US&mkt=EN-US&sru=https%3a%2f%2flogin.live.com%2flogin.srf%3flc%3d1033%26id%3d74335%26tw%3d0%26fs%3d0%26ts%3d-1%26sec%3d%26mspp_shared%3d1%26seclog%3d0%26claims%3d%26wa%3dwsignin1.0%26wp%3dMBI_SSL%26ru%3dhttps%3a%2f%2fwww.microsoft.com%2frpsauth%2fv2%2faccount%2fmsa%2fsignincallback%253fstate%253deyJSdSI6Imh0dHBzOi8vd3d3Lm9mZmljZS5jb20_YXV0aHR5cGVwYXJhbW5hbWU9YXV0aCIsIkxjIjoiOSIsIkhvc3QiOiJ3d3cubWljcm9zb2Z0LmNvbSJ9%26contextid%3dFB7ACDAA247AA57C%26opid%3dFA8DB03672609C66%26opidt%3d1714315321&uiflavor=web&id=74335&uaid=a90c3e53986b4840ad9fa04a2d6c3eb1&lic=1')
driver.find_element(By.ID,'liveSwitch').click()
print("Klik pertama")
time.sleep(2)
driver.find_element(By.ID,'MemberName').send_keys('NagiNgai54')
print("Klik kedua")
time.sleep(2)
driver.find_element(By.ID,'iSignupAction').click()
time.sleep(2)
print("Klik ketiga")
driver.find_element(By.ID,'PasswordInput').send_keys('Nagisenpai1234#')
print("Klik ke empat")

time.sleep(2)
driver.find_element(By.ID,'iSignupAction').click()
time.sleep(2)
driver.find_element(By.ID,'FirstName').send_keys("Nagi")
time.sleep(2)
driver.find_element(By.ID,'LastName').send_keys("HAloza")
time.sleep(2)
driver.find_element(By.ID,'iSignupAction').click()


driver.find_element(By.ID,'BirthDay').send_keys('2')
driver.find_element(By.ID,'BirthMonth').send_keys('January')
driver.find_element(By.ID,'BirthYear').send_keys('1999')
driver.find_element(By.ID,'iSignupAction').click()
time.sleep(10)

pyautogui.click(1031,686)

#iam stuck captcha2 here 
print("berhasil")
time.sleep(60)