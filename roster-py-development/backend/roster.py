# TODO @kjin if we decide to modularize the seed function later then we can uncomment this
# import sys, os
# # Add the path to seed directory so we can import database seeding module
# sys.path.append(os.path.join(os.getcwd(),'seed'))
# import seed
from flask import Flask, redirect, url_for
from flask_cors import CORS
from blueprints.admin_blueprint import admin_blueprint
from blueprints.team_blueprint import team_blueprint
from blueprints.dancer_blueprint import dancer_blueprint
from blueprints.user_blueprint import user_blueprint
from flask import render_template
from flask import make_response
from flask import request
from flask_migrate import Migrate
import os
import time
from database import db # Import SQLAlchemy instance
from models import Dancer, Team, User
import db_config

from enum import Enum


# NOTE: sqlalchemy provides us with a DRY way to make queries to the database by allowing us to 
# take full advantage of the code structure of our models.
app = Flask(__name__)
print("connecting to postgres...", flush=True)
#clean this url up using format string
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5000/roster"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@172.28.1.2:5432/roster"
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("connected to postgres", flush=True)
db.init_app(app)
migrate = Migrate(app, db)

CORS(app)

#Connect to the  Database
#########################################
db_name = db_config.db_name
db_user = db_config.db_user
db_pass = db_config.db_pass
db_host = db_config.db_host
db_port = db_config.db_port
connected = False

# Handles seeding of the database
def seed_database(db):
    print("hello world seeding")
    db.session.add(User("kevin", "kevin", "kevin"))
    db.session.add(User("anson", "anson", "anson"))
    db.session.add(Team("project", "aimbot", "tonight", False, 20, "yuwen's mom's house"))
    db.session.add(Dancer(1, "anusha", "a@a.com", "000", "female", "junior", "1"))
    print("Committing...")
    db.session.commit()


print("Creating database...")
# App context required because we are operating outside Flask view/blueprint: see https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
with app.app_context():
    db.create_all() 
    db.session.commit()
    # TODO seed here?
    print("Seeding database...")
    seed_database(db)

'''
This needs to be in the app somewhere to avoid 404 errors. Also, we should place
methods that instantiate model instances (e.g. a User object) in this file to avoid 
circular import errors.
'''
@app.route('/')
def home():
    return render_template('index.html')
@app.route("/test/<name>")
def test(name):
    new_user = User(name, name, "123")
    db.session.add(new_user)
    db.session.commit()
    all_users = User.query.all()
    results = [{"name": u.name,"password": u.password,"username": u.username} for u in all_users]
    return str(results)
    #return 'test %s!' % new_user.get_name()

#For testing purposes only
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['Username']
        return redirect(url_for('test', name=user))
    else:
        user = request.args.get('Username')
        return redirect(url_for('test', name=user))


#register blueprints
app.register_blueprint(admin_blueprint)
app.register_blueprint(dancer_blueprint)
app.register_blueprint(team_blueprint)
app.register_blueprint(user_blueprint)

    

if __name__ == "__main__":
    #run the app on port 5000

    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)