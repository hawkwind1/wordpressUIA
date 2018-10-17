#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 9:38
# @Author  : PanCheng
# @Site    : 
# @File    : runtest.py
# @Software: PyCharm

import unittest
import os

# 定义测试用例的目录为当前目录
test_dir = os.getcwd()
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')

# 运行用例
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)
