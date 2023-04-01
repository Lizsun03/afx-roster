# import blueprint class, and the make_response function
from flask import Blueprint, make_response, request, redirect, url_for
import sys

admin_blueprint = Blueprint('admin_blueprint', __name__, url_prefix='/auth')

'''
	router.HandleFunc("/api/auth/signup", signup(m, db)).Methods(http.MethodPost)
	router.HandleFunc("/api/auth/signin", signin(db)).Methods(http.MethodPost)
	router.HandleFunc("/api/auth/logout", logout).Methods(http.MethodPost)
	router.HandleFunc("/api/auth/verify", verify(db)).Methods(http.MethodPost)
	router.HandleFunc("/api/auth/sendreset", sendReset(m, db)).Methods(http.MethodPost)
	router.HandleFunc("/api/auth/resetpw", resetPassword(db)).Methods(http.MethodPost)
'''

@admin_blueprint.route('/signup', methods = ['POST'])
def signup():
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    res = make_response()
    res.set_cookie("test", value=encoded_jwt)
    return res

@admin_blueprint.route("/test/<name>", methods = ['GET'])
def test(name):
    return 'test %s!' % name

#For testing purposes only
@admin_blueprint.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['Username']
        return redirect(url_for('admin_blueprint.test', name=user), code=303)
    else:
        user = request.args.get('Username')
        return redirect(url_for('admin_blueprint.test', name=user), code=303)


@admin_blueprint.route('/signin', methods = ['POST'])
def signin():
	'''
		-Get username and password from the request
		-Check if username and password are in the database User
			-If True:
				-Create cookie
			-Else:
				-Redirect to log in page	
	'''

	#TODO

	return None


@admin_blueprint.route('/logout', methods = ['POST'])
def logout():
	'''
		-Check if a User is signed in
			-If True
				-Destroy the cookie
		-(Actually, the logout button should only show on the app if there is a User logged in.)
	'''

	#TODO

	return None

@admin_blueprint.route('/sendreset', methods = ['POST'])
def send_reset():

	#TODO

	return None

@admin_blueprint.route('/resetpw', methods = ['POST'])
def reset_password():

	#TODO

	return None

