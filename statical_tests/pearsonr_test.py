from scipy.stats import pearsonr

def pearson(arr1, arr2):
    r, p = pearsonr(arr1, arr2)
    return r, p
