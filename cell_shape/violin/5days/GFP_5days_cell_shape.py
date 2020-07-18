import matplotlib.pyplot as plt
import pandas as pd

## import original module
from cell_shape_violin_function import plot_figure

## read data
df = pd.read_excel("GFP_5days_cell_shape.xlsx",index_col=0)

## plot figure
colors = ["darkgray","lime"]

plot_figure(
    df,
    colors,
    aspect=(3.2,3.5),   # figure size. (width,height)
    dotsize=3,          # swarmplot's dotsize
    yaxis=(1,3.4,11),   # yaxis limit. (min, max, number of ticks)
    save=False          # save figure
)
