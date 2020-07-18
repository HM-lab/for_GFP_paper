from scipy import stats

def Utest(arr1, arr2):
    u, p = stats.mannwhitneyu(arr1, arr2, alternative='two-sided')
    return u, p
