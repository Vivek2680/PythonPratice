def message(): #defineing function
    print("Enter the name: ")
    return int(input())
# message() #calling function or invocation
# a= int(input())
# print(message) #memory address

# nums = iter([1,2,3])

# print(next(nums))
# print(next(nums))

# for i in nums:
#     print(i)
a = message()
print("a:",a)