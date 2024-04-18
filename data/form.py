from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class BaseForm(FlaskForm):
    menu = SubmitField('Меню')
    about_us = SubmitField('О нас')
    basket = SubmitField('Корзина')
    add_position = SubmitField('+ позиция')


class PositionForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    prise = IntegerField("Цена", validators=[DataRequired()])
    save = SubmitField('Сохранить')
