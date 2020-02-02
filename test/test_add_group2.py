# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.session import SessionHelper
from fixture.application import Application
import random
import string
from data.add_group import constant as testdata
from data.add_group import testdata1


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group2(app, group):
        old_groups = app.group.get_group_list()
       # group = Group(name="surmame", header="123123", footer="123123")
        app.group.create(group)
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


