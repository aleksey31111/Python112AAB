from flask import Flask,render_template, url_for
from flask_sqlalthemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column((db.Integer, primary_key=True))
    content = db.Column(db.String(200), nullable=False)
    data_created = db.Column(db.DataTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.id}"

@app.route('/')
def index():
    # return "Hello, World"
    return render_template()


if __name__ == '__main__':
    app.run(debug=True)