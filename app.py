###############################################
# Backend source code for team: CodeCrafters  #
# By, Rahul. Pagare (backend dev)             #
###############################################


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