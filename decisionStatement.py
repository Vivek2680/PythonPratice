# #o/p= 1,2,3,4,5.....50

# input_number1 = int(input("Enter the number: "))
# input_number2 = int(input("Enter the number: "))
# start = min(input_number1, input_number2)
# end = max(input_number1, input_number2)
# for i in range(start, end+1):
#     print(i)
# #input_number1 = 1
# #input_number2 = 50
# #outpout = 1,2,3,4,5.....50

#------------------------------------------------------------------------------
#o/p= 1,t,3,t,5,t.....50

# input_number1 = int(input("Enter the number: "))
# input_number2 = int(input("Enter the number: "))
# start = min(input_number1, input_number2)
# end = max(input_number1, input_number2)
# for i in range(start, end+1):
#     if i == 50:
#         print(i)
#     elif i & 1 == 0:
#         print("t")
#     else:
#         print(i)
# #input_number1 = 1
# #input_number2 = 50
# #o/p = 1,t,3,t,5,t.....50

#-----------------------------------------------------------------------------
# #o/p = 1,2,t,4,5,t,7,8,t...50

# input_number1 = int(input("Enter the number: "))
# input_number2 = int(input("Enter the number: "))
# start = min(input_number1, input_number2)
# end = max(input_number1, input_number2)
# for i in range(start, end+1):
#     if i % 3 == 0:
#         print("t")
#     else:
#         print(i)
#input_number1 = 1
#input_number2 = 50
#o/p = 1,2,t,4,5,t,7,8,t...50

#-----------------------------------------------------------------------------
#o/p = 1,2,fiz,4,buz,7,8,fiz,buz,11,fiz,13,14,fiz,16....50

# input_number1 = int(input("Enter the number: "))
# input_number2 = int(input("Enter the number: "))
# start = min(input_number1, input_number2)
# end = max(input_number1, input_number2)
# for i in range(start, end+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizbuz")
#     # elif i == 50:
#     #     print(i)
#     elif i % 5 == 0:
#         print("buz")
#     elif i % 3 == 0:
#         print("fiz")
#     else:
#         print(i)
#input_number1 = 1
#input_number2 = 50
#o/p = 1,2,fiz,4,buz,7,8,fiz,buz,11,fiz,13,14,fizbuz,16....50