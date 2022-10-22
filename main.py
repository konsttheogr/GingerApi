from flask import Flask, url_for, render_template, request
#from requests_html import HTML
import os
app = Flask(__name__)

print("https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application")

psw = os.environ['psw']
@app.route(f"/{psw}/hello/<name>")
def hello(name):
    return f"<p>Hello, {name}!</p>"
    
@app.route(f"/{psw}/check")
def check():
    return '200'
 
@app.route(f"/{psw}/template/<template>")
def teplate(template, a=None, b=None, c=None, d=None):
    print(args)
    return render_template(template, arg1=a)

"""
with open('templates/test.html') as f:
    source = f.read()
    html = HTML(html=source)
    print(f"{html.text} \n\n\n\n\n {html.html} \n\n\n\n Title: {html.find('title')[0].text}")
    

<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}"""
    
"""
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv("PORT", default=5000))
