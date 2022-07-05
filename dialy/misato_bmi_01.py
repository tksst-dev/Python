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

# 体重と身長を入力
weight = float(input('体重（kg）：　'))
height = float(input('身長（cm）：　')) / 100

# BMI判定と結果表示
bmi = calc(weight, height)
result = check(bmi)
print('BMI：' + str(bmi))
print('判定：' + result)
