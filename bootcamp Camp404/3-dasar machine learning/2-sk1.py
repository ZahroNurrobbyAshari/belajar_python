import numpy as np

myArray = [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]

reArray = np.reshape(myArray,(5,5))
# print(reArray)

ijo =reArray[0::2,0::2]
print(ijo)

red = reArray[0,1:4]
print(red)

ungu = reArray[:5,1]
print(ungu)

biru = reArray[1:4,0]
print(biru)