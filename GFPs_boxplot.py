import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

Df_ratio = pd.read_csv("~/Desktop//GFP_paper/cell_shape_FPs.csv",index_col=0)
Df_GFPs = Df_ratio.iloc[:,[1,2,4]]


thres = 1.6


Df = pd.DataFrame()
for i in np.arange(len(Df_GFPs.T)):
    up = i*100
    down = i*100+100

    a = Df_GFPs.iloc[up:down,:]

    #over threshold
    over_GFP = a.iloc[:,0][a.iloc[:,0] > thres]
    over_sfGFP = a.iloc[:,1][a.iloc[:,1] > thres]
    over_ymoxGFP = a.iloc[:,2][a.iloc[:,2] > thres]

    #length
    b = len(over_GFP)
    c = len(over_sfGFP)
    d = len(over_ymoxGFP)

    arr = np.zeros(0)
    arr = np.append(arr,[b,c,d])
    #print(arr)

    #add to DataFrame
    df = pd.DataFrame(arr)
    Df = pd.concat([Df,df],axis=1,sort=False)

Df = Df.T
Df.index = [1,2,3]
lists = ["GFP","superfolderGFP","ymoxGFP"]
Df.columns = lists

##t-test
t_values = []
p_values = []
Df_ttest = pd.concat([Df,Df.iloc[:,0]],axis=1,sort=False)
#print(Df_ttest)
for l in np.arange(len(Df_ttest.T)-1):
    t, p = stats.ttest_ind(Df_ttest.iloc[:,l],Df_ttest.iloc[:,l+1], equal_var=False)
    t_values.append(t)
    p_values.append(p)

p_values = np.array(p_values)
p_values = p_values * (len(Df_ttest.T)-1)
print(p_values)

Df_melt = pd.melt(Df)
colors = ["lime","skyblue","cadetblue"]

plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5

fig = plt.figure(figsize=(3.5,3))
ax1 = fig.add_subplot(111)
plt.subplots_adjust(left=0.2, right=0.8, bottom=0.1, top=0.9)
ax1.set_axisbelow(True)
plt.gca()
ax1.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

plt.ylim(0,25)
ax1 = sns.boxplot(x="variable",y="value",data=Df_melt,palette=colors,width=0.65,linewidth=1)

#plt.savefig("GFPs_boxplot.pdf")
plt.show()
