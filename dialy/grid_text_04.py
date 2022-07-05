import tkinter as tk

# トップレベルウインドウの生成
root = tk.Tk()
root.title('gridテスト')
root.geometry('400x200')

# ウィジットの数
WIDGET_MAX = 8

# Labelウィジットのリストの生成
labels = [tk.Label(root, text = 'NO_' + str(num), relief = tk.SOLID) for num in range(WIDGET_MAX)]

# 各列の割合を指定
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# 各行の割合を指定
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# grid関数で配置
labels[0].grid(column = 0, row = 0, sticky = tk.N)
labels[1].grid(column = 1, row = 0, sticky = tk.S)
labels[2].grid(column = 2, row = 0, sticky = tk.E)
labels[3].grid(column = 3, row = 0, sticky = tk.W)
labels[4].grid(column = 0, row = 1, sticky = tk.NS)
labels[5].grid(column = 1, row = 1, sticky = tk.SE)
labels[6].grid(column = 2, row = 1, sticky = tk.EW)
labels[7].grid(column = 3, row = 1, sticky = tk.NSEW)

# トップレベルウインドウの表示
root.mainloop()
