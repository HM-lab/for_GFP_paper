import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Df = pd.read_csv("cell_size_intensity_M.csv",index_col=0)

##############################
intensity_thres = 10
size_thres = 1000
FP = 4
##############################

Df_255 = Df[Df["intensity"] != 255]
Df_thres = Df[(Df["intensity"]>=intensity_thres) & (Df["intensity"]<255) & (Df["size"]>=size_thres)]
print(Df_thres.corr())

colors = ["lime","skyblue","khaki","cadetblue","lightcoral"]

plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5

fig = plt.figure(figsize=(3.5,3.5))
ax1 = fig.add_subplot(111)
ax1.set_axisbelow(True)
plt.gca()
# plt.subplots_adjust(left=0.1, right=0.75, bottom=0.1, top=0.9)
# ax1.grid(axis="y", color="grey", lw=1,ls="--",zorder=.5)
plt.scatter(Df_255["size"],Df_255["intensity"],color="grey",linewidth=0.5,edgecolor="black",alpha=0.5)
plt.scatter(Df_thres["size"],Df_thres["intensity"],color=colors[FP],linewidth=0.5,edgecolor="black",alpha=0.5)
ax1.set_yticks(np.linspace(0,250, 6))
ax1.set_ylim(0, 250)
ax1.set_xticks(np.linspace(0,12000, 5))
ax1.set_xlim(0, 12000)
plt.text(5000,260,"n="+str(len(Df_thres))+"\nR="+str(Df_thres.corr().iloc[0,1]))
plt.show()

# plt.savefig("mScarlet_size_intensity.pdf")
