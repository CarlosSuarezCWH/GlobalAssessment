from flask import Flask, request, render_template, session, redirect, url_for
from ObtainSkills import *
from query import *
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/insert")
def insert():
    return render_template("insert.html")

@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/panel", methods = ['POST', 'GET'])
def panel():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        email = request.values.get("email", None)
        password = request.values.get("password", None)
        sql = "SELECT * FROM students WHERE email = %s AND password = %s"
        val = [(email, password)]
        mycursor.executemany(sql, val)
        print("0")
        account = mycursor.fetchone()
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            print("1")
            return 'Logged in successfully!'
        else:
            print("2")
            return render_template("index.html")
    #return render_template('index.html', msg=msg)

@app.route('/panel/home')
def panel_home():
    if 'loggedin' in session:
        return render_template('panel.html', username=session['email'])
    return redirect(url_for('login'))

@app.route("/form")
def form():
    return render_template("form.html")
@app.errorhandler(404)
def notfound(error):
    return render_template('404.html'), 404
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        datos=[]
        datos.append(request.values.get("Name", None))
        datos.append(request.values.get("ID_student",None))
        datos.append(request.values.get("algebra", None))
        datos.append(request.values.get("programacion", None))
        datos.append(request.values.get("analisis", None))
        datos.append(request.values.get("comunicacion", None))
        datos.append(request.values.get("fisica", None))
        datos.append(request.values.get("ingenieria", None))
        datos.append(request.values.get("password", None))
        datos.append(request.values.get("ayudar", None))
        datos.append(str(1))
        datos.append(str(1))
        datos.append(request.values.get("hablar", None))
        datos.append(request.values.get("explicar", None))
        print(datos)
        #insert_students(datos)
        insert_crude(datos)
        return render_template("login.html")



if __name__== "__main__":
    app.run(debug=True)