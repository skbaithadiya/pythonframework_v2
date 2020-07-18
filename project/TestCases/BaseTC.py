from selenium import webdriver
from datetime import date
import time, sys
import ProjectConstant
# adding framework to project
sys.path.insert(0, ProjectConstant.FRAMEWORK_PATH)
from framework.WebDriverFactory.DriverFactory import DriverFactory
from framework.Utils.Logging.LoggingUtils import LoggingUtils
from framework.Utils.DataUtils.ExcelRW import ExcelReader, ExcelWriter

class BaseTestClass(object):
    def __init__(self):
        self.logger = self.get_logger()
        self.driver = self.start_driver()


    def get_logger(self):
        log_utils = LoggingUtils()
        today = date.today()
        current_date_time = today.strftime("%b-%d-%Y")
        log_file_name = ProjectConstant.LOG_FILE_NAME + "_" + current_date_time + ProjectConstant.LOG_FILE_EXTENTION
        logger = log_utils.get_logger(ProjectConstant.LOG_FILE_PATH, log_file_name)
        self.logger = logger
        return logger

    def get_data(self, tc_id, header_name):
        data_reader = ExcelReader()
        self.logger.debug("Reading file: %s"%ProjectConstant.LOGIN_DATA_FILE_PATH)
        data = data_reader.get_data_by_header_and_tc_id(logger=self.logger, file_path=ProjectConstant.LOGIN_DATA_FILE_PATH, 
        sheet_name=ProjectConstant.LOGIN_DATA_SHEET_NAME, tc_id=tc_id, header_name=header_name)
        return data
    
    def set_result(self, tc_id, header, tc_result):
        data_writer = ExcelWriter()
        self.logger.debug("Writing to file: %s"%ProjectConstant.LOGIN_DATA_FILE_PATH)
        write = data_writer.set_test_result(logger=self.logger, file_path=ProjectConstant.LOGIN_DATA_FILE_PATH, 
        sheet_name=ProjectConstant.LOGIN_DATA_SHEET_NAME, testcase_id=tc_id, header_name=header, result=tc_result)
        return write

    def start_driver(self):
        browser = ProjectConstant.BROWSER
        entry_url = ProjectConstant.ENTRY_URL
        self.logger.info("Starting WebDriver [%s] on: %s" %(browser, entry_url))
        driver = DriverFactory.init_driver(self.logger, entry_url, browser)
        self.driver = driver
        return driver


    def terminate_driver(self, driver):
        self.logger.info('BaseTestClass: terminate driver')
        DriverFactory.close_browser(self.logger, driver)
