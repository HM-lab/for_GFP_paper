import pandas as pd

## import original module
from western_quantify_function import calculate_and_plot

## read data
label_lists = {
    'no_DTT':[0,1,2],    #target bands, - DTT
    'add_DTT':[4,5,6],   #target bands, + DTT
}

label = 'no_DTT'
df = pd.read_excel("GFPs_LU_western.xlsx",index_col=0).iloc[:,label_lists[label]]

## plot and save figure
calculate_and_plot(df, ylim=8, save=True, label=label)
