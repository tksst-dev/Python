import tkinter as tk

# BMI計算関数
def calc(weight, height):
    return weight / (height ** 2)


# 肥満度判定結果
def check(bmi):
    if bmi < 18.5:
        result = '低体重'
    elif bmi < 25.0:
        result = '普通体重'
    elif bmi < 30.0:
        result = '肥満度１'
    elif bmi < 35.0:
        result = '肥満度２'
    elif bmi < 40.0:
        result = '肥満度３'
    else:
        result = '肥満度４'
    return result

# トップレベルウインドウの生成
root = tk.Tk()
root.title('肥満度チェック')
root.geometry('250x150')

# Labelウィジットの生成
label_1 = tk.Label(root, text = '体重')
label_2 = tk.Label(root, text = 'kg')
label_3 = tk.Label(root, text = '身長')
label_4 = tk.Label(root, text = 'cm')
label_5 = tk.Label(root, text = '身長と体重を入力してください。')

# Entryウィジットの生成
weight = tk.Entry(width = 5)
height = tk.Entry(width = 5)

# Buttonのハンドラ関数
def judgement():
    w = float(weight.get())
    h = float(height.get()) / 100
    s = check(calc(w, h))
    label_5['text'] = '肥満度：' + str(s)

# Buttonウィジットの生成
button = tk.Button(root, text = 'BMI判定', command = judgement)


# 各列の割合の指定
root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)

# 各行の割合を指定
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.rowconfigure(3, weight = 1)

# １行目
label_1.grid(column = 0, row = 0, sticky = tk.E)
weight.grid(column = 1, row = 0)
label_2.grid(column = 2, row = 0, sticky = tk.W)

# ２行目
label_3.grid(column = 0, row = 1, sticky = tk.E)
height.grid(column = 1, row = 1)
label_4.grid(column = 2, row = 1, sticky = tk.W)

# ３行目
button.grid(column = 0, row = 2, columnspan = 3)


# ４行目
label_5.grid(column = 0, row = 3, columnspan = 3)

# トップレベルウィンドウの表示
root.mainloop()
