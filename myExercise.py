import sys

student_info = {}   #dictionary use is making process simpler
content = open("student.txt","r")
inputs = sys.argv[1]

for line in content:
    name = line.split(":")[0]
    student_info[name] = str((line.split(":")[1])).rstrip("]").lstrip("[").strip("\'").strip("\n")

content.close()

print(student_info)

try:
    for item in inputs.split(","):
        university = student_info[item]
        print("Name: {}, University: {}.".format(item,university),end= " ")
except KeyError:
    print("No record of '{}' was found!".format(item))