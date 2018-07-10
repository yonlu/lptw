from sys import argv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

script, username, password = argv

driver = webdriver.Firefox()

driver.get("https://portal.medprocure.com/index.php")

usernameElement = driver.find_element_by_id("kt_login_user")
usernameElement.send_keys(username)

passwordElement = driver.find_element_by_id("kt_login_password")
passwordElement.send_keys(password)
passwordElement.send_keys(Keys.RETURN)

driver.implicitly_wait(10) #seconds

distributorButton = driver.find_element_by_id("dist-button")
distributorButton.click()

driver.implicitly_wait(3) #seconds

formulary = driver.find_element_by_xpath("//table/tbody/tr/td[2]/table/tbody/tr[2]/td[4]")
print(formulary)
formulary.click()

# Template for a single deletion
#allButton = driver.find_element_by_id("KT_selAll")
#allButton.click()
#
#delAllButton = driver.find_element_by_class_name('KT_delete_op_link')
#delAllButton.click()
#
#alert = driver.switch_to_alert()
#alert.accept()

for x in range(130):
    driver.implicitly_wait(10) #seconds
    allButton = driver.find_element_by_id("KT_selAll")
    allButton.click()

    driver.implicitly_wait(10) #seconds

    delAllButton = driver.find_element_by_class_name('KT_delete_op_link')
    delAllButton.click()

    driver.implicitly_wait(10) #seconds

    alert = driver.switch_to_alert()
    alert.accept()
    driver.implicitly_wait(8) #seconds

driver.implicitly_wait(5) #seconds
