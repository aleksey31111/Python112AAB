import sqlite3
import os
from flask import Flask, render_template, url_for, \
    request, flash, session, redirect, abort, g
from FDataBase import FDataBase


# Конфигурация
DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = '5da71799475846cdf0e1153a36662edb94a60b9c'
# "abcdef123456ghiklm789101112noprst"
# import os
# os.urandom(20).hex()
# '5da71799475846cdf0e1153a36662edb94a60b9c'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


## Формирование Секретного Ключа ##
# app.config['SECRET_KEY'] = "abcdef123456ghiklm789101112noprst"


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


# Из Консоли Сщздаем Базу Данных:
# from flaskapp_lesson_47 import create_db
# create_db()

# menu = ["Главная", "О нас", "Обратная связь"]
# menu = [
#     {"name": "Главная", "url": "index"},
#     {"name": "О нас", 'url': 'about'},
#     {"name": "Обратная связь", 'url': 'contact'}]


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/index")
@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    # print(url_for('index'))
    return render_template("index.html", title="Главная", menu=dbase.get_menu())
    # return "index"


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template("about.html", title="О сайте", menu=[])
    # return "<h1>О сайте</h1>"


@app.route("/contact", methods=["POST", "GET"])
def contact():
    # if request.method == 'POST':
    # print(request.form)
    # context = {
    #     'username': request.form['username'],
    #     'email': request.form['email'],
    #     # 'email': request.form['email'],
    #     'message': request.form['message']
    # }
    # return render_template('contact.html', **context, title="Обратная связь", menu=menu)
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Сщщбщение Отправленно Успешно!", category='success')
        else:
            flash("Ошибка Отправки Данных", category='error')
    return render_template('contact.html', title="Обратная связь", menu=[])


@app.route('/login', methods=["POST", "GET"])
def login():
    if 'userLogged' == session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'Aleksey' \
            and request.form['passw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="Авторизация", menu=[])


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        'page404.html', title="Страница не найдена", menu=[])  # , 404


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    # print(url_for("profile/<username>"))
    return f"Пользователь: {username}"


if __name__ == '__main__':
    app.run(debug=True)
