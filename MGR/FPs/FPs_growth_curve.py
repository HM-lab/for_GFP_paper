import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal
import statistics as stats

## read data
temperature = '30C'   #'30C' or '38C'

df = pd.read_excel(
    "FPs_" + temperature + "_for_growth_curve.xlsx",
    header=None,index_col=0, delimiter='\t', skiprows=46
).T.reset_index(drop=True).iloc[:,:96]

df.columns = np.arange(len(df.T))

## calcurate oscillation cycle
N = len(df.T)
T = len(df)
array_maxid = []
for i in np.arange(0,N,1):
    array_x=np.arange(0,T)
    array_y=df[i].values

    maxid = signal.argrelmax(array_y, order=5)
    maxid_diff = np.diff(maxid)[0].tolist()
    array_maxid += maxid_diff

cycle = stats.mode(array_maxid)

## take moving average
df_averaged = df.rolling(window=cycle).mean().dropna().reset_index(drop=True)

## plot figure
plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5
colors = ["black","green","blue","gold","teal","red"]

draw_error_bar = False

fig = plt.figure(figsize=(5,3))

for n in np.arange(6,12,1):
    x = df_averaged.iloc[:,np.arange(n,n+85,12).tolist()].T.mean().values
    times = np.array(df_averaged.index/6)
    yerror = df_averaged.iloc[:,np.arange(n,n+85,12).tolist()].T.std().values

    if draw_error_bar == True:
        plt.errorbar(times, x, yerr=yerror,
                     errorevery=5, linewidth=3, color=colors[n-6],
                     elinewidth=1, ecolor="grey", alpha=0.5, zorder=3)

    plt.errorbar(times, x,
                 errorevery=3, linewidth=3, color=colors[n-6],
                 alpha=1, zorder=3)

    plt.ylim(0,1.2)
    plt.yticks(np.linspace(0,1.2,5))
    plt.xlim(0,75)
    plt.xticks(np.linspace(0,75,6))

    plt.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

plt.show()

## save figure
# plt.savefig("FPs_" + temperature + "_averagedowth_curve.pdf")
