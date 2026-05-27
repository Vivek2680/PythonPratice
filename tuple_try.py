# my_tuple =(1,2,3,4,5)
# # my_tuple1 = (9,0)
# #run
# # In and NOT IN still work here 
# print(5 in my_tuple)
# print(5 not in my_tuple)
# print(len(my_tuple))
# print(len(my_tuple1))
# my_tuple1 += my_tuple
# print(my_tuple1)

# not run
# my_tuple.append(0)
# print(my_tuple)
# del my_tuple[0]
# print(my_tuple)
# my_tuple[1] = -10
# print(my_tuple)

# data = [[1], [2]]

# for row in data:
#     row = row + [99]

# print(data)

# a = [[1], [2], [3]]

# b = a[:]

# for i, row in enumerate(b):

#     if i == 1:
#         row.append(100)

#     else:
#         row = row + [99]

# print(a)
# print(b)

# def change(nums):
#     nums = nums + [99]

# data = [1, 2]

# change(data)

# print(data)

# x = 10

# def test():
#     x = 99
#     print("inside:", x)

# test()

# print("outside:", x)

# def modify(val):
#     val += [100]
#     return val

# nums = [1]

# result = modify(nums)

# print(nums)
# print(result)
# print(nums is result)

# def update(n):
#     n += 5
#     print("inside:", n)

# x = 10

# update(x)

# print("outside:", x)

# x = [1]

# def outer(lst):

#     def inner():
#         lst.append(99)

#     inner()

# outer(x)

# print(x)

def process(data):

    data.append(10)

    data = data + [20]

    return data

nums = [1]

result = process(nums)

print(nums)
print(result)
print(nums is result)

# my_tuple = (1,10,100)
# my_tuple += (1000,10000)
# print(my_tuple)

# tuple1 = (1,2,3)
# for element in tuple1:
#     print(element)

# tuple2 = (1,2,3,4)
# tuple3 = (1,2,3,4)
# tuple4 = tuple1 + tuple2
# tuple5 = tuple3 * 2
# print(tuple4)
# print(tuple5)

# my_tuple = tuple((1,2,"string"))
# print(my_tuple)

# my_list = [1,2,3]
# print(my_list)
# print(type(my_list))
# tup = tuple(my_list)# type conversion
# print(tup)
# print(type(tup))
# lst = list(tup)# type conversion
# print(lst)
# print(type(lst))

# var = 123
# t1 = (1,)
# t2 = (2,)
# t3 = (3,var)

# t1,t2,t3 = t2,t3,t1
# print(t1,t2,t3)

