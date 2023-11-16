import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from scipy import stats
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

parser.add_argument(
    #wide or detail
    "--data_width",
    default="wide",
    type=str,
)

args = parser.parse_args()

#データの幅を選択(広義of詳細)
data_width = args.data_width

dataname = args.dataname
alldata = args.data
log = {}
if data_width == "wide":
    dropout_vals = [0.0, 0.2, 0.4, 0.6, 0.8]
elif data_width == "detail":
    dropout_vals = [0.3, 0.34, 0.38, 0.42, 0.46]
else:
    print("data_width is wide or detail")
    exit()
# ファイル名のリスト
filenames = [f"result/{dataname}_dropout{dropout_val}_predict_{alldata}.txt" for dropout_val in dropout_vals]

# 各ファイルからデータを読み込み、データフレームに変換
df_list = [pd.read_csv(filename, sep=" ", header=None) for filename in filenames]

#各データフレームの名称と色
labels = [f"dropout:{dropout_val}" for dropout_val in dropout_vals]

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
    log[f"{nearest_df[0][0]}_max:{dropout_vals[max_index]}"] = max_value
    log[f"{nearest_df[0][0]}_min:{dropout_vals[min_index]}"] = min_value
    all_nearest_df = pd.concat([all_nearest_df, nearest_df]).reset_index(drop=True)

print(log)

# 散布図のplot
fig1, ax1 = plt.subplots()
for i in range(len(all_nearest_df)):
    ax1.scatter(all_nearest_df[0][i], all_nearest_df[1][i], color=colors[i%len(labels)], label=labels[i%len(labels)])
# 軸の名前を設定
plt.xlabel('true')
plt.ylabel('predict')
plt.tight_layout()
plt.savefig(f'resultplot/dropout{data_width}_scatter.png')
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
plt.xlabel('true')
plt.ylabel('predict')
plt.tight_layout()
plt.savefig(f"resultplot/dropout{data_width}.png")
plt.show(block=False)
plt.close()

