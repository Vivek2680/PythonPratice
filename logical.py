# Logical Expresion
# val = int(input("Endte a num: "))
# print(val>0)
# print(not(val>0))
# print(val != 0)
# print(not(val == 0))
#----------------------------------------------------------------------------------

# i = 1
# j = not not 1
#ans one hai 

#---------------------------------------------------------------------------------

# a = [0,0,1,1]
# b = [0,1,0,1]
# for i in a:
#     for j in b:
#         print(i,j)
#         # c = i&j
#         # print(c)

#--------------------------------------------------------------------------------
empty = []
n = int(input("Enter number of list element: "))
for i in range(n):
    num = int(input("Enter the list element: "))
    # empty.append(num) # Har element last me insert ho ga 
    empty.insert(0,num) # Har bar 0 index pe insert ho ga 
print(empty)

#--------------------------------------------------------------------------------

#why indexing always start from 0 : 
# because it is a compair distance from start to where you to stop
# and for array it is conti. memory alloc.
#int = 2 byte ,float = 4 byte , str = 8 byte
#starting address + (size of data type*index)= to get address each element

#-------------------------------------------------------------------------------

# num = [1,2,3,4,5]
# #update list
# num[0]= 77
# #print list with specifie address
# print(num[0])
# print(num[1])
# print(num[2])
# print(num[3])
# print(num[4])
# #print whole list
# print(num)
# #5th element update 2nd element
# num[1] = num[4]
# print(num[1])
# #len funtion give length of list
# print(len(num))
# #delete elemnt from list
# del num[2]
# print(num)
# print(len(num))
#negative indexing allow
# print(num[-1])
# print(num[-2])
# print(num[-3])
# print(num[-4])
# print(num[-5])
# print(num[-6])
# del num[-1]
#-----------------dyan replacement or in middle----------------------
# print(num)
# replacement = input("enter the new element: ")
# num[int((len(num))//2)] = replacement
# print(num)