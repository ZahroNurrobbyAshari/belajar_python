# Membuat program menggunakan for loop , list , range

banyak = int(input("Berapa ?"))
nama = []
umur = []

for i in range(0,banyak):
    print("data ke "+str(i))
    input_nama = str(input("nama : "))
    input_umur = int(input("umur : "))
    
    nama.append(input_nama)
    umur.append(input_umur)
    
print(nama)
print(umur)