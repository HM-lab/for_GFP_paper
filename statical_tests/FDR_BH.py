import numpy as np

def adjust_bh(p_values):
    p_values=np.array(p_values)
    m=len(p_values)
    sorted_idx=np.argsort(p_values)
    sorted_p=p_values[sorted_idx]
    one_to_m=np.arange(1,m+1)
    q_prime=m*sorted_p/one_to_m
    q_values=np.zeros(m)
    q_values[m-1]=q_prime[m-1]
    for i in range(m-2,-1,-1):
        q_values[i]=np.min([q_prime[i],q_values[i+1]])

    return q_values[np.argsort(sorted_idx)]
