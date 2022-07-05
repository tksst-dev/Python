import tkinter as tk

# トップレベルウインドウの生成
root = tk.Tk()
root.title('おみくじ')
root.geometry('400x200')

# Labelウィジットの生成
label = tk.Label(root,
                 text = '運勢は大吉です。',
                 padx = 5, pady = 5,
                 relief = tk.SUNKEN,
                 foreground = 'red')

# Labelウィジットの表示
label.pack(pady = 50)

# トップレベルウインドウの表示
root.mainloop()
