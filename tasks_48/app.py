from flask import Flask,render_template, url_for, request, redirect
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
        return f"<Task {self.id}Ю"

@app.route('/', method=['POST', 'GET'])
def index():
    # return "Hello, World"
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Dont add you Task {e}"
    else:
        tasks = Todo.query.order_by(Todo.data_created.desc()).all(())
        return render_template("index.html", tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(('/'))
    except Exception as e:
        return f"Not saccess task {e}"


@app.route('/update/<int:id>', method=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.content= request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"Not Update {e}"

    else:
        return render_template(('update.html', task=task))


if __name__ == '__main__':
    app.run(debug=True)