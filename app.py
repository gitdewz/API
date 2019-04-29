from flask import Flask, jsonify, render_template, redirect, request, session, url_for
import os
from string import Template
from create import Create
from load import Load
import pymongo

app = Flask(__name__, static_folder="../client", template_folder="../client/html")

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
@app.route('/start/')
@app.route('/start/<user>')
def start(user=None): 
    return render_template('start.html', user=user)

@app.route('/register/')
def register(user=None): 
    return render_template('confirmation.html', user=user)

@app.route('/dashboard/')
def dashboard(): 
    print(session.get('email'))
    return render_template('dashboard.html')

@app.route('/project/<project>')
def project(user=None): 
    return render_template('project.html', user=user)


@app.route('/tasks/')
@app.route('/tasks/<task>')
def tasks(user=None, task=None):
    load = Load("task", task)
    if task != None:
        return load.load_task()        
    return render_template('tasks.html', user=user)

@app.route('/login', methods=['post'])
def login():
    print(request.form['email'])
    print(request.form['password'])
    session['email'] = request.form['email']
    session['authenticated'] = True
    return redirect(url_for(".dashboard"))
 

@app.route('/api/create/<item_type>', methods=['post'])
def create(user=None, item_type=None):
    print(item_type)
    create = Create(item_type, request.form)
    create.create_item()       
    return redirect(url_for('tasks'))

@app.route('/api/<item_type>/<item_key>', methods=['get'])
def load(item_type=None, item_key=None):
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = mongo_client["tracker"]
    item_type = item_type
    item_collection = db[item_type]
    item = item_collection.find_one({'key': item_key})
    data = {
        "key": item['key'],
        "project": item['project'],
        "short_description": item['short_description'],
        "notes": item['notes'],
    }
    return jsonify(data)





if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5556'))
    except ValueError:
        PORT = 5556
    app.secret_key = os.urandom(12)
    app.run(HOST, PORT)