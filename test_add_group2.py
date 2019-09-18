# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_group_page(wd)
        self.log_out(wd)

    def log_out(self, wd):
        # выход из приложения
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        # Проверяем наличие созданной группы
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Groups'])[1]/following::form[1]").click()

    def create_group(self, wd):
        # приступаем к созданию новой группы
        wd.find_element_by_name("new").click()
        # заполнение формы создания группы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("123123")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("123123")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("123123")
        # Сохраняем новую форму
        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        # открываем страницу с группами
        wd.find_element_by_link_text("groups").click()

    def login(self, wd):
        # логин
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # открытие главной страницы
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
