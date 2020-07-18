import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel("cys_number_cell_shape.xlsx",index_col=0).iloc[:,:4]

position = pd.DataFrame([0,0,0,0,0,0,
                        -0.6,-0.6,-0.6,
                        -1,-1,-1,-1,-2,-2])
position.index = df.index
df["position"] = position[0]

## plot figure
plt.rcParams['font.family'] = 'arial'
plt.rcParams["font.size"] = 10.5

colors = ["darkgray","lime","skyblue","khaki","cadetblue","lightcoral",
          "indigo","mediumorchid","plum","darkgreen","mediumseagreen",
          "mediumaquamarine","mediumturquoise","orchid","violet"]

plt.figure(figsize=(7,5))
for i in np.arange(len(df)):
    plt.scatter(df.iloc[i,1], df.iloc[i,-1],
                marker="o", color=colors[i], edgecolor="black",
                linewidth=1, s=100+int(df.iloc[i,0]*100),
                alpha=1, zorder=i+2)

plt.axhline(y=0, color="grey", lw=3, zorder=0.5)
plt.axhline(y=-0.6, color="grey", lw=3, zorder=0.5)
plt.axhline(y=-1, color="grey", lw=3, zorder=0.5)
plt.axhline(y=-2, color="grey", lw=3, zorder=0.5)

plt.xlim(1.14,1.46)
plt.xticks(np.linspace(1.15,1.45,6))

plt.show()

## save figure
# plt.savefig("Cys_cellElongation_2.pdf")
