from selenium import webdriver
from project.TestCases.BaseTC  import BaseTestClass
from TestSteps.LoginPageTestSteps import LoginPageTestSteps
from framework.Utils.ImageCompare.ImageComparison import ImageComparison
import ProjectConstant
import time, logging, os, glob
import unittest
import pytest
from pathlib import Path


# from webdriver_manager.chrome import ChromeDriverManager

class testLoginTestCasesOpenCV(BaseTestClass):
    def __init__(self):
        self.base = BaseTestClass()
        self.logger = self.base.logger
        self.driver = self.base.driver
        self.image = ImageComparison()

    def test_login_opencv(self):
        testcase_result = "Failed"
        testscenario = "LoginTestScenario"
        testcase = "loginWithStandardUser"
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
                teststep = "LoginPage"
                # login_screenshot = ProjectConstant.SCREENSHOT_FOLDER_PATH + "\\login2.png"
                l_sc_path = os.path.join(ProjectConstant.SCREENSHOT_FOLDER_PATH, testscenario, testcase, teststep)
                print(l_sc_path)
                Path(l_sc_path).mkdir(parents=True, exist_ok=True)
                

                for f_name in os.listdir(l_sc_path):
                    if not f_name.startswith('baseline'):
                        print("no baseline yet")
                        sc_path = os.path.join(l_sc_path, "baseline_", "navigateLoginPage.png")
                    else:
                        sc_path = os.path.join(l_sc_path, "navigateLoginPage.png")
                driver.save_screenshot(sc_path)

                user = login.set_username(username)
                passd = login.set_password(password)
                login_btn = login.click_login_button()
                teststep = "WelcomePage"
                l_sc_path = os.path.join(ProjectConstant.SCREENSHOT_FOLDER_PATH, testscenario, testcase, teststep)
                print(l_sc_path)
                # welcome_screenshot = ProjectConstant.SCREENSHOT_FOLDER_PATH + "\\welcome2.png"
                Path(l_sc_path).mkdir(parents=True, exist_ok=True)
                for f_name in os.listdir(l_sc_path):
                    if not f_name.startswith('baseline'):
                        print("no baseline yet")
                        sc_path = os.path.join(l_sc_path, "baseline_", "navigateWelcomePage.png")
                    else:
                        sc_path = os.path.join(l_sc_path, "navigateWelcomePage.png")
                # sc_path = os.path.join(l_sc_path, "navigateWelcomePage.png")
                driver.save_screenshot(sc_path)
                self.terminate_driver(driver)

                #TODO
                #open cv code
                # self.image.compare_images(login_screenshot, welcome_screenshot, )


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
        
    def test_login(self):
        testcase_result = "Failed"
        try:
            logger = self.logger
            logger.info('Starting Testcase: test_login')
            driver = self.driver
            print("before viewport")
            eye_driver = self.eyes.open(driver=driver, app_name="SauceDemo", test_name="LoginTest", 
            viewport_size={"width": 800, "height": 600})
            
            print("eye: " + str(eye_driver))
            print("driver: " + str(driver))
            print("after viewport")
            username = self.base.get_data("tc1", "username")
            password = self.base.get_data("tc1", "password")
            if driver is not None:           
                #login
                print("before login")
                login = LoginPageTestSteps(driver, logger)
                navigate = login.navigate_to_login_page()
                print("after navigate to login")
                try:
                    self.eyes.check("Logintest",Target.window()) #eyes
                except Exception as e:
                    print(e)
                user = login.set_username(username)
                passd = login.set_password(password)
                login_btn = login.click_login_button()
                try:
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