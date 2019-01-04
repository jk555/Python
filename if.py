number = 5
if number == 5:
        print("Number is defined and truthy")

text = "Python"
if text:
    print("text is defined and truthy")

#Boolean and None

#python_course = True
#if python_course:
#    print("This will execute")
#aliens_found = None
#if aliens_found:
#    print("This will not execute")

#! operator
#    number = 5
    #    if number != 5:
    #    print("This will not execute")
    #
    #python_course = True
    #if not python_course:
#    print("This will not execute")


#Multiple if conditions
#number=3
#python_course=True
#if number ==3 and python_course:
#    print("This will execute")
#
#if number==17 or python_course:
#    print("This will also execute")

#ternery If Statements
#a=1
#b=2
#"b is bigger than a" if a > b else "a is smallet than b"

student_names = ["Mark","Katerina","Jessica"]
print(student_names[1])
#last is -1 index
print(student_names[-1])
print(student_names[-2])
#Adding to the list: Add at the end
#student_names.append("Homer")
print(student_names)

print("Mark" in student_names)
#How many elements do we have in list
print(len(student_names))

#list can include multiple types items in the list. But try to avoid that.

#how to delete the item from the list.
#del(student_names[2])
print(student_names)

#List slicing: [1: means ignore first one and print the rest
print(student_names[1:])

#ignore first and last and print the rest of the list
print(student_names[1:-1])


