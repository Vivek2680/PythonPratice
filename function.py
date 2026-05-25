# def message(): #defineing function
#     print("Enter the name: ")
#     return int(input())
# message() #calling function or invocation
# a= int(input())
# print(message) #memory address

# nums = iter([1,2,3])

# print(next(nums))
# print(next(nums))

# for i in nums:
#     print(i)
# a = message(5)
# print("a:",a)

# def hello(n):
#     print("hello,",n)
    
# name = input("Enter your name: ")
# hello(name)

# def mes(num):
#     print("Enter the num:",num)
# num = 1234
# mes(1)
# print(num)

# def mes(what , num):
#     print("Enter",what,"num",num)
# mes("11","tell")
# mes("price",12)
# mes("food",13)

# def into(first_name,last_name):
#     print("Hello, my name is:",first_name,last_name)
# # into("Vivek","Kushwaha")
# # into("Leo","Set")
# # print ("Changing order")
# # into("Kushwaha","Vivek")
# # into("Set","Leo")
# into(first_name="Vivek",last_name="Kushwaha")#keyword argument
# into(first_name="Leo",last_name="Set")#keyword argument
# #order dekho parameter ka 

# def adding(a,b,c):
#     print(a,"+",b,"+",c,"=",a+b+c)
# adding(1,2,3)
# adding(c=1,b=2,a=3)
# adding(1,b=2,c=3)
# adding(1,a=1,b=3)#TypeError: adding() got multiple values for argument 'a'

#defult val
# def intro(a="vivek",b = "kushwaha"):
#     print(a,b)
# intro() # no argument pass but defult work here.

#Return
# def happy(wishes = True):
#     print("one....")
#     print("Two....")
#     print("Three...")
#     if not wishes:
#         return
#     print("Happy")
# # happy()
# happy(False)# no need to handle return

# a = [[1], [2], [3]]

# b = a[:]
# # b[0] = 1

# b[0].append(99)

# print(a)
# print(b)

# def check(val):
#     if val == 10:
#         print("Val is 10")
#     else:
#         print("Val is not 10")
# # print(f"{check(10)}")# it give none buz u arew call funt inside print function
# check(5)
# # print()

# def list_sum(lst):
#     s = 0
#     for element in lst:
#         s += element
#     return s
# print(list_sum([5,4,3]))#
# print(list_sum(2))#for element in lst:
#TypeError: 'int' object is not iterable

# def my_list_fun(n):
#     lst = [i for i in range (20,-1,-1)]
#     # for itretor in range(20,0,-1):
#     #     lst.append(itretor)
#     return lst
# print(my_list_fun(10))


