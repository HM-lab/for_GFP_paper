import numpy as np
import pandas as pd
from scipy import stats

p_values =[]
for n in np.arange(len(Df.T)-1):
    a = np.array(Df.iloc[:,0])
    b = np.array(Df.iloc[:,n+1])
    f,p = stats.levene(a,b,center="median")
    p_values.append(p)#*(N-1))

print(p_values)
