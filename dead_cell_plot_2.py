import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import glob
import pandas as pd

Df_30 = pd.read_csv("dead_cells_30C.csv",index_col=0).T
Df_38 = pd.read_csv("dead_cells_38C.csv",index_col=0).T

Df_30_mean = Df_30.mean()
Df_30_std = Df_30.std(ddof=False)

Df_38_mean = Df_38.mean()
Df_38_std = Df_38.std(ddof=False)

arr_mean = np.array([Df_30_mean, Df_38_mean]).reshape(1,12)
arr_std = np.array([Df_30_std, Df_38_std]).reshape(1,12)

# t_values = []
# p_values = []

t, p = stats.ttest_ind(Df_38.iloc[:,0],Df_38.iloc[:,3], equal_var=False)
# t_values.append(t)
# p_values.append(p)
p
# p_values = np.array(p_values)
# print(p_values)





x = [0,1,2,3,4,5,7,8,9,10,11,12]


colors = ["darkgray","lime","skyblue","khaki","cadetblue","lightcoral","dimgrey","limegreen","deepskyblue","darkkhaki","darkcyan","coral"]

plt.rcParams["font.family"] = "arial"
plt.rcParams["font.size"] = 11

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(1,1,1)
ax.set_axisbelow(True)
ax.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

width = 0.9
plt.bar(x, arr_mean[0], yerr=arr_std[0], color=colors, width=width, linewidth=0.8, edgecolor="black", capsize=3)
plt.xticks([0,1,2,3,4,5,7,8,9,10,11,12])
plt.ylim(0,70)
plt.savefig("dead_cell_plot_2.pdf")
