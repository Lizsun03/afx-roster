from flask import Blueprint, make_response
from flask import request

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route("/user")
def users_index():
    cur.execute("SELECT * FROM USERS;")
    users = cur.fetchall()
    user_rows = ['role']
    ret = {}
    for user in users:
        other_rows = {}
        for i in range(len(user_rows)):
            other_rows[user_rows[i]] = user[i + 1]
        ret[user[0]] = other_rows
    return ret

@user_blueprint.route("/user/add", methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        role = request.form['role']
        sql = "INSERT INTO USERS (role) VALUES (%s, );"
        cur.execute(sql, (role))
        conn.commit()
        return
    return 

@user_blueprint.route("/user/<int:user_id>")
def user(user_id):
    cur.execute("SELECT * FROM USERS WHERE USER_ID == (%s) ;", (user_id, ))
    user = cur.fetchall()
    user_rows = ['role']
    ret = {}
    for i in range(len(user_rows)):
        ret[user_rows[i]] = user[0][i+1]
    return ret

@user_blueprint.route("/user/<int:user_id>/edit", methods=['GET', 'POST'])
def edit_dancer(user_id):
    if request.method == 'POST':
        role = request.form['role']
        sql = "UPDATE USERS SET ROLE = (%s), WHERE USER_ID = (%s);"
        cur.execute(sql, (role, dancer_id))
        conn.commit()
        return
    return
