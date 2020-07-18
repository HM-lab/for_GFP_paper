import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statistics as stats

plt.rcParams["font.family"] = "arial"
plt.rcParams["font.size"] = 12

Df_mgr = pd.read_csv("/Users/katohisaaki/Desktop/Pyworks/data_C10_n4.csv",index_col=0).iloc[:,8:16]
Df_intensity = pd.read_csv("/Users/katohisaaki/Desktop/Pyworks/data_C10_GFP.csv",index_col=0).iloc[:,8:16]

Df_mgr.columns = np.arange(len(Df_mgr.T))
Df_intensity.columns = np.arange(len(Df_intensity.T))

GFPmgr_arr = Df_mgr.iloc[:,0]
GFPintensity_arr = Df_intensity.iloc[:,0]

GFPmgr_mean = GFPmgr_arr.mean()
GFPintensity_mean = GFPintensity_arr.mean()

C10mgr = Df_mgr.iloc[:,1:]
C10intensity = Df_intensity.iloc[:,1:]

C10mgr_norm = np.log2(C10mgr/GFPmgr_mean)
C10intensity_norm = np.log2(C10intensity/GFPintensity_mean)


Df_melt1 = pd.melt(C10mgr_norm)
Df_melt2 = pd.melt(C10intensity_norm)

##outlier
outlier = -2
Df_melt1 = Df_melt1.iloc[:outlier,:]
Df_melt2 = Df_melt2.iloc[:outlier,:]


fig = plt.figure(figsize=(4.5,5.5))
ax1 = fig.add_subplot(111)
plt.subplots_adjust(left=0.2, right=0.8, bottom=0.3, top=0.7)
ax1.set_axisbelow(True)
plt.gca()
ax1.grid(axis="y", color="grey", lw=1,ls="--",zorder=.5)

ax1 = sns.barplot(x="variable",y="value",data=Df_melt1,color="skyblue",capsize=0.2,linewidth=1,errwidth=1,edgecolor=".2",ax=ax1,zorder=2)

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

ax1.set_yticks(np.linspace(-6, 1, 8))
ax2.set_yticks(np.linspace(-6, 1, 8))
ax1.set_ylim(-6,1)
ax2.set_ylim(-6,1)

#plt.savefig("C10GFPs_MGR.pdf")
plt.show()
