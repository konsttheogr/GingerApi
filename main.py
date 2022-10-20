from flask import Flask, url_for, render_template, request
app = Flask(__name__)

print("https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application")
@app.route("/")
def hello_world(name='noname'):
    return f"<p>Hello, {name}!</p>"
    #render_template('hello.html', name=name)
    
"""<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}"""
    

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
    
"""   

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    

@app.route('/')
def index():
    resp = flask.make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
    
"""
