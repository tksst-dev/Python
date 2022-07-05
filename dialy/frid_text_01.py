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
for num in range(WIDGET_MAX):
    labels[num].grid()

# トップレベルウインドウの表示
root.mainloop()
