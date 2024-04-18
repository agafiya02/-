from flask import Flask, render_template, redirect
from flask_restful import Api
from flask_login import LoginManager
from data.form import PositionForm, BaseForm
from data import session, position
import datetime

app = Flask(__name__)
api = Api(app)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'my_secret_key'
session.global_init("db/menu.db")


@login_manager.user_loader
def load_user(order_id):
    db_sess = session.create_session()
    return db_sess.query(position.Position).get(order_id)


@app.route('/', methods=['GET', 'POST'])
def index():
    form1 = BaseForm()
    if form1.validate_on_submit():
        pass
    return render_template('base.html', form=form1)


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/basket')
def basket():
    return render_template('basket.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/add_position', methods=['GET', 'POST'])
def add_position():
    form = PositionForm()
    if form.validate_on_submit():
        db_sess = session.create_session()
        if db_sess.query(position.Position).filter(position.Position.name == form.name.data).first():
            return render_template('add_position.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        order = position.Position(
            name=form.name.data,
            email=form.price.data,
        )
        db_sess.add(order)
        db_sess.commit()
    return render_template('add_position.html', title='Регистрация', form=form)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
