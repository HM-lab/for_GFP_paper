import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import random

Df = pd.read_csv("/Users/katohisaaki/Desktop/GFP_paper/cell_shape_Tpi1s.csv",index_col=0)
Df = round(Df, 5)

Df_1_1 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1_1Cell.csv").iloc[:,[11,17,2]]
Df_2_1 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1C41S_1Cell.csv").iloc[:,[11,17,2]]
Df_3_1 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1C126S_1Cell.csv").iloc[:,[11,17,2]]
Df_4_1 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1CS2_1Cell.csv").iloc[:,[11,17,2]]


Df_1_2 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1_2Cell.csv").iloc[:,[11,17,2]]
Df_2_2 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1C41S_2Cell.csv").iloc[:,[11,17,2]]
Df_3_2 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1C126S_2Cell.csv").iloc[:,[11,17,2]]
Df_4_2 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1CS2_2Cell.csv").iloc[:,[11,17,2]]


Df_1_3 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1_3Cell.csv").iloc[:,[11,17,2]]
Df_2_3 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1C41S_3Cell.csv").iloc[:,[11,17,2]]
Df_3_3 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1C126S_3Cell.csv").iloc[:,[11,17,2]]
Df_4_3 = pd.read_csv("~/Desktop/CellProfiler/BY4743_Tpi1CS2_3Cell.csv").iloc[:,[11,17,2]]

Df_new = pd.DataFrame(np.zeros(300))
lists = ["Tpi1","C41S","C126S","CS2"]
for i in lists:
    Df_new[i] = 0
# Df_new
Df_new = Df_new.iloc[:,1:]

Df_1 = pd.concat([Df_1_1,Df_1_2,Df_1_3],axis=0,sort=False).reset_index(drop=True)
Df_1_ratio = Df_1.iloc[:,0]/Df_1.iloc[:,1]
Df_1_ratio = round(Df_1_ratio, 5)

Df_2 = pd.concat([Df_2_1,Df_2_2,Df_2_3],axis=0,sort=False).reset_index(drop=True)
Df_2_ratio = Df_2.iloc[:,0]/Df_2.iloc[:,1]
Df_2_ratio = round(Df_2_ratio, 5)

Df_3 = pd.concat([Df_3_1,Df_3_2,Df_3_3],axis=0,sort=False).reset_index(drop=True)
Df_3_ratio = Df_3.iloc[:,0]/Df_3.iloc[:,1]
Df_3_ratio = round(Df_3_ratio, 5)

Df_4 = pd.concat([Df_4_1,Df_4_2,Df_4_3],axis=0,sort=False).reset_index(drop=True)
Df_4_ratio = Df_4.iloc[:,0]/Df_4.iloc[:,1]
Df_4_ratio = round(Df_4_ratio, 5)

Df_merge = pd.concat([Df_1.iloc[:,2],Df_2.iloc[:,2],Df_3.iloc[:,2],Df_4.iloc[:,2]],axis=1,sort=False)
Df_ratio = pd.concat([Df_1_ratio, Df_2_ratio, Df_3_ratio, Df_4_ratio],axis=1,sort=False)

for l in np.arange(len(Df.T)):
    for n in np.arange(len(Df)):
        a = Df_ratio.iloc[:,l][Df_ratio.iloc[:,l] == Df.iloc[n,l]].index.tolist()
        print(a)
        Df_new.iloc[n,l] = Df_merge.iloc[a[0],l]

print(Df_new)
Df_new.to_csv("cell_size_Tpi1s.csv")
