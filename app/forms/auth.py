from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


#from app.models import User



class SignUpForm(FlaskForm):
    name = StringField(
        'Ваш нік',
        validators=[DataRequired(), Length(min=5, max = 20)]
    )
    email = StringField(
        'email',
        validators=[DataRequired(), Email]
    )
    password = PasswordField(
        'Пароль', 
        validators=[DataRequired(), Length(min=5)]
    )
    confirm_password =PasswordField(
        'Підвтерьте пароль',
        validators=[DataRequired, EqualTo('password')]
        )
    submit = SubmitField('Зареєструватися') 
    
class LogInForm(FlaskForm):
    email = StringField(
        'email',
        validators=[DataRequired(), Email]
        )
    password = PasswordField(
        'Пароль',
        validators=[DataRequired]
    )
    renember_me = BooleanField(
        "Запам'ятати мене",
    )
    submit = SubmitField('Увійти')