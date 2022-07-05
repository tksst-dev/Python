import tkinter as tk
from tkinter import messagebox

# トップレベルウインドウの生成
root = tk.Tk()
root.geometry('300x100')
root.title('Enterテスト')

# Enterウィジットの生成と配置
txt = tk.Entry(width = 20)
txt.pack(pady = 20)

# ハンドラ関数
def click():
    messagebox.showinfo('メッセージ', txt.get())

# Buttonウィジットの生成と配置
btn = tk.Button(root, text = '表示', command = click)
btn.pack()

# トップレベルウインドウの表示
root.mainloop()
