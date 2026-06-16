# class Solution:
#     # def __init__(self,my_list,MIN_LENGTH):
#     #     self.my_list = list(my_list)
#     #     self.MIN_LENGTH = 0
#     def list_length(self,MIN_LENGTH = 0) -> int:
#         try:
#             length = int(input("Enter the length of list: "))
#             if length < MIN_LENGTH:
#                 return ValueError (f"Lenth of list can't be {length} cause it's negative.")
#             return length
#         except ValueError as e:
#             print(f"Invalid input {e}, Try again🔁.")
# obj = Solution()
# obj.list_length()
# class Solution:
#     # my_list = []
#     def list_length(self, MIN_LENGTH: int = 0) -> int:
#         try:
#             length = int(input("Enter the length of list: "))
#             if length < MIN_LENGTH:
#                 return ValueError (f"Lenth of list can't be {length} cause it's negative.")
#             return length
#         except ValueError as e:
#             print(f"Invalid input {e}, Try again🔁.")
# obj = Solution()
# obj.list_length()
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         '''Return indices of two numbers that add upto target.'''
#         seen = {}
#         for i , num in enumerate(nums):
#             complement = target - num
#             if complement in seen:
#                 return [seen[complement],i]
#             seen[num] = i
#         return []
# obj = Solution()
# print(obj.twoSum([0,1,2,3,4,5,6,7,8,9],10))

# Source - https://stackoverflow.com/a/69697922
# Posted by Alexey S. Larionov, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-10, License - CC BY-SA 4.0

# number = int(input("Number: "))
# reversed_number = 0
# while number > 0:
#     digit = number % 10
#     reversed_number = reversed_number * 10 + digit
#     number = number // 10

# print(f"Reversed: {reversed_number}")

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         num = str(x)
#         return x == num[ : :-1]
# obj = Solution()
# print(obj.isPalindrome(121))

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         result = 0
#         roman_dict ={
#             'I' : 1,
#             'V' : 5,
#             'X' : 10,
#             'L' : 50,
#             'C' : 100,
#             'D' : 500,
#             'M' : 1000
#         }
#         for i in range(len(s)):
#             if i < len(s)-1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
#                 result -= roman_dict[s[i]]
#             else:
#                 result += roman_dict[s[i]]
#         return result
# obj = Solution()
# print(obj.romanToInt('IV'))

# name, mark, rank = 'vivek', 86.457, 7
# print (f"Mark: {mark:.2f}")
# print (f"Mark: {mark:.0f}")
# print (f'Count: {100000:,}')

# '''padding and alignment'''
# print(f'{name:<15}|{mark:>8.2f}|Rank: {rank}')
# price,gst = 500,0.18
# print(f'Price: Rs.{price}| GST: Rs.{gst:.2f}| Total: Rs.{price*(1+gst):.2f}')
# print(f'A: {name:^8}')
# print(f'A: {name:.^10}')

# string = "Hello, How are you doing today"
# count_vowel= 0
# for ch in string:
#     if ch in 'aeiouAEIOU':
#         count_vowel += 1
# print(count_vowel)
# print(string.split()[3])
# print(string[::-1])
# non_palin,palin = 'abcdef','axttxa'
# print(non_palin == non_palin[::-1])
# print(palin == palin[::-1])

# with open("data.txt","r") as f:
#     data = f.read()
# print(data)
# with open ('data.txt','w') as f:
#     f.write("leo,45,indore\n")
#     f.write("set,45,maihar\n")

# # with open("data.txt","r") as f:
# #     data = f.read()
# # print(data)
# with open ('data.txt','r') as f:
#     for line in f:
#         name,mark,city = line.strip().split(',')
#         print(f'{name:<15} | {mark:>5} | {city}')
#         print("-----------------------------------")
# from typing import List
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#        common = ''
#        prefix = strs[0]
#        for word in strs[1:]:
#            while not word.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                   return ''
#        return prefix
# obj = Solution()
# print(obj.longestCommonPrefix(["flower","flow","flight"]))

# from typing import List
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         common = ''
#         shortest_element = min(strs, key= len)
#         if not strs:
#             return common

#         for idx, element in enumerate(shortest_element):
#             '''
#             here shortest element is flow and this for loop iterate through word 'flow'
#             give us f, l, o, w
#             '''
#             # print(element)
#             for ch in strs:
#                 print(ch[0])
#                 '''
#                 here ch is element of list strs means flower, flow, flight
#                 '''
#                 # print(ch)
#                 if ch[idx] != element:
#                     '''
#                     it compare letter of ch upto idx of element(flow) mean 0 to 3 index of ch if they are not same as "flow"
#                     then return common otherwish continue
#                     '''
#                     return common
#                 '''
#                 add letter which are same only 
#                 like flow and flower it will add f in 0th iteration then l in 1st iteration.....so on 
#                 '''
#             common += element
#         return common
# obj = Solution()
# print(obj.longestCommonPrefix(["flower","flow","flight"]))

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
# print(f"{'Hello':^20}")  # centers text in 20 characters
print(f"| {'NAME':<6}: Vivek")
print(f"{'|':>40}")