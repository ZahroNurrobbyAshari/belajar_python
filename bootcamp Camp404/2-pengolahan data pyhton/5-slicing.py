data = ["pisang","mangga","pepaya","salak","jeruk","durian"]

print(data)
print("")
print("Data [0:2]   --> dari index awal hingga sebelum index 2",data[0:2])
print("Data [:3]    --> 3 data pertama : ",data[:3])
print("Data [-3:]   --> 3 data terakhir : ",data[-3:])
print("Data [::2]   --> lompat dua, mulai elemen pertama : ",data[::2])
print("Data [3::2]  --> lompat dua, mulai indeks ketiga : ",data[3::2])
print("Data [-2::1] --> lopat satu ke kanan, mulai indeks ke -2 : ",data[-2::1])
print("Data [-2::-1] --> lopat satu ke kiri, mulai indeks ke -2 : ",data[-2::-1])