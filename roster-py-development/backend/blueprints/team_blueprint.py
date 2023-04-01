# import blueprint class, and the make_response function
from flask import Blueprint, make_response
from flask import request
from database import db

team_blueprint = Blueprint('team_blueprint', __name__)


print("hello")

@team_blueprint.route("/team/<int:team_id>")
def team(team_id):
    cur.execute("SELECT * FROM TEAM WHERE TEAM_ID == (%s) ;", (team_id, ))
    team = cur.fetchall()
    team_rows = ['level', 'prac_time', 'prac_loc', 'dir_names']
    ret = {}
    for i in range(len(team_rows)):
        ret[team_rows[i]] = team[0][i+1]
    return ret

@team_blueprint.route("/team/add", methods=['GET', 'POST'])
def create_team():
    if request.method == 'POST':
        level = request.form['level']
        prac_time = request.form['prac_time']
        prac_loc = request.form['prac_loc']
        dir_names = request.form['dir_names']
        sql = "INSERT INTO TEAMS (level, prac_time, prac_loc, dir_names) VALUES (%s, %s, %s, %s, );"
        cur.execute(sql, (level, prac_time, prac_loc, dir_names))
        db.commit()
        # Change url for redirect
        return
    # What to return...?
    return 

@team_blueprint.route("/team/<int:dancer_id>/edit", methods=['GET', 'POST'])
def edit_team(team_id):
    if request.method == 'POST':
        level = request.form['level']
        prac_time = request.form['prac_time']
        prac_loc = request.form['prac_loc']
        dir_names = request.form['dir_names']
        sql = "UPDATE TEAMS SET LEVEL = (%s), PRAC_TIME = (%s), PRAC_LOC = (%s), DIR_NAMES = (%s), WHERE TEAM_ID = (%s);"
        cur.execute(sql, (level, prac_time, prac_loc, dir_names, team_id))
        db.commit()
        return
    return

@team_blueprint.route("/team")
def team_index():
    cur.execute("SELECT * FROM TEAMS;")
    teams = cur.fetchall()
    team_rows = ['level', 'prac_time', 'prac_loc', 'dir_names']
    ret = {}
    for team in teams:
        other_rows = {}
        for i in range(len(team_rows)):
            other_rows[team_rows[i]] = team[i + 1]
        ret[team[0]] = other_rows
    return ret

@team_blueprint.route("/team/<int:dancer_id>/add", methods=['GET', 'POST'])
def add_to_team(team_id):
    if request.method == 'POST':
        dancer_ids = request.form['dancer_ids']
        sql = "UPDATE DANCERS SET TEAM_ID = (%s), WHERE DANCER_ID = (%s);"
        for dancer_id in dancer_ids: 
            cur.execute(sql, (team_id, dancer_id))
        conn.commit()
        return
    return