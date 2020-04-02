from flask import Flask,render_template, request, redirect, url_for
from modele import Note
app = Flask(__name__)

@app.route('/')
def hello_world():
    title ="ようこそ"
    message = "PiedPiperのNOTEです。"

    note = Note()
    note_deta = note.get_deta()

    return render_template('test.html',note_deta=note_deta)


@app.route('/note/<req_id>',methods=['POST', 'GET'])
def get_note(req_id):
    id= request.args.get('q')
    note = Note()
    note_deta = note.get_deta()
    note_body = note_deta

    return render_template('note_body.html', id=id) 


if __name__ == '__main__':
    app.debug = True
    app.run()
