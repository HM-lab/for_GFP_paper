import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

list = ["Vector","GFP","superfolderGFP","Venus","ymoxGFP","mScarlet"]
N = len(list)

Df_ratio = pd.read_csv("~/Desktop//GFP_paper/cell_shape_FPs.csv",index_col=0)
Df = Df_ratio.iloc[:,[4,2,1]]

colors = ["cadetblue","skyblue","lime"]

plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5

fig = plt.figure(figsize=(6,2.8))
ax1 = fig.add_subplot(111)
plt.subplots_adjust(left=0.2, right=0.8, bottom=0.1, top=0.9)
ax1.set_axisbelow(True)
plt.gca()

bin = 25
plt.hist(Df.T, bins=bin, histtype='step',color=colors , fill=True, alpha=0.7)
plt.grid(axis="x", color="grey", lw=1,ls="--",zorder=.5)
plt.axvline(x=1.6,color="red")

plt.xlim(1,2.4)
plt.ylim(1,60)
plt.savefig("GFPs_hist.pdf")

plt.show()
