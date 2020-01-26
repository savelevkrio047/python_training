from model.contact import Contact
from random import randrange
def test_del_first_user(app):
    if app.user.count() == 0:
        app.user.create(Contact(firstname="123", secondname="312", surname="123",
                                nickname="123", title="123", company="123",
                                address="123", home="123", mobile="123", work="123",
                                email="123"))
    old_users = app.user.get_user_list()
    app.user.delete_first_user()
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[0:1] = []
    assert old_users == new_users

def test_delete_some_group(app):
    if app.user.count() == 0:
        app.user.create(Contact(firstname="123", secondname="312", surname="123",
                                nickname="123", title="123", company="123",
                                address="123", home="123", mobile="123", work="123",
                                email="123"))
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    app.user.delete_user_by_index(index)
    new_users =  app.user.get_user_list()
   # assert len(old_users) - 1 == len(new_users)
   # old_users[index:index + 1] = []
    for i in new_users:
        if not (i in old_users):
            old_users.append(i)
    assert old_users == new_users

