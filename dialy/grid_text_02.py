import tkinter as tk

# トップレベルウインドウの生成
root = tk.Tk()
root.title('gridテスト')
root.geometry('400x200')

# ウィジットの数
WIDGET_MAX = 8

# Labelウィジットのリストの生成
labels = [tk.Label(root, text = 'NO_' + str(num), relief = tk.SOLID) for num in range(WIDGET_MAX)]

# grid関数で配置
labels[0].grid(column = 0, row = 0)
labels[1].grid(column = 1, row = 0)
labels[2].grid(column = 2, row = 0)
labels[3].grid(column = 3, row = 0)
labels[4].grid(column = 0, row = 1)
labels[5].grid(column = 1, row = 1)
labels[6].grid(column = 2, row = 1)
labels[7].grid(column = 3, row = 1)

# トップレベルウインドウの表示
root.mainloop()
