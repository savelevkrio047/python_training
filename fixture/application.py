from selenium import webdriver
import unittest, time, re
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.user import UserHelper


class Application:

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif  browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("unrecognized browser %S" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        # открытие главной страницы
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        wd = self.wd
        self.wd.quit()



