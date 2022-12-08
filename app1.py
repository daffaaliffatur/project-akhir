from flask import Flask,redirect, url_for,render_template,request
import os
from index import d_dtcn

secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True

@app.route("/",methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("camera.html")
    else:
        return render_template("index.html")

@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            d_dtcn()
            return render_template("index.html")
    else:
        return render_template("index.html")

@app.route('/about', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        return redirect(url_for("index"))
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
    
