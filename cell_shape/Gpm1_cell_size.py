import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

list = ["Gpm1","Gpm1-S151C"]
N = len(list)

Df_ratio = pd.read_csv("~/Desktop//GFP_paper/cell_size_Gpm1s.csv",index_col=0)
Df_ratio.columns = list
Df_ratio.mean()
Df_melt = pd.melt(Df_ratio).dropna()

colors = ["orchid","violet"]


plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5

plt.figure(figsize=(2.4,4))
plt.subplots_adjust(left=0.25, right=0.9)


plt.gca()

##vilolinplot
#sns.violinplot(x="variable",y="value",data=Df_melt,palette=colors,zorder=1)

##swarmplot
sns.violinplot(x="variable",y="value",data=Df_melt,inner=None, color="white",facecolor="black", linewidth=1,zorder=3)
sns.swarmplot(x="variable",y="value",data=Df_melt,palette=colors,edgecolor="black",size=1.5,linewidth=0.35,zorder=4)

plt.ylim(1800,11000)
plt.yticks(np.linspace(1800,11000,11))
plt.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

plt.savefig("FPs_violin.pdf")
plt.show()
