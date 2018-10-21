#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/21 10:47
# @Author  : PanCheng
# @Site    : 
# @File    : screensave.py
# @Software: PyCharm

import os
import datetime
import sys

#####-----下面的save　screen封装了driver原有的save screen功能，在文件名称上加上id、用例文件名称、用例名称和当前时间
def _snapshot_file_path(id):
    #获取当前运行文件名称 注意，这里两次使用了f_back,所以调用方式是 test_case ->save_screenshot_wrapper -> _snapshout..
    test_file_path = sys._getframe().f_back.f_back.f_code.co_filename
    test_file_name = os.path.split(test_file_path)[1].rsplit('.')[0]

    # 获取调用方法的名称
    func_name = sys._getframe().f_back.f_back.f_code.co_name

    #获取当前时间并进行格式化
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    #拼接当前抓图的存放路径
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = parentdir + '\\reports\\image\\' + current_time + "_" + test_file_name + "_" + func_name + "_" + str(id) + ".png"
    print(file_path)
    return file_path

def save_screenshot_wrapper(dr, id):
    # 保存screenshot
    dr.save_screenshot(_snapshot_file_path(id))





######### ----下面的装饰器用于测试方法前，测试方法出错时会自动保存图片

def _snapshot_file_path_decro():
    #获取当前运行文件名称 注意，这里两次使用了f_back,所以调用方式是 test_case ->save_screenshot_wrapper -> _snapshout..
    test_file_path = sys._getframe().f_back.f_back.f_code.co_filename
    test_file_name = os.path.split(test_file_path)[1].rsplit('.')[0]

    # # 获取调用方法的名称  可能因为装饰器的缘故，无法获取到调用测试方法的名称
    # func_name = sys._getframe().f_back.f_back.f_code.co_name

    #获取当前时间并进行格式化
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    #拼接当前抓图的存放路径
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # file_path = parent_dir + '\\reports\\image\\' + current_time + "_" + test_file_name + "_" + func_name + ".png"
    file_path = parent_dir + '\\reports\\image\\' + current_time + "_" + test_file_name + "_" + ".png"
    return file_path


# 装饰器  #  暂时不能用，没有找到办法将dr传给装饰器，因为self.driver不能做为参数传递
def save_screen_shot_decorator(dr):
    def decorator(func):
        def inner(*args):
            try:
                f = func(*args)
                return f
            except:
                dr.save_screenshot(_snapshot_file_path_decro())
                raise
        return inner
    return decorator