import pandas as pd
import scipy.stats as st

df = pd.DataFrame([[142,171],
                   [155.5,155.5]])

_, p = st.fisher_exact(df)
print(f'p値 = {p :.5}')
