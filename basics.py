# print("Hello, World!")
# 3+4 is an expression, it will be evaluated and the result will be 7
# a= 7
# print(a)
# 12 is int
# 12.12 is float
# "12" is string
# True/False is boolean
#'12' is also string
#why we neeed variables?
#variables are used to store data that can be used later in the program. 
# They allow us to give a name to a value, making it easier to read and understand the code. 
# Variables can also be used to store user input, perform calculations, and manipulate data. 
# They are essential for creating dynamic and interactive programs. 
#--------------------------------------------------------------------------------------------------
# variable - myOfficiaName
# function - myOfficiaName()
# class - MyOfficiaName  
# object - myOfficiaNameObj
# constants - MY_OFFICIAL_NAME
#---------------------------------------------------------------------------------
# age = int(input("Enter your age: "))
# print(f"My age is {age}.")
#---------------------------------------------------------------------------------
# age = "twenty-two"
# print(f"My age is {age}.")
#---------------------------------------------------------------------------------
# name = input("Enter your name: ")
# profession = input("Enter your profession: ")
# experience = int(input("Enter your experience: "))
# print(f"My name is {name}, I am a {profession} with {experience} years of experience.")
#---------------------------------------------------------------------------------
#Data types in Python:
# text type- str
# num type - int, float, complex
# boolean type - bool
# sequence type - list, tuple, range
# mapping type - dict
# set type - set, frozenset
# binary type - bytes, bytearray, memoryview
# None type - NoneType
#---------------------------------------------------------------------------------
#Examples of data types in Python:
# x= 10 int
# y= 20.5 float 
# z= 1+2j complex
# a = ["apple", "banana", "cherry"] list
# b = ("apple", "banana", "cherry") tuple
# c = range(6) range
# d = {"name": "John", "age": 30, "city": "New York"} dict
# e = {"apple", "banana", "cherry"} set
# f = frozenset({"apple", "banana", "cherry"}) frozenset
# g = True bool
# h = None NoneType
# i = b"Hello" bytes
# j = bytearray(5) bytearray
# k = memoryview(bytes(5)) memoryview
# l = "hello" str
# x =  10
# print("x is of type", type(x))
#---------------------------------------------------------------------------------
#Arthmetic operators in Python:
# a = int(input("Enter firt number: "))
# b = int(input("Enter second number: "))
# sum = a + b
# print(f"The sum of {a} and {b} is {sum}.")
# sub = a - b
# print(f"The difference of {a} and {b} is {sub}.")
# mul = a * b
# print(f"The product of {a} and {b} is {mul}.")
# div = a / b
# print(f"The quotient of {a} and {b} is {div}.") 
# floor = a // b
# print(f"The floor division of {a} and {b} is {floor}.")
# mod = a % b
# print(f"The modulus of {a} and {b} is {mod}.")
# exp = a ** b
# print(f"The exponent of {a} and {b} is {exp}.")
#---------------------------------------------------------------------------------
# p =  parentheses
# e = exponentiation
# m = multiplication
# d = division
# a = addition
# s = subtraction
# Precedence ______Parentheses, Exponentiation, Multiplication and Division (from left to right) 
# Addition and Subtraction (from left to right)
#---------------------------------------------------------------------------------
# Assignment operators in Python:
# a = 10
# a += 5 | a = a + 5
# print(a)
# a -= 5 | a = a - 5
# print(a)
# a *= 5 | a = a * 5
# print(a)
# a /= 5 | a = a / 5
# print(a)
# a //= 5 | a = a // 5
# print(a)
# a %= 5 | a = a % 5
# print(a)
# a **= 5 | a = a ** 5
# print(a)
# print(100 >> 2)
# print(100 << 2)
# x =1 
# print(x:=3)
#---------------------------------------------------------------------------------
#comparison operators in Python:
# a = 10
# b = 20
# print(a == b) # False
# print(a != b) # True
# print(a > b) # False
# print(a < b) # True
# print(a >= b) # False
# print(a <= b) # True  
#---------------------------------------------------------------------------------
#logical operators in Python:
# a = True
# b = False
# print(a and b) # False
# print(a or b) # True
# print(not a) # False
# print(not b) # True
#---------------------------------------------------------------------------------
#bitwise operators in Python:
# a = 10 # 1010 in binary
# b = 4  # 0100 in binary
# print(a & b) # 0000 in binary, 0 in decimal
# print(a | b) # 1110 in binary, 14 in decimal
# print(a ^ b) # 1110 in binary, 14 in decimal
# print(~a) # 0101 in binary, -11 in decimal
# print(a << 2) # 101000 in binary, 40 in decimal
# print(a >> 2) # 0010 in binary, 2 in decimal
#---------------------------------------------------------------------------------
#example
# x = 10
# print(x<5 and x>0)
# print(x<5 or x>0)
# print(not(x<5 and x>0))
#---------------------------------------------------------------------------------
# Idetity operators in Python: obj comparison, type data comparison
# a = 10
# b = 10
# print(a is b) # True
# print(a is not b) # False
#---------------------------------------------------------------------------------
# x= ["Maruti", "BMW"]
# y = ["Maruti", "BMW"]
# z = x
# print(x is y)
# print(x is not y)
# print(x is z)
# print(x is not z)
# print(y is z)
# print(y is not z)
#---------------------------------------------------------------------------------
# Ṁembership operators in Python:
# x = "Maruti"
# print (x in y)
# print (x not in y)
#---------------------------------------------------------------------------------
# name = str(input("Enter your name: "))
# console input is always string, we can convert it to int or float if needed.
# print(f"My name is {name}.")
# print("my name is " + name + ".")
# print("my name is {}.".format(name))
# print("MY name is ", name, ".")
# print(f"My name is {name.upper()}.")
# print(f"My name is {name.lower()}.")
# print(f"My name is {name.title()}.")
#--------------------------------------------------------------------------------
#Type casting in Python:
# x = input("Enter a number: ")
# y = input("Enter another number: ")
# sum = int(x) + int(y) #type casting, converting string to int
# print(f"The sum of {x} and {y} is {sum}.")
#---------------------------------------------------------------------------------
