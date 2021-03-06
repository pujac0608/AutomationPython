from Base import InitiateDriver
from Pages.Registration import Registration


def test_validate_Registration():
    driver = InitiateDriver.StartBrowser()
    registration = Registration(driver)
    registration.enter_username("Test_Username")
    registration.enter_email("test@gmail.com")
    InitiateDriver.CloseBrowser()

