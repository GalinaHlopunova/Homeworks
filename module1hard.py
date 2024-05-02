grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {"Johnny","Bilbo","Steve","Khendrik","Aaron"}
average_grade = {}
students_list = list(students)
students_list.sort()
for i in range(len(students_list)):
    average_grade[students_list[i]] = sum(grades[i])/len(grades[i])
print (average_grade)
