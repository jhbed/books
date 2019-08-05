from books.models import Book
from flask import render_template, url_for, flash, redirect
from books.forms import RegistrationForm, LoginForm
from books import app


@app.route('/')
@app.route('/home')
def home():
    posts = Book.query.all()
    return render_template('home.html', post_data=posts)

@app.route('/about')
def blah():
    return render_template('about.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash('It worked!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
