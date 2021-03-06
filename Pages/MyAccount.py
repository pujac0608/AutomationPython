global driver


class MyAccountClass:

    def __init__(self, obj):
        global driver
        driver = obj

    def Click_MyAccount_Menu(self):
        MyAcc = driver.find_element_by_xpath('//a[contains(text(), "My Account")]')
        MyAcc.click()

    def Click_MyAcc_Update_SubMenu(self):
        MyAccUpdate = driver.find_element_by_xpath('//a[contains(text(), "Update")]')
        MyAccUpdate.click()
