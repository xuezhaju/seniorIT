import pandas as pd
import numpy as np

s1 = pd.Series(["1", "qwq", "awa", np.nan])
print(s1[2])

d = {"a": 1, "b": 2, "c":3}
s2 = pd.Series(d)
print(s2)

s3 = pd.Series([2, 4, 3, 5], index=["qwq", "awa", "zwz", "ovo"])
print(s3)

for i in s3.index:
    print(i)
    
for i in s3.values:
    print(i)