from flask import Flask, request, render_template
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
@app.route("/login")
def login():
    return render_template("login.html")
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
        return str(datos)


if __name__== "__main__":
    app.run(debug=True)