from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from  model.contact import Contact

class UserHelper:
    def __init__(self, app):
        self.app = app


    def open_add_contact_form(self):
        # open add_contact form
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def delete_first_user(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.user_cache = None
    def open_users_page(self):
        wd = self.app.wd
        #self.app.open_home_page()
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()

    def modify_first_user(self, new_group_data):
        wd = self.app.wd
        self.open_users_page()
        self.select_first_group()
        #open modif form
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        #fill form
        self.fill_user_form(new_group_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.open_users_page()
        self.user_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_user_form(self, contact):
        wd = self.app.wd
        # заполнение формы создания rконтакта
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.secondaryphone)

    def create(self, contact):
        # fill contact form
        wd = self.app.wd
        self.open_add_contact_form()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.secondaryphone)
        # submit contact creation
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        #wd.app.open_home_page()
        # self.open_home_page(wd)
        self.user_cache = None

    user_cache = None

    def count(self):
        wd = self.app.wd
        self.open_users_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_users_page()
            self.user_cache = []
            for element in wd.find_elements_by_name("entry"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.user_cache.append(Contact(firstname=text, id=id))

        return list(self.user_cache)

    def delete_user_by_index(self, index):
        #Delete first user
        wd = self.app.wd
        self.open_users_page()
        self.select_user_by_index(index)
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        #self.open_users_page()
        self.group_cache = None

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
