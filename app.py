from todo import app, Mytodo

todo = Mytodo()

@app.route('/addTodos', methods=['GET', 'POST'])
def add():
    return todo.add()

@app.route('/delete/<int:sno>')
def delete(sno):
    return todo.delete(sno)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    return todo.update(sno)

@app.route('/', methods=['GET', 'POST'])
def show():
    return todo.Show()

if __name__ == "__main__":
    app.run(debug=True, port=8000)