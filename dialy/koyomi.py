import tkinter as tk
import datetime as da
import calendar as ca
from tkinter import messagebox

WEEK = ['日', '月', '火', '水', '木', '金', '土']
WEEK_COLER = ['red', 'black', 'black', 'black', 'black', 'black', 'blue']

# 表示するカレンダあーの生成
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
    for week in cal:
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
            label_day.bind('<Button-1>', click)
            label_day.grid(row = r, column = i, padx = 2, pady = 1)
        r = r + 1

# カレンダーの日付がクリックされたときの処理
def click(event):
    t = event.widget['text']
    event.widget['baackground'] = 'gray'
    messagebox.showinfo('メッセージ', str(t) + '日です。') 

# ウィンドウの生成
root = tk.Tk()
root.title('カレンダー')
root.geometry('220x200')
root.resizable(0, 0)

# 現在の年月日取得
yer = [da.date.today().year] * 2
mon = [da.date.today().month] * 2
today = da.date.today().day

# ウインドウの幅に合わせて列を均等に３分割
for n in range(3):
    root.grid_columnconfigure(n, weight = 1)

# ボタン 年月 ボタンの表示（１行目）    
label = tk.Label(root, font=('', 10))
button_1 = tk.Button(root,
                     text = '＜',
                     font = ('', 10),
                     command = lambda:disp(-1))
button_1.grid(row = 0, column = 0, pady = 10)
label.grid(row = 0, column = 1)
button_2 = tk.Button(root,
                     text = '＞',
                     font = ('', 10),
                     command = lambda:disp(1))
button_2.grid(row = 0, column = 2)

# カレンダーの日付表示（２行目）
frame = tk.Frame(root)
frame.grid(row = 1, column = 0, columnspan = 3)
disp(0)

root.mainloop()
