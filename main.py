from flask import Flask,render_template,Blueprint,app, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import *
import os
from flask_migrate import Migrate
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from constants.http_status_codes import HTTP_200_OK,HTTP_401_UNAUTHORIZED
from flask_jwt_extended import JWTManager
JWT_SECRET_KEY=os.environ.get('jwt_secret_key')
app = Flask(__name__)
jwt=JWTManager(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:UPGRAD@localhost/placement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
migrate=Migrate(app,db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    # is_superuser=db.Column(Boolean, unique=False,default=False)
    # is_active=db.Column(Boolean, unique=False,default=True)

    def __repr__(self):
        return f'<User: {self.email}>'

db.create_all()

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/drives")
def drive():
    return render_template('drives.html')

# @app.route("/login")
# def login():
#     return render_template('login.html')

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

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/applicants")
def applicants():
    return render_template('applicants.html')

@app.post('/api/login')
def userlogin():
    email = request.json.get('email', '')
    user = User.query.filter_by(email=email).first()

    if user:
        refresh = create_refresh_token(identity=user.id)
        access = create_access_token(identity=user.id)

        return jsonify({
                'user': {
                    'refresh': refresh,
                    'access': access,
                    'email': user.email
                }

            }), HTTP_200_OK

    return jsonify({'error': 'This email id is not registered. Please contact admin.'}), HTTP_401_UNAUTHORIZED
