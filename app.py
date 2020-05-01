from flask import Flask, render_template, request, redirect, url_for
from note import Note
import pandas as pd
import re
import os
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": "password",
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@app.route('/')
@auth.login_required
def index():
    index = "index"
    note = Note()
    df = note.get_deta()
    note_list = df[0:3]
    p = re.compile(r"<[^>]*?>")
    q = re
    for note in note_list:
        note["body"] = note["body"].replace("　", "").replace("\n", "")
        note["publishAt"] = re.sub("-", "/", note["publishAt"])

    return render_template('index.html', note_list=note_list, index=index)


@app.route('/note')
@auth.login_required
def note_list():
    note = Note()
    df = note.get_deta()
    note_list = df
    p = re.compile(r"<[^>]*?>")
    q = re
    for note in note_list:
        note["body"] = note["body"].replace("　", "").replace("\n", "")
        note["publishAt"] = re.sub("-", "/", note["publishAt"])

    return render_template('note.html', note_list=note_list,)


@app.route('/note/<id>', methods=['POST', 'GET'])
@auth.login_required
def get_note(id):
    note = Note()
    note_body = note.get_note(id)
    name = note_body["name"]
    body = note_body["body"]
    publishAt = note_body["publish_at"]
    publishAt = re.sub("-", "/", publishAt)
    eyecatch = note_body["eyecatch"]
    style = """ <style type = "text/css" >.navbar-toggler>.navbar-toggler-icon {
        background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 32 32' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(25,25,25,1)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 8h24M4 16h24M4 24h24'/%3E%3C/svg%3E");}
        .nav-item >a{color:#191919;} .nav-item>a:after{background-color:#191919;}
@media screen and (max-width:575px) {.nav-item >a{color:#fff;} .nav-item>a:after{background-color:#fff;}}
        </style>"""
    #
#
    return render_template('note_body.html', name=name, body=body, publishAt=publishAt, eyecatch=eyecatch, style=style)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
