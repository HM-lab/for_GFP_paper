import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statistics as stats

plt.rcParams["font.family"] = "arial"
plt.rcParams["font.size"] = 9

Df_mgr = pd.read_csv("/Users/katohisaaki/Desktop/GFP_paper/FPs_MGR.csv",index_col=0).iloc[:,6:]
Df_GFP = pd.read_csv("/Users/katohisaaki/Desktop/GFP_paper/FPs_GFP.csv",index_col=0).iloc[:,6:]

#Df_mgr = Df_mgr.iloc[:,[1,2,4]]
#Df_GFP = Df_GFP.iloc[:,[1,4,2]]

Df_mgr.columns = np.arange(len(Df_mgr.T))
Df_GFP.columns = np.arange(len(Df_GFP.T))


Df_melt1 = pd.melt(Df_mgr)
Df_melt2 = pd.melt(Df_GFP)
# Df_melt2.loc[Df_melt2["variable"] == 0, "value"] =-1
# Df_melt2.loc[Df_melt2["variable"] == 1, "value"] =-1
# Df_melt2.loc[Df_melt2["variable"] == 2, "value"] =-1
# Df_melt2.loc[Df_melt2["variable"] == 3, "value"] =-1
# Df_melt2.loc[Df_melt2["variable"] == 4, "value"] =-1
Df_melt2.loc[Df_melt2["variable"] == 5, "value"] =-1

colors = ["darkgray","palegreen","skyblue","khaki","cadetblue","lightcoral"]


fig = plt.figure(figsize=(4.2,3))
ax1 = fig.add_subplot(111)
ax1.set_axisbelow(True)
plt.gca()
plt.subplots_adjust(left=0.1, right=0.75, bottom=0.1, top=0.9)
ax1.grid(axis="y", color="grey", lw=1,ls="--",zorder=.5)
ax1 = sns.barplot(x="variable",y="value",data=Df_melt1,palette=colors,capsize=0.2,linewidth=1,errwidth=1,edgecolor=".2",ax=ax1,zorder=2)

ax2 = ax1.twinx()
ax2 = sns.boxplot(x="variable",y="value",data=Df_melt2,color="lime",width=0.75,linewidth=0.8,fliersize=2,ax=ax2,zorder=1,boxprops=dict(alpha=1))


#グラフの太さを指定　
#### Set these based on your column counts
columncounts = np.repeat(55,len(Df_melt1))

# Maximum bar width is 1. Normalise counts to be in the interval 0-1. Need to supply a maximum possible count here as maxwidth

def normaliseCounts(widths,maxwidth):
    widths = np.array(widths)/float(maxwidth)
    return widths

widthbars = normaliseCounts(columncounts,95) #それぞれの軸の％をだす [55,55,55]だと55/100 (0.55)

# Loop over the bars, and adjust the width (and position, to keep the bar centred)
for bar,newwidth in zip(ax1.patches,widthbars):
    x = bar.get_x()
    width = bar.get_width()
    centre = x+width/2.

    bar.set_x(centre-newwidth/2.)
    bar.set_width(newwidth)

ax1.set_yticks(np.linspace(0, 5, 6))
ax2.set_yticks(np.linspace(0, 2000, 6))
ax1.set_ylim(0, 5)
ax2.set_ylim(0,2000)


# plt.savefig("N10GFPs_MGR.pdf")
plt.show()
