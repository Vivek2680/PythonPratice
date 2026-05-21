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

room = [[[False for rooms in range(20)]for flor in range(15)]for bulding in range(3)]
room[1][9][13] = True
room[0][4][1] = True
vacancy = 0

for room_num in range(20):
    if not room[1][9][room_num]:
        vacancy += 1

for element in room:
    print(element)
print(f"Vacany in 3rd building of 15 floor is {vacancy}")