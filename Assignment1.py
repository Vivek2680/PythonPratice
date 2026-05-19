# def presonDetail():
#     name = input("Enter your Name: ")
#     age = int(input("Enter your Age: "))
#     course = input("Enter your Course: ")
#     print(f"Name: {name}\nAge: {age}\nCourse: {course}")

# presonDetail()

#------------------------------------------------------------------

# preson = []
# entry = int(input("How many presonDetail you want to enter: "))
# for i in range(entry):
#     print(i+1)
#     i+=1
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     course = input("Enter your course: ")
#     preson.append((name,age,course))
# print("\nPrinting detail of preson for list\n")
# for i,j in enumerate(preson):
#     print(f"{i+1}\nName: {name}\nAge: {age}\nCourse: {course}")
# print(preson)

# Create empty list and fill entry of preson on it 
# Then use for loop with index(i) and value(j)
# Then print them 

#---------------------------------------------------------------------

# num1 = int(input("Enter first num: "))
# num2 = int(input("Enter second num: "))
# print(f"Sum of {num1} and {num2} is {num1+num2}")

#---------------------------------------------------------------------

# num1 = float(input("Enter first num: "))
# num2 = float(input("Enter second num: "))
# print(f"Multiplication of {num1} and {num2} is {num1*num2}")

#---------------------------------------------------------------------

# alphabet = str(input("Enter one alphabet: "))
# # ascii_val = list(bytes(alphabet,'ascii'))[0]
# # ascii_val = alphabet.encode('ascii')[0]
# # print(f"The ASII valu of {alphabet} is {ascii_val}")
# print(f"The ASII valu of {alphabet} is {ord(alphabet)}")
# #ord() converts a character into its integer Unicode value.

#---------------------------------------------------------------------

# a=30
# b=40
# print(f"Sum is",a+b)
# print(f"Multiplication of {a} and {b} is",a*b)
# print(f"Division of {a} and {b} is",a/b)
# print(f"Floored division of {a} and {b} is",a//b)
# print(f"Remainder of {a} and {b} is {a%b}")
# print(f"Power of {a} to the {b} is {a**b}")

#---------------------------------------------------------------------

# Tax Calculator

# def tax_calcu(income):
#     if income <= 85528:
#         tax = income * 0.18 - 556.02
#         print(f"tax calculated is {tax} of {income}")
#     elif income >=85529:
#         tax = income * 0.32 + 14839.02
#         print(f"tax calculated is {tax} of {income}")
#     if tax < 0:
#         print("No tax")
# income = float(input("Enter your income: "))
# tax_calcu(income)

#---------------------------------------------------------------------

# def gregotian(year):
#     if year < 1582:
#         print("Not within the Gregotian calendar period.")
#     else:
#         print("The entered year falls into the Gregorian era.")
#         if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 ):
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is a common year.")


# year = int(input("Enter year: "))
# gregotian(year)

#----------------------------------------------------------------------

# for i in range(5):
#     print(f"{i+1} Mississippi")
# print("Ready or not, here I come")

#----------------------------------------------------------------------

# user_input = input("Enter the word: ")
# user_input = user_input.upper()
# word_without_vowels =  ""

# for letter in user_input:
#     if letter == 'A':
#         continue
#     elif letter == 'E':
#         continue
#     elif letter == 'I':
#         continue
#     elif letter == 'O':
#         continue
#     elif letter == 'U':
#         continue
#     else:
#         word_without_vowels += letter       
# print(word_without_vowels)

#------------------------------------------------------------------------

# NEED IMPROVMENT:

# block = int(input("Enter the number of block: "))
# layer = 0
# hight = 1
# while block>layer:
#     block -= layer
#     layer += 1
#     hight
#     if layer > block:
#         break
# print(f"Hight of pyramid {layer}")




#------------------------------------------------------------------------

# c0 = int(input("Enter any number non-negative and non-zero integer: "))
# count = 0
# while c0 != 1:
#     if c0 & 1 == 1:
#         c0 = 3*c0+1
#     elif c0 & 1 == 0:
#         c0 = c0//2
#     print(c0)
#     count += 1
# print ("Steps =", count)

#------------------------------------------------------------------------