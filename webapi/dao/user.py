def mock_auth_user(login_name, password) :
    return True, "succeed"


def mock_insert_user(login_name, pwd, phone, email, fullname, gender) :
    return True


def mock_update_user(login_name, pwd, phone, email, fullname, gender) :
    return True

def mock_show_basic_info(login_name) :
    return {"login name" : login_name,
            "fullname" : "test",
            "phone" : "12345678",
            "email" : "test@foo.com",
            "gender" : "male"}
