import random

num = random.randint(0, 6)

if num == 0:
    print('大吉')
elif num == 1:
    print('中吉')
elif num == 2:
    print('吉')
elif num == 3:
    print('凶')
elif num == 4:
    print('凶')
elif num == 5:
    print('中凶')
else:
    print('大凶')
