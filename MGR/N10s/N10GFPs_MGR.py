import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

## read data
df_mgr = pd.read_excel("N10_GFPs_MGR.xlsx",index_col=0).iloc[:,1:]
df_GFP = pd.read_excel("N10_GFPs_GFP.xlsx",index_col=0).iloc[:,1:]
df_mgr.columns = np.arange(len(df_mgr.T))
df_GFP.columns = np.arange(len(df_GFP.T))

## melt dataframe
df_melt1 = pd.melt(df_mgr)
df_melt2 = pd.melt(df_GFP)

## plot figure
plt.rcParams["font.family"] = "arial"
plt.rcParams["font.size"] = 10.5

fig = plt.figure(figsize=(3.5,3))
ax1 = fig.add_subplot(111)
plt.subplots_adjust(left=0.1, right=0.75, bottom=0.1, top=0.9)
ax1.set_axisbelow(True)
plt.gca()

## ax1 = MGR
ax1.grid(axis="y", color="grey", lw=1,ls="--",zorder=.5)
ax1 = sns.barplot(x="variable", y="value", data=df_melt1,
                  color="skyblue", capsize=0.2,linewidth=1,
                  errwidth=1, edgecolor=".2", ax=ax1, zorder=2)

## ax2 = GFP intensity
ax2 = ax1.twinx()
ax2 = sns.boxplot(x="variable", y="value", data=df_melt2,
                  color="lime", width=0.75, linewidth=0.8,
                  fliersize=2, ax=ax2, zorder=1, boxprops=dict(alpha=1))


## set bar width
columncounts = np.repeat(55,len(df_melt1))
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

ax1.set_yticks(np.linspace(0, 5, 6))
ax2.set_yticks(np.linspace(0, 20000, 6))
ax1.set_ylim(0, 5)
ax2.set_ylim(0,20000)

plt.show()

## save figure
# plt.savefig("N10GFPs_MGR_noEGFP_2.pdf")
