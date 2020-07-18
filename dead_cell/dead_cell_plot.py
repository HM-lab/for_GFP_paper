import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## read data
df_30 = pd.read_excel("percentage_of_dead_cells_30C.xlsx",index_col=0)
df_38 = pd.read_excel("percentage_of_dead_cells_38C.xlsx",index_col=0)

number = len(df_30.T)  #Number of strains

## calculate and reshape
arr_mean = np.array([df_30.mean(),
                     df_38.mean()]).reshape(1,number*2)

arr_std = np.array([df_30.std(ddof=False),
                    df_38.std(ddof=False)]).reshape(1,number*2)

## plt figure
plt.rcParams["font.size"] = 11
plt.rcParams["font.family"] = "arial"

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(1,1,1)
ax.set_axisbelow(True)
ax.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

color_plot = True

if color_plot == False:
    x = range(number)
    width = 0.45
    for i in np.arange(number):
        plt.bar(x[i], arr_mean[0][i], yerr=arr_std[0][i],
                color="lightgray", edgecolor="black",
                width=width, linewidth=0.8, capsize=3)
        plt.bar(x[i]+width, arr_mean[0][i+number], yerr=arr_std[0][i+number],
                color="dimgrey", edgecolor="black",
                width=width, linewidth=0.8, capsize=3)

    plt.xticks([val+width/2 for val in x])
else:
    colors = ["darkgray","lime","skyblue","khaki","cadetblue","lightcoral",
              "dimgrey","limegreen","deepskyblue","darkkhaki","darkcyan","coral"]

    x = list(range(number*2+1))
    x.pop(number)
    width = 0.9
    plt.bar(x, arr_mean[0], yerr=arr_std[0], color=colors, width=width, linewidth=0.8, edgecolor="black", capsize=3)
    plt.xticks(x)

plt.ylim(0,70)
plt.show()
