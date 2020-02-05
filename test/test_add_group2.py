# -*- coding: utf-8 -*-
import pytest
from model.group import Group


def test_add_group2(app, data_groups):
        group = data_groups
        old_groups = app.group.get_group_list()
       # group = Group(name="surmame", header="123123", footer="123123")
        app.group.create(group)
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


