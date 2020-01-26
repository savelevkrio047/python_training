# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.session import SessionHelper
from fixture.application import Application
import random
import string

def random_string(prefix, maxlen):
   symbols =  string.ascii_letters + string.digits + " "*10
   return  prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + [Group(name=random_string("name",10), header=random_string("header",20), footer=random_string("footer", 20))
            for i in range(5)]
testdata1 = [Group(name=name, header=header, footer=footer)
            for name in ["", random_string("name", 10)]
            for header in ["", random_string("header", 10)]
            for footer in ["", random_string("footer", 10)]]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group2(app, group):
        old_groups = app.group.get_group_list()
       # group = Group(name="surmame", header="123123", footer="123123")
        app.group.create(group)
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


