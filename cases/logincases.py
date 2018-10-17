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


class LoginCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_success(self):
        # arrangement
        username = "pyse17"
        password = "pyse17"

        # action
        login_page_instance = LoginPage(self.driver)
        dashboard_page = login_page_instance.login(username,password)
        # assert
        self.assertTrue(username in dashboard_page.greeting_link.text)
        self.assertTrue("wp-admin" in dashboard_page.get_url())

    def test_login_fail(self):
        # arrangement
        datas = [
            {"username": "pyse17", "password": "", "partialURL": "wp-login", "veriyInfo": u"密码一栏为空"},
            {"username": "pyse18", "password": "pyse18", "partialURL": "wp-login", "veriyInfo": u"无效用户名"},
            {"username": "", "password": "pyse17", "partialURL": "wp-login", "veriyInfo": u"用户名一栏为空"},
        ]

        for data in datas:
            # action
            login_page_instance = LoginPage(self.driver)
            login_fail_message = login_page_instance.login_as_expecting_error(data["username"], data["password"])
            # assert
            self.assertTrue(data["veriyInfo"] in login_fail_message)
            self.assertTrue(data["partialURL"] in login_page_instance.get_url())


# if __name__ == "__main__":
#     unittest.main()


