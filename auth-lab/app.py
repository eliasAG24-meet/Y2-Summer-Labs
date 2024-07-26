from flask import Flask, session, render_template, url_for, redirect, request
import pyrebase
Config = {
  'apiKey': "AIzaSyD-oNqjqI-V20lo9du9QMp3W9vsM4ylwuM",
  'authDomain': "auth-lab-f3552.firebaseapp.com",
  'projectId': "auth-lab-f3552",
  'storageBucket': "auth-lab-f3552.appspot.com",
  'messagingSenderId': "424070432103",
  'appId': "1:424070432103:web:4e1abff0bff2fdb4bfdbc2",
  'measurementId': "G-QYVLEVTMJQ",
  'databaseURL':"https://auth-lab-f3552-default-rtdb.europe-west1.firebasedatabase.app/"

}

firebase = pyrebase.initialize_app(Config)
db = firebase.database()
auth = firebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/home', methods=['GET', 'POST'])
def home() :
  if request.method == 'POST' :
    session['user'] 
    session['quotes'] = []

    session['quotes'].append(request.form['quo'])
    return render_template('thanks.html')
  else :
    return render_template('home.html')

@app.route('/display', methods = ['GET','POST'])
def display():
  return render_template('display.html')

@app.route('/thanks', methods = ['GET','POST'])
def thanks():
  return render_template('thanks.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
  error = ""
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    user1 = {'fullName':"",'email':"",'username':""}
    try :
      session['user'] = auth.create_user_with_email_and_password(email,password)
      session['quotes'] = []
      uid = session['user']['localId']
      db.child('Users').child(uid).set(user1)
      return redirect(url_for('home'))
    except :
      error = "Authentication failed"
  return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin() :
  error = ""
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try :
      user = auth.sign_in_with_email_and_password(email,password)
      session['user'] = user
      session['quotes'] = []

      
      return redirect(url_for('home'))
    except :
      error = "Authentication failed"
      return redirect(url_for('signin'))
  return render_template('signin.html')

@app.route('/signout',methods=['GET', 'POST'])
def signout():
  session['user'] = None
  session['email'] = None
  session['password'] = None
  auth.current_user = None
  return redirect(url_for('signin'))
  return render_template('signin.html')









if __name__ == '__main__':
    app.run(debug=True)
