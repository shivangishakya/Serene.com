from flask import Flask, jsonify, request, g
from flask_cors import CORS
from functools import wraps
from sqlite3 import dbapi2 as sqlite3
import toml, sqlite3, textwrap
import pickle, warnings
import requests
from datetime import datetime
import os
import weasyprint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from helper import stress_desc, format_survey



############################################################
#
#                      APP INITIALIZATION
#
############################################################

app = Flask(__name__)
app.config.from_file(f"./etc/users.toml", toml.load)
CORS(app, resources={r'/*': {'origins': '*'}})

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

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
        
    responses = format_survey(jsondata)

    url = 'http://localhost:3000/predict'
    r = requests.post(url,json=responses)
    print(r.json())

    return r

@app.route('/insert-recipient', methods=['POST'])
@login_required
def insert_recp():
    recp = request.get_json()
    auth = request.authorization
    query = """Update users set recipient = ? where username = ?"""
    data = (recp["recipient"], auth.username)
    insert_query_db(query=query, args=data)
    return jsonify({"msg": "INSERTED"})

 
@app.route('/generate-pdf', methods=['POST'])
@login_required
def generate_pdf():
    # Generate PDF report
    auth = request.authorization
    query = "SELECT * FROM users"
    users = query_db(query=query,)
    
    recp = None
    for user in users:
        if auth.username == str(user["username"]):
            recp = user["recipient"]
            break
    print(recp)
    if recp is None or recp == "":
        return "RECIPIENT EMAIL IS EMPTY"

    val = int(request.get_json()["val"])

    html = '''
    <html>
        <head>
            <title>Stress Report</title>
        </head>
        <body>
            <h1>Report of {}</h1>
            <p>Generated on {}</p>
            <h3>Your Stress Level is predicted as {}</h3>
            <h2>Please follow the below tips</h2>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
        </body>
    </html>
    '''.format(auth.username, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), val, stress_desc(val)[0], stress_desc(val)[1], stress_desc(val)[2], stress_desc(val)[3], stress_desc(val)[4])

    pdf = weasyprint.HTML(string=html).write_pdf()

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = 'shivangi.shakya@gmail.com'
    msg['To'] = str(recp)
    msg['Subject'] = 'PDF Generated'

    # Attach PDF file to email
    part = MIMEApplication(pdf, Name="report.pdf")
    part['Content-Disposition'] = 'attachment; filename="report.pdf"'
    msg.attach(part)

    # Send the email
    smtp = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
    smtp.starttls()
    smtp.login('shivangi.shakya@gmail.com', 'xhJgW92yLczt1M5D')
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()

    return 'Email sent with PDF attachment!'