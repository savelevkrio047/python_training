from model.contact import Contact
from fixture.user import UserHelper



def test_modify_users_fio(app):
    if app.user.count() == 0:
        app.user.create(Contact(firstname="123", secondname="312", surname="123",
                            nickname="123", title="123", company="123",
                            address="123", home="123", mobile="123", work="123",
                            email="123"))
    app.user.modify_first_user(Contact(firstname="change1", secondname="change2", surname="family1"))





def test_modify_users_titlecomandhomemobile(app):
    if app.user.count() == 0:
        app.user.create(Contact(firstname="123", secondname="312", surname="123",
                            nickname="123", title="qqqq", company="wwww",
                            address="eeee", home="ww", mobile="dddd", work="123",
                            email="123"))
    app.user.modify_first_user(Contact(firstname="change1", secondname="change2", surname="family1"))