import matplotlib.pyplot as plt
import pandas as pd

## import original module
from cell_shape_violin_function import plot_figure

## set variables
data_labels = {
    'FPs': ['cell_shape_FP.xlsx', 6,
            ["darkgray","lime","skyblue","khaki","cadetblue","lightcoral"]],
    'N10s': ['cell_shape_N10.xlsx', 3,
             ["indigo","mediumorchid","plum"]],
    'Gpm1': ['cell_shape_Gpm1.xlsx', 2,
             ["orchid","violet"]],
    'Tpi1': ['cell_shape_Tpi1s.xlsx', 4,
             ["darkgreen","mediumseagreen","mediumaquamarine","mediumturquoise"]],
}

'''
data_labels = {
    'label': [''.xlsx file name', number of strains, [color palette]]
}
'''

shape = 'axis_ratio'  # size or axis_ratio
data_label = 'FPs'    # FPs, N10s, Gpm1, Tpi1

## read data
data = data_labels[data_label]

df = pd.read_excel(data[0], header=1, index_col=0)
if shape == 'axis_ratio':
    df = df.iloc[:,:data[1]]
elif shape == 'size':
    df = df.iloc[:,data[1]+1:]

colors = data[2]

## plot figure
plot_figure(
    df,
    colors,
    aspect=(5,3.7),   # figure size. (width, height)
    dotsize=1.5,      # swarmplot's dotsize
    yaxis=(1,2.8,10), # yaxis limit. (min, max, number of ticks)
    save=False        # save figure
)
