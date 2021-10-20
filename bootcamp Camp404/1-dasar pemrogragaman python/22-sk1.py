kata = ("satu","dua","tiga","empat","lima","enam","tujuh","delapan")
print("Data kata : ",kata)

i=0
count=0

for n in kata:
    for m in kata[i]:
        if m == 'a':
            count+=1
    i+=1
print("Jumlah huruf 'a' ada : ",count)