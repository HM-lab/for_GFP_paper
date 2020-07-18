import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## read data
param = "C114_C"
df = pd.read_excel("CalMorph_data.xlsx",index_col=0).loc[:,param].T

## reshape dataframe
df_reshaped = pd.DataFrame({"Vector":df.loc["Vector_1":"Vector_5"].values,
                            "GFPy66g":df.loc["GFPy66g_1":"GFPy66g_5"].values,
                            "Gpm1":df.loc["Gpm1_1":"Gpm1_5"].values,
                            "Gpm1-mutant":df.loc["Gpm1mutant_1":"Gpm1mutant_5"].values})

## melt dataframe
df_melt = pd.melt(df_reshaped)

## plot figure
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
sns.boxplot(x="variable",y="value",data=df_melt,
            width=0.8,palette=colors,ax=ax,linewidth=1,zorder=3)
sns.stripplot(x="variable",y="value",data=df_melt,
              jitter=False,size=3,ax=ax,color="black",linewidth=1.5,zorder=10)

plt.show()

## save figure
plt.savefig("C114_C_pdf.pdf")
