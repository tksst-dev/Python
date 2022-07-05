# BMI計算関数
calc = lambda weight, height: weight / (height ** 2)

# 肥満度判定結果
def check(bmi):
    judg = [[18.5, '低体重'], [25.0, '普通体重'],
            [30.0, '肥満度１'], [35.0, '肥満度２'],
            [40.0, '肥満度３']]

    result = '肥満度４'
    for i in range(len(judg)):
        if bmi < judg[i][0]:
            result = judg[i][1]
            break
    return result

# 体重と身長を入力
weight = float(input('体重（kg）：　'))
height = float(input('身長（cm）：　')) / 100

# BMI判定と結果表示
bmi = calc(weight, height)
result = check(bmi)
print('BMI：' + str(bmi))
print('判定：' + result)
