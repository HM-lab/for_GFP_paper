import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import random

Df_V1 = pd.read_csv("~/Desktop/CellProfiler/BY4743_V(HU)_1Cell.csv").iloc[:,[11,17]]
Df_m1 = pd.read_csv("~/Desktop/CellProfiler/BY4743_+URA3_1Cell.csv").iloc[:,[11,17]]

Df_V2 = pd.read_csv("~/Desktop/CellProfiler/BY4743_V(HU)_1Cell.csv").iloc[:,[11,17]]
Df_m2 = pd.read_csv("~/Desktop/CellProfiler/BY4743_+URA3_1Cell.csv").iloc[:,[11,17]]

Df_V3 = pd.read_csv("~/Desktop/CellProfiler/BY4743_V(HU)_1Cell.csv").iloc[:,[11,17]]
Df_m3 = pd.read_csv("~/Desktop/CellProfiler/BY4743_+URA3_1Cell.csv").iloc[:,[11,17]]

n=0
arr_mean = np.zeros(0)
arr_std = np.zeros(0)
arr_thres = np.zeros(0)
thres = 1.5

number = 100
p_values = []
while n < number:
    Df_V = pd.concat([Df_V1.loc[random.sample(list(Df_V1.index),100),:].reset_index(drop=True),\
                        Df_V2.loc[random.sample(list(Df_V2.index),100),:].reset_index(drop=True),\
                        Df_V3.loc[random.sample(list(Df_V3.index),100),:].reset_index(drop=True)],\
                        axis=0,sort=False).reset_index(drop=True)
    Df_m = pd.concat([Df_m1.loc[random.sample(list(Df_m1.index),100),:].reset_index(drop=True),\
                        Df_m2.loc[random.sample(list(Df_m2.index),100),:].reset_index(drop=True),\
                        Df_m3.loc[random.sample(list(Df_m3.index),100),:].reset_index(drop=True)],\
                        axis=0,sort=False).reset_index(drop=True)


    list2 = ["A","B"]
    N = len(list2)
    Df = pd.concat([Df_V,Df_m],axis=1,sort=False)

    Df_ratio = pd.DataFrame()
    vals = np.arange(0,int(len(Df.T)),2)

    for i in vals:
        a = 0
        a = (Df.iloc[:,i]/Df.iloc[:,i+1]).dropna()
        Df_ratio = pd.concat([Df_ratio,a],axis=1,sort=False)

    arr_mean = np.append(arr_mean,Df_ratio.mean())
    arr_std = np.append(arr_std,Df_ratio.std())
    for m in np.arange(len(Df_ratio.T)):
        arr_thres = np.append(arr_thres,len(Df_ratio.iloc[:,m][Df_ratio.iloc[:,m] > thres].dropna()))

    n += 1

    a = np.array(Df_ratio.iloc[:,0])
    b = np.array(Df_ratio.iloc[:,1])
    f,p = stats.levene(a,b,center="median")
    p_values.append(p)

means = arr_mean.reshape((number,2))
stds = arr_std.reshape((number,2))
thress = arr_thres.reshape((number,2))

Df_mean = pd.DataFrame(means)
Df_std = pd.DataFrame(stds)
Df_thres = pd.DataFrame(thress)


#print(Df_ratio)
Df_melt = pd.melt(Df_ratio)
Df_melt2 = pd.melt(Df_mean)
Df_melt3 = pd.melt(Df_std)
Df_melt4 = pd.melt(Df_thres)
#print(Df_melt)

colors = ["palegreen","lightcoral"]


fig = plt.figure(figsize=(15,10))
fig.add_subplot(2,2,1)
sns.set(style='whitegrid',font='arial',font_scale=2)


Df_ratio = pd.read_csv("cell_shape_V_HU.csv",index_col=0)
p_values2 = []
for n in np.arange(len(Df_ratio.T)-1):
    a = np.array(Df_ratio.iloc[:,0])
    b = np.array(Df_ratio.iloc[:,n+1])
    f,p = stats.levene(a,b,center="median")
    p_values2.append(p)#*(N-1))

print(p_values2)

Df_melt = pd.melt(Df_ratio)



##vilolinplot
sns.violinplot(x="variable",y="value",data=Df_melt,palette=colors,)

##swarmplot
sns.violinplot(x="variable",y="value",data=Df_melt,inner=None  ,color="0.95", linewidth=0.3)
sns.swarmplot(x="variable",y="value",data=Df_melt,palette=colors, size=3,edgecolor="black",linewidth=0.5)

#for s in np.arange(len(p_values)):
#    plt.text(1+s,0.9,"{0:.3e}".format(p_values[s]))

plt.ylim(1,)
#plt.axhline(y=threshold,ls="--",color='red',zorder=3)
plt.xlabel("_")


fig.add_subplot(2,2,3)
sns.boxplot(x="variable",y="value",data=Df_melt2,palette=colors)
plt.ylim(1,2)

fig.add_subplot(2,2,4)
sns.boxplot(x="variable",y="value",data=Df_melt3,palette=colors)

fig.add_subplot(2,2,2)
sns.boxplot(x="variable",y="value",data=Df_melt4,palette=colors)


#plt.savefig("cell_shape.png")
plt.show()
