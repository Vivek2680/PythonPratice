#class is blueprint of obj
#a class is a design
#obj is real thing created from the blueprint 
#obj is a instance of class
# class My_life:
#     name = "vivek"#properties
#     age = "22"#properties

#     def get_name(self):#Methods on class 
#         print(self.name)#self current obj ko point kare ga

# fool = My_life()#obj creation in class
# #() ko constrector ko call karne ke liye use ho rga hai 

# print(fool)#<__main__.My_life object at(memory address) 0x100d96f40>
# fool.get_name()#call method
# print(fool.name)#call prepert

class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    
    def printdata(self):
        print("Name",self.name)
        print("Age",self.age)

vivek = Student("Vivek",20)
print(vivek)
vivek.printdata()

# def main ():
#     user_input()

# def user_input():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     print("Your name:",name)
#     print("Your age:",age)

# if __name__ == "__main__":
#     main()

