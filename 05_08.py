'''
У минулому модулі ми працювали із системою оцінок ECTS. Напишіть функцію formatted_grades, 
яка приймає на вхід словник оцінювання студентів за предмет наступного вигляду:

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
І повертає список відформатованих рядків, щоб під час виведення наступного коду:

for el in formatted_grades(students):
    print(el)
Виходила наступна таблиця:

   1|Nick      |  A  |  5
   2|Olga      |  B  |  5
   3|Mike      | FX  |  2
   4|Anna      |  C  |  4
перший стовпець — ширина 4 символи, вирівнювання по правому краю
другий стовпець — ширина 10 символів, вирівнювання по лівому краю
третій та четвертий стовпець — ширина 5 символів, вирівнювання по центру
вертикальний символ | не входить у ширину стовпця
'''

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