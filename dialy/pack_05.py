import tkinter as tk

root = tk.Tk()
root.title('Labelテスト')
root.geometry('300x100')

label_top = tk.Label(root, text = 'TOP', relief = tk.SOLID, width = 8)
label_bottom = tk.Label(root, text = 'BOTTOM', relief = tk.SOLID, width = 8)
label_left = tk.Label(root, text = 'LEFT', relief = tk.SOLID, width = 8)
label_right = tk.Label(root, text = 'RIGHT', relief = tk.SOLID, width = 8)

label_top.pack(anchor = tk.N)
label_bottom.pack(anchor = tk.S)
label_left.pack(anchor = tk.W)
label_right.pack(anchor = tk.E)

# トップレベルウインドウの表示
root.mainloop()
