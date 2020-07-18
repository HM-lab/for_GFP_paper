import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Df = pd.read_csv("~/Desktop/Book11.csv",index_col=0)
# arr = [np.array(Df.iloc[:,i]) for i in np.arange(len(Df.T)).tolist()]

Df = pd.read_excel("~/Desktop/mean_and_SD.xlsx",index_col=0).iloc[:,:4]

# Df_mean=Df.mean()
# Df_SE =Df.sem(ddof=False)

# pos = pd.DataFrame([0,1,1,1,1,1,1,1,1,0,0,0,0])
pos = pd.DataFrame([0,0,0,0,0,0,-0.6,-0.6,-0.6,-1,-1,-1,-1,-2,-2])
pos.index=Df.index
Df["pos"] = pos[0]

plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5


colors = ["darkgray","lime","skyblue","khaki","cadetblue","lightcoral","indigo","mediumorchid","plum","darkgreen","mediumseagreen","mediumaquamarine","mediumturquoise","orchid","violet"]
# sns.regplot(Df.iloc[:,1], Df.iloc[:,0])

plt.figure(figsize=(7,5))
for i in np.arange(len(Df)):
    plt.scatter(Df.iloc[i,1] ,Df.iloc[i,-1] ,marker="o" ,color=colors[i], linewidth=1, edgecolor="black" ,s=100+int(Df.iloc[i,0]*100), alpha=1,zorder=i+2)
plt.axhline(y=0, color="grey", lw=3, zorder=0.5)
plt.axhline(y=-0.6, color="grey", lw=3, zorder=0.5)
plt.axhline(y=-1, color="grey", lw=3, zorder=0.5)
plt.axhline(y=-2, color="grey", lw=3, zorder=0.5)

plt.xlim(1.14,1.46)
plt.xticks(np.linspace(1.15,1.45,6))

# plt.grid(axis="x", color="grey", lw=0.85,ls="--",zorder=.1)

plt.savefig("Cys_cellElongation_2.pdf")
plt.show()
