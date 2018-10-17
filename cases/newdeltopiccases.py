#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 12:39
# @Author  : PanCheng
# @Site    : 
# @File    : newdeltopiccases.py
# @Software: PyCharm
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from pages.loginpage import LoginPage
from pages.topiclistpage import TopicListPage
from pages.newtopicpage import NewTopicPage
from pages.trashtopiclistpage import TrashTopicListPage


class NewDelTopicCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    def tearDown(self):
        self.driver.quit()

    def _new_a_topic(self):
        login_page = LoginPage(self.driver)
        dashboard_page = login_page.login_as_pyse17()
        topic_list_page = dashboard_page.navigate_to_topic_list_page()
        new_topic_page = topic_list_page.navigate_to_write_topic_page()

        # 创建新文章
        topic_title = "Pansc Tests Creating a new topic: time: {}".format(time.ctime())
        topic_content = topic_title + "\n this is the content"
        post_id = new_topic_page.write_and_push_a_new_topic(topic_title, topic_content) #获取创建的新文章的post_id

        return post_id

    def test_new_a_topic_success(self):
        login_page = LoginPage(self.driver)
        dashboard_page = login_page.login_as_pyse17()
        topic_list_page = dashboard_page.navigate_to_topic_list_page()
        new_topic_page = topic_list_page.navigate_to_write_topic_page()

        # 创建新文章
        topic_title = "Pansc Tests Creating a new topic: time: {}".format(time.ctime())
        topic_content = topic_title + "\n this is the content"
        post_id = new_topic_page.write_and_push_a_new_topic(topic_title, topic_content) #获取创建的新文章的post_id

        # 到topiclistpage页面验证新发布的topic已经展示在list上
        topic_list_page = TopicListPage(self.driver)
        topic_list_text = topic_list_page.get_topic_text_by_post_id(post_id)
        print("post_id :" + topic_title)
        print("topic_list_text :" + topic_list_text)
        self.assertEqual(topic_title, topic_list_text)

    def test_del_a_topic_success(self):
        # 创建一篇新文章
        post_id = self._new_a_topic()
        # 将新文章移入回收站
        topic_list_page = TopicListPage(self.driver)
        topic_list_page.move_topic_to_trash_bin_by_post_id(post_id)
        # 将该文章彻底删除
        trash_topic_list_page = TrashTopicListPage(self.driver)
        trash_topic_list_page.del_a_topic_item_throguly_by_post_id(post_id)
        # 到文章列表页面校验文章已不存在
        topic_list_page = TopicListPage(self.driver)

        self.assertTrue(topic_list_page.topic_item_not_exist(post_id))


# if __name__ == "__main__":
#     suite = unittest.defaultTestLoader.discover("./",pattern="new*.py")
#     runner = unittest.TextTestRunner()
#     runner.run(suite)



