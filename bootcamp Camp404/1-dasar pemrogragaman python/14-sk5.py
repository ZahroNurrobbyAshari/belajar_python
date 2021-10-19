jumlah = int(input("jumlah : "))
hargasatuan = int(input("harga :"))

def hitungTotal(jumlah,hargasatuan):
    return jumlah*hargasatuan

def hitungNet(jumlah,hargasatuan):
    return (jumlah*hargasatuan)-5000

if (hitungTotal(jumlah,hargasatuan)>=50000):
    print(hitungNet(jumlah,hargasatuan))
else : 
    print(hitungTotal(jumlah,hargasatuan))
    