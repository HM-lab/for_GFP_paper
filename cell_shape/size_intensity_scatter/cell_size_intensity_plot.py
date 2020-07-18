import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## set variables
label_lists = {
    'EGFP': ['G', 'lime'],
    'sfGFP': ['sf', 'skyblue'],
    'Venus': ['Ve', 'khaki'],
    'moxGFP': ['Y', 'cadetblue'],
    'mScarlet': ['M', 'lightcoral']
}

##############################
FP = 'Venus'
plot_color = label_lists[FP][1]
intensity_min_thres = 10
size_min_thres = 1000
##############################

## read data
df = pd.read_csv("cell_size_intensity_" + label_lists[FP][0] + ".csv",index_col=0)

## apply threshold
df_255 = df[df["intensity"] != 255]  #exclude saturated
df_thres = df[(df["intensity"]>=intensity_min_thres) & (df["intensity"]<255) & (df["size"]>=size_min_thres)]

## plot figure
plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5

fig = plt.figure(figsize=(3.5,3.5))
ax1 = fig.add_subplot(111)
ax1.set_axisbelow(True)
plt.gca()

plt.scatter(df_255["size"],df_255["intensity"],color="grey",linewidth=0.5,edgecolor="black",alpha=0.5)
plt.scatter(df_thres["size"],df_thres["intensity"],color=plot_color,linewidth=0.5,edgecolor="black",alpha=0.5)

ax1.set_yticks(np.linspace(0,250, 6))
ax1.set_ylim(0, 250)
ax1.set_xticks(np.linspace(0,12000, 5))
ax1.set_xlim(0, 12000)

# plt.text(5000,260,"n="+str(len(df_thres))+"\nR="+str(df_thres.corr().iloc[0,1]))

plt.show()

## save figure
# plt.savefig("mScarlet_size_intensity.pdf")
