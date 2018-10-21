#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 9:38
# @Author  : PanCheng
# @Site    : 
# @File    : runtest.py
# @Software: PyCharm

import unittest
import os
import time
from tools.HTMLTestRunner import HTMLTestRunner
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(test_report_file_path):

    # 读取报告内容
    f = open(test_report_file_path, 'rb')
    mail_body = f.read()
    f.close()

    # 采用related定义内嵌资源的邮件体
    msg = MIMEMultipart('related')
    msgtext = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msgtext)
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    # 发邮件出错 smtplib.SMTPDataError: (554, b'DT:SPM 126 smtp4 ，将下面的两行代码加上
    msg['from'] ='pansc2005@126.com'
    msg['to'] = 'pansc2011@126.com'

    # 增加附件
    att = MIMEText(mail_body, 'html', 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="htmlReport.html" '
    msg.attach(att)

    # 邮箱相关的帐户密码
    smtp = smtplib.SMTP()
    smtpserver = 'smtp.126.com' #发送邮箱服务器
    user = 'pansc2005@126.com'#发送邮箱用户/密码
    password = '790520'
    sender = 'pansc2005@126.com'  #发送邮箱
    receiver = 'pansc2011@126.com' #接收邮箱

    # 发送
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("email has send out!")


# 运行用例
if __name__ == "__main__":

    # 定义测试用例的目录为当前目录
    test_dir = os.getcwd()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')

    # －－－－－－－Text runner
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    # －－－－－－HTMLTextrunner
    #设置测试报告路径
    report_create_time = time.strftime("%Y-%m-%d_%H%M%S")
    report_file_name = "Wordpress_UIA_Report_" + report_create_time + ".html"

    parent_path = os.getcwd().rsplit('\\', 1)[0]
    report_file_path = parent_path + "\\reports\\" + report_file_name
    #运行测试并生成report文件
    with open(report_file_path, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Wordpress_UIA_Report '+ report_create_time,
                                description='execution results:',
                                verbosity=2
                                )
        runner.run(discover)

    # 结果发送邮件
    print(report_file_path)
    send_mail(report_file_path)

