from Base import InitiateDriver
import time


def test_Validate_Login_ValidData():
    driver = InitiateDriver.StartBrowser()
    loginTab = driver.find_element_by_xpath('//label[@for="tab2"]')
    uname = driver.find_element_by_name('_txtUserName')
    Pass = driver.find_element_by_name('_txtPassword')
    LoginBtn = driver.find_element_by_xpath('//input[@value="Login"]')
    loginTab.click()
    uname.send_keys("test")
#    driver.implicitly_wait(20)
    Pass.send_keys("test")
#    driver.set_script_timeout(20)
    LoginBtn.click()
    time.sleep(10)
    myacc = driver.find_element_by_xpath('//a[contains(text(), "My Account")]')
    myacc.click()
    time.sleep(10)
    driver.close()
