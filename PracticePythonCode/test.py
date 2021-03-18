from selenium.webdriver import Chrome
import logging


def Validate_Registration():
    path = "D:\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    print("Pytest")


Validate_Registration()

# log = logging.getLogger(__name__)
# log.setLevel(logging.DEBUG)

# warn = logging.FileHandler("warning.txt")
# warn.setLevel(logging.WARNING)

# info = logging.FileHandler("info.txt")
# info.setLevel(logging.INFO)

