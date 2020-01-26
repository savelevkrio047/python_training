from model.contact import Contact
from fixture.user import UserHelper



def test_modify_users_fio(app):
    if app.user.count() == 0:
        app.user.create(Contact(firstname="Геннадий1",
        lastname="Савельев1",
        homephone="4302014",
        mobilephone="89200101840",
        workphone="89087380653",
        secondaryphone="89107380653"))
    app.user.modify_first_user(Contact(firstname="change1", lastname="change2", homephone="4301932"))





def test_modify_users_titlecomandhomemobile(app):
    if app.user.count() == 0:
        app.user.create(Contact(firstname="Геннадий1",
                               lastname="Савельев1",
                               homephone="4302014",
                               mobilephone="89200101840",
                               workphone="89087380653",
                               secondaryphone="89107380653"))
    app.user.modify_first_user(Contact(firstname="change2", lastname="change2", homephone="1234567"))