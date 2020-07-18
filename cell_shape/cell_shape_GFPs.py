import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

list = ["GFP","superfolderGFP","ymoxGFP"]
N = len(list)

Df_ratio = pd.read_csv("~/Desktop//GFP_paper/cell_shape_FPs.csv",index_col=0).iloc[:,[1,2,4]]
Df_ratio.columns = list

Df_melt = pd.melt(Df_ratio).dropna()

colors = ["lime","skyblue","cadetblue"]

plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5

fig = plt.figure(figsize=(3,3.7))

plt.gca()
ax = fig.add_subplot(1,1,1)

ax.set_axisbelow(True)

##swarmplot
sns.violinplot(x="variable",y="value",data=Df_melt,inner=None, color="white",facecolor="black", linewidth=1,zorder=3)
sns.swarmplot(x="variable",y="value",data=Df_melt,palette=colors,edgecolor="black",size=1.5,linewidth=0.35,zorder=4)

##boxplot
# sns.boxplot(x="variable",y="value",data=Df_melt,width=0.6,medianprops=dict(lw=0),palette=colors,linewidth=1,zorder=4)

# lw = 2
# plt.plot([-0.4,0.4],[1.3223,1.3223],color="red",lw=lw,zorder=5)
# plt.plot([0.6,1.4],[1.2876,1.2876],color="red",lw=lw,zorder=5)
# plt.plot([1.6,2.4],[1.2019,1.2019],color="red",lw=lw,zorder=5)


plt.ylim(1,2.8)
plt.yticks(np.linspace(1,2.8,10))
plt.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

# plt.savefig("FPs_violin.pdf")
plt.show()
