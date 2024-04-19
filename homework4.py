immutable_var=19,25,"май",False
print(immutable_var)
#immutable_var[1]=20
#immutable_var.append("вебинар")
print(type(immutable_var))
print("Кортеж - зто неизменяемый тип данных в Python, который используется для хранения упорядоченной последовательности элементов.")
mutable_list=[19,25,"май",False]
mutable_list[1]=20
mutable_list[2]="апрель"
mutable_list[3]=True
mutable_list.append("вебинар")
print(mutable_list)