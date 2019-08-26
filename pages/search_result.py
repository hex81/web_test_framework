# -*- coding: utf-8 -*-
# file name: search_result 
# author: hex7
# date: 19/8/2019


from .baidu_search import BaiDuSearchPage

from selenium.webdriver.common.by import By


class BaiDuResultPage:

    LINK_DIVS = (By.CSS_SELECTOR, '#content_left> div')

    @classmethod
    def phrase_results(cls, phrase):
        xpath = f"//div[@id='content_left']//*[contains(text(), '{phrase}')]"
        return By.XPATH, xpath

    def __init__(self, browser):
        self.browser = browser

    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    def phrase_result_count(self, phrase):
        phrase_results = self.browser.find_elements(
            *self.phrase_results(phrase))
        return len(phrase_results)

    def search_input_value(self):
        search_input = self.browser.find_element(
            *BaiDuSearchPage.SEARCH_INPUT)
        return search_input.get_attribute('value')
