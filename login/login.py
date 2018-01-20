from flask import request,Blueprint,g,redirect,url_for,\
    abort,render_template_string,flash,current_app
from database import db_session
from models import User
from login.sms_handler import send_sms

bp = Blueprint("login", __name__)

'''
def connect_db():
    rv = sqlite3.connect(current_app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()

def get_db():
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db
'''

@bp.route("/", methods=["POST"])
def login():
    #1. put session id in redis
    #2. put secret info in redis
    #3.
    rs=User.query.all()
    print(str(rs))
    #print(str([{entry["title"]:entry["text"]} for entry in entries]))

    return render_template_string(str([ str(user) for user in rs]))

@bp.route("/get-verify-code", methods=["GET"])
def verify_code():
    #ip limitation
    phone_number = request.args["phone_number"]
    #send verify code to phone number
    #save verify code in redis and set available time
    pass

@bp.route("/register", methods=["POST"])
def register():
    #if not session.get('logged_in'):
    #    abort(401)
    print(request.json)
    u = User(request.json)
    db_session.add(u)
    db_session.commit()

    print("in register end")
    #flash('New entry was successfully posted')
    #return render_template_string(str({"test":"register"}))
    return redirect(url_for('login.login'))

