# import csv
# records = [
#     ['Name','Marks','City','Grade'],
#     ['Vivek',85,'Bhopal',"A"]
# ]
# with open ('student.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# with open('student.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["Name"]}: {row["Marks"]} mark ({row["City"]})')
# import csv
# records = [
#     ['Name','Marks','Age'],
#     ['Vivek',85,22],
#     ['leo',98,22]    
# ]
# found = False
# with open ('stud.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)
# with open ('stud.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["Name"]}: {row["Marks"]} Mark | Age: {row["Age"]}')
# find = input("Enter the name of studen you want to get: ")
# with open ('stud.csv','r') as f:
#     for row in csv.DictReader(f):
#         if find == row['Name']:
#             print(f'{row["Name"]}: {row["Marks"]} | Age:{row["Age"]}')
#             found = True
# if not found:
#     print("Studen not found!")
# import pandas as pd
# import numpy as np
# print(pd.__version__)
# print(np.__version__)
# nums1d = np.array([1,2,3,4,5])
# num2d = np.array([[23,34,67],[35,56,0],[26,46,0]])
# print(num2d.shape)
# print(num2d.dtype)
# print(num2d.ndim)

# class Solution:
#     def isValid(self, s: str) -> bool:
#         parentheses_dict = {
#             ')' : '(',
#             '}' : '{',
#             ']' : '[',
#         }
#         my_list = []
#         for ch in s:
#             # if  ch in parentheses_dict.values():
#             #     my_list.append(ch)
#             # elif ch in parentheses_dict:
#             #     if not my_list:
#             #         return False
#             #     else:
#             #         if my_list[-1] == parentheses_dict[ch]:
#             #             my_list.pop()
#             #         else:
#             #             return False
#             if ch in parentheses_dict:
#                 if not my_list or my_list[-1] != parentheses_dict[ch]:
#                     return False
#                 my_list.pop()
#             else:
#                 my_list.append(ch)
#         return not my_list
        
# obj = Solution()
# print(obj.isValid('()'))

#-------------------------------------------

# my = [0,1,2]
# my1 = [1]
# print(sorted(my + my1))

class Solution:
    def mergeTwoLists(self,list1, list2):
        result = []
        if len(list1) and len(list2) not in range(0,50):
            return f"out of range"
        else:
            tail = min(list1,list2)
obj = Solution()
print(obj.mergeTwoLists([0,1,2],[0,1,3,4]))
