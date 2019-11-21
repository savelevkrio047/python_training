from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

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




    def create(self, contact):
        # fill contact form
        wd = self.app.wd
        self.open_add_contact_form()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.secondname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.surname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(u"ЭФтех")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("123")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("qwe@ewq.uq")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("qwe@ewq.uq")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(u"апу")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("email3").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='E-mail3:'])[1]/following::label[1]").click()
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("qwe.ewq.uq")
        #wd.find_element_by_name("bday").click()
        #wd.find_element_by_name("bday").select_by_visible_text("8")
        #wd.find_element_by_name("bmonth").click()
        #wd.find_element_by_name("bmonth").select_by_visible_text("February")
        #wd.find_element_by_name("bmonth").click()
        #wd.find_element_by_name("byear").click()
        #wd.find_element_by_name("byear").clear()
        #wd.find_element_by_name("byear").send_keys("1995")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("123321")
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("321123")
        # submit contact creation
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        #wd.app.open_home_page()
        # self.open_home_page(wd)

