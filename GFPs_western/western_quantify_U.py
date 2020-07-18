import pandas as pd

## import original module
from western_quantify_function import calculate_and_plot

## read data
label_lists = {
    'target':[0,4,8],       #target bands, - DTT
    'target_DTT':[1,5,9],   #target bands, + DTT
    'ladder':[2,6,10],      #ladder bands, - DTT
    'ladder_DTT':[3,7,11]   #ladder bands, + DTT
}

label = 'target'
df = pd.read_excel("GFPs_western.xlsx",index_col=0).iloc[:,label_lists[label]]

## plot and save figure
calculate_and_plot(df, ylim=1.2, save=True, label=label)
