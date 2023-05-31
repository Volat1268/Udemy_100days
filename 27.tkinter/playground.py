def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


add(5, 10, 3)

class Student:
    def __init__(self, **kw):
        self.age = kw.get("age")
        self.first_name = kw.get("first_name")
        self.last_name = kw.get("last_name")
        self.country = kw.get("country")
        self.score = kw.get("score")

first_student = Student(age=20, first_name="Aleks", last_name="Volat", country="Belarus", score=55)

print(first_student.year)