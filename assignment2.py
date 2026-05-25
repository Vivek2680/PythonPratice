beatles = []
# length_list = int(input("Enter how many element you want to add in list: "))
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

print("-------------using append method----------")
for index in range(2):
    
    user_input = input("Enter the element of list by append: ")
    beatles.append(user_input)
print(beatles)
print("------------deleting append element-----------")
del beatles[3:5]
# del beatles[3]
# del beatles[4]
print(beatles)

print("----------using insert methd-------------")
for index in range(1):
    user_input_insert = input("Enter the element of list by insert: ")
    beatles.insert(0,user_input_insert)
print(beatles)

#----------------------------------------------------------------------







