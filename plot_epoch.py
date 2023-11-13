import matplotlib.pyplot as plt
import pandas as pd

# データを定義します
data = {
    'Train MAE': [0.24689536, 0.13528028, 0.10776418, 0.10679102, 0.095377654],
    'Train RMSE': [0.3097716798707712, 0.1745908964223308, 0.1405839330260566, 0.1387652297833131, 0.12510889495704156],
    'Test MAE': [0.2843116, 0.17189005, 0.15571454, 0.152317, 0.14757837],
    'Test RMSE': [0.3580856205391732, 0.22263812108438602, 0.20792557429406003, 0.20077105284746116, 0.20039105034201174]
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