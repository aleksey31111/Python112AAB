from flask import Flask, render_template, url_for


app = Flask(__name__)

menu = [
           {"name": "лавная", "url": "index"},
           {"name":"О нас", 'url':'about'},
           {"name":"Обратная связь", 'url':'contact'}]



@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", title="Главная", menu=menu)

@app.route("/about")
def about():
    return render_template("about.html", title="Описание", menu=menu)

@app_route("/profile/<int:username>")
def profile(username):
    return f"Username: {username}"


if __name__ == '__main__':
    app.run(debug=True)
