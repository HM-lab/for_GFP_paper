import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

Df = pd.read_csv("/Users/katohisaaki/Desktop/GFP_paper/cell_shape_FPs.csv",index_col=0)
Df2 = pd.read_csv("/Users/katohisaaki/Desktop/GFP_paper/cell_shape_N10s.csv",index_col=0).iloc[:,1:]

colors = ["darkgray","lime","skyblue","khaki","cadetblue","lightcoral"]
colors2 = ["indigo","mediumorchid","plum"]


plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5

x = np.arange(len(Df.T))

fig = plt.figure(figsize=(8,3.5))

ax = fig.add_subplot(1,1,1)

ax.set_axisbelow(True)
ax.grid(axis="y", color="grey", lw=1,ls="--",zorder=.5)

plt.bar(x, Df.std(ddof=False),color=colors,edgecolor="black")
plt.bar([6,7,8], Df2.std(ddof=False),color=colors2,edgecolor="black")


min = 0
max = 0.4
ax.set_yticks(np.linspace(min, max, 6))
ax.set_ylim(min,max)
ax.set_xticks(np.linspace(0, 8, 9))



plt.savefig("cell_shape_bar(SD).pdf")
plt.show()
