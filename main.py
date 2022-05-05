from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/drives")
def drive():
    return render_template('drives.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/add")
def adddrive():
    return render_template('adddrive.html')

@app.route("/detail")
def detailpage():
    return render_template('detailpage.html')

@app.route("/learners")
def learners():
    return render_template('learners.html')

@app.route("/addlearner")
def addlearner():
    return render_template('addlearner.html')

@app.route("/adddetails")
def adddetails():
    return render_template('adddetails.html')
