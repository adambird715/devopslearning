from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items
from todo_app.data.session_items import add_item
from todo_app.data.session_items import save_item
import os

app = Flask(__name__)
app.config.from_object(Config())



@app.route('/', methods=['POST','GET'])
@app.route('/index/', methods=['POST','GET'])
def index():
    tasks = get_items()
    return render_template('index.html',tasks=tasks)


@app.route('/post', methods=['POST','GET'])
def post():
    title = request.form.get('title')
    add_item(title)
    return redirect("/")

@app.route('/save')
def save():
    title = request.form.get('title')
    save_item(title)
    return redirect("/")

# @app.route('/delete/<int:task_id>')
# def delete(task_id):
#     session.delete(task_id)
#     session.commit()
#     return redirect("/")