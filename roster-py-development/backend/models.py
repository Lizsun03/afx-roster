"""DB not connected yet"""
from database import db

from enum import Enum

'''
 Models
''' 
class Dancer(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    year = db.Column(db.String(15), nullable=False)
    dance_exp = db.Column(db.String(4), nullable=False)

    def __init__(self, team_id, name, email, phone, gender, year, dance_exp):
        self.team_id = team_id
        self.name = name
        self.email = email
        self.phone = phone
        self.gender = gender
        self.year = year
        self.dance_exp = dance_exp

#Creates a Level Enum denoting the level - training, project, or comp - of a dancer
class Level(Enum):

    training = 0
    project = 0
    comp = 0




class Team(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    prac_time = db.Column(db.String(50), nullable=False)
    is_locked = db.Column(db.Boolean, nullable=False)
    max_picks = db.Column(db.Integer, nullable=False)
    prac_loc = db.Column(db.String(100), nullable=False)
    dancers = db.relationship('Dancer', backref='teams', lazy=True)
    #Create Column object for director names
    dirs = db.relationship('User', backref='teams', lazy=True)
    

    def __init__(self, level, name, prac_time, is_locked, max_picks, prac_loc):
        self.level = level
        self.name = name
        self.prac_time = prac_time
        self.is_locked = is_locked
        self.max_picks = max_picks
        self.prac_loc = prac_loc
        # Initialize director

class Role(Enum):
    
    DIRECTOR = 1
    ADMIN = 2
    MEMBER = 3

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.Enum(Role), default = Role.MEMBER, nullable = False)
    username = db.Column(db.String(64),index=False,unique=True,nullable=False)
    name = db.Column(db.String(100))
    password = db.Column(db.String(255), nullable=False)
    #created = db.Column(db.DateTime,index=False,unique=False,nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    #TODO: Admin User belongs to all teams

    def __init__(self, name, username, password, role=Role.MEMBER):
        self.role = role
        self.name = name
        self.username = username
        # self.password = self.generate_pwd_hash(password)
        self.password = password
        self.create_user()
    
    # @staticmethod
    # def generate_pwd_hash(password):
    #     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    def create_user(self):
        postgreSQL_addUser_Query = "INSERT INTO users (role, name, username, password, team_id) VALUES ({role}, {name}, {username}, {password}, {team_id})".format(role=self.role, 
        name=self.name, username = self.username, password=self.password, team_id=0)


        print(postgreSQL_addUser_Query)
    
    def get_name(self):
        return self.name
    
    def get_role(self):
        return self.role
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
