from selenium import webdriver
from project.TestCases.BaseTC  import BaseTestClass
from TestSteps.LoginPageTestSteps import LoginPageTestSteps
import time, logging
import unittest
import pytest
from selenium import webdriver

class testLoginTestCases(BaseTestClass):
    def __init__(self):
        self.base = BaseTestClass()
        self.logger = self.base.logger
        self.driver = self.base.driver       
        

    def test_login(self):
        testcase_result = "Failed"
        try:
            logger = self.logger
            logger.info('Starting Testcase: test_login')
            driver = self.driver
            username = self.base.get_data("tc1", "username")
            password = self.base.get_data("tc1", "password")
            if driver is not None:           
                #login
                login = LoginPageTestSteps(driver, logger)
                navigate = login.navigate_to_login_page()
                user = login.set_username(username)
                passd = login.set_password(password)
                login_btn = login.click_login_button()
                self.terminate_driver(driver)

                if (navigate or user or passd or login_btn) is not False:
                    testcase_result = 'Passed'
            else:
                logger.info('problem initiating WebDriver')
        except Exception as e:
            self.logger.error(e)
            testcase_result = False
        self.base.set_result("tc1", "test_result", testcase_result)
        time.sleep(1)
        return testcase_result

    def test_failed_login_user(self):
        testcase_result = "Failed"
        try:
            logger = self.logger
            logger.info('Starting Testcase: test_login')
            driver = self.driver
            username = self.base.get_data("tc2", "username")
            password = self.base.get_data("tc2", "password")
            if driver is not None:           
                #login
                login = LoginPageTestSteps(driver, logger)
                navigate = login.navigate_to_login_page()
                user = login.set_username(username)
                passd = login.set_password(password)
                login_btn = login.click_login_button()
                # self.terminate_driver(driver)
                if (navigate or user or passd or login_btn) is not False:
                    testcase_result = 'Passed'
            else:
                logger.info('problem initiating WebDriver')
        except Exception as e:
            self.logger.error(e)
            testcase_result = False
        self.base.set_result("tc2", "test_result", testcase_result)
        time.sleep(1)
        return testcase_result

    def test_problem_user(self):
        testcase_result = "Failed"
        try:
            logger = self.logger
            logger.info('Starting Testcase: test_login')
            driver = self.driver
            username = self.base.get_data("tc3", "username")
            password = self.base.get_data("tc3", "password")
            if driver is not None:           
                #login
                login = LoginPageTestSteps(driver, logger)
                navigate = login.navigate_to_login_page()
                user = login.set_username(username)
                passd = login.set_password(password)
                login_btn = login.click_login_button()
                self.terminate_driver(driver)
                if (navigate or user or passd or login_btn) is not False:
                    testcase_result = 'Passed'
            else:
                logger.info('problem initiating WebDriver')
        except Exception as e:
            self.logger.error(e)
            testcase_result = False
        self.base.set_result("tc3", "test_result", testcase_result)
        time.sleep(1)
        return testcase_result