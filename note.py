import requests
import json
import pandas as pd


class Note():
    def get_deta(self):
        api_url = "https://note.com/api/v2/creators/piedpiper_aoyama/contents?kind=note"
        notes_url = "https://note.com/api/v1/notes/"
        urlname = "piedpiper_aoyama"

        # 総記事件数の取得
        # payload = {'urlname': urlname}
        res = requests.get("https://note.com/api/v2/creators/"+urlname).content

        df = json.loads(res)
        note_count = df['data']['noteCount']

        # 総取得ページ数
        df = []
        page_num = (note_count//6) + 1
        for page in range(page_num):
            payload = {'page': page+1}
            res = requests.get(api_url, params=payload).content
            a = json.loads(res)["data"]["contents"]
            df.extend(a)
        return df

    def get_note(self, id):
        notes_url = "https://note.com/api/v1/notes/"
        res = requests.get(notes_url + str(id)).content
        df = json.loads(res)
        note = df['data']

        return note
# note = Note()
# note.get_deta()
