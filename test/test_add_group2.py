# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.session import SessionHelper
from fixture.application import Application





def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="123123", header="123123", footer="123123"))
    app.session.log_out()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.log_out()
