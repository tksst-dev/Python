import sqlite3

conn = sqlite3.connect('dairy.db')
cur = conn.cursor()


# 既にある場合は削除
cur.execute("DROP TABLE IF EXISTS weather")
cur.execute("DROP TABLE IF EXISTS action")

# テーブルの生成
cur.execute("""CREATE TABLE weather(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT)""")
print('weatherテーブルを作成しました。')

weather = ['快晴', '晴れ', '曇り', '雨', '雪', '台風', '晴れのち曇り', '晴れのち雨', '晴れのち雪', '曇りのち晴れ', '曇りのち雨', '曇りのち雪', '雨のち晴れ',  '雨のち曇り',  '雨のち雪']

for w in weather:
    cur.execute("INSERT INTO weather(type) VALUES('" + w + "')")

cur.execute("SELECT * FROM weather")
for row in cur:
    print(str(row[0]) + ',' + str(row[1]))


# テーブルの生成
cur.execute("""CREATE TABLE action(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT)""")
print('actionテーブルを作成しました。')

action = ['出社', 'テレワーク', '外回り', '出張', '休日']

for a in action:
    cur.execute("INSERT INTO action(type) VALUES('" + a + "')")

cur.execute("SELECT * FROM action")
for row in cur:
    print(str(row[0]) + ',' + str(row[1]))

conn.commit()
conn.close()
