import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

Df = pd.read_csv("/Users/katohisaaki/Desktop/GFP_paper/GFPs_western.csv",index_col=0)

lists = [1,2,4,5,7,8]

Df_new = Df.iloc[:,lists]
Df_new_mean = Df_new.mean()
Df_new_std = Df_new.std(ddof=False)

plt.rcParams["font.size"] = 10
plt.rcParams["font.family"] = "arial"

fig = plt.figure(figsize=(5,4))
ax1 = fig.add_subplot(111)
plt.subplots_adjust(left=0.2, right=0.8, bottom=0.3, top=0.7)
ax1.set_axisbelow(True)
plt.gca()
ax1.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

colors = ["lime","skyblue","cadetblue"]

x1 = [0,1,2]
x2 = [4,5,6]

w = 0.8
ax1.bar(x1,Df_new_mean[[0,2,4]],yerr=Df_new_std[[0,2,4]],width=w,color=colors,edgecolor="black",capsize=5)
ax1.bar(x2,Df_new_mean[[1,3,5]],yerr=Df_new_std[[1,3,5]],width=w,color=colors,edgecolor="black",capsize=5)


ax1.set_yticks(np.linspace(0, 1.2, 5))
ax1.set_xticks([])
ax1.set_ylim(0,1.2)


# plt.savefig("GFPs_western.pdf")
plt.show()
