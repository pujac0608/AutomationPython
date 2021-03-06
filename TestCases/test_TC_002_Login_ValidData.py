from Base import InitiateDriver


def test_Validate_Login_ValidData():
    driver = InitiateDriver.StartBrowser()
    loginTab = driver.find_element_by_xpath('//label[@for="tab2"]')
    uname = driver.find_element_by_name('_txtUserName')
    Pass = driver.find_element_by_name('_txtPassword')
    LoginBtn = driver.find_element_by_xpath('//input[@value="Login"]')
    loginTab.click()
    uname.send_keys("test")
    Pass.send_keys("test")
    LoginBtn.click()
