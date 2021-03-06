from flask import Flask , request,redirect , make_response, render_template

app = Flask(__name__)

todos = ['Buy Coffee', 'Generate sale voucher','Delivery Product']

@app.route('/')
def index():
	user_ip= request.remote_addr
	response = make_response(redirect('/hello'))
	response.set_cookie('user_ip',user_ip)
	
	return response
	
	
@app.route('/hello')
def hello():

	user_ip= request.cookies.get('user_ip')
	context = {
     'user_ip':user_ip, 
	 'todos':todos,
	}
	#return 'Hello World Flask!, tu ip es {}'.format(user_ip)
	#return render_template('hello.html',user_ip=user_ip, todos=todos)
	return render_template('hello.html',**context)


##set FLASK_APP=hello.py wn
##export FLASK_APP=hello.py lnx 
##FLASK_DEBUG=1
##302 code for redirect