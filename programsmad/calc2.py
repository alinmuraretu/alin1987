
# Program make a simple calculator


import sys
def my_except_hook(exctype, value, traceback):
        print('')
sys.excepthook = my_except_hook


# This function adds two numbers 
def add(x, y):
   if x + y == int(x + y):
      return int(x + y)
   else:
      return x + y

          
# This function subtracts two numbers 
def subtract(x, y):
   if x - y == int(x -y):
     return int(x - y)
   else:
      return x - y


# This function multiplies two numbers
def multiply(x, y):
   if x * y == int(x * y):
     return int(x * y)
   else:
      return x * y

# This function divides two numbers
def divide(x, y):
   if x / y == int(x / y):
     return int(x / y)
   else:
      return x / y
    

print("Select operation.")
print("+.Add")
print("-.Subtract")
print("*.Multiply")
print("/.Divide")

# Take input from the user 

while True:
   num1 = float(input("Enter first number: "))
   choice = input("Enter operation(+ - * /): ")
   num2 = float(input("Enter second number: "))
   if choice == '+':
      print(num1,"+",num2,"=", add(num1,num2))
   elif choice == '-':
      print(num1,"-",num2,"=", subtract(num1,num2))
   elif choice == '*':
      print(num1,"*",num2,"=", multiply(num1,num2))
   elif choice == '/':
      print(num1,"/",num2,"=", divide(num1,num2))
   else:
      break

   