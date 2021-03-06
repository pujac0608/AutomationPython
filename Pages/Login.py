

global driver


class LoginClass:

    def __init__(self, obj):
        global driver
        driver = obj

    def Click_Login_Tab(self):
        LogTab = driver.find_element_by_xpath('//label[@for="tab2"]')
        LogTab.click()

    def enter_username(self, username):
        uname = driver.find_element_by_name('_txtUserName')
        uname.send_keys(username)

    def enter_password(self, password):
        passwd = driver.find_element_by_name('_txtPassword')
        passwd.send_keys(password)

    def login_Btn(self):
        LogBtn = driver.find_element_by_xpath('//input[@value="Login"]')
        LogBtn.click()

