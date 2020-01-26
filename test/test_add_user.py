# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from model.contact import Contact
from fixture.session import SessionHelper
from fixture.application import Application



    
def test_add_user(app):
    old_users = app.user.get_user_list()
    user = Contact(
        lastname="Савельев1",
        firstname="Геннадий1",
        homephone="4302014",
        mobilephone="89200101840",
        workphone="89087380653",
        secondaryphone="89107380653")
    app.user.create(user)
    assert len(old_users) + 1 == app.user.count()
    new_users = app.user.get_user_list()
    for i in new_users:
       if not (i in old_users):
           old_users.append(i)

    assert sorted(old_users, key=Contact.id_or_max) == sorted(new_users, key=Contact.id_or_max)
#def test_add_empty_user(app):

 #   app.user.open_add_contact_form()
 #   app.user.create(Contact(firstname="", secondname="", surname="",
 #                           nickname="", title="", company="",
  #                          address="", home="", mobile="", work="",
 #                           email=""))
