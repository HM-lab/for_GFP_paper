import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## read data
df_1 = pd.read_csv("hKO_ydj1_MGR.csv",index_col=0)
df_2 = pd.read_csv("hKO_ydj1_MGR_2.csv",index_col=0)
df_3 = pd.read_csv("hKO_ydj1_MGR_3.csv",index_col=0)

## calculate genetic interaction
def calc_genetic_interaction(df):
    means = df.mean()

    Ma_GFP = means[1] / means[0]
    Ma_mox = means[2] / means[0]

    Mb = means[3] / means[0]

    Mab_GFP = means[4] / means[0]
    Mab_mox = means[5] / means[0]

    ipsilon_GFP = Mab_GFP - (Ma_GFP * Mb)
    ipsilon_mox = Mab_mox - (Ma_mox * Mb)

    list_ip = [ipsilon_GFP, ipsilon_mox]

    return list_ip

list_df = []
for i in [df_1, df_2, df_3]:
    ip = calc_genetic_interaction(i)
    list_df.append(ip)

df_ip = pd.DataFrame(list_df)

## plot figure
plt.rcParams["font.size"] = 12
plt.rcParams["font.family"] = "arial"
max = 2
min = -1
width = 0.15

fig = plt.figure(figsize=(3.5,4))
ax = fig.add_subplot(1,1,1)
ax.set_axisbelow(True)

ax.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

plt.plot([0,0,0], df_ip.iloc[:,0],
          "o", markersize=8, color="lime",
          linewidth=0.5, markeredgecolor="black")
plt.plot([1,1,1], df_ip.iloc[:,1],
          "o", markersize=8, color="cadetblue",
          linewidth=0.5, markeredgecolor="black")

plt.axhline(y=df_ip.mean()[0],
            xmin=(0-min)/(max-min)-width, xmax=(0-min)/(max-min)+width,
            color='red', linestyle='-', linewidth=1, zorder=1)
plt.axhline(y=df_ip.mean()[1],
            xmin=(1-min)/(max-min)-width, xmax=(1-min)/(max-min)+width,
            color='red', linestyle='-', linewidth=1, zorder=1)

plt.xticks([0,1])
plt.xlim(min,max)
plt.ylim(-0.3,0.5 )
plt.show()

## sve figure
# plt.savefig("genetic_interaction_hKO_ydj1.pdf")
