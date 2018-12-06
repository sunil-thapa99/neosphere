student_tuples = [
('John', 15),
('Jane', 12),
('Dave', 10)
]
# print(sorted(student_tuples, key=lambda student: student[1]))
from operator import itemgetter, attrgetter

print(sorted(student_tuples, key=itemgetter(1))) 

