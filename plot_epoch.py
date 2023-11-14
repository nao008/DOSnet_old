import matplotlib.pyplot as plt
import pandas as pd

# データを定義します
data = {
    'train MAE': [0.22684985, 0.13963868, 0.12096729, 0.10556118, 0.099834174],
    'train RMSE': [0.29553216353569, 0.17763033116680382, 0.15572491273736705, 0.13662158374275865, 0.13080303915307018],
    'test MAE': [0.26087496, 0.17985545, 0.16440299, 0.14937057, 0.14799653],
    'test RMSE': [0.3367021640666689, 0.23670846897876327, 0.22470274104234153, 0.20581440226246003, 0.20683542022784482]
}


# データフレームを作成します
df = pd.DataFrame(data, index=[20, 60, 100, 150, 200])

# グラフをプロットします
plt.figure(figsize=(10, 5))
for column in df.columns:
    plt.plot(df.index, df[column], marker='o', label=column)
plt.legend()
plt.xlabel('epoch')
plt.ylabel('Value')
plt.title('Trends by number of epochs')
plt.grid(True)
plt.savefig("resultplot/epoch.png")
plt.show()