tuple = tuple(input("masukkan data tuple :"))
char = str(input("masukkan karakter :"))

def countchar(tuple,char):
    i = 0
    count=0
    for x in tuple:
        for y in tuple[i]:
            if y == char : 
                count+=1
        i+=1
    print("jumlah ", char , " : ",count)


countchar(tuple,char)