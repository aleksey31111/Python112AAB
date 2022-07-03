import sqlite3
import os
from flask import Flask, render_template, url_for, \
    flash, request, session, redirect, abort, g
from FDataBase import FDataBase

DATABASE = '/tmp/article.db'
DEBUG = True
app = Flask(__name__)
app.config['SECRET_KEY'] = '5443d109810cff4cf27c1b69b0ede52abd1db3a86dbed1'
# menu = [
#     {"name": "ЗаГлавная", "url": "home"},
#     {"name": "О создателях страницы", "url": "about_creators"},
#     {"name": "Связь", "url": "bonds"}
# ]
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'article.db')))


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


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/home")
@app.route("/")
def home():
    db = get_db()
    dbase = FDataBase(db)
    # print(url_for('home'))
    return render_template("home.html", title="ЗаГлавная",
                           menu=dbase.get_menu(),
                           posts=dbase.get_posts_anonce())


# @app.route("/about_creators")
# def about_creators():
#     print(url_for("about_creators"))
#     return render_template("about_creators.html", title="О создателях страницы", menu=menu)


@app.route("/bonds", methods=["POST", "GET"])
def bonds():
    # print(url_for("bonds.html"))
    if request.method == 'POST':
        print(request.form)
        if len(request.form['username']) > 2:
            flash("Сообщение Отправлено Успешно", category='success')
        else:
            flash("Ошибка Отправки Данных", category='error')

    return render_template("bonds.html", title="Связь", menu=[])


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
        return f"Пользователь: {username}"


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page404.html', title="Страница Не Найдена", menu=dbase.get_menu())  # menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' == session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'Aleksey' \
            and request.form['passw'] == '654321':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title="Авторизация", menu=[])


@app.route("/add_post", methods=['POST', 'GET'])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 3 and len(request.form['post']) > 5:
            res = dbase.add_post(request.form['name'], request.form['post'])
            if not res:
                flash("Ошибка добавления статьи", category='error')
            else:
                flash("Успешное добавления статьи", category='success')
        else:
            flash("Ошибка добавления статьи", category='error')

    return render_template("add_post.html", title="Добавление статьи", menu=dbase.get_menu())


@app.route('/post/<int:id_post>')
def show_post(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.get_post(id_post)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.get_menu(), title=title,
                           post=post)


if __name__ == '__main__':
    app.run(debug=True)
