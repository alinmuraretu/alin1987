#collection of instructions
#collection of code

def function1():  
    print('delivery')
    print('delivery 2')
print('this is outside function')

function1()

# a maping
#input or an argument
def function2(x):
    return 2*x
a = function2(3)
#return a value or output
print(a)

b = function2(4)
print(b)

c = function2(5)
print(c)

def function3(a,  b):
    return a + b

e = function3(2, 3)
print(e)

def function4(x):    
    print(x)
    print("still in this function")
    return 3 * x
f = function4(4)
print(f)

def function5(some_argument):
    print(some_argument)
    print("still in this function")


#Bmi calculator
name1 = "Alin"
height_m1 = 2
weight_kg1 = 80

name2 = "Madalina"
height_m2 = 1.8
weight_kg2 = 75

name3 = "Ionela"
height_m3 = 1.9
weight_kg3 = 70

print('hello world')

print("    /|") 
print("   / |")
print("  /  |")
print(" /___|")

#variabels
character_name = "Alin"
character_age = "20"
is_male = False
print("There once was a man named " + character_name + ", ") 
print("he was " + character_age + " years old. ")
  
#strings

print("There \nonce was")  
phrase = "There Once "
print(phrase + " maybe is there")  
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(phrase.isupper())
#lungimea caracterului
print(len(phrase))
#cum sa iei un index din caracter
print(phrase[0])
print(phrase[3])
#functia index 
print(phrase.index("Once"))
print(phrase.index("e"))
#cum sa inlocuiesti ceva
print(phrase.replace("There", "Just"))

#Working with numbers 
print(2)
print(2.503)
print(-2034)
print(3 + 4.5)
print(9 - 5)
print(8 * 5)
print(9 / 3)
#reminder(modules operations)
print(9 % 8)

#store variabels
my_num = -50
print(abs(my_num))
print(pow(4 , 5))
print(max(4 , 7))
print(min(4 , 7))
print(round(4,5))

#Getting input from user
name = input("Enter your name:")
age = input("Enter your age:")
print("Hello, " + name + "! You are " + age + " years old!")

#Building a basic calculator

num1 = int(input("Enter a number: ")) 
num2 = int(input("Enter another number: ")) 
result = float(num1) + float(num2)

print(result)

#mad LABS GAME!!!
color = input("enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + "are blue")
print("I love " + celebrity)

#List
#tuple
coordinates = [(4, 5), (6,7), (8,9), (10,11)]
print(coordinates[0])

#function2
def say_hi(name, age):
    print("Hello " + name + " you are " + age + "!")  
    
say_hi("Alin", "42")
say_hi("Ionela", "43")

#Return Statement
def cube(num):
    return num * num * num
result = cube(3)
print(result)

#if statement
is_male = True
is_tall = True

if  is_male and is_tall:
    print("you are a tall male") 
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are a not a male but are tall")
else:
    print("You are either not a male or not tall or both")