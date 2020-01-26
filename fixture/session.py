class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # логин
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath('/html/body/div/div[4]/form/input[3]').click()
        # self.open_groups_page()

    def log_out(self):
        # выход из приложения
        # wd.find_element_by_link_text("Logout").click()
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_log_out(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.log_out()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.log_out()
        self.login(username, password)

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("/html/body/div/div[1]/form/b").text[1:-1]





