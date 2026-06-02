#shadowing var

# def mult(x):
#     var = 7
#     return x * var
# var = 3#local val

# print(mult(7))

# def my_fun():
#     global var
#     var = 3
#     print("do i know the valu of var?",var)
# var = 1
# my_fun()
# print(var)

#---------------------------
#example

# var = 2
# print(var)

# def return_var():
#     global var
#     var = 5
#     return var
# print(return_var())
# print(var)

#------------------------

# def my_fun(n):
#     print("i got it ",n)
#     n +=1
#     print("i have",n)
# var = 1
# my_fun(var)
# print(var)

#-----------------------

# def my_fun(my_list1):
#     print("1",my_list1)
#     print("3",my_list2)
#     my_list1 = [0,1]#assing
#     print("3",my_list1)
#     print("4",my_list2)
# my_list2 = [2,3]
# my_fun(my_list2)
# print("5",my_list2)

#-----------------------
#mutation = stru change
# def my_fun(my_list1):
#     print("1",my_list1)
#     print("3",my_list2)
#     del my_list1[0]#assing
#     print("3",my_list1)
#     print("4",my_list2)
# my_list2 = [2,3]
# my_fun(my_list2)
# print("5",my_list2)

#--------------------

#loop and recursion 

# def num(x):
#     print(x)
#     if x==0:
#         print("going out of loop")
#         return
#     else:
#         print("go in rec", x)
#         num(x - 1)
#         print("out of rec,",x)
# num(5)
# print("complete rec")

# def fact(x):
#     if x<=0:
#         return 1
#     else:
#         return x * fact(x-1)
# print(fact(5))

# def f(n):

#     if n == 0:
#         print("done")
#         return

#     print(n)

#     f(n-1)

#     print(n)

# f(3)



# print(22/7)
# f='a'
# g='b'
# h = "3"
# print((f+g)*h)
s = "hello world"
# for ch in s:
#     if ch in 'aeoiu':
#         continue
#     else:
#         print(ch,end="")
# print()
# s[0] = 'H'#TypeError: 'str' object does not support item assignment
# s = 'H' + s[1:len(s)]#new object
# print(s)
# print(s[10::-1])
# verb = input("enter verb: ")
# print(f"i can {verb}better than you")
# print(4*f"{verb} "+verb)