import pandas as pd

tamu = [20,85,100]

dTamu = pd.Series(tamu,index=["jumat","sabtu","minggu"])
print(dTamu)

print(dTamu["minggu"])