from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/features')
def features():
    return render_template('features.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/sign-in')
def sign_in():
    return render_template('sign_in.html')


@app.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')


app.run(debug=True)
