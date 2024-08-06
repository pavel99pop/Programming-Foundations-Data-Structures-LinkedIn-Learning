my_list = [1, 7, 3]
print(sorted(my_list))
print(sorted(my_list, reverse=True))

top_students = [('Bob', 80), ('Alice', 82), ('Jake', 90)]
print(sorted(top_students))
print(sorted(top_students, key=lambda x : x[1], reverse=True))