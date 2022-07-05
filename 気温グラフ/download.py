import os, requests, pandas as pd, json
base_url = 'https://www.data.jma.go.jp/obd/stats/data/mdrr/tem_rct/alltable'
base_dir = os.path.dirname(__file__)
# CSVファイルをダウンロード
def download_csv(name, url):
    # ファイルをダウンロード --- (*1)
    data = requests.get(base_url + url).content
    text = data.decode('shift_jis')
    # 取得したCSVファイルを保存 --- (*2)
    csvfile = os.path.join(base_dir, name + '.csv')
    with open(csvfile, 'wt', encoding='utf-8') as fp:
        fp.write(text)
    # Pandasで東京の気温を取り出す --- (*3)
    df = pd.read_csv(csvfile)
    tokyo = df[df['観測所番号'] == 62078]
    value = tokyo.iat[0, 9] # 先頭行の9列目
    date = "{}/{}/{}".format(tokyo.iat[0, 4], tokyo.iat[0, 5], tokyo.iat[0, 6])
    return value, date

# 最高気温と最低気温のCSVファイルをダウンロード
h,date = download_csv('high', '/mxtemsadext01.csv')
l, date = download_csv('low', '/mntemsadext01.csv')
line = '{},{},{}'.format(date, h, l) # CSVの行を作る
# データを追記保存 --- (*4)
csv_file = os.path.join(base_dir, 'data.csv')
with open(csv_file, 'ta+', encoding='utf-8') as fp:
    fp.write(line + '\n')
    print(line)
