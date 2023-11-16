import matplotlib.pyplot as plt
import pandas as pd

# データを辞書形式で定義
data = {
    'model0': [0.16664739, 0.21602112071546442, 0.20780216, 0.2674656095412875],
    'model1': [0.12731685, 0.1657191377894558, 0.1715524, 0.22430902385064247],
    'model2': [0.11463376, 0.1499690860940069, 0.15415356, 0.2065505529143035],
    'model3': [0.109980635, 0.1434798142718718, 0.14816703, 0.1988091090613793],
    'model4': [0.32328784, 0.4201461015910621, 0.34640843, 0.44047965635374614],
}

# データフレームに変換
df = pd.DataFrame(data, index=["train_rme", "train_rmae", "test_rme", "test_rmae"])

# グラフをプロットします
plt.figure(figsize=(10, 5))
for column in df.columns:
    plt.plot(df.index, df[column], marker='o', label=column)
plt.legend()
plt.xlabel('metric')
plt.ylabel('value(eV)')
plt.title('Trends by number of models')
plt.grid(True)
plt.savefig("resultplot/model.png")
plt.show()
