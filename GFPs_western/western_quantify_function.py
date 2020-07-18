import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def calculate_and_plot(data, ylim=1.2, save=False, label=None):
    ## calculate mean and SD
    means = data.mean()
    SDs = data.std(ddof=False)

    ## plot figure
    plt.rcParams["font.size"] = 10
    plt.rcParams["font.family"] = "arial"

    fig = plt.figure(figsize=(2.5,4))
    plt.subplots_adjust(left=0.2, right=0.8, bottom=0.3, top=0.7)
    ax = fig.add_subplot(111)
    ax.set_axisbelow(True)
    plt.gca()

    colors = ["lime","skyblue","cadetblue"]

    bar_width = 0.8
    ax.grid(axis="y", color="grey", lw=0.85,ls="--",zorder=.5)
    plt.bar(data.columns,means,yerr=SDs,
            color=colors,edgecolor="black",
            width=bar_width,capsize=5)

    ax.set_yticks(np.linspace(0, ylim, 5))
    ax.set_ylim(0,ylim)

    plt.show()

    if save==True:
        # save figure
        plt.savefig("GFPs_western_" + label + ".pdf")
