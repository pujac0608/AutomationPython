from Base import InitiateDriver
import time
from Pages.MyAccount import MyAccountClass
from Pages.Login import LoginClass


def test_Validate_Login_ValidData():
    driver = InitiateDriver.StartBrowser()
    LoginRef = LoginClass(driver)
    MyAccount = MyAccountClass(driver)
    LoginRef.Click_Login_Tab()
    LoginRef.enter_username("test")
    LoginRef.enter_password("test")
    LoginRef.login_Btn()
    time.sleep(5)
    MyAccount.Click_MyAccount_Menu()
    time.sleep(5)
    MyAccount.Click_MyAcc_Update_SubMenu()
    time.sleep(5)
    allwindows = driver.window_handles
    for win in allwindows:
        driver.switch_to.window(win)
        if driver.current_url == "https://www.thetestingworld.com/testings/manage_customer.php":

            time.sleep(3)
            driver.close()
    driver.switch_to.window(allwindows[0])
    MyAccount.Click_MyAccount_Menu()
    time.sleep(3)
    driver.close()