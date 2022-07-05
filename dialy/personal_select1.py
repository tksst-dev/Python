import sqlite3

conn = sqlite3.connect('sample.db')

cur = conn.cursor()

# SELECT文による、すべてのデータ抽出
for row in cur.execute("SELECT * FROM personal"):
    print(row)

# 接続の切断
conn.close()
