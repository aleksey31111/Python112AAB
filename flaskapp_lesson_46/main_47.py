import sqlite3
import os
from flask import Flask, render_template,request,flash,request, flash,session
from flask import Flask, render_template, url_for
DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'dfsdf56456df6356156236876876'
### Console ### Generate key
# os.urandom(20).hex()



app = Flask(__name__)
app.config.form_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))

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

menu = [
           {"name": "лавная", "url": "index"},
           {"name":"О нас", 'url':'about'},
           {"name":"Обратная связь", 'url':'contact'}]

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
    print(url_for('index'))
    return render_template("index.html", title="Главная", menu=dbase.get_menu())

@app.route("/about")
def about():
    return render_template("about.html", title="Описание", menu=menu)

@app_route("/profile/<int:username>")
def profile(username):
    return f"Username: {username}"



@app.route("/contact", methods=["POST", "GET"])
# def contact():
#     if request.method == 'POST':
#         print(request.form)
#         context = {
#             'username': request.rorm['username']
#             'email': request.form['message']
#         }
#         return render_template('contact_47.html', **context, title="Обратная связь", menu=menu)
#     return render_template('contact_47.html', title="обратная связь", menu=menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Page NOT Found",
                           menu=menu)


if __name__ == '__main__':
    app.run(debug=True)


