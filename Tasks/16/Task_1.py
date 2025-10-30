class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Student(Person):
    def __init__(self, name, age, gender, student_id, grade, courses=None):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.grade = grade
        self.courses = courses if courses else []
        self.grades = {}

    def add_course(self, course):
        self.courses.append(course)

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def study(self, subject):
        return f"{self.name} is studying {subject}"


class Teacher(Person):
    def __init__(self, name, age, gender, employee_id, subject, salary):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary
        self.classes = []

    def teach(self, topic):
        return f"{self.name} is teaching {topic}"

    def assign_class(self, class_name):
        self.classes.append(class_name)

    def get_salary(self):
        return self.salary

    def give_grade(self, student, grade):
        return f"{self.name} gave {student} a grade of {grade}"