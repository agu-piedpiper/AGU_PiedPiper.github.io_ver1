import requests
import json
import pandas as pd


class Note():
    def get_deta(self):
        api_url = "https://note.com/api/v1/notes/"
        urlname = "piedpiper_aoyama"

        # 総記事件数の取得
        payload = {'urlname': urlname}
        res = requests.get("https://note.mu/api/v1/users/",
                           params=payload).content

        df = json.loads(res)
        note_count = df['data']['note_count']

        # 総取得ページ数
        page_num = (note_count//10) + 1
        for page in range(page_num):
            payload = {'urlname': urlname, 'page': page}
            res = requests.get(api_url, params=payload).content
            df = json.loads(res)["data"]["notes"]
            data_json = json.dumps(df, ensure_ascii=False)
            df_s = pd.read_json(data_json)

        return df, df_s


# note = Note()
# note.get_deta()
