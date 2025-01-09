from flask import Flask, request, redirect, url_for, make_response

app = Flask(__name__)
cookie_name = 'my_app_cookie'

users = {}
users['admin'] = '1234'

def validate_cookie(cookie):
    return True

@app.route('/')
def home():
    cookie = request.cookies.get(cookie_name)

    if not cookie:
        return redirect(url_for('login'), code=301)
    
    return "Hello World!\n"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return 
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        if (username == "Joey574" and password == "1234"):
            resp = make_response("Setting Cookie\n")
            resp.set_cookie(cookie_name, '1')

            return resp
        return "Invalid username or password\n", 400

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return "", 200



if (__name__ == '__main__'):
    app.run(debug=False)