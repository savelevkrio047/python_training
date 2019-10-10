from selenium import webdriver
import unittest, time, re
from fixture.session import SessionHelper

class Application:


    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session=SessionHelper(self)

    def return_to_group_page(self):
        # Проверяем наличие созданной группы
        wd = self.wd
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Groups'])[1]/following::form[1]").click()

    def create_group(self, group):
        # приступаем к созданию новой группы
        wd = self.wd
        wd.find_element_by_name("new").click()
        # заполнение формы создания группы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Сохраняем новую форму
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def open_groups_page(self):
        # открываем страницу с группами
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        # открытие главной страницы
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        wd = self.wd
        self.wd.quit()