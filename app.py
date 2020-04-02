from flask import Flask,render_template, request, redirect, url_for
from modele import Note
app = Flask(__name__)

@app.route('/')
def hello_world():
    title ="ようこそ"
    message = "PiedPiperのNOTEです。"

    note = Note()
    note_deta = note.get_deta()
    # note_name = note_deta["name"]
    # note_body = note_deta["body"][0:150]
    # note_eyecatch = note_deta["eyecatch"]
    # note_publish_at = note_deta["publish_at"]
    return render_template('test.html',note_deta=note_deta)


if __name__ == '__main__':
    app.debug = True
    app.run()
