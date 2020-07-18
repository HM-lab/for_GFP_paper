import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

## read data
df = pd.read_csv("hKO_ydj1_MGR.csv",index_col=0)
df.columns = np.arange(len(df.T))

## melt dataframe
df_melt = pd.melt(df)

## plot figure
plt.rcParams["font.family"] = "arial"
plt.rcParams["font.size"] = 10.5
colors = ["darkgray","lime","cadetblue",
          "dimgrey","seagreen","darkcyan"]

fig = plt.figure(figsize=(4.2,3))
ax = fig.add_subplot(111)
plt.subplots_adjust(left=0.1, right=0.75, bottom=0.1, top=0.9)
ax.set_axisbelow(True)
plt.gca()

ax.grid(axis="y", color="grey", lw=1,ls="--",zorder=.5)

ax = sns.barplot(x="variable", y="value", data=df_melt,
                 palette=colors, capsize=0.2, linewidth=1, errwidth=1,
                 edgecolor=".2", ax=ax, zorder=2)

## set bar width
columncounts = np.repeat(55,len(df_melt))
def normaliseCounts(widths,maxwidth):
    widths = np.array(widths)/float(maxwidth)
    return widths

widthbars = normaliseCounts(columncounts,95)

for bar,newwidth in zip(ax.patches,widthbars):
    x = bar.get_x()
    width = bar.get_width()
    centre = x+width/2.
    bar.set_x(centre-newwidth/2.)
    bar.set_width(newwidth)

ax.set_yticks(np.linspace(0,5, 6))
ax.set_ylim(0, 5)

plt.show()

## save figure
# plt.savefig("hKO_ydj1s_growth_barplot.pdf")
