#Dojo

numbers= [-5, 23, 0, -9, 12, 99, 105, -43]
numbersLenght = len(numbers)

#Calculating the max

x = 0
for i in numbers:
    inum = float(i)
    if inum < x:
        x = inum
print (x)


#calculating the min

x = 0
for i in numbers:
    inum = float(i)
    if inum > x:
        x = inum
print (x)

#Calculating the average

numbersSum= 0
for i in range(0, numbersLenght):
    numbersSum += numbers[i]
print(f'{numbersSum/numbersLenght}')