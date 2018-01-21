from flask import request,Blueprint,g,redirect,url_for,\
    abort,render_template_string,flash,current_app, make_response
from models import User
from login.sms_handler import send_sms
import json
from login.constant import LOGIN_SUCCESS, LOGIN_FAIL, SMS_SUCCESS, REGISTER_SUCCESS, REGISTER_FAIL
import redis
import random
import hashlib

bp = Blueprint("login", __name__)

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

def gen_session_id(digit_sign):
    m = hashlib.md5()
    m.update((str(digit_sign) + str(random.randint(1, 100))).encode('utf-8'))
    session_id = m.hexdigest()
    r.setex(session_id, str(digit_sign), 86400)
    return session_id

@bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        rs=User.query.all()
        return render_template_string(str([ str(user) for user in rs]))

    name,password,phone_num,vcode = request.json.get('user_name'),request.json.get('password'),request.json.get('phone_num'),request.json.get('vcode')

    if phone_num and vcode:
        u = User.query.filter(User.phone_num==phone_num).first()
        if u:
            hascode = r.exists(vcode)
            if hascode:
                session_id = gen_session_id(phone_num)
                resp = make_response(json.dumps(LOGIN_SUCCESS))
                resp.set_cookie('bpetid', session_id)
                return resp
                #return render_template_string(str(json.dumps(LOGIN_SUCCESS)))

    if name and password:
        u = User.query.filter(User.user_name==name).first()
        if u:
            if password == u.password:
                session_id = gen_session_id(name)
                resp = make_response(json.dumps(LOGIN_SUCCESS))
                resp.set_cookie('bpetid', session_id)
                return resp
                #return render_template_string(str(json.dumps(LOGIN_SUCCESS)))

    return render_template_string(json.dumps(LOGIN_FAIL))


@bp.route('/get-verify-code', methods=['GET'])
def verify_code():
    #ip limitation
    phone_number = request.args['phone_num']

    code = str(random.randint(1000, 9999))
    try:
        if r.setex(code, 0, 300):
            send_sms(code, phoneNumbers=phone_number)
        else:
            return render_template_string(json.dumps({"err_code":"1", "err_desc":"store code error"}))
    except Exception as e:
        return render_template_string(json.dumps({"err_code":"1", "err_desc":"sms error: " + e}))

    return render_template_string(json.dumps(SMS_SUCCESS))


@bp.route("/register", methods=["POST"])
def register():
    try:
        u = User(request.json)
        u.save()

        session_id = gen_session_id(u.user_name)
        resp = make_response(json.dumps(LOGIN_SUCCESS))
        resp.set_cookie('bpetid', session_id)
    except Exception as e:
        return render_template_string(json.dumps(REGISTER_FAIL))
    return resp

