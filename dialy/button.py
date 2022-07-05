import tkinter as tk

# 表示用のグローバル変数
count = 0

# トップレベルウインドウの生成
root = tk.Tk()
root.title('ボタンテスト')
root.geometry('300x150')

# Labelウィジットの生成と配置
label = tk.Label(root, text = '0', font = ('System', 50))
label.pack(pady=20)

# ハンドラ関数
def count_up():
    global count
    count = count + 1
    label['text'] = str(count)

# Buttonウィジットの生成と配置
button = tk.Button(root,
                   text = 'カウントアップ',
                   command = count_up,
                   font = ('System', 20))
button.pack()

# トップレベルウインドウの表示
root.mailloop()
