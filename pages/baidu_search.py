# -*- coding: utf-8 -*-
# file name: baidu_search 
# author: hex7
# date: 19/8/2019

from basicTest import BasicTest
from conftest import logger

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BaiDuSearchPage(BasicTest):

    URL = 'http://www.baidu.com'

    SEARCH_INPUT = (By.ID, "kw")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        logger.info(f"Search {phrase}")
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
