from scipy.stats import pearsonr
import pandas as pd

def pearson(arr1, arr2):

    r, p = pearsonr(arr1, arr2)
    # r, p = pearsonr(data.Height, data.CP) # 身長とCP
    # r, p = pearsonr(data.Weight, data.CP) # 体重とCP
    # print('相関係数 r = {r}'.format(r=r))
    # print('有意確率 p = {p}'.format(p=p))
    return r, p
