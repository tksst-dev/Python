import sqlite3

# dairy.dbの生成
conn = sqlite3.connect('dairy.db')
print('dairy.dbを作成しました。')

cur = conn.cursor()


# 既にある場合は削除
cur.execute("DROP TABLE IF EXISTS dairy")

# テーブルの生成
cur.execute("""CREATE TABLE dairy(
                date TEXT PRIMARY KEY,
                weather INTEGER,
                adequacy INTEGER,
                action INTEGER,
                event TEXT)""")
print('dairyテーブルを作成しました。')

# dairy
sql = """INSERT INTO dairy(date, weather, adequacy, action, event)
            VALUES('2022_1_1', 2, 80, 4, 'あけまして、おめでとう。
目が覚めたら１０時だった。
今年こそは、ダイエットすると決めていたのに、
結局ダラダラ１日が過ぎてしまった。')"""
cur.execute(sql)

sql = """INSERT INTO dairy(date, weather, adequacy, action, event)
            VALUES('2022_6_1', 1, 40, 4, '今日は７時に起きて、久々にでかけた。
駅前は、結構にぎわっている。
')"""
cur.execute(sql)

cur.execute("SELECT * FROM dairy")
for row in cur:
    print(str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(row[4]))

conn.commit()
print('初期登録しました。')

conn.close()
