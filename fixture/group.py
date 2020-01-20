class GroupHelper:
    def __init__(self, app):
        self.app = app


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #open modif form
        wd.find_element_by_name("edit").click()
        #fill form
        self.fill_group_form(new_group_data)
        #submit modification
        wd.find_element_by_name("update").click()
        self.return_to_group_page()






    def return_to_group_page(self):
        # Проверяем наличие созданной группы
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Groups'])[1]/following::form[1]").click()

    def create(self, group):
        self.open_groups_page()
        # приступаем к созданию новой группы
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Сохраняем новую форму
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        # заполнение формы создания группы
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def open_groups_page(self):
        # открываем страницу с группами
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()
    def delete_first_group(self):
        #Delete first user
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.app.open_home_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
    def count(self):
        wd = self.app.wd
        self.return_to_group_page()
        return len(wd.find_elements_by_name("selected[]"))


