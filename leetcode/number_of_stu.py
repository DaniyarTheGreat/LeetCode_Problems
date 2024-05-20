def countStudents(students, sandwiches):
    while students:
        if len(sandwiches) == 0:
            break
        if students[0] != sandwiches[0]:
            students.append(students[0])
        else:
            sandwiches.pop(0)
        students.pop(0)
    return len(students)
        
students = [1,1,0,0]
sandwiches = [0,1,0,1]

print(countStudents(students, sandwiches))