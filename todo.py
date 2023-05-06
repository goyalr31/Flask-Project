from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f'{self.sno} - {self.title}'


class Mytodo:
    def add(self):
        if request.method == 'POST':
            title = request.form['title'] 
            desc = request.form['desc'] 
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
            return redirect("/")
        allTodo= Todo.query.all()
        return render_template("addTodos.html" , allTodo=allTodo)


    def delete(self,sno):
        todo= Todo.query.filter_by(sno=sno).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect("/")


    def update(self, sno):
        if request.method == 'POST':
            title = request.form['title'] 
            desc = request.form['desc'] 
            todo = Todo.query.filter_by(sno=sno).first()
            todo.title = title
            todo.desc = desc
            db.session.add(todo)
            db.session.commit()
            return redirect("/")


        todo= Todo.query.filter_by(sno=sno).first()
        return render_template("update.html", todo=todo)


    def Show(self):
        allTodo= Todo.query.all()
        return render_template("index.html" , allTodo=allTodo)

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)
