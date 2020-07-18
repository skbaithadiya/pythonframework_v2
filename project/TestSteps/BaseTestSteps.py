from selenium import webdriver
from framework.Utils.Logging.LoggingUtils import LoggingUtils


class BaseTestSteps(object):

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
