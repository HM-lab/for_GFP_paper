import pandas as pd
from scipy.stats import spearmanr

array_a = np.array(range(10))
array_b = np.array(range(10,20))

#スピアマン順位相関係数とp値
correlation, p_value = spearmanr(array_a,array_b)
