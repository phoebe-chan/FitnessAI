from flask import *
from datetime import datetime
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy 
import sqlalchemy

app = Flask(__name__)
app.config['SECRET KEY'] = "e"
app.config['MAX_CONTENT_LENGTH'] = 1000000
app.config['SESSION_TYPE'] = 'filesystem' 
app.config['SESSION_FILE_DIR'] = app.root_path + "/cache"
app.config['SESSION_FILE_THRESHOLD'] = 1000
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///girlsinai.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Session(app)
db = SQLAlchemy(app)

@app.route('/menu')
def index():
    return send_file('menu.html')

@app.route('/situps')
def situps():
    return send_file('situps.html')


@app.route('/squats')
def squats():
    return send_file('squats.html')

@app.route('/pushups')
def squats():
    return send_file('pushups.html')
    

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 80, debug = True) #runs the app 