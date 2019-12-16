from six.moves import input

x = 2
x = x + 2
print(x)

print(10/2)
print(10/3)

nam = input('Cum te numesti?')
print("Welcome", nam)

inp = input("Europe floor?")
usf = int(inp) + 1
print("Us floor", usf)


#Conditional Steps
x = 5 
if x < 10:
   print('Smaler')
if x > 20:
     print('Biger')
print('Finis')
 
 
 #Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r') 