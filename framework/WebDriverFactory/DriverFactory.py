from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from sys import platform
import time, os, sys
from framework import FrameworkConstant
from framework.Listener.WebEventListener import WebEventListener

class DriverFactory():

    def init_driver(logger, entry_url, browser):
        driver = None
        logger.debug('initializing Webdriver')
        logger.debug(entry_url)
        if platform == "linux" or platform == "linux2":
            # linux
            logger.debug('Running Test on Linux Machine')
        elif platform == "darwin":
            # OS X
            logger.debug('Running Test on OSX Machine')
        elif platform == "win32":
            logger.debug('Running Test on Windows Machine')
            # Windows...
            if browser.lower() == 'chrome':
                driver = DriverFactory.get_chrome(logger, 'win', entry_url)
            elif browser.lower() == 'firefox':
                driver = DriverFactory.get_firefox(logger, 'win', entry_url)
            elif browser.lower() == 'safari':
                driver = DriverFactory.get_safari(logger, 'win', entry_url)
            else:
                logger.debug('Not supported browser')
        else:
            logger.debug('Not supported platform')
            # web = WebEventListener(logger)
        # when use EventFiringWebDriver uncomment below line and return `event_driver`
        # event_driver = EventFiringWebDriver(driver, WebEventListener(logger))
        return driver
    
    def get_chrome(logger, os_name, entry_url):
        """ get chrome browser """
        driver_path = None
        if os_name.lower() == 'win':
            driver_path = os.path.join(FrameworkConstant.DRIVER_DIR_PATH, "chrome",
            os_name, FrameworkConstant.CHROME_WIN_NAME)

        driver = webdriver.Chrome(driver_path)
        driver.get(entry_url)
        driver.maximize_window()
        return driver

    def get_firefox(logger, os_name, entry_url):
        pass

    def get_safari(logger, os_name, entry_url):
        pass

    def close_browser(logger, driver):
        time.sleep(2)
        driver.close()
        logger.debug('closing the browser')

    def test():
        logger.debug('called driver factory')

#test
# DriverFactory.init_driver("https://www.saucedemo.com", "chrome")