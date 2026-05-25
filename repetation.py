# row = []
# for ic in range(8):
#     row.append("WHITE_PAWN")
# print(row)

# row = ["WHITE_PAWN" for i in range(8)]
# print(row)

# sqares = [x**2 for x in range(1,11)]
# print(sqares)

# twos = [2**index for index in range(8)]
# print(twos)

# sqares = [x**2 for x in range(1,11)]
# odd = [f"{x} is odd num" for x in sqares if x % 2 != 0] # x % 2 != 0 give output only odd
# print(odd)

#-----------------------------------------------------------------------

# 2D list

# my_list = []
# for i in range(8):
#     row = ["Vivek" for i in range(8)]
#     my_list.append(row)
# # for element in my_list:
# #     print(element)
# # print(len(my_list))
# # print(my_list[0][1])
# #[0] my_list ka index hai then [1] my_list ke [0] index in side 2 element.
# my_list[0][0] = "Rook"
# my_list[0][7] = "Rook"
# my_list[7][0] = "Rook"
# my_list[7][7] = "Rook"

# my_list[0][1] = "Knight"
# my_list[0][6] = "Knight"
# my_list[7][1] = "Knight"
# my_list[7][6] = "Knight"

# my_list[0][2] = "Bishop"
# my_list[0][5] = "Bishop"
# my_list[7][2] = "Bishop"
# my_list[7][5] = "Bishop"

# my_list[0][4] = "Queen"
# my_list[7][4] = "Queen"
# for element in my_list:
#     print(element)

# temp = [[0.0 for hrs in range(24)] for days in range(31)]
# total = 0.0
# temp1 = 14
# temp2 = 30
# count = 0
# highest = -100
# hot_day = 0
# #inset val in 12 pm of all day
# for days in temp:
#     if count == 0 :
#         days[11] = temp1
#         count = 1
#     else:
#         days[11] = temp2
#         count = 0
# #findng highest temp in 12 pm of all day
# for days in temp:
#     for temps in days:
#         if temps > highest:
#             highest = temps
# #finding total hot day in month 
# for days in temp:
#     if days[11]>20.0:
#         hot_day += 1

# for element in temp:
#     print(element)

# for day in temp:
#     total += day[11]
# avg = total/31
# print("The Avg of 12 pm is:",avg)
# print("The highest temp is:",highest)
# print("The total day of Hot day is:",hot_day)

#----------------------------------------------------------------

# 3D list

# room = [[[False for rooms in range(20)]for flor in range(15)]for bulding in range(3)]
# room[1][9][13] = True
# room[0][4][1] = True
# vacancy = 0

# for room_num in range(20):
#     if not room[1][9][room_num]:
#         vacancy += 1

# for element in room:
#     print(element)
# print(f"Vacany in 2rd building of 10 floor is {vacancy}")
# var = 1
# while var< 10:
#     print("#")
#     var = var <<1
# val = [1,2,3]
# new = val[-1:-2]
# print(new)

# a = [1, 2]
# b = [3, 4]
# c = a + b
# print(c)
# my_list= [1,2,3]
# for i in range(len(my_list)):
#     my_list.insert(1,my_list[my_list[my_list[i]]])
#     # print(my_list)
# print (my_list)

# nums = [1, 2, 3, 4]

# result = []

# for n in nums:
#     if n % 2 == 0:
#         result.append(n * 2)

# print(result)

# x = [1, 2, 3]

# y = [i + 1 for i in x]

# print(x)
# print(y)

# a = [1, 2, 3, 4]

# b = [i for i in a if i > 2]

# print(b)

# nums = [2, 4, 6]

# result = [n if n > 3 else 0 for n in nums]

# print(result)
# x=[i for i in range(3)]
# print(x)
# name = ["ram","shyam","mohan"]
# upper_name = [n.upper() for n in name]
# print(upper_name)

# a=(i for i in range(5))
# print(a)

# square = [n**2 for n in range(1,6)]
# print(square)

# cube = [n**2 for n in range(1,21) if n % 3 == 0]
# print(cube)
# a= [1,2,3,4,5]
# for element in a:
#     print(element)

# num = [[n for n in range(3)] for r in range(3)]
# print(num)

# nums = [5, 12, 17, 20, 25, 30]
# new_num = []
# for element in nums:
#     if element % 5 == 0 and element > 15:
#         new_num.append(element)
# print(new_num)
# new_num = [element for element in nums if element % 5 == 0 and element > 15]
# print(new_num)

# nums = [1,2,3,4,5,6]
# new_num = []
# for element in nums:
#     if element % 2 == 0:
#         new_num.append(element*10)
#     else:
#         new_num.append(element)
# print(new_num)
# new_num = [element*10 if element % 2 ==0 else element for element in nums]
# print(new_num)

# nums = [10,20,30,40]

# result = [nums[i] for i in range(len(nums)-1, -1, -1)]

# print(result)

# nums = [1,2,3]

# for i in nums:
#     nums.append(i)

#     if len(nums) > 6:
#         break

# print(nums)
# word = "python"
# my_list = [ch.upper() for ch in word]
# print(my_list)

# pairs = []

# for i in range(3):
#     for j in range(2):
#         pairs.append((i, j))

# print(pairs)

# nums = [1,2,3,4,5]
# new_num = [ 'even' if element % 2 == 0 else 'odd' for element in nums]
# print(new_num)
# new_num = []
# for element in nums:
#     if element % 2 == 0:
#         new_num.append('even')
#     else:
#         new_num.append('odd')
# print(new_num)

# names = ["ram", "shyam", "mohan", "riya", "amit"]
# # new_name = [ch for ch in names if len(ch) > 4]
# new_name = []
# for ch in names:
#     if len(ch) > 4:
#         new_name.append(ch)
# print(new_name)

# result = []

# for ch in "python":
#     if ch != "o":
#         result.append(ch.upper())
# print(result)

# result = [ch.upper()for ch in "python" if ch != "o"]
# print(result)

# result = [n**2 for n in range (1,21) if n % 2 == 0 and n % 3 == 0]
# print(result)

# matrix = [[0]*3]*2
# matrix[0][1] = 5
# print(matrix)

# num = [n for n in range(5,0,-1)]
# print(num)

# vals = [(i, j, k)
#         for i in range(2)
#         for j in range(3)
#         for k in range(4)]

# for element in vals:
#     print(element)

# nums = iter([1,2,3])

# print(next(nums))
# print(next(nums))

# for i in nums:
#     print(i)
# num = [n**2 for n in range(0,21,2) if n % 2 == 0 ]
# print(num)

# num = []
# new_num = [num.append(i) for i in range (3)]
# print(num)
# print(new_num)

