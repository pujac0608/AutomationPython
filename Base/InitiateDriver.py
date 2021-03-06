from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader

global driver


def StartBrowser():
    global driver
    if ConfigReader.readConfigData("Details", "Browser") == "Chrome":
        path = "./driver/chromedriver.exe"
        driver = Chrome(executable_path=path)
    elif ConfigReader.readConfigData("Details", "Browser") == "Firefox":
        path = "./driver/chromedriver.exe"
        driver = Firefox(executable_path=path)
    else:
        path = "./driver/chromedriver.exe"
        driver = Chrome(executable_path=path)

    driver.get(ConfigReader.readConfigData("Details","ApplicationURL"))
#   driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    return driver


def CloseBrowser():
    driver.close()
