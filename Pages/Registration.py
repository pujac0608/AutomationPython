from Library import ConfigReader

global driver


class Registration:

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username):
        uname = driver.find_element_by_name(ConfigReader.fetchElement("Registration", "uname"))
        uname.send_keys(username)

    def enter_email(self, email):
        email = driver.find_element_by_name(ConfigReader.fetchElement("Registration", "email"))
        email.send_keys("email")

