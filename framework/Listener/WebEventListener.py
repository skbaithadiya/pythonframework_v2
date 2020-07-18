from selenium import webdriver
import time
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class WebEventListener(AbstractEventListener):
    def __init__(self, logger):
        self.logger = logger

    def before_navigate_to(self, url, driver):
        self.logger.info('Navigating to: ' + url)

    def after_navigate_to(self, url, driver):
        self.logger.info('Successfully navigated to: ' + url)

    def before_navigate_back(self, driver):
        self.logger.info('Navigating Back')

    def after_navigate_back(self, driver):
        self.logger.info('Successfully Navigated Back')

    def before_navigate_forward(self, driver):
        self.logger.info('Successfully Navigated Forward')

    def after_navigate_forward(self, driver):
        self.logger.info('Successfully Navigated Forward')

    def before_find(self, by, value, driver):
        pass

    def after_find(self, by, value, driver):
        pass

    def before_click(self, element, driver):
        self.logger.info('Preparing to click on: ' + str(element))

    def after_click(self, element, driver):
        self.logger.info('Clicked on: ' + str(element))

    def before_change_value_of(self, element, driver):
        self.logger.info('Changing value of element [' + str(element) + ']')

    def after_change_value_of(self, element, driver):
        self.logger.info('Changed value to:' + str(element.get_attribute("value")))
        
    def before_execute_script(self, script, driver):
        pass

    def after_execute_script(self, script, driver):
        pass

    def before_close(self, driver):
        pass

    def after_close(self, driver):
        pass

    def before_quit(self, driver):
        pass

    def after_quit(self, driver):
        pass

    def on_exception(self, exception, driver):
        self.logger.error('Exception [' + str(exception) + '] Occurred. Driver [' + str(driver) + ']')