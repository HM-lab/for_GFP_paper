from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import seaborn as sns
from scipy import signal
import statistics as stats

plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5

Df = pd.read_excel("/Users/katohisaaki/Desktop/96well_Growth/20200205_FPs_38C.xlsx",header=None,index_col=0,delimiter='\t',skiprows=46).T
Df_new = Df.reset_index(drop=True).iloc[:,:96]

##############################
genotypes=12 #set genotypes
int = 10 #set time interval
section = 30 #set section
R2_thres = 0.95
OD_thres = 0.01
data_output = True
##############################

N = len(Df_new.T)
T = len(Df_new)
Df_new.columns = np.arange(N)
array_maxid = []
for i in np.arange(0,N,1):
    array_x=np.arange(0,T)
    array_y=Df_new[i].values

    maxid = signal.argrelmax(array_y, order=5)
    maxid_diff = np.diff(maxid)[0].tolist()
    array_maxid += maxid_diff

cycle = stats.mode(array_maxid)

N = len(Df_new.T)
T = len(Df_new)

Df_GR = Df_new.rolling(window=cycle).mean().dropna().reset_index(drop=True)

colors = ["black","green","blue","gold","teal","red"]

fig = plt.figure(figsize=(5,3))
#plt.subplots_adjust(left=0.2, right=0.8, bottom=0.3, top=0.7)

for n in np.arange(6,12,1):
    x = Df_GR.iloc[:,np.arange(n,n+85,12).tolist()].T.mean().values
    times = np.array(Df_GR.index)
    ye = Df_GR.iloc[:,np.arange(n,n+85,12).tolist()].T.std().values


    plt.errorbar(times,x,yerr=ye,errorevery=5,linewidth=3,color=colors[n-6],elinewidth=1,ecolor="grey",alpha=0.5,zorder=3)
    plt.errorbar(times,x,errorevery=3,linewidth=3,color=colors[n-6],alpha=1,zorder=3)


    plt.ylim(0,1.2)
    plt.yticks(np.linspace(0,1.2,5))
    plt.xlim(0,450)
    plt.xticks(np.linspace(0,450,6))

    plt.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

plt.savefig("FPs_38C_growth_curve.pdf")
plt.show()
