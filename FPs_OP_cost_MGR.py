import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean
from statistics import stdev

Df_30 = pd.read_csv("/Users/katohisaaki/Desktop/FPs_MGR_30C_EXCEL.csv",index_col=0)
Df_38 = pd.read_csv("/Users/katohisaaki/Desktop/FPs_MGR_38C_EXCEL.csv",index_col=0)
Df_30
lis_v = [0,6]
lis_G = [1,7]
lis_Ve = [3,9]
costs_arr = []
costs = []

for i in np.arange(len(Df_30)):
    a = Df_30.iloc[i,0]
    for n in np.arange(len(Df_30)):
        b = Df_30.iloc[i,1]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30)):
    a = Df_30.iloc[i,0]
    for n in np.arange(len(Df_30)):
        b = Df_30.iloc[i,3]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30)):
    a = Df_30.iloc[i,6]
    for n in np.arange(len(Df_30)):
        b = Df_30.iloc[i,7]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30)):
    a = Df_30.iloc[i,6]
    for n in np.arange(len(Df_30)):
        b = Df_30.iloc[i,9]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30)):
    a = Df_38.iloc[i,0]
    for n in np.arange(len(Df_30)):
        b = Df_38.iloc[i,1]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30)):
    a = Df_38.iloc[i,0]
    for n in np.arange(len(Df_30)):
        b = Df_38.iloc[i,3]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30)):
    a = Df_38.iloc[i,6]
    for n in np.arange(len(Df_30)):
        b = Df_38.iloc[i,7]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30)):
    a = Df_38.iloc[i,6]
    for n in np.arange(len(Df_30)):
        b = Df_38.iloc[i,9]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

print(costs_arr)
x = [0,1,2,3,5,6,7,8]
fig = plt.figure()
ax = fig.add_subplot(111)
for m in np.arange(8):
    plt.bar(x[m],mean(costs_arr[m]),yerr=stdev(costs_arr[m]), capsize=5,color="gray",edgecolor="black")
ax.set_xticks([0,1,2,3,5,6,7,8])
ax.set_yticks(np.linspace(0,1,11))

plt.ylim(0,1)
plt.savefig("cost_of_op_EXCEL.pdf")
