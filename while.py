# while True:
#     print("I hate myself!")

#--------------------------------------------------------------------------------

# larger_number = -99999999
# num = int(input("Enter the number or type -1 to exit: "))
# while num != -1:
#     if num > larger_number:
#         larger_number = num
#     num = int(input("Enter the number or type -1 to exit: "))
# print(f"The larger number is: {larger_number}")

#--------------------------------------------------------------------------------

# while True:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     start = min(num1, num2)
#     end = max(num1, num2)
#     for i in range(start, end+1):
#         print(i, end=" ")
#     print()
#     break
# num = int(input("Enter the number: "))
# count = 1
# while count <= num:
#     print(count, end=" ")
#     count += 1
#     print()

#------------------------------------------------------------------------------

# num = int(input("Enter the first number: "))
# count = 1
# even = 0
# odd = 0

# while count <= num:
#     if count & 1 == 0:
#         even += 1
#     elif count & 1 == 1:
#         odd += 1
#     if count == 25:
#         break
#     count += 1
    
# print("even",even)
# print("Odd",odd)

#-------------------------------------------------------------------------------

# num = int(input("Enter the num: "))
# for i in range(num):
#     print(i+1, end = " ")
# print()

#--------------------------------------------------------------------------------

# for i in range(2,8):
#     print(i, end = " ")
# print()

# for i in range(2,8,3):
#     print(i, end = " ")
# print()

# for i in range(1,1):
#     print(i)

# for i in range(2,1):
#     print(i)

# power = 1
# for expo in range(16):
#     print("2 to the power of ",expo, " is", power)
#     power *= 2

# for i in range(2,3):
#     print(i)

# print("The break inst: ")
# for i in range (1,6):
#     if 3<=i<=4:
#         #break
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")

#continue only work on itration