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

data = np.loadtxt(f'result/{dataname}_predict_{alldata}.txt')

x = data[:, 0]
y = data[:, 1]

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

fig = plt.figure(figsize=(8, 8))

gs = fig.add_gridspec(4, 4)

ax = fig.add_subplot(gs[1:4, :3])
axx = fig.add_subplot(gs[0, :3], sharex=ax)
axy = fig.add_subplot(gs[1:4, 3], sharey=ax)

ax.scatter(x, y, s=10)
ax.grid()
ax.plot(x, intercept + slope*x, 'r', label='y={:.2f}x+{:.2f}'.format(slope,intercept))

axx.hist(x, bins=100, alpha=0.5)
axy.hist(y, bins=100, orientation='horizontal', alpha=0.5)

axx.axis('off')
axy.axis('off')

ax.set_xlabel("ture(eV)")
ax.set_ylabel("predict(eV)")

plt.savefig(f"resultplot/{dataname}_{alldata}.png")
plt.show()