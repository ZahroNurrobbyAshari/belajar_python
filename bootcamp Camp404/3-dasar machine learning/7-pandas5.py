import pandas as pd

nilaiMTK = {
    "Nama":["Ali","Boni","Dodi"],
    "Nilai":[90,88,75],
    "Grade":["A","A","B"]
}

dataNilaiMTK = pd.DataFrame(nilaiMTK)
print(dataNilaiMTK)

print(dataNilaiMTK.iloc[2])