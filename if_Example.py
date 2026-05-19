# def largerNumber(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(f"The larger number is: {largerNumber(num1, num2)}")

#-----------------------------------------------------------------------------

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num1 > num2:
#     print(f"The larger number is: {num1}")
# else:    
#     print(f"The larger number is: {num2}")

#-----------------------------------------------------------------------------

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# if num1 > num2 and num1 > num3:
#     print(f"The larger number is: {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"The larger number is: {num2}")
# else:
#     print(f"The larger number is: {num3}")

#-----------------------------------------------------------------------------
#better way to find the largest number among three numbers between 3 numbers

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# lager_number = num1
# if num2 > lager_number:
#     lager_number = num2
# if num3 > lager_number: 
#     lager_number = num3
# print(f"The larger number is: {lager_number}")

#-----------------------------------------------------------------------------
#using inbuilt function max() to find the largest number among three numbers

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# lager_number = max(num1, num2, num3)
# smaller_number = min(num1, num2, num3)
# print(f"The larger number is: {lager_number}")
# print(f"The smaller number is: {smaller_number}")

