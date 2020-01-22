# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from model.contact import Contact
from fixture.session import SessionHelper
from fixture.application import Application



    
def test_add_user(app):
    app.user.create(Contact(
        firstname=u"Геннадий1",
        secondname=u"Николаевич1",
        surname=u"Савельев1",
        nickname="Geksa",
        title=u"График оплаты",
        company=u"ЭФтеъ",
        address=u"Пушкина 11 а кв 4",
        home="123", mobile="123321",
        work=u"работа",
        email="qwe@ewq.uq"))


def test_add_empty_user(app):

    app.user.open_add_contact_form()
    app.user.create(Contact(firstname="", secondname="", surname="",
                            nickname="", title="", company="",
                            address="", home="", mobile="", work="",
                            email=""))
