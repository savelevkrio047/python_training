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

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(15)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserHelper(self)

    def open_home_page(self):
        # открытие главной страницы
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        wd = self.wd
        self.wd.quit()



