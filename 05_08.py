grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

def formatted_grades(students):
    num_stud = 1
    students_list = list()
    for name, val in students.items():
        for val1, name1 in grades.items():
            if val1 is val:
                students_list.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(num_stud, name, val, name1))
                '{:>4}|{:<10}|{:^5}|{:^5}'.format(num_stud, name, val, name1)
                num_stud += 1
    return students_list
        
for el in formatted_grades(students):
    print(el)