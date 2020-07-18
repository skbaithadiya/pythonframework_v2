from selenium import webdriver
from selenium.webdriver.common.by import By
from WebElements.BaseWebElement import BaseWebElement
import time


class LoginPageWebElements(BaseWebElement):

    def __init__(self, login_driver, logger):
        self.base = BaseWebElement(login_driver, logger)
        self.driver = self.base.driver
        self.logger = self.base.logger

    def txt_username(self):
        return self.base.get_element(By.ID, 'user-name')
    
    def txt_password(self):
        return self.base.get_element(By.ID, 'password')

    def btn_login(self):
        return self.base.get_element(By.CLASS_NAME, 'btn_action')




