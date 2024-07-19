from flask import Flask, render_template, url_for, redirect, request
import random

app = Flask(__name__, template_folder='Templates', static_folder='static')
@app.route('/home', methods = ['GET','POST'])
def home():
    
    if request.method == 'GET':
        return render_template('home.html')
    else :
        b = request.form['birthmonth']
        return redirect(url_for('fortune', bu = b))
    return render_template("home.html")

@app.route('/fortune/<bu>')
def fortune(bu):
    bo = len(bu)
    if bo > 12:
        return render_template("home.html")
    else:
        fortune1 = ['youre going to eat raw meat today','your baddies will not play DTI with you','you are so not watermelon tomorrow','youre getting chased by three white women in five minutes','youre going to wake up as a skittle soldier','youre going to start getting brain delay, calling dua lipa, dula pip.','jojo siwa will hunt you down.','youre going to become one of the students muffens.','youre going to have a pretty day (pretty ugly)','im calling your mom as we speak.']
        DefinedFortune = fortune1[bo]
        return render_template("fortune.html", F = DefinedFortune ) 

if __name__ == '__main__':
    app.run(debug=True)