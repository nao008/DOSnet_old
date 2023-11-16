import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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


print(log)

# 散布図のplot
fig1, ax1 = plt.subplots()
# 凡例用のハンドラとラベルを保存するリスト
handlers = []
labels_list = []
for i in range(len(all_nearest_df)):
    scatter = ax1.scatter(all_nearest_df[0][i], all_nearest_df[1][i], color=colors[i%len(labels)], label=labels[i%len(labels)])
    # 同じラベルが既にリストに存在しない場合に、ハンドラとラベルを追加
    if labels[i%len(labels)] not in labels_list:
        handlers.append(scatter)
        labels_list.append(labels[i%len(labels)])
plt.legend(handles=handlers, labels=labels_list)
plt.xlabel('true(eV)')
plt.ylabel('predict(eV)')
plt.grid(True)
plt.tight_layout()
plt.savefig(f'resultplot/seed_scatter.png')
plt.show(block=False)
plt.close()

#エラーバーのplot
fig2, ax2 = plt.subplots()
list = []
for i in range(len(all_nearest_df)):
    list.append(all_nearest_df[1][i])
    if i % len(labels) == len(labels)-1:
        plt.vlines(all_nearest_df[0][i], min(list), max(list), color='black')
        list = []
# 軸の名前を設定
plt.xlabel('true(eV)')
plt.ylabel('predict(eV)')
plt.grid(True)
plt.tight_layout()
plt.savefig(f"resultplot/seed.png")
plt.show(block=False)
plt.close()


