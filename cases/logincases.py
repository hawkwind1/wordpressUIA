#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/11 23:35
# @Author  : PanCheng
# @Site    : 
# @File    : logincases.py
# @Software: PyCharm
import unittest
from selenium import webdriver
from pages.loginpage import *
from tools.screensave import *
from parameterized import parameterized


class LoginCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        '''
        测试登录成功的场景
        :return:
        '''
        # arrangement
        username = "pyse17"
        password = "pyse17"

        # action
        login_page_instance = LoginPage(self.driver)
        dashboard_page = login_page_instance.login(username,password)
        # save screen
        save_screenshot_wrapper(self.driver, 1)
        # assert
        self.assertTrue(username in dashboard_page.greeting_link.text)
        self.assertTrue("wp-adminy" in dashboard_page.get_url())

    # @save_screen_shot_decorator
    @parameterized.expand([
        ("psw_empty", "pyse17", "",  "wp-login", u"密码一栏为空", 1),
        ("invaliduser", "pyse18", "pyse18", "wp-login", u"无效用户名", 2),
        ("user_empty", "", "pyse17", "wp-login", u"用户名一栏为空", 3),
    ])
    def test_login_fail(self, name, username, password, partialURL, verifyInfo, id):
        '''
        测试登录失败的各种场景
        :return:
        '''
        # action
        login_page_instance = LoginPage(self.driver)
        login_fail_message = login_page_instance.login_as_expecting_error(username, password)
        # save screen
        save_screenshot_wrapper(self.driver, id)
        # assert
        self.assertTrue(verifyInfo in login_fail_message)
        self.assertTrue(partialURL in login_page_instance.get_url())


if __name__ == "__main__":
    unittest.main()


