import tkinter as tk
from tkinter import messagebox

# トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('300x100')
root.title('radiobuttonテスト')

# ラジオボタンを配置するフレーム
frame = tk.Frame(root)
frame.grid_columnconfigure(0, weight = 1)
frame.grid_columnconfigure(1, weight = 1)
frame.grid_columnconfigure(2, weight = 1)
frame.grid_columnconfigure(3, weight = 1)
frame.grid_columnconfigure(4, weight = 1)

action = ['出社', 'テレワーク', '外回り', '出張', '休日']
var = tk.IntVar(value = 1)

# Radiobuttonウィジットの生成と配置
for i, act in enumerate(action):
    radio = tk.Radiobutton(frame,
                           text = act,
                           variable = var,
                           value = i)
    radio.grid(row = 0, column = i)
frame.grid(row = 0, column = 0, columnspan = 2)

# ハンドラ関数
def click_get():
    messagebox.showinfo('メッセージ', action[var.get()])

def click_set():
    var.set(4)

# Buttonウィジットの姿勢と配置
button_1 = tk.Button(root, text = '表示', command = click_get)
button_1.grid(row = 1, column = 0)

button_2 = tk.Button(root, text = '設定', command = click_set)
button_2.grid(row = 1, column = 1)

# トップレベルウィンドウの表示
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.mainloop()
