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

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data.
    res = create_data(data)
    prediction = model.predict([res])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify({"message:": str(output)})