from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.add_argument(r'user-data-dir=C:\Users\55859\AppData\Local\Google\Chrome\User Data\Auto')

driver = webdriver.Chrome(executable_path=r'./chromedriver', options=options)
driver.get('https://web.whatsapp.com')

sleep(10)

profileGet = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div')
profileGet.click()

msgInput = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
msgInput.send_keys(" Somos a diversão da noite ")
msgInput.send_keys(Keys.ENTER)

for i in range(5, 0, -1):
    msgInput.send_keys(i)
    msgInput.send_keys(Keys.ENTER)
    sleep(1)

while(True):
    msgInput.send_keys('*BOLSONARO CHUPA PICA 8===========================D*')
    msgInput.send_keys(Keys.ENTER)