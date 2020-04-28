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
    for a in note_list:
        a["body"] = p.sub("", a["body"]).replace("　", "")
        a["publishAt"] = re.sub("-", "/", a["publishAt"])

    return render_template('index.html', note_list=note_list, index=index)


@app.route('/note')
@auth.login_required
def note_list():
    note = Note()
    df = note.get_deta()
    note_list = df
    p = re.compile(r"<[^>]*?>")
    q = re
    for a in note_list:
        a["body"] = p.sub("", a["body"]).replace("　", "")
        a["publishAt"] = re.sub("-", "/", a["publishAt"])

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
    style = """<style type = "text/css" >.nav-item >a{color:#252525;} .nav-item>a:after{background-color:#252525;} </style>"""

    return render_template('note_body.html', name=name, body=body, publishAt=publishAt, eyecatch=eyecatch, style=style)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
