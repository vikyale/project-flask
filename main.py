from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World Flask'
	
##set FLASK_APP=hello.py wn
##export FLASK_APP=hello.py lnx 