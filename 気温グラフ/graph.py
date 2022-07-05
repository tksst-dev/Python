import pandas as pd, matplotlib.pyplot as plt
# CSVファイルを読み込む --- (*1)
df = pd.read_csv('data.csv', header=None, 
        names=['date','High','Low'],
        index_col=0)
# グラフを描画しPNGファイルに保存 --- (*2)
df.plot() # 描画
plt.savefig('kion.png') # PNGで保存
plt.show()

