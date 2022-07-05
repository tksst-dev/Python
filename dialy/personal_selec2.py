import sqlite3

conn = sqlite3.connect('sample.db')

cur = conn.cursor()

# idが、’002’と等しい行の抽出
for row in cur.execute("SELECT * FROM personal WHERE id = '002'"):
    print(row)
print()     # 改行

# heightが、173以上の行の抽出
for row in cur.execute("SELECT * FROM personal WHERE height >= 173"):
    print(row)
print()     # 改行

# weightが、75.8以外の行の抽出
for row in cur.execute("SELECT * FROM personal WHERE weight != 75.8"):
    print(row)
print()     # 改行


# 接続の切断
conn.close()
