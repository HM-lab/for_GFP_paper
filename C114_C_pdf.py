import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

Df = pd.read_excel("/Volumes/HDD/CalMorph/CalMorph_data.xlsx",index_col=0)

Df_data = pd.DataFrame(data=Df).T
Df_new = pd.DataFrame(Df_data,dtype="float32")

param = "C114_C"

Df_param = pd.DataFrame({"Vector":Df.loc["V_1":"V_5",param].values,
                    "GFPy66g":Df.loc["GFPy66g_1":"GFPy66g_5",param].values,
                    "Gpm1":Df.loc["Gpm1_1":"Gpm1_5",param].values,
                    "Gpm1-mutant":Df.loc["Gpm1m_1":"Gpm1m_5",param].values})

Df_param_melt = pd.melt(Df_param)


plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 12

fig = plt.figure(figsize=(4.5,4))
plt.subplots_adjust(left=0.2, right=0.8, bottom=0.1, top=0.9)
ax = fig.add_subplot(1,1,1)
ax.set_axisbelow(True)
plt.gca()

colors = ["lightgray","lime","orchid","darkorchid"]
plt.ylim(0.95,1.06)
ax.grid(axis="y", color="grey", lw=1,ls="--",zorder=.5)
sns.boxplot(x="variable",y="value",data=Df_param_melt,width=0.8,palette=colors,ax=ax,linewidth=1,zorder=3)
sns.stripplot(x="variable",y="value",data=Df_param_melt,jitter=False,size=3,ax=ax,color="black",linewidth=1.5,zorder=10)

#plt.xlabel("genotypes")
#plt.ylabel("M:Bud axis ratio")
#plt.savefig("C114_C.pdf")
plt.show()
