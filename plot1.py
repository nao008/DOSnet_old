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
args = parser.parse_args()

# print(args.dataname)
dataname = args.dataname

# データを読み込む
data = np.loadtxt(f'{dataname}_predict_test.txt')

# 散布図のデータ
x = data[:, 0]
y = data[:, 1]

# 回帰線の計算
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# プロット作成
fig, ax = plt.subplots()

# 散布図
ax.scatter(x, y)

# 回帰線
ax.plot(x, intercept + slope*x, 'r', label='y={:.2f}x+{:.2f}'.format(slope,intercept))

# ヒストグラム
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom + height + spacing, width, 0.2]
rect_histy = [left + width + spacing, bottom, 0.2, height]

ax_histx = plt.axes(rect_histx)
ax_histy = plt.axes(rect_histy)

ax_histx.hist(x, bins=50, alpha=0.5)
ax_histy.hist(y, bins=50, orientation='horizontal', alpha=0.5)

# ラベルとタイトル
ax.set_xlabel("y")
ax.set_ylabel("predict")
ax.set_title("predict vs y")

plt.show()
