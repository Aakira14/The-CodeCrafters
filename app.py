################################################
# Backend source code for team: CodeCrafters   #
# By, Rahul. Pagare (Back-end Dev.)            #
################################################

'''
if authenticate => Checks for access.
else => Doesn't check access.
'''


'''
CodeCrafters Running Variables
'''

authenticate = True

# Non-flask modules
import string
import pickle
import random
import os
import datetime

# Flask modules
from flask import Flask
from flask import (
    Flask,
    make_response,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
)

#from flask_cors import CORS, cross_origin
from flask_httpauth import HTTPBasicAuth
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = "%YTHT34%^$#@CodeCrafters$T#$RT%@%F$$#WTRv!"

csrf = CSRFProtect(app)


def gen_reg_id():
    return "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase)
        for k in range(random.randint(12, 20))) + "".join(
            random.choice(string.digits)
            for x in range(random.randint(30, 60)))



class AllowedUsers:
    def __init__(self):
        self.users = {} # NOTE: format = {id: {username, ban_status}}
        self.version = "map1"

    def register_user(self, reg_id: str, username: str) -> bool:
        self.username = username.strip() # No triailing spaces; beware!
        safe = True
        val_only = []
        for key in self.users:
            val_only.append(self.users[key]['username'])
        if self.username in val_only:
            safe = False

        #if nickname not in self.users.keys():

        if safe:
            self.users[reg_id] = {'username': self.username, 'ban_status': False}
            return True
        else:
            return False

    def remove_user(self, reg_id):
        if reg_id not in self.users.keys():
            return False
        else:
            self.users = self.users.pop(reg_id)
            return True

    def ban_user(self, reg_id):
        if reg_id not in self.users.keys():
            return False
        else:
            self.users[reg_id]['ban_status'] = True
            return True

    def unban_user(self, reg_id):
        if reg_id not in self.users.keys():
            return False
        else:
            self.users[reg_id]['ban_status'] = False
            return True


if not os.path.exists('/home/RahulP/CodeCrafters/RegisteredUsers.db'):
    lll = AllowedUsers()
    lll.register_user(gen_reg_id(), 'RahulPagare20')
    lll.register_user(gen_reg_id(), 'Aakira14')
    lll.register_user(gen_reg_id(), 'Jaden2010')
    with open('/home/RahulP/CodeCrafters/RegisteredUsers.db', 'wb') as tp:
        pickle.dump(lll, tp)


@app.errorhandler(404)
def page_not_found(err):
    return "<H1>That page wasn't found on our servers.</H1><a href='/'>Click here to go to the home page.</a>"




@app.before_request
def before_req_check():
    global authenticate
    allowed_paths = ["/inner/server/login", '/images/codecrafters_pr.png']#, '/inner/stylesheet/style_index.html.css']
    if authenticate:
        if request.path not in allowed_paths:
            allow = False
            cookies = request.cookies
            if 'Registration' in cookies:
                reg_id = cookies.get('Registration')
            else:
                return render_template('login.html', error_message="Authentication Mandated.")

            with open('/home/RahulP/CodeCrafters/RegisteredUsers.db', 'rb') as tp:
                raw = pickle.load(tp)

            if reg_id in raw.users.keys():
                if raw.users[reg_id]['ban_status']:
                    return '<h1>[!] Account banned!</h1>'
                else:
                    allow = True
            else:
                return render_template('login.html', error_message="Invalid Cookie")

            if not allow:
                if authenticate:
                    return render_template('login.html', error_message="Authentication Mandated.")
                else:
                    allow = True
            else:
                pass




@app.route('/inner/server/login', methods=["POST"])
def login_page_server():
    #allowed_usernames = ['RahulPagare20', 'Aakira14', 'Jaden2010']
    username_raw = request.form['username']
    password_raw = request.form['password']
    username = str(username_raw.strip())
    password = str(password_raw.strip())
    if password != "RAJ20_14_2010":
        return render_template('login.html', error_message="Invalid password.")
    else:
        with open('/home/RahulP/CodeCrafters/RegisteredUsers.db', 'rb') as tp:
            raw = pickle.load(tp)
        present = False
        user_reg_id = "[!]"
        for key in raw.users.keys():
            if raw.users[key]['username'] == username:
                present = True
                user_reg_id = key
                break

        #if username not in raw.users.keys():
        if not present:
            return render_template('login.html', error_message="Invalid username.")
        else:
            resp = make_response(render_template('index.html'))
            resp.set_cookie('Registration', user_reg_id, expires=datetime.datetime.now() +datetime.timedelta(days=30))
            return resp



@app.route('/')
def hello_world():
    return render_template('index.html')




@app.route('/inner/stylesheet/style_index.html.css')
def style_index():
    global cwd, project_dir
    return send_file(
        f'/home/RahulP/CodeCrafters/stylesheets/style_index.html.css')


@app.route('/images/codecrafters_pr.png')
def codecrafters_pr_png():
    global cwd, project_dir
    return send_file(
        f'/home/RahulP/CodeCrafters/images/codecrafters_pr.png')

@app.route('/images/jaden_pfp.jpg')
def jaden_pfp_jpg():
    global cwd, project_dir
    return send_file(
        f'/home/RahulP/CodeCrafters/images/jaden_pfp.jpg')

@app.route('/images/aakira_pfp.png')
def aakira_pfp_png():
    global cwd, project_dir
    return send_file(
        f'/home/RahulP/CodeCrafters/images/aakira_pfp.png')

@app.route('/images/rahul_pfp.png')
def rahul_pfp_png():
    global cwd, project_dir
    return send_file(
        f'/home/RahulP/CodeCrafters/images/rahul_pfp.png')


@app.route('/images/codecrafters_pfp.png')
def codecrafters_pfp():
    global cwd, project_dir
    return send_file(
        f'/home/RahulP/CodeCrafters/images/codecrafters_pfp.png')