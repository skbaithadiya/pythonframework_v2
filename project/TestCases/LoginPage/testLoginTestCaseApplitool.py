from selenium import webdriver
from project.TestCases.BaseTC  import BaseTestClass
from TestSteps.LoginPageTestSteps import LoginPageTestSteps
import ProjectConstant
import time, logging
import unittest
import pytest
from selenium import webdriver
from applitools.selenium import Eyes, Target, ClassicRunner
from applitools.common import logger, StdoutLogger, BatchInfo, Region

# from webdriver_manager.chrome import ChromeDriverManager

class testLoginTestCasesAppli(BaseTestClass):
    def __init__(self):
        self.base = BaseTestClass()
        self.logger = self.base.logger
        self.driver = self.base.driver
        runner = ClassicRunner()
        self.eyes = Eyes(runner)
        # Initialize the eyes SDK and set your private API key.
        self.eyes.api_key = ""
        self.view_port_size = {"width": 800, "height": 600}
        self.eyes.set_viewport_size(driver=self.driver, size=self.view_port_size)
        
        
    def batch_info(self):
        """
        Use one BatchInfo for all tests inside module
        """
        return BatchInfo("Some general Test cases name")
    
    def test_login_applitools_tc1(self):
        testcase_result = "Failed"

        try:
            logger = self.logger
            logger.info('Starting Testcase: test_login')
            driver = self.driver
            username = self.base.get_data("tc1", "username")
            password = self.base.get_data("tc1", "password")
            if driver is not None:           
                #login
                print("before login")
                login = LoginPageTestSteps(driver, logger)
                navigate = login.navigate_to_login_page()
                print("after navigate to login")
                try:
                    self.eyes.open(driver=driver, app_name="SauceDemo", test_name="LoginScreen")
                    self.eyes.check("Logintest",Target.window()) #eyes
                    self.eyes.close(False) #eyes close
                except Exception as e:
                    self.logger.error(e)
                    print(e)
                user = login.set_username(username)
                passd = login.set_password(password)
                login_btn = login.click_login_button()
                try:
                    self.eyes.open(driver=driver, app_name="SauceDemo", test_name="WelcomeScreen")
                    self.eyes.check("WelcomeTest", Target.window()) #eyes
                    self.eyes.close(False) #eyes close
                except Exception as e:
                    print(e)
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


        
    def test_login_applitools_tc2(self):
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
                try:
                    self.eyes.open(driver=driver, app_name="SauceDemo", test_name="LoginScreen")
                    self.eyes.check("Logintest",Target.window()) #eyes
                    self.eyes.close(False) #eyes close
                except Exception as e:
                    print(e)
                user = login.set_username(username)
                passd = login.set_password(password)
                login_btn = login.click_login_button()
                try:
                    self.eyes.open(driver=driver, app_name="SauceDemo", test_name="WelcomeScreen")
                    self.eyes.check("Logintest",Target.window()) #eyes
                    self.eyes.close(False) #eyes close
                except Exception as e:
                    self.logger.error(e)
                    print(e)
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