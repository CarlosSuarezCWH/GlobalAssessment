from flask import Flask, request, render_template
from insert import *
from obtainForm import *
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
        Name= str(request.values.get("Name", None))
        ID_student= str(request.values.get("ID_student",None))
        algebra = float(request.values.get("algebra", None))
        programacion = float(request.values.get("programacion", None))
        analisis = float(request.values.get("analisis", None))
        comunicacion = float(request.values.get("comunicacion", None))
        fisica = float(request.values.get("fisica", None))
        ingenieria = float(request.values.get("ingenieria", None))
        password = request.values.get("password", None)
        quiere_ayudar= str(request.values.get("ayudar", None))
        puede_ayudar=str(1)
        socializar = str(1)
        hablar = str(request.values.get("hablar", None))
        explicar = float(request.values.get("explicar", None))
        Skills=Calculate(algebra, programacion, analisis, comunicacion, fisica, ingenieria, hablar, explicar, socializar, puede_ayudar,quiere_ayudar)
        insert_crude()
        return str(Skills)
if __name__== "__main__":
    app.run(debug=True)