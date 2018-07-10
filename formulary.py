from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://portal.medprocure.com/contract_price.php?custparent_id=3600&distributor_id=167")

#username = driver.find_element_by_id("kt_login_user")
#username.send_keys()
#
#password = driver.find_element_by_id("kt_login_password")
#password.send_keys()
#password.send_keys(Keys.RETURN)
#
##loginButton = driver.find_element_by_id("kt_loginl")
##loginButton.click()
#
#driver.implicitly_wait(10) #seconds
#
#customerButton = driver.find_element_by_id("cust-button")
#customerButton.click()

allButton = driver.find_element_by_id("KT_selAll")
