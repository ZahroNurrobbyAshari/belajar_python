# buat 2 set
merkMobil = {"avanza","xenia","expander","ertiga"}
mobilku = {"avanza","xenia"}
print("set merk mobil : ",merkMobil)
print("set mobilku : ",mobilku)
print("----------------------------")

# cek sebuah set adalah himpunan bagian atau bukan
if mobilku.issubset(merkMobil):
    print("mobilku bagian dari merk mobil")
print("----------------------------")


# tambah elemen
merkMobil.add("sedan")
print("add elemen sedan")
print(merkMobil)
print("----------------------------")


# kurangi elemen
merkMobil.remove("xenia")
print("remove elemen xenia")
print(merkMobil)
print("----------------------------")

# menambahkan elemen yang belum ada
merkMobil.update(["avanza","sigra"])
print("update elemen avanza , sigra")
print(merkMobil)
print("karena avanza sudah ada maka tidak akan ditambahkan")
print("----------------------------")

# menghilangkan elemen yang sama
merkMobil.difference_update(mobilku)
print("menghilangkan elemen yang sama")
print(merkMobil)
print("----------------------------")

