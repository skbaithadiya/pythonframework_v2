from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseWebElement(object):

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def is_element_displayed(self, element):
        if element.is_displayed():
            self.logger.debug('%s WebElement is displayed' %element)
            return element
        else:
            self.logger.error('%s WebElement is displayed' %element)
            return False
    
    def get_element(self, by, value):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((by, value)))
            self.logger.info(element)
            return element
        except exceptions.TimeoutException as e:
            self.logger.info("timeout finding element [%s] - [%s]"%(by, value))
            self.logger.error(e)
            return False
        except exceptions.NoSuchElementException as e:
            self.logger.info("Unable to find element [%s] - [%s]"%(by, value))
            self.logger.error(e)
            return False