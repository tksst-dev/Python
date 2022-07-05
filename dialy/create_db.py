# ライブラリのインポート
import sqlite3

# データベースへの接続（ない場合は作成）
conn = sqlite3.connect('sample.db')
print('データベースを作成しました。')

# 接続の切断
conn.close()
