# Student's Class
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        """
        :param lecturer: «Lecturer whose work must be evaluated by the student»
        :param course: «Course assigned to the selected lecturer»
        :param grade: «The grade given by the student to the selected lecturer for this course»
        :return: «Completed dictionary attribute for the Lecturer class»
        """
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


# Parent class
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Child class
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in
                student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Students
evelina_sokolova = Student('Evelina', 'Sokolova', 'Female')
sergey_makarov = Student('Sergey', 'Makarov', 'Male')
# Students / Courses in progress
evelina_sokolova.courses_in_progress += ['Python']
sergey_makarov.courses_in_progress += ['Python']

# Reviewers
maxim_reviewer = Reviewer('Maxim', 'Romanoff')
matvei_reviewer = Reviewer('Matvei', 'Danilov')
# Reviewers / Courses in progress
maxim_reviewer.courses_attached += ['Python']
matvei_reviewer.courses_attached += ['Python']

# Lecturers
oleg_lecturer = Lecturer('Oleg', 'Temnov')
# Lecturers / Courses attached
oleg_lecturer.courses_attached += ['Python']

# The reviewer gives a grade to the student
maxim_reviewer.rate_hw(evelina_sokolova, 'Python', 10)
matvei_reviewer.rate_hw(evelina_sokolova, 'Python', 10)
maxim_reviewer.rate_hw(sergey_makarov, 'Python', 9)
matvei_reviewer.rate_hw(sergey_makarov, 'Python', 8)

# A student gives a grade to the lecture for a course
evelina_sokolova.rate_lecturer(oleg_lecturer, 'Python', 10)
sergey_makarov.rate_lecturer(oleg_lecturer, 'Python', 7)

# Displaying the result of the code on the screen for checking
print('[Student] Evelina Sokolova:', evelina_sokolova.grades)
print('[Student] Sergey Makarov:', sergey_makarov.grades)
print('[Lecturer] Oleg Temnov:', oleg_lecturer.grades)
