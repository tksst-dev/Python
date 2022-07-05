import sqlite3

# dairy.dbの生成
conn = sqlite3.connect('dairy.db')
cur = conn.cursor()

cur.execute("SELECT * FROM dairy")
for row in cur:
    print(str(row[0]) + ',' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3]) + ',' + str(row[4]))

conn.close()
