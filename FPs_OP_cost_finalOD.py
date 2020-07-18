from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import seaborn as sns
from scipy import signal
import statistics as stats
from statistics import mean
from statistics import stdev


Df_30C = pd.read_excel("/Users/katohisaaki/Desktop/96well_Growth/20191202_FPs.xlsx",header=None,index_col=0,delimiter='\t',skiprows=46).T.reset_index(drop=True).iloc[:,:96].dropna()
Df_38C = pd.read_excel("/Users/katohisaaki/Desktop/96well_Growth/20200205_FPs_38C.xlsx",header=None,index_col=0,delimiter='\t',skiprows=46).T.reset_index(drop=True).iloc[:,:96].dropna()

arr_30C = np.array(Df_30C.iloc[-1,:]).reshape(8,12)
Df_30C_new = pd.DataFrame(arr_30C)

Df_30C_new.to_csv("FPs_30C_finalOD.csv")

arr_38C = np.array(Df_38C.iloc[-1,:]).reshape(8,12)
Df_38C_new = pd.DataFrame(arr_38C)
Df_38C_new

Df_38C_new.to_csv("FPs_38C_finalOD.csv")

costs_arr = []
costs = []
for i in np.arange(len(Df_30C_new)):
    a = Df_30C_new.iloc[i,0]
    for n in np.arange(len(Df_30C_new)):
        b = Df_30C_new.iloc[i,1]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30C_new)):
    a = Df_30C_new.iloc[i,0]
    for n in np.arange(len(Df_30C_new)):
        b = Df_30C_new.iloc[i,3]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30C_new)):
    a = Df_30C_new.iloc[i,6]
    for n in np.arange(len(Df_30C_new)):
        b = Df_30C_new.iloc[i,7]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30C_new)):
    a = Df_30C_new.iloc[i,6]
    for n in np.arange(len(Df_30C_new)):
        b = Df_30C_new.iloc[i,9]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30C_new)):
    a = Df_38C_new.iloc[i,0]
    for n in np.arange(len(Df_30C_new)):
        b = Df_38C_new.iloc[i,1]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30C_new)):
    a = Df_38C_new.iloc[i,0]
    for n in np.arange(len(Df_30C_new)):
        b = Df_38C_new.iloc[i,3]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30C_new)):
    a = Df_38C_new.iloc[i,6]
    for n in np.arange(len(Df_30C_new)):
        b = Df_38C_new.iloc[i,7]
        cost = 1 - (b/a)
        costs.append(cost)
costs_arr.append(costs)

costs = []
for i in np.arange(len(Df_30C_new)):
    a = Df_38C_new.iloc[i,6]
    for n in np.arange(len(Df_30C_new)):
        b = Df_38C_new.iloc[i,9]
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
# plt.savefig("cost_of_op(final_OD).pdf")
