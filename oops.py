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

# class Student:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
    
#     def printdata(self):
#         print("Name",self.name)
#         print("Age",self.age)

# vivek = Student("Vivek",20)
# print(vivek)
# vivek.printdata()

# def main ():
#     user_input()

# def user_input():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     print("Your name:",name)
#     print("Your age:",age)

# if __name__ == "__main__":
#     main()

#--------------------------------------

# class Ex():
#     def __init__(self,val = 1):
#         self.first = val
#     def set_second(self,val):
#         self.second = val
# ex_obj_1 = Ex()
# ex_obj_2 = Ex(2)
# ex_obj_2.set_second(3)
# ex_obj_3 = Ex(4)
# ex_obj_3.third = 5#"."method/property add krna
# print(ex_obj_1)
# print(ex_obj_1.__dict__)
# print(ex_obj_2.__dict__)
# print(ex_obj_3.__dict__)

#-------------------------------------

# class Classy:
#     def __init__(self,par1):
#         self.par1 = par1
#         print("This is constructor",par1)
        # self.par2 = par2
    # def method1(self,par):
    #     print("This is method",par)
# print(Classy.method1)
# obj = Classy()
# obj.method1(1)
# Classy.method1(1,2)#instance method ko call krne ke liye pehle obj create krna pdta hai but class method ko direct class se call kr skte hai
# Classy.__init__(2,'vivek')

# class Star:
#     def __init__(self,name,galaxy):
#         self.name = name
#         self.galaxy = galaxy
#     def __str__(self):
        # return f"Star name: {self.name}, Galaxy: {self.galaxy}"
# # Star.__init__("Sun","Milky Way")
# sun = Star("Sun","Milky Way")
# print(sun)
#------------------------------------------
#
# class Vehicle:
#     pass
# class LandVehicle(Vehicle):
#     pass
# class TrackedVehicle(LandVehicle):
#     pass
# for cls in (Vehicle, LandVehicle, TrackedVehicle):
#     for parent in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls, parent), end=' ')
#     print()

#-------------------------------------------

# class Super:
#     supVar = 1
# class Sub(Super):
#     subVar = 2
# obj = Sub()
# print(obj.supVar)
# print(obj.subVar)

#-------------------------------------------


# class Super:
#     def __init__(self):
#         self.supVar = 1
# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 2
# class SubSub(Sub):
#     def __init__(self):
#         super().__init__()
#         self.subSubVar = 3

# obj = SubSub()
# print(obj.supVar)
# print(obj.subVar)
# print(obj.subSubVar)
# print(int("20",4)) 

# class Super:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return f"my name is {self.name}."
# class sub (Super):
#     def __init__(self, name):
#         super().__init__(name)#super class ko access kar rha hai
# obj = sub ("Vivek")
# print(obj)

# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
# class Sub (SuperA,SuperB):
#     pass

# obj = Sub()
# print(obj.var_a,obj.fun_a())
# print(obj.var_b,obj.fun_b())

# multilevel inheratice
# class SuperA():
#     var_a = 10
#     def fun(self):
#         return 11
# class SuperB(SuperA):
#     var_b = 20
#     def fun(self):
#         return 21
# class Level3 (SuperB):
#     pass

# obj = Level3()
# print(obj.fun(),obj.var_a)
# # print(obj.var_b,obj.fun_b())

# class Left():
#     var = 'L'
#     def fun(self):
#         return f"Left"











# class One():
#     def do_it(self):
#         print("do_it form one")
#     def doanything(self):
#         self.do_it()
# class Two(One):
#     def do_it(self):
#         print("do it from Two")
# one = One()
# two = Two()
# one.doanything()
# two.doanything()

# def reciprocal(n):
#     try:
#         n = 1/n
#     except ZeroDivisionError:
#         print("Division failed")
#         return None
#     else:
#         print("Everything went fine")
#         # return n
#     finally:
#         print("It's time to say goodbye")
#         return n
# n = int(input("Enter tha value of n: "))
# print(reciprocal(n))

try:
    i = int("Hello")
except Exception as e:
    print(e)
    print(e.__rept__())