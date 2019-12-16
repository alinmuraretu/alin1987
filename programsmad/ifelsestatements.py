e = 9
f = 8
if e < f:
    print('e is lees than f')
elif e == f:
    print('e is equal to f')
else:
    print(' e is greater than f') 
    
g = 9
h = 8
if g < h:
    print('g is less than h')
else:
    if g == h:
        print('g is equal to h')
    else:
        print('g is greater than h')
        

name = "Alin"
inaltimea_m = 1.8
greutatea_kg = 95

bmi = greutatea_kg / (inaltimea_m ** 2)
print('bmi: ')
print(bmi)
if bmi < 25:
    print(name)
    print('is not overweight')
else:
    print(name)
    print('is overweight')


    
    