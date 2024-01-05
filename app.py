from datetime import datetime
from logging import DEBUG
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.secret_key = b'Ej~"\\5\xbf\x1c'

app.logger.setLevel(DEBUG)

feedback = []


def store_feedback(url):
    feedback.append(dict(
        url=url,
        user='Test-User',
        date=datetime.now()
    ))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_feedback(url)
        app.logger.debug('stored feedback: ' + url)
        flash("Your Feedback : " + url)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
