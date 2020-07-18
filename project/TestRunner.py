import time, sys
import ProjectConstant
import importlib.util   
# adding framework to project
sys.path.insert(0, ProjectConstant.FRAMEWORK_PATH)

from TestCases.LoginPage.testLoginTestCase import testLoginTestCases
# from TestCases.LoginPage.testLoginTestCaseApplitool import testLoginTestCasesAppli
from TestCases.LoginPage.testLoginTestCaseOpenCV import testLoginTestCasesOpenCV
from TestPlan import RegressionTestCases
from TestCases.BaseTC import BaseTestClass

import unittest
class TestExecution():

    login = testLoginTestCases()
    login.test_login()
    # login.test_failed_login_user()
    # login.test_problem_user()

    # #calling applitools python sdk
    # login = testLoginTestCasesAppli()
    # login.test_login_applitools_tc1()
    # login.test_login_applitools_tc2()

    # #calling applitools python screenshot sdk
    # login = testLoginTestCasesAppli()
    # login.test_login_screenshot()

    #compare screenshot using opencv
    login = testLoginTestCasesOpenCV()
    login.test_login_opencv()


# 1. create test plan for which testcases to choose and run, their order
# 2. create test run config: browser, entry url, specific user, parallel etc
# 3. run them
# 4. generate logs during execution
# 5. generate test results, execution reports, screenshots etc.
# 6. 