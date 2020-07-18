import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Df = pd.read_csv("/Users/katohisaaki/Desktop/GFP_paper/AA_count.csv",index_col=0)
Df2 = pd.read_csv("/Users/katohisaaki/Desktop/GFP_paper/AA_count_100000.csv",index_col=0)
Df2 = pd.concat([Df.iloc[:,0],Df2],axis=1,sort=False)

a = np.log2(Df.iloc[:,2]/Df.iloc[:,0])
b = np.log2(Df2.iloc[:,2]/Df2.iloc[:,0])

Df_new = pd.concat([a,b],axis=1,sort=False)
Df_new.columns = ["total","highly"]

##sort Df_new
Df_new = Df_new.sort_values(by="total",ascending=False)
#Df_new =Df_new.loc[["R","K","D","E","N","Q","H","Y","W","S","T","G","P","A","M","C","F","L","V","I"]]
##

x = np.arange(len(Df_new.index))
labels = Df_new.index
width = 0.45

plt.rcParams["font.size"] = 12
plt.rcParams["font.family"] = "arial"

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(1,1,1)
ax.set_axisbelow(True)
plt.gca()

plt.bar(x,Df_new.iloc[:,0],color="darkgray",width=width,edgecolor="black",label="Total protein",align="center",zorder=2)
plt.bar(x+width,Df_new.iloc[:,1],color="sandybrown",width=width,edgecolor="black",label="Highly expressed protein",align="center",zorder=2)
plt.xticks(x + width*0.5, labels)

plt.axhline(y=0, color='black',linestyle='-',linewidth=0.5,zorder=1)
ax.grid(axis="y", color="grey", lw=1,ls="--",zorder=.5)
#ax.grid(axis="x", color="grey", lw=1,ls="--",zorder=.5)

#plt.legend(loc='upper right')

ax.set_yticks(np.linspace(-3, 2, 6))
ax.set_ylim(-3,2)

plt.savefig("AA_count.pdf")

plt.show()
