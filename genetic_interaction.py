import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
plt.rcParams["font.size"] = 12
plt.rcParams["font.family"] = "arial"

Df_1 = pd.read_csv("hKO_ydj1_MGR.csv",index_col=0).iloc[:,6:]
Df_2 = pd.read_csv("hKO_ydj1_MGR_2_3.csv",index_col=0).iloc[:,:6]
Df_3 = pd.read_csv("hKO_ydj1_MGR_2_3.csv",index_col=0).iloc[:,6:]
Df_1.mean()
def calc_genetic_interaction(df):
    means = df.mean()

    # Ma_GFP = means[0] - means[1]
    # Ma_mox = means[0] - means[2]
    Ma_GFP = means[1] / means[0]
    Ma_mox = means[2] / means[0]

    #
    # Mb = means[0] - means[3]
    Mb = means[3] / means[0]
    #
    # Mab_GFP = means[0] - means[4]
    # Mab_mox = means[0] - means[5]
    Mab_GFP = means[4] / means[0]
    Mab_mox = means[5] / means[0]


    ipsilon_GFP = Mab_GFP - (Ma_GFP * Mb)
    ipsilon_mox = Mab_mox - (Ma_mox * Mb)

    list_ip = [ipsilon_GFP, ipsilon_mox]

    return list_ip

list_df = []
for i in [Df_1, Df_2, Df_3]:
    ip = calc_genetic_interaction(i)
    list_df.append(ip)

# print(list_df)

Df_ip = pd.DataFrame(list_df)
print(Df_ip)
t, p = stats.ttest_ind(Df_ip.iloc[:,0],Df_ip.iloc[:,1], equal_var=False)
print(p)

fig = plt.figure(figsize=(3.5,4))
ax = fig.add_subplot(1,1,1)
ax.set_axisbelow(True)

ax.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

plt.plot([0,0,0], Df_ip.iloc[:,0], "o", markersize=8, color="lime", linewidth=0.5, markeredgecolor="black")
plt.plot([1,1,1], Df_ip.iloc[:,1], "o", markersize=8, color="cadetblue", linewidth=0.5, markeredgecolor="black")

max = 2
min = -1

width = 0.15
plt.axhline(y=Df_ip.mean()[0], xmin=(0-min)/(max-min)-width, xmax=(0-min)/(max-min)+width, color='red',linestyle='-',linewidth=1,zorder=1)
plt.axhline(y=Df_ip.mean()[1], xmin=(1-min)/(max-min)-width, xmax=(1-min)/(max-min)+width, color='red',linestyle='-',linewidth=1,zorder=1)
# plt.axhline(y=0, color='black',linestyle='-',linewidth=1,zorder=1)

plt.xticks([0,1])
plt.xlim(min,max)
plt.ylim(-0.3,0.5 )
# plt.ylim(-2,2)
plt.savefig("genetic_interaction_hKO_ydj1.pdf")
