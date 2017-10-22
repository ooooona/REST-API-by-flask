from dao import user as userDAO

def user_authentication(login_name, password) :
    return userDAO.mock_auth_user(login_name, password)


def add_user(login_name, pwd, phone, email, fullname, gender) :
    return userDAO.mock_insert_user(login_name, pwd, phone, email, fullname, gender)


def update_user(login_name, pwd, phone, email, fullname, gender) :
    return userDAO.mock_update_user(login_name, pwd, phone, email, fullname, gender)
