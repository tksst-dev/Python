import tkinter as tk
import random

omi = ['大吉', '中吉', '小吉', '吉', '凶', '中凶', '大凶']

# トップレベルウインドウの生成
root = tk.Tk()
root.title('おみくじ')
root.geometry('300x150')

# Labelウィジットの生成
label = tk.Label(root,
                 text = '運勢は' + random.choice(omi) + 'です。',
                 padx = 10, pady = 10,
                 relief = tk.RIDGE)

# Labelウィジットの表示
label.pack(expand = True)

# トップレベルウインドウの表示
root.mainloop()
