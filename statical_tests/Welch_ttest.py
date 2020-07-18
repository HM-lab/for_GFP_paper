from scipy import stats
import numpy as np

arr1 = [0,1,2]
arr2 = [3,4,5]

##t-test
t_values = []
p_values = []

t, p = stats.ttest_ind(arr1,arr2, equal_var=False)
t_values.append(t)
p_values.append(p)

p_values = np.array(p_values)
print(p_values)
