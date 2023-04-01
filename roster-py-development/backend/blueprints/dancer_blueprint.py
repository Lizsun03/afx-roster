# import blueprint class, and the make_response function
from flask import Blueprint, make_response
from flask import request

dancer_blueprint = Blueprint('dancer_blueprint', __name__)
# cur = conn.cursor()

'''
	router.HandleFunc("/api/auth/signup", signup(m, db)).Methods(http.MethodPost)
	router.HandleFunc("/api/auth/signin", signin(db)).Methods(http.MethodPost)
	router.HandleFunc("/api/auth/logout", logout).Methods(http.MethodPost)
	router.HandleFunc("/api/auth/verify", verify(db)).Methods(http.MethodPost)
	router.HandleFunc("/api/auth/sendreset", sendReset(m, db)).Methods(http.MethodPost)
	router.HandleFunc("/api/auth/resetpw", resetPassword(db)).Methods(http.MethodPost)
'''


@dancer_blueprint.route("/test")
def test():
    return "test"

# https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
'''
    returns in the format: 
    {id1: 
        {name: name, email: email, ...}, 
    id2: 
        {name: name, email: email, ...}, 
    }
'''
@dancer_blueprint.route("/dancer")
def dancers_index():
    cur.execute("SELECT * FROM DANCERS;")
    dancers = cur.fetchall()
    dancer_rows = ['name', 'email', 'phone', 'gender', 'year', 'dance_exp']
    ret = {}
    for dancer in dancers:
        other_rows = {}
        for i in range(len(dancer_rows)):
            other_rows[dancer_rows[i]] = dancer[i + 1]
        ret[dancer[0]] = other_rows
    return ret

'''
    returns in the format: 
    {name: name, email: email, ...}
'''
@dancer_blueprint.route("/dancer/<int:dancer_id>")
def dancer(dancer_id):
    cur.execute("SELECT * FROM DANCERS WHERE DANCER_ID == (%s) ;", (dancer_id, ))
    dancer = cur.fetchall()
    dancer_rows = ['name', 'email', 'phone', 'gender', 'year', 'dance_exp']
    ret = {}
    for i in range(len(dancer_rows)):
        ret[dancer_rows[i]] = dancer[0][i+1]
    return ret


    """
    instead of querying model, we can just use the database object directly
    then use the rows and put them into a dictionary
    JSON encode the dictionary and then return in the body of the response
    this makes it so we don't have to have a model for every type of data
    """

@dancer_blueprint.route("/dancer/add", methods=['GET', 'POST'])
def create_dancer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        year = request.form['year']
        dance_exp = request.form['dance_exp']
        sql = "INSERT INTO DANCERS (name, email, phone, gender, year, dance_exp) VALUES (%s, %s, %s, %s, %s, %s);"
        cur.execute(sql, (name, email, phone, gender, year, dance_exp))
        db.commit()
        # Change url for redirect
        return
    # What to return...?
    return 

@dancer_blueprint.route("/dancer/<int:dancer_id>/edit", methods=['GET', 'POST'])
def edit_dancer(dancer_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        year = request.form['year']
        dance_exp = request.form['dance_exp']
        sql = "UPDATE DANCERS SET NAME = (%s), EMAIL = (%s), PHONE = (%s), GENDER = (%s), YEAR = (%s), DANCE_EXP = (%s), WHERE DANCER_ID = (%s);"
        cur.execute(sql, (name, email, phone, gender, year, dance_exp, dancer_id))
        db.commit()
        return
    return

