from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path=r"C:\Users\Thunder\Desktop\geckodriver.exe")
browser.maximize_window()
browser.get("https://10fastfingers.com/typing-test/turkish")
time.sleep(2)
cookies = browser.find_element_by_xpath("//*[@id='CybotCookiebotDialogBodyButtonDecline']")
cookies.click()
a = 1
kutu = browser.find_element_by_xpath("//*[@id='inputfield']")
while a < 400:
    kelime = browser.find_element_by_xpath("//*[@id='row1']/span["+str(a)+"]")
    a += 1
    kutu.send_keys(kelime.text)
    time.sleep(0.1)
    kutu.send_keys(" ")
