from flask import Flask, render_template
import random

app = Flask(__name__, template_folder='Templates', static_folder='static')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/fortune')
def fortune():
    fortune1 = ['youre going to eat raw meat today','your baddies will not play DTI with you','you are so not watermelon tomorrow','youre getting chased by three white women in five minutes','youre going to wake up as a skittle soldier','youre going to start getting brain delay, calling dua lipa, dula pip.','jojo siwa will hunt you down.','youre going to become one of the students muffens.','youre going to have a pretty day (pretty ugly)','im calling your mom as we speak.']
    RandomNumber = random.randint(0,9)
    DefinedFortune = fortune1[RandomNumber]
    return render_template("fortune.html", F = DefinedFortune ) 


if __name__ == '__main__':
    app.run(debug=True)