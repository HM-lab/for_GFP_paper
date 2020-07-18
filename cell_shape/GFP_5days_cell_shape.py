
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

list = ["Vector","GFP"]
N = len(list)

Df_ratio = pd.read_csv("/Users/katohisaaki/Desktop/GFP_paper/GFP_5day_scell_shape.csv",index_col=0)
Df_ratio.columns = list
# print(Df_ratio.mean())

Df_melt = pd.melt(Df_ratio).dropna()

colors = ["darkgray","lime"]


plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5

plt.figure(figsize=(3.2,3.5))

plt.gca()


##swarmplot
sns.violinplot(x="variable",y="value",data=Df_melt,inner=None, color="white",facecolor="black", linewidth=1,zorder=3)
sns.swarmplot(x="variable",y="value",data=Df_melt,palette=colors,edgecolor="black",size=3,linewidth=0.35,zorder=4)

plt.ylim(1,3.4)
plt.yticks(np.linspace(1,3.4,11))
plt.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

# plt.savefig("GFP_5days_violin.pdf")

plt.show()
