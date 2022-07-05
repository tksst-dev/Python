import tkinter as tk

root = tk.Tk()
root.title('Labelテスト')
root.geometry('300x100')

label_top = tk.Label(root, text = 'TOP', relief = tk.SOLID, width = 8)
label_bottom = tk.Label(root, text = 'BOTTOM', relief = tk.SOLID, width = 8)
label_left = tk.Label(root, text = 'LEFT', relief = tk.SOLID, width = 8)
label_right = tk.Label(root, text = 'RIGHT', relief = tk.SOLID, width = 8)

label_left.pack(side = tk.LEFT)
label_top.pack(side = tk.TOP)
label_right.pack(side = tk.RIGHT)
label_bottom.pack(side = tk.BOTTOM)

# トップレベルウインドウの表示
root.mainloop()
