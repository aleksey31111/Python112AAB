from flask import Flask, render_template, url_for

app = Flask(__name__)

# menu = ["Главная", "О нас", "Обратная связь"]
menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", 'url': 'about'},
    {"name": "Обратная связь", 'url': 'contact'}]


@app.route("/index")
@app.route("/")
def index():
    print(url_for('index'))
    return render_template("index.html", title="Главная", menu=menu)
    # return "index"


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template("about.html", title="О сайте", menu=menu)
    # return "<h1>О сайте</h1>"


@app.route("/profile/<username>")
def profile(username):
    # print(url_for("profile/<username>"))
    return f"Пользователь: {username}"


if __name__ == '__main__':
    app.run(debug=True)
