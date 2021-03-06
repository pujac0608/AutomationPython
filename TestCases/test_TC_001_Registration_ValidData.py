from Base import InitiateDriver
from Library import ConfigReader


def test_validate_Registration():
    driver = InitiateDriver.StartBrowser()
    uname = driver.find_element_by_name(ConfigReader.fetchElement("Registration", "uname"))
    email = driver.find_element_by_name(ConfigReader.fetchElement("Registration", "email"))
    passw = driver.find_element_by_name(ConfigReader.fetchElement("Registration", "passw"))
    conPassw = driver.find_element_by_name(ConfigReader.fetchElement("Registration", "conPassw"))
    uname.send_keys("Testone")
    email.send_keys("test@gmail.com")
    passw.send_keys("admin")
    conPassw.send_keys("admin")
    InitiateDriver.CloseBrowser()
