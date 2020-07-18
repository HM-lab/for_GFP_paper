import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_figure(data, colors, aspect=(3,3.7), dotsize=1.5, yaxis=(1,2.8,10), save=False):
    df_melt = pd.melt(data).dropna()

    plt.rcParams['font.family'] = 'arial'
    plt.rcParams["font.size"] = 10.5

    fig = plt.figure(figsize=aspect)
    plt.gca()
    ax = fig.add_subplot(1,1,1)
    ax.set_axisbelow(True)

    sns.violinplot(x="variable", y="value", data=df_melt,
                   inner=None, color="white", facecolor="black",
                   ax=ax, linewidth=1, zorder=3)
    sns.swarmplot(x="variable",y="value",data=df_melt,
                   palette=colors, edgecolor="black", size=dotsize,
                   ax=ax, linewidth=0.35, zorder=4)

    plt.ylim(yaxis[0],yaxis[1])
    plt.yticks(np.linspace(yaxis[0],yaxis[1],yaxis[2]))
    plt.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)

    if save == True:
        plt.savefig("cell_shape_violin.pdf")
    else:
        plt.show()
