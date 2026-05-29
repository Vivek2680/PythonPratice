student_dict = {}
student_entry = int(input("Enter the number of student you want to enter: "))
for i in range(student_entry):
    name = input("Enter the name of student: ")
    mark = int(input(f"Enter the mark of {name} is (0-10): "))
    # student_dict.update({name : mark})
# print(student_dict)
# print(mark)
    if mark not in range(0,11):# mark out of range input
        print(f"out of range mark(0-10): {mark}")
        break

    if name in student_dict:
        student_dict[name] +=  (mark, )#TypeError: unsupported operand type(s) for +=: 'int' and 'tuple': casue of line 78
    else:
        student_dict[name] = (mark, )
print(student_dict)
for name,score in student_dict.items():
    sum = 0
    # print(name,"->",marks)
    for m in score:
        # print(mark)
        sum += m
    print(name, "->",sum/len(score))