from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user
from app import app, db
from app.forms import LoginForm, RegistrationForm, CommentForm
from app.models import *


@app.route('/')
def start_page_view():
    return render_template('start_page.html')


@app.route('/main')
def main_page_view():
    return render_template('main_page.html')


@app.route('/fud')
def fud():
    a_treat = A_treat.query.all()
    pizza = Pizza.query.all()
    drinks = Drinks.query.all()
    title_page_fud = ["Лакомства", "Съешь меня", "Выпей меня"]
    return render_template('fud.html', a_treat=a_treat, pizza=pizza, drinks=drinks, title_page_fud=title_page_fud)

@app.route('/film')
def film():
    today = Today.query.all()
    title_page_today = "Посмотри меня"
    return render_template('film.html', today=today, title_page_today=title_page_today)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_page_view'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неверное имя пользователя или пароль')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('main_page_view'))
    return render_template('login.html', title='login', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main_page_view'))
    return render_template('registration.html', form=form)


from flask_login import logout_user

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('start_page_view'))


@app.route('/comment', methods=['GET', 'POST'])
def comment():
    form = CommentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            com = Comment(text=form.text.data, user_username=current_user.username)
            db.session.add(com)
            db.session.commit()
            return redirect(url_for('comment'))
        else:
            flash('Пожалуйста напишите Ваш отзыв перед отправкой')
            form = CommentForm()
    comments = Comment.query.all()

    return render_template('comments.html', form=form, comments=comments)
