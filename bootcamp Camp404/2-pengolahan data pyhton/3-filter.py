data = [1,2,3,4,5]

hasillambda = map(lambda x : x!=4,data)
print("hasil lambda:",list(hasillambda))

hasilfilter = filter(lambda x : x!=4,data)
print("hasil filter:",list(hasilfilter))