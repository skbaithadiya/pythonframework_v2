from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from TestSteps.BaseTestSteps import BaseTestSteps
from WebElements.LoginPageWebElements import LoginPageWebElements
import time


class LoginPageTestSteps(BaseTestSteps):
    def __init__(self, driver, logger):
        self.base_ts = BaseTestSteps(driver, logger)
        self.driver = self.base_ts.driver
        self.logger = self.base_ts.logger
        self.login_page = LoginPageWebElements(self.driver, self.logger)

    def set_username(self, user):
        username = self.login_page.txt_username()
        if username is not False:
            username.clear()
            username.send_keys(user)
            self.logger.info('set_username: %s'%user)
            return True
        else:
            self.logger.error('username is not displayed!')
            return False

    def set_password(self, passd):
        
        password = self.login_page.txt_password()
        if password is not False:
            password.clear()
            password.send_keys(passd)
            self.logger.info('set password: %s'%passd)
            return True
        else:
            self.logger.error('password is not displayed!')
            return False

    def click_login_button(self):
        btn_login = self.login_page.btn_login()
        if btn_login is not False:
            self.logger.info('click login button')
            btn_login.click()
            return True
        else:
            self.logger.error('btn_login is not displayed!')
            return False

    def navigate_to_login_page(self):
        self.logger.info('navigating to login page')
        self.driver.get("https://www.saucedemo.com")
        # WebDriverWait(self.driver, 10).until()