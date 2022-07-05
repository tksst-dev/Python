import tkinter as tk
import tkinter.ttk as ttk
import datetime as da
import calendar as ca
from tkinter import messagebox
import csv

# 日付文字列を作る関数
def make_text_1(y, m, d):
    return str(y) + '年' + str(m) + '月' + str(d) + '日'

def make_text_2(y, m, d):
    return str(y) + '_' + str(m) + '_' + str(d)

# 日付をクリックした際に呼びだされる関数
def click(event):
    t = event.widget['text']
    n = str(yer[0]) + '_' + str(mon[0]) + '_' + str(t)
    v_date = da.date(yer[0], mon[0], t)         # クリックした日
    t_date = da.date(yer[1], mon[1], today)     # 今日
    if v_date > t_date:
        messagebox.showinfo('メッセージ', '未来は閲覧できません。')
        return
    elif v_date == t_date:
        title['text'] = make_text_1(yer[0], mon[0], t) + 'の日記'
        combo.current(0)
        sclH.set(0)
        var.set(0)
        text.delete('1.0', 'end')
        return
    elif event.widget['background'] != 'gray':
        messagebox.showinfo('メッセージ', 'データがありません。')
        return

    with open('dairy.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == n:
                title['text'] = make_text_1(yer[0], mon[0], t) + 'の日記'
                combo.current(row[1])
                sclH.set(row[2])
                var.set(row[3])

    with open(n + '.txt') as f:
        data = f.read()
    text.delete('1.0', 'end')
    text.insert('1.0', data)

# [保存]ボタンをクリックした際に呼び出される関数
def save(t_day):
    d_1 = combo.current()
    d_2 = sclH.get()
    d_3 = var.get()

    with open('dairy.csv', 'a', newline = "") as f:
        writer = csv.writer(f)
        writer.writerow([t_day, d_1, d_2, d_3])

    with open(t_day + '.txt', 'w') as f2:
        f2.write(text.get('1.0', 'end-1c'))

    messagebox.showinfo('メッセージ', 'データを保存しました。')
        
# CSVファイルに、引数の日付があればTrue、なければfaalseを返す関数
def check(y, m, d):
    if (y, m, d) == (yer[0], mon[0], today):
        return False
    with open('dairy.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            y_m_d = row[0].split('_')
            if (str(y), str(m), str(d)) == (y_m_d[0], y_m_d[1], y_m_d[2]):
                return True
    return False

# 表示するカレンダーの生成
WEEK = ['日', '月', '火', '水', '木', '金', '土']
WEEK_COLER = ['red', 'black', 'black', 'black', 'black', 'black', 'blue']

def disp(arg):
    global yer
    global mon

    mon[0] += arg

    # 年をまたぐ処理と年月の表示
    if mon[0] < 1:
        mon[0], yer[0] = 12, yer[0] - 1
    elif mon[0] > 12:
        mon[0], yer[0] = 1, yer[0] + 1
    label['text'] = str(yer[0]) + '年' + str(mon[0]) + '月'

    # Pythonカレンダーの処理
    cal = ca.Calendar(firstweekday = 6)
    cal = cal.monthdayscalendar(yer[0], mon[0])

    # フレーム上のウィジットを削除
    for widget in frame.winfo_children():
        widget.destroy()

    # １行目に曜日を表示
    r = 0
    for i, x in enumerate(WEEK):
        label_day = tk.Label(frame,
                             text = x,
                             font = ('', 10),
                             width = 3,
                             fg = WEEK_COLER[i])
        label_day.grid(row = r, column = i, pady = 1)


    # ２行目に曜日を表示
    r = 1
    for week in cal:
        for i, day in enumerate(week):
            day = ' ' if day == 0 else day
            label_day = tk.Label(frame,
                                 text = day,
                                 font = ('', 10),
                                 fg = WEEK_COLER[i],
                                 borderwidth = 1)
            if (yer[0], mon[0], today) == (yer[1], mon[1], day):
                label_day['relief'] = 'solid'
            if check(yer[0], mon[0], today) == (yer[1], mon[1], day):
                label_day['background'] = 'gray'
            label_day.bind('<Button-1>', click)
            label_day.grid(row = r, column = i, padx = 2, pady = 1)
        r = r + 1

# トップレベルウインドウの生成（リサイズ不可）
root = tk.Tk()
root.title('日記アプリ')
root.geometry('520x280')
root.resizable(0, 0)

# カレンダー用のフレーム
c_frame = tk.Frame(root)
frame = tk.Frame(c_frame)

# ウインドウの幅に合わせて列を均等に３分割
for n in range(3):
    c_frame.grid_columnconfigure(n, weight = 1)

# 現在の年月日取得
yer = [da.date.today().year] * 2
mon = [da.date.today().month] * 2
today = da.date.today().day

# ボタン 年月 ボタンの表示（１行目）    
label = tk.Label(c_frame, font=('', 10))
button_1 = tk.Button(c_frame,
                     text = '＜',
                     font = ('', 10),
                     command = lambda:disp(-1))
button_1.grid(row = 0, column = 0, pady = 10)
label.grid(row = 0, column = 1)
button_2 = tk.Button(c_frame,
                     text = '＞',
                     font = ('', 10),
                     command = lambda:disp(1))
button_2.grid(row = 0, column = 2)

# カレンダーの日付表示（２行目）
frame.grid(row = 1, column = 0, columnspan = 3)
disp(0)


# 日記用のフレーム
d_frame = tk.Frame(root)

# タイトルと[保存]ボタン
t_frame = tk.Frame(d_frame)
title = tk.Label(t_frame,
                 text = make_text_1(yer[0], mon[0], today) + 'の日記',
                 font = ('', 12))
title.grid(row = 0, column = 0, padx = 20)

button = tk.Button(t_frame, text = '保存', command = lambda:save(make_text_2(yer[0], mon[0], today)))
button.grid(row = 0, column = 1)
t_frame.grid(row = 0, column = 0, pady = 10)

# 天気の選択
weather = ('快晴', '晴れ', '曇り', '雨', '雪', '台風', '晴れのち曇り', '晴れのち雨', '晴れのち雪', '曇りのち晴れ', '曇りのち雨', '曇りのち雪', '雨のち晴れ',  '雨のち曇り',  '雨のち雪',  '')

w_frame = tk.Frame(d_frame)
label_1 = tk.Label(w_frame, text = '今日の天気　：　',  font = ('', 10))
label_1.grid(row = 0, column = 0, sticky = tk.W)
combo = ttk.Combobox(w_frame, state = 'readonly', values = weather)
combo.current(0)
combo.grid(row = 0, column = 1)

# 充実度
label_2 = tk.Label(w_frame, text = '今日の充実度：　', font = ('', 10))
label_2.grid(row = 1, column = 0, sticky = tk.W)
sclH = tk.Scale(w_frame, orient = tk.HORIZONTAL, from_ = 1, length = 180)
sclH.grid(row = 1, column = 1)
w_frame.grid(row = 1, column = 0)

# 行動
r_frame = tk.Frame(d_frame)
action = ['出社', 'テレワーク', '外回り', '出張', '休日']
r_frame.grid_columnconfigure(0, weight = 1)
r_frame.grid_columnconfigure(1, weight = 1)
r_frame.grid_columnconfigure(2, weight = 1)
r_frame.grid_columnconfigure(3, weight = 1)
r_frame.grid_columnconfigure(4, weight = 1)
var = tk.IntVar()
var.set(0)

for i, act in enumerate(action):
    radio = tk.Radiobutton(r_frame,
                           text = act,
                           variable = var,
                           value = i)
    radio.grid(row = 0, column = i)
r_frame.grid(row = 3, column = 0)

# テキストフィールド
text = tk.Text(d_frame, width = 40, height = 10)
text.grid(row = 4, column = 0)
scroll_v = tk.Scrollbar(d_frame, orient = tk.VERTICAL, command = text.yview)
scroll_v.grid(row = 4, column = 1, sticky = tk.N + tk.S)
text["yscrollcommand"] = scroll_v.set


c_frame.grid(row = 0, column = 0, padx=10)
d_frame.grid(row = 0, column = 1)

root.mainloop()
