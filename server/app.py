from flask import Flask, jsonify, request, g
from flask_cors import CORS
from functools import wraps
from sqlite3 import dbapi2 as sqlite3
import toml, sqlite3, textwrap
import numpy as np
import pickle, sklearn, pandas as pd, warnings
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
import csv, openpyxl, requests



############################################################
#
#                      APP INITIALIZATION
#
############################################################

app = Flask(__name__)
app.config.from_file(f"./etc/users.toml", toml.load)
CORS(app, resources={r'/*': {'origins': '*'}})

# Load the model
model = pickle.load(open('./static/model.pkl','rb'))
warnings.simplefilter(action="ignore", category=FutureWarning)

############################################################
#
#                      DATABASE FUNCTIONS
#
############################################################

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, \
                value in enumerate(row))

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(app.config["DATABASE"])
        db.row_factory = make_dicts
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_query_db(query, args=()):
    cur = get_db()
    cur.execute(query, args)
    cur.commit()

@app.cli.command("init")
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("books.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()

############################################################
#
#                  HELPER FUNCTIONS
#
############################################################

def check_auth(username):
    query = "SELECT * FROM users"
    users = query_db(query=query,)
    for user in users:
        if username == str(user["username"]):
            return True
    return False

def login_required(f):
    """ basic auth for api """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username):
            return jsonify({'message': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated_function

def create_data(data):
    res = []
    list_cols = ['Academics', 'Looks_Fitness', 'Social_life', \
                 'Xtra_curricular', 'Athletics', 'Career', \
                    'Finance', 'Relationship', 'Cultural_Shock',\
                    'Emotional_bullied', 'Physical_bullied',\
                    'Verbal_bullied', 'Social_bullied',\
                    'Cyber_bullied', 'International',\
                    'Miss_home', 'Family_friends',\
                    'Food', 'Sensory', \
                    'Miss_social', \
                    'Native_language', 'Courses', 'Loan', \
                    'Stressed_commute']
    for i in list_cols:
        if i == 'Courses':
            if data['Courses'] == 3:
                res.append(1)
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(0)
            elif data['Courses'] == 2:
                res.append(0)
                res.append(1)
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(0)
            elif data['Courses'] == 4:
                res.append(0)
                res.append(0)
                res.append(1)
                res.append(0)
                res.append(0)
                res.append(0)
            elif data['Courses'] == 0:
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(1)
                res.append(0)
                res.append(0)
            elif data['Courses'] == 5:
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(1)
                res.append(0)
            elif data['Courses'] == 1:
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(1)
                res.append(0)
            else:
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(0)
                res.append(0)
        else:
            if data[i] == 1:
                res.append(1)
                res.append(0)
            else:
                res.append(0)
                res.append(1)
    return res


############################################################
#
#                           APIs
#
############################################################

############################################################
#                    1. HOMEPAGE
############################################################

@app.route("/", methods=["GET"])
def home():
    return textwrap.dedent(
        """
        <h1>Welcome Students</h1>
        <p>Don't Worry about Anything. Track your mental\
              health by calculating your stress levels in \
                just few minutes.</p>\n
        <p>So Start Now!!!</p>\n
    """
    )

############################################################
#                    2. USER REGISTRATION
############################################################

@app.route("/register/", methods=["POST"])
def create_user():
    data = request.get_json()
    print (data)
    if check_auth(data['username']):
        return jsonify({"message": "User  Already Exists"})
    user_data = f"{data['username']} {data['password']}"
    app.logger.debug(user_data)
    query = "INSERT INTO users(username, password) VALUES (?, ?)"
    values = (data['username'], data['password'])
    insert_query_db(query, values)
    return jsonify({"authenticated": "true"})

############################################################
#                    3. USER LOGIN
############################################################

@app.route('/login/', methods=['GET'])
@login_required
def login():
    auth = request.authorization
    print("AUTH: ", auth)
    print("REQUEST HEADERS:\n", request.headers)
    Headers = str(request.headers)
    return jsonify({"authenticated": "true" ,"Auth_Headers": Headers})

############################################################
#                    4. MODEL PREDICTION
############################################################

@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.json
    # Make prediction using model loaded from disk as per the data.
    features = [[data['Academics'], data['Looks_Fitness'], data['Social_life'], data['Xtra_curricular'], data['Athletics'], data['Career'], data['Finance'], data['Relationship'], data['Cultural_Shock'], data['Emotional_bullied'], data['Physical_bullied'], data['Verbal_bullied'], data['Social_bullied'], data['Cyber_bullied'], data['International'], data['Miss_home'], data['Family_friends'], data['Food'], data['Sensory'], data['Miss_social'], data['Native_language'], data['Courses'], data['Loan'], data['Stressed_commute']]]
    prediction = model.predict(features)[0]
    # Take the first value of prediction
    response = {'prediction': int(prediction)}
    return jsonify({"message:": str(response)})

@app.route('/api/surveys',methods=['POST'])
def surveys():
    # Get the data from the POST request.
    jsondata = request.get_json()
    for i in range(len(jsondata)):
        jsondata[i] = ''.join(jsondata[i])
        
    ques = ['Primary Reasons of Stress', 'Have you been bullied?', \
            'Are you an International Student?', 'What do you miss the most about your home?',\
                  'How many courses you have taken?', 'Financing the education', \
                    'Is your commute to college stressful?']
    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(ques)
    ws.append(jsondata)

    wb.save('quiz.xlsx')
    rbook = openpyxl.load_workbook('quiz.xlsx', data_only=True)
    rsheet = rbook.active

    responses = {}
    data = rsheet.cell(row=2, column=1).value
    if "Academic" in data:
        responses["Academics"] = 1
    else:
        responses["Academics"] = 0
    if "fitness" in data:
        responses["Looks_Fitness"] = 1
    else:
        responses["Looks_Fitness"] = 0
    if "Social" in data:
        responses["Social_life"] = 1
    else:
        responses["Social_life"] = 0
    if "extra-curricular" in data:
        responses["Xtra_curricular"] = 1
    else:
        responses["Xtra_curricular"] = 0
    if "Athletic" in data:
        responses["Athletics"] = 1
    else:
        responses["Athletics"] = 0
    if "Career" in data:
        responses["Career"] = 1
    else:
        responses["Career"] = 0
    if "Financial" in data:
        responses["Finance"] = 1
    else:
        responses["Finance"] = 0
    if "Relationship" in data:
        responses["Relationship"] = 1
    else:
        responses["Relationship"] = 0
    if "Cultural" in data:
        responses["Cultural_Shock"] = 1
    else:
        responses["Cultural_Shock"] = 0

    data = rsheet.cell(row=2, column=2).value
    if "Mentally/emotionally bullied" in data:
        responses["Emotional_bullied"] = 1
    else:
        responses["Emotional_bullied"] = 0
    if "Physically bullied" in data:
        responses["Physical_bullied"] = 1
    else:
        responses["Physical_bullied"] = 0
    if "Verbal bullying" in data:
        responses["Verbal_bullied"] = 1
    else:
        responses["Verbal_bullied"] = 0
    if "Social bullying" in data:
        responses["Social_bullied"] = 1
    else:
        responses["Social_bullied"] = 0
    if "Cyber bullying" in data:
        responses["Cyber_bullied"] = 1
    else:
        responses["Cyber_bullied"] = 0

    data = rsheet.cell(row=2, column=3).value
    if "Yes" in data:
        responses["International"] = 1
    else:
        responses["International"] = 0

    data = rsheet.cell(row=2, column=4).value
    if "No, I don't miss my home" in data:
        responses["Miss_home"] = 0
    else:
        responses["Miss_home"] = 1
    if "Yes, Family and friends" in data:
        responses["Family_friends"] = 1
    else:
        responses["Family_friends"] = 0
    if "Yes, Food" in data:
        responses["Food"] = 1
    else:
        responses["Food"] = 0
    if "Yes, Sensory experience of staying in home" in data:
        responses["Sensory"] = 1
    else:
        responses["Sensory"] = 0
    if "Yes, Social life of my hometown" in data:
        responses["Miss_social"] = 1
    else:
        responses["Miss_social"] = 0
    if "Yes, Native language conversations" in data:
        responses["Native_language"] = 1
    else:
        responses["Native_language"] = 0
    
    data = rsheet.cell(row=2, column=5).value
    if data == 1:
        responses["Courses"] = 1
    elif data == 2:
        responses["Courses"] = 2
    elif data == 3:
        responses["Courses"] = 3
    elif data == 4:
        responses["Courses"] = 4
    elif data == "More than 4":
        responses["Courses"] = 5
    else:
        responses["Courses"] = 0

    data = rsheet.cell(row=2, column=6).value
    if "Loan" in data:
        responses["Loan"] = 1
    else:
        responses["Loan"] = 0

    data = rsheet.cell(row=2, column=7).value
    if "Yes" in data or "Maybe" in data:
        responses["Stressed_commute"] = 1
    else:
        responses["Stressed_commute"] = 0

    url = 'http://localhost:3000/predict'
    r = requests.post(url,json=responses)
    print(r.json())

    return data
    