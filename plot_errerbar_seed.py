import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import argparse

parser = argparse.ArgumentParser(description="result plot")
parser.add_argument(
    "--dataname",
    default="CH_data",
    type=str,
)

parser.add_argument(
    "--data",
    default="test",
    type=str,
)

args = parser.parse_args()

dataname = args.dataname
alldata = args.data
log = {}
seed_vals = [42, 666, 2023, 1, 3]
list_len = len(seed_vals)
# ファイル名のリスト
filenames = [f"result/{dataname}_seed{seed_val}_predict_{alldata}.txt" for seed_val in seed_vals]

# 各ファイルからデータを読み込み、データフレームに変換
df_list = [pd.read_csv(filename, sep=" ", header=None) for filename in filenames]

#各データフレームの名称と色
labels = [f"seed:{seed_vals}" for seed_vals in seed_vals]
colors = ['red', 'blue', 'green', 'yellow', 'purple']

fig, ax = plt.subplots()
# プロットしたい値のリスト
values = [0, 1, 2, 3, 4, 5, 6]
# 抽出した全要素をまとめるdf
all_nearest_df = pd.DataFrame()
for value in values:
    #valueごとに抽出した要素をまとめるdf
    nearest_df = pd.DataFrame()
    for df in df_list:
        # カラム0の値がvalueに最も近い行を見つける
        nearest = df.iloc[(df[0]-value).abs().argsort()[:1]]
        nearest_df = pd.concat([nearest_df, nearest]).reset_index(drop=True)
    # print(nearest_df)
    #logに残す
    max_value = nearest_df[1].max()
    min_value = nearest_df[1].min()
    max_index = nearest_df[1].idxmax()
    min_index = nearest_df[1].idxmin()
    log[f"{nearest_df[0][0]}_max:{seed_vals[max_index]}"] = max_value
    log[f"{nearest_df[0][0]}_min:{seed_vals[min_index]}"] = min_value
    all_nearest_df = pd.concat([all_nearest_df, nearest_df]).reset_index(drop=True)

m = all_nearest_df.pivot_table(index=0, values=1, aggfunc='mean')
e = all_nearest_df.pivot_table(index=0, values=1, aggfunc='sem')

list_len = len(seed_vals)
# 散布図のplot
for i in range(len(all_nearest_df)):
    ax.scatter(all_nearest_df[0][i], all_nearest_df[1][i], color=colors[i%list_len], label=labels[i%list_len])

# エラーバーの追加
m.plot(xlim=[-0.2, 6.2], yerr=e)
# 軸の名前を設定
plt.xlabel('true')
plt.ylabel('predict')
print(log)
plt.tight_layout()
plt.savefig("resultplot/seed.png")
plt.show()

