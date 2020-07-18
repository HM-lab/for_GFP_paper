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

x = np.arange(len(Df_new))

plt.rcParams["font.size"] = 10
plt.rcParams["font.family"] = "arial"

fig = plt.figure(figsize=(5,4))
ax1 = fig.add_subplot(111)
plt.subplots_adjust(left=0.2, right=0.8, bottom=0.3, top=0.7)
ax1.set_axisbelow(True)

ax1.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

w = 0.4
plt.bar(x, Df_new_mean[[0,2,4]],yerr=Df_new_std[[0,2,4]],width=w,color="royalblue",edgecolor="black",label="-DTT",capsize=5)
plt.bar(x+w, Df_new_mean[[1,3,5]],yerr=Df_new_std[[1,3,5]],width=w,color="coral",edgecolor="black",label="+DTT",capsize=5)
plt.xticks(x + w*0.5, Df_new.index)

ax1.set_yticks(np.linspace(0, 1.2, 5))
ax1.set_ylim(0,1.2)


# plt.savefig("GFPs_western.pdf")
plt.show()
