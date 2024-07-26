from flask import Flask,render_template,url_for,redirect,request, session
import pyrebase
from firebase_admin import credentials, initialize_app, storage


firebaseConfig = {
  "apiKey": "AIzaSyBke4FWtl2eGvXXPLDGkxcMxWvy6QMuAhU",
  "authDomain": "indivproject-4c0e8.firebaseapp.com",
  "projectId": "indivproject-4c0e8",
  "storageBucket": "indivproject-4c0e8.appspot.com",
  "messagingSenderId": "476203652110",
  "appId": "1:476203652110:web:648b31babed052cbe3985f",
  "measurementId": "G-9FSCWXTQ8R",
  "databaseURL": "https://indivproject-4c0e8-default-rtdb.europe-west1.firebasedatabase.app/"
  }


# Init firebase with your credentials
# cred = credentials.RefreshToken('db.json')
# initialize_app(cred, {'storageBucket': "indivproject-4c0e8.appspot.com"})

# default_app = firebase_admin.initialize_app(cred)





firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
storage = firebase.storage()

@app.route('/review/<genre>', methods=['GET','POST'])
def review(genre):
	revs = db.child('review').child(genre).get().val()
	return render_template('review.html', revs = revs, genre = genre)

@app.route('/home', methods = ['GET','POST'])
def home():
	if request.method == 'POST':
		b = request.form['songs']
		return redirect(url_for('songs', genre = b))
	return render_template('home.html')


@app.route('/songs/<genre>', methods=['GET', 'POST'])
def songs(genre):
	songs_dict = db.child('songs').child(genre).get().val()
	print(songs_dict)
	return render_template('songs.html', genre = genre, songs_dict = songs_dict)
	if request.method =='POST':
		review = request.form['name']
		db.child('review').child(genre).set({"review" : review})
		return redirect('/songs/<genre>')
	return render_template('home.html')
		
@app.route('/', methods=['GET','POST'])
def welcome():
	return render_template('welcome.html')
	
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error = ""
	if request.method == 'POST':
		username = request.form['username']
		email = request.form['email']
		password = request.form['password']


		try:
			session['user'] = auth.create_user_with_email_and_password(email,password)

			return redirect(url_for('home'))
		except Exception as e:
			print(e)
			error = "Authentication failed"
			return render_template('signup.html')
	return render_template('signup.html')

@app.route('/signin', methods=['GET','POST'])
def signin():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try :
			session['user'] = auth.sign_in_with_email_and_password(email,password)
			return redirect(url_for('home'))
		except :
			error = "Authentication failed"
			print(error)
			return render_template('signin.html')
	return render_template('signin.html')


@app.route('/signout',methods=['GET', 'POST'])
def signout():
  session['user'] = None
  auth.current_username = None
  return redirect(url_for('welcome'))

@app.route('/pop', methods=['GET','POST'])
def pop():
	return render_template('pop.html')

@app.route('/rock', methods=['GET','POST'])
def rock():
	return render_template('rock.html')

@app.route('/jazz', methods=['GET','POST'])
def jazz():
	return render_template('jazz.html')

@app.route('/indie', methods=['GET','POST'])
def indie():
	return render_template('indie.html')
def add():
    # if request.method == 'POST':
    #     file = request.files['file']
    #     if file:
    #         filename = file.filename
    #         file_path = os.path.join('uploads', filename)
    #         file.save(file_path)

          
    #         storage.child(f"audio/{filename}").put(file_path)
    #         file_url = storage.child(f"audio/{filename}").get_url(None)

    #         os.remove(file_path) 
    #         user = session.get('user')
    #         if user:
    #             user_id = user['localId']
    #             db.child("favorites").child(user_id).push({"filename": filename, "url": file_url})

    #         return redirect(url_for('home', url=file_url))
    return render_template('pop.html')

if __name__ == '__main__':
    app.run(debug=True)  