from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("please scan qr code and press any key tocontinue:")
t=driver.find_element_by_css_selector('span[title="Bijaya It"]')
t.click()
testinput=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
testinput.send_keys("hy, i have implemented the automation successfully")
testinput.send_keys(Keys.RETURN)
