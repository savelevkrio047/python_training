# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from model.contact import Contact
from fixture.session import SessionHelper
from fixture.application import Application



    
def test_add_user(app):
    old_users = app.user.get_user_list()
    user = Contact(
        firstname="Геннадий1",
        secondname="Николаевич1",
        surname=u"Савельев1",
        nickname="Geksa",
        title=u"График оплаты",
        company=u"ЭФтеъ",
        address=u"Пушкина 11 а кв 4",
        home="123", mobile="123321",
        work=u"работа",
        email="qwe@ewq.uq"
         )
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
