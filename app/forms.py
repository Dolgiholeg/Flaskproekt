from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', [DataRequired(message='Введите логин')])
    password = PasswordField('Пароль', [DataRequired(message='Введите пароль')])
    submit = SubmitField('ВХОД')


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', [DataRequired(message='Введите логин')])
    email = StringField('Адрес электронной почты', [DataRequired(message='Введите адрес электронной почты'),
                                                    Email(message='Неверный формат данных')])
    password = PasswordField('Пароль', [DataRequired(message='Введите пароль')])
    password2 = PasswordField('Подтверждение пароля', [DataRequired(message='Введите пароль повторно'),
                                                       EqualTo('password', message='Пароли не совпадают')])
    first_name = StringField('Имя', [DataRequired(message='Введите Ваше Имя')])
    last_name = StringField('Фамилия', [DataRequired(message='Введите Вашу Фамилию')])
    submit = SubmitField('ВХОД')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста, используйте другое имя пользователя')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста, используйте другой адрес электронной почты')


class CommentForm(FlaskForm):
    text = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Отправить')




