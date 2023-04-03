# Flask Setup
Begin by creating a new project directory:

$ mkdir flask-vue-crud
$ cd flask-vue-crud

## Within "flask-vue-crud", create a new directory called "server". Then, create and activate a virtual environment inside the "server" directory:

$ python3 -m venv env
$ source env/bin/activate
(env)$

The above commands may differ depending on your environment.

## Install Flask along with the Flask-CORS extension:

(env)$ pip install Flask Flask-Cors

link: https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
https://auth0.com/blog/beginner-vuejs-tutorial-with-user-login/
https://towardsdatascience.com/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4


./bin/init.sh
foreman start

NiginX
Default config -> /usr/local/etc/nginx/nginx.conf
New server:
launchctl unload /usr/local/cellar/nginx/1.23.3/homebrew.mxcl.nginx.plist
launchctl load /usr/local/cellar/nginx/1.23.3/homebrew.mxcl.nginx.plist

OR

brew services stop nginx
brew services start nginx
brew services restart nginx

sudo nano /usr/local/etc/nginx/nginx.conf 
sudo nano /usr/local/etc/nginx/conf.d/helloserene.com.conf

Kill Process 80:
sudo kill -9 $(sudo lsof -ti :80)

WEBSITE: http://helloserene.com/

Add host to macOS:
sudo nano /etc/hosts

### ENDPOINT 1: @app.route("/register/", methods=["POST"])
This endpoint is used for registering a user/creating an account for a user to authenticate themselves.
ex:
 http POST http://helloserene.com/register/ username=310 password=absd

### ENDPOINT 2: @app.route("/login/", methods=["POST"])
This endpoint is used for logging in and authenticating a user, if their account already exists.
ex:
 http --auth 310:absd --auth-type basic GET http://helloserene.com/login/
After executing, the users table is checked to see if the specified user's account exists and authenticates if the password is correct.

### ENDPOINT 4: @app.route("/predict", methods=["POST"])
This endpoint is used for predicting the stress level.
ex:
http --auth 310:absd --auth-type basic POST http://127.0.0.1:3000/predict

### ENDPOINT 4: @app.route("/insert-recipient", methods=["POST"])
This endpoint is used for inserting recipient email.
ex:
http --auth 310:absd --auth-type basic POST http://127.0.0.1:3000/insert-recipient recipient=vatsalmakani@yahoo.com

### ENDPOINT 5: @app.route("/generate-pdf", methods=["POST"])
This endpoint is used for generating PDF for the report and sending to the recipient added.
ex:
http --auth 310:absd --auth-type basic POST http://127.0.0.1:3000/generate-pdf val=3


python3 request.py

