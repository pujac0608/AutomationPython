from Base import InitiateDriver
import time
from Pages.Login import LoginClass


def test_Validate_Login_ValidData():
    driver = InitiateDriver.StartBrowser()
    time.sleep(2)
    loginElement = LoginClass(driver)
    time.sleep(2)
    loginElement.Click_Login_Tab()
    loginElement.enter_username("test")
    loginElement.enter_password("test")
    loginElement.login_Btn()
    time.sleep(2)
    driver.close()

