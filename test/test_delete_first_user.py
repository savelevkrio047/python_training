from model.contact import Contact

def test_delete_first_user(app):
    if app.user.count() == 0:
        app.user.create(Contact(firstname="123", secondname="312", surname="123",
                                nickname="123", title="123", company="123",
                                address="123", home="123", mobile="123", work="123",
                                email="123"))
    app.user.delete_first_user()
