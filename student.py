class Student:
    def __init__(self, Registration_number, name, age, course, place):
        self.Registration_number = Registration_number
        self.name = name
        self.age = age
        self.course = course
        self.place = place

    def to_list(self):
        return [self.Registration_number, self.name, self.age, self.course, self.place]
