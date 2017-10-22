from app import app, userfield as uf
from dto import user as userDTO
from flask import request, jsonify


@app.route("/login", methods=["POST"])
def login():
    user_info = request.get_json()
    login_name = user_info[uf.login_name]
    password = user_info[uf.password]
    auth, msg = userDTO.user_authentication(login_name, password)
    if not auth:
        return uf.LOGIN_ERROR
    else:
        return uf.LOGIN_SUCC


@app.route("/register", methods=["POST"])
def register():
    user_info = request.get_json()
    login_name = user_info[uf.login_name]
    password = user_info[uf.password]
    auth, msg = userDTO.user_authentication(login_name, password)
    if auth:
        return uf.REGISTER_ERROR
    phone = user_info[uf.phone]
    email = user_info[uf.email]
    fullname = user_info[uf.last_name] + user_info[uf.first_name]
    gender = user_info[uf.gender]
    return userDTO.add_user(login_name, password, phone, email, fullname, gender)


@app.route("/<login_name>/update", methods=["POST"])
def update(login_name):
    user_info = request.get_json()
    login_name = user_info[uf.login_name]
    password = user_info[uf.password]
    phone = user_info[uf.phone]
    email = user_info[uf.email]
    fullname = user_info[uf.last_name] + user_info[uf.first_name]
    gender = user_info[uf.gender]
    return userDTO.update_user(login_name, password, phone, email, fullname, gender)


@app.route("/<login_name>/basicinfo", methods=["GET"])
def show_basic_information(login_name) :
    return jsonify(userDTO.show_basic_information(login_name))