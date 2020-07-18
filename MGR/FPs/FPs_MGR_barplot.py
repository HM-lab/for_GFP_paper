import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statistics as stats

plt.rcParams["font.family"] = "arial"
plt.rcParams["font.size"] = 10.5

Df_mgr = pd.read_csv("/Users/katohisaaki/Desktop/GFP_paper/FPs_38C_MGR.csv",index_col=0).iloc[:,6:]
Df_mgr.columns = np.arange(len(Df_mgr.T))

Df_melt1 = pd.melt(Df_mgr)

fig = plt.figure(figsize=(4.2,3))
ax1 = fig.add_subplot(111)
plt.subplots_adjust(left=0.1, right=0.75, bottom=0.1, top=0.9)
ax1.set_axisbelow(True)
plt.gca()
ax1.grid(axis="y", color="grey", lw=1,ls="--",zorder=.5)

colors = ["darkgray","lime","skyblue","khaki","cadetblue","lightcoral"]

ax1 = sns.barplot(x="variable",y="value",data=Df_melt1,palette=colors,capsize=0.2,linewidth=1,errwidth=1,edgecolor=".2",ax=ax1,zorder=2)


columncounts = np.repeat(55,len(Df_melt1))


def normaliseCounts(widths,maxwidth):
    widths = np.array(widths)/float(maxwidth)
    return widths

widthbars = normaliseCounts(columncounts,95)

for bar,newwidth in zip(ax1.patches,widthbars):
    x = bar.get_x()
    width = bar.get_width()
    centre = x+width/2.

    bar.set_x(centre-newwidth/2.)
    bar.set_width(newwidth)

ax1.set_yticks(np.linspace(0,6, 7))
ax1.set_ylim(0, 6)

plt.savefig("FPs_growth_barplot.pdf")
plt.show()
