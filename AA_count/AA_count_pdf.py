import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## read data
df_total = pd.read_csv("AA_count.csv",index_col=0)
df_high = pd.read_csv("AA_count_100000.csv",index_col=0)

## convert "percentge" to relative frequency (Log2 form)
probability = df_total.loc[:,'pro']
relative_freq_total = np.log2(df_total.loc[:,'per']/probability)
relative_freq_high = np.log2(df_high.loc[:,'per']/probability)
df_relative_freq = pd.concat([relative_freq_total,
                              relative_freq_high],
                              axis=1,sort=False)
df_relative_freq.columns = ["total","highly"]

## sort df
df_relative_freq = df_relative_freq.sort_values(by="total",ascending=False)

## plot figure
x = np.arange(len(df_relative_freq.index))
x_labels = df_relative_freq.index
bar_width = 0.45

plt.rcParams["font.size"] = 12
plt.rcParams["font.family"] = "arial"

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(1,1,1)
ax.set_axisbelow(True)
plt.gca()

plt.bar(x,df_relative_freq.loc[:,'total'],
        color="darkgray",edgecolor="black",
        width=bar_width,label="Total protein",
        align="center",zorder=2)
plt.bar(x+bar_width,df_relative_freq.loc[:,'highly'],
        color="sandybrown",edgecolor="black",
        width=bar_width,label="Highly expressed protein",
        align="center",zorder=2)
plt.xticks(x + bar_width*0.5, x_labels)

plt.axhline(y=0, color='black',linestyle='-',linewidth=0.5,zorder=1)
ax.grid(axis="y", color="grey", lw=1,ls="--",zorder=.5)

ax.set_yticks(np.linspace(-3, 2, 6))
ax.set_ylim(-3,2)

plt.show()

## save figure
plt.savefig("AA_count.pdf")
