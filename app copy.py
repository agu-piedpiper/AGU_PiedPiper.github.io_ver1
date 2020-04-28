from flask import Flask, render_template, request, redirect, url_for
from note import Note
import pandas as pd
import re
app = Flask(__name__)


@app.route('/')
def index():
    note = Note()
    df, df_s = note.get_deta()
    note_list = df[0:3]
    p = re.compile(r"<[^>]*?>")
    q = re
    for a in note_list:
        a["body"] = p.sub("", a["body"]).replace("　", "")
        a["publishAt"] = re.sub("-", "/", a["publishAt"])

    return render_template('index.html', note_list=note_list)


@app.route('/note')
def note_list():
    note = Note()
    df, df_s = note.get_deta()
    note_list = df
    p = re.compile(r"<[^>]*?>")
    q = re
    for a in note_list:
        a["body"] = p.sub("", a["body"]).replace("　", "")
        a["publishAt"] = re.sub("-", "/", a["publishAt"])

    return render_template('note.html', note_list=note_list,)


@app.route('/test')
def test():

    p = re.compile(r"<[^>]*?>")
    note = Note()
    df, df_s = note.get_deta()
    note_list = df
    for a in note_list:
        a["body"] = (p.sub("", a["body"]))

    return render_template('test.html', note_list=note_list)


@app.route('/note/<id>', methods=['POST', 'GET'])
def get_note(id):
    # id= request.args.get('q')
    note = Note()
    df, df_s = note.get_deta()
    note_body = df_s.query("id == @id").to_dict()
    name = list(note_body["name"].values())[0]
    body = list(note_body["body"].values())[0]
    publishAt = str(list(note_body["publishAt"].values())[0])
    publishAt = re.sub("-", "/", publishAt)
    eyecatch = list(note_body["eyecatch"].values())[0]

    return render_template('note_body.html', name=name, body=body, publishAt=publishAt, eyecatch=eyecatch)


if __name__ == '__main__':
    app.debug = True
    app.run()
