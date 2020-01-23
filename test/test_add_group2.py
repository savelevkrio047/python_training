# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.session import SessionHelper
from fixture.application import Application





def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="123123", header="123123", footer="123123"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
