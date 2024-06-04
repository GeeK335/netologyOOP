# Helper classes
class PersonalInfo:
    """
    This class represents personal information of an individual.

    Attributes:
        name (str): The first name of the individual.
        surname (str): The last name of the individual.
        fullname (str): The full name of the individual (combination of first name and last name).
        gender (str): The gender of the individual.

    Methods:
        __init__: Initializes the PersonalInfo object with the provided name, surname, and gender.
    """

    def __init__(self, name: str, surname: str, gender: str):
        if not name or not surname or not gender:
            raise ValueError('Name, surname, and gender must be non-empty strings.')

        self.name: str = name.strip()
        self.surname: str = surname.strip()
        self.fullname: str = f'{name.strip()} {surname.strip()}'
        self.gender: str = gender.strip()


class MathMethods:
    def average(self, grades: list) -> float:
        """
        Calculate the average grade from a list of grades.

        Args:
            grades (list): A list of grades for a student.

        Returns:
            float: The average grade rounded to one decimal place.
        """
        if not grades:
            return 'Еще нет оценок'

        # Merging lists if they contain lists
        merged_list = [el for sublist in grades for el in (sublist if isinstance(sublist, list) else [sublist])]
        return round(sum(merged_list) / len(merged_list), 1)


# Student's Class
class Student(PersonalInfo, MathMethods):
    """
    A class to represent a student with personal information, grades, courses in progress,
    and finished courses.

    Attributes:
        name (str): The first name of the student.
        surname (str): The last name of the student.
        gender (str): The gender of the student.
        finished_courses (list): List of courses finished by the student.
        courses_in_progress (list): List of courses currently in progress for the student.
        grades (dict): Dictionary containing grades for different courses.
        average_value (int): The average grade of the student.

    Methods:
        __str__(self) -> str: Return a formatted string with the student's personal information,
        average grade, courses in progress, and finished courses.
        __gt__(self, second) -> bool: Compare the average grades of two students and return True
        if the current student has a higher average grade.
        __eq__(self, second) -> bool: Compare the average grades of two students and return True
        if they are equal.
        rate_lecturer(self, lecturer, course, grade) -> dict: Rate a lecturer for a specific
        course and update the lecturer's grades dictionary.
    """

    def __init__(self, name: str, surname: str, gender: str):
        super().__init__(name, surname, gender)
        self.finished_courses: list = []
        self.courses_in_progress: list = []
        self.grades: dict = dict()
        self.average_value: int

    def __str__(self) -> str:
        """
        Return a formatted string with the student's personal information,
        average grade, courses in progress, and finished courses.

        Returns:
            str: A formatted string containing the student's personal information,
            average grade, courses in progress, and finished courses.
        """
        self.average_value: float = self.average(list(self.grades.values()))
        name: str = f'Имя: {self.name}'
        surname: str = f'Фамилия: {self.surname}'
        average_rate: str = f'Средняя оценка за лекции: {self.average_value}'
        courses_in_progress: str = (f'Курсы в процессе изучен'
                                   f'ия: {', '.join(self.courses_in_progress)}')
        courses_finished: str = f'Завершенные курсы: {', '.join(self.finished_courses)}'
        return f'{name}\n{surname}\n{average_rate}\n{courses_in_progress}\n{courses_finished}'

    def __gt__(self, other) -> str:
        """
        Compare the average grades of two students and determine which student has
        a higher average grade.

        Parameters:
            other (Student): The other student to compare the average grade with.

        Returns:
            str: A formatted string indicating which student has a higher average grade
            and by how much.

        Raises:
            ValueError: If the average grades are not calculated properly or if the comparison
            is not between two Student instances.
        """
        if None in (self.average_value, other.average_value):
            raise ValueError('Average grades are not calculated properly.')
        if not isinstance(other, Student):
            raise ValueError('Comparison can only be done between two Student instances.')

        self_more: str = (f'{self.fullname}({self.average_value}) результативнее '
                          f'{other.fullname}({other.average_value})')
        second_more: str = (f'{other.fullname}({other.average_value}) результативнее '
                            f'{self.fullname}({self.average_value}).')

        return self_more if self.average_value > other.average_value else second_more

    def __eq__(self, other) -> str:
        """
        Compare the average grades of two students and determine if they are equal.

        Parameters:
            other (Student): The other student to compare the average grade with.

        Returns:
            str: A formatted string indicating whether the students have equal average grades
            and providing details on their names and average grades.

        Raises:
            ValueError: If the average grades are not calculated properly or if the comparison
            is not between two Student instances.
        """
        if None in (self.average_value, other.average_value):
            raise ValueError('Average grades are not calculated properly.')
        if not isinstance(other, Student):
            raise ValueError('Comparison can only be done between two Student instances.')

        equality: str = (f'{self.fullname} и {other.fullname} одинаково результативны. Их средняя '
                         f'оценка за лекции составляет: {self.average_value}')
        inequality: str = (f'{self.fullname}({self.average_value}) и {other.fullname}'
                           f'({other.average_value}) не одинаково результативны.')

        return equality if self.average_value == other.average_value else inequality

    def rate_lecturer(self, lecturer, course: str, grade: int):
        """
        Rate a lecturer for a particular course.

        Parameters:
            lecturer (Lecturer): The lecturer to be rated.
            course (str): The course for which the lecturer is being rated.
            grade (int): The grade given to the lecturer for the course.

        Returns:
            str: If the rating is successful, returns None. If the conditions for rating
            are not met, returns 'Ошибка'.
        """
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in
                self.courses_in_progress):
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'


# Parent class
class Mentor(PersonalInfo):
    def __init__(self, name: str, surname: str, gender: str):
        super().__init__(name, surname, gender)
        self.courses_attached: list = []


# Lecturers class
class Lecturer(Mentor, MathMethods):
    def __init__(self, name: str, surname: str, gender: str):
        super().__init__(name, surname, gender)
        self.grades = dict()
        self.average_value: int

    def __str__(self) -> str:
        """
        Return a formatted string with the student's personal information,
        average grade, courses in progress, and finished courses.

        Returns:
            str: A formatted string containing the student's personal information,
            average grade, courses in progress, and finished courses.
        """
        self.average_value: float = self.average(list(self.grades.values()))
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_value}')

    def __gt__(self, other) -> str:
        """
        Compare the average grades of two lecturers and determine which lecturer has
        a higher average grade.

        Parameters:
            other (Lecturer): The other lecturer to compare the average grade with.

        Returns:
            str: A formatted string indicating which lecturer has a higher average grade
            and by how much.

        Raises:
            ValueError: If the average grades are not calculated properly or if the comparison
            is not between two Lecturer instances.
        """
        if None in (self.average_value, other.average_value):
            raise ValueError('Average grades are not calculated properly.')
        if not isinstance(other, Lecturer):
            raise ValueError('Comparison can only be done between two Student instances.')

        self_more: str = (f'{self.fullname}({self.average_value}) результативнее {other.fullname}'
					 f'({other.average_value})')
        second_more: str = (f'{other.fullname}({other.average_value}) результативне'
                            f'е {self.fullname}'
					   f'({self.average_value}).')

        return self_more if self.average_value > other.average_value else second_more

    def __eq__(self, other) -> str:
        """
        Compare the average grades of two students and determine if they are equal.

        Parameters:
            other (Lecturer): The other lecturer to compare the average grade with.

        Returns:
            str: A formatted string indicating whether the lecturers have equal average grades
            and providing details on their names and average grades.

        Raises:
            ValueError: If the average grades are not calculated properly or if the comparison
            is not between two Lecturer instances.
        """
        if None in (self.average_value, other.average_value):
            raise ValueError('Average grades are not calculated properly.')
        if not isinstance(other, Lecturer):
            raise ValueError('Comparison can only be done between two Student instances.')

        equality: str = (f'{self.fullname} и {other.fullname} одинаково результативны. Их средняя '
					f'оценка за лекции составляет: {self.average_value}')
        inequality: str = (f'{self.fullname}({self.average_value}) и {other.fullname}'
					  f'({other.average_value}) не одинаково результативны.')

        return equality if self.average_value == other.average_value else inequality


# Reviewers class
class Reviewer(Mentor):
    def rate_student(self, student, course: str, grade: list):
        """
        Rate a student for a specific course.

        Parameters:
            student (Student): The student to be rated.
            course (str): The course for which the student is being rated.
            grade (list): Ratings inside the list.

        Returns:
            str: If the rating is successful, returns None. If the conditions for rating
            are not met, returns 'Ошибка'.
        """
        if (isinstance(student, Student) and course in student.courses_in_progress and course in
                self.courses_attached):
            student.grades.setdefault(course, []).extend(grade)
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        """
        Returns a string with the reviewer's first and last name.
        """
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Students
evelina_sokolova = Student('Эвелина', 'Соколова', 'Женщина')
sergey_makarov = Student('Сергей', 'Макаров', 'Мужчина')
# Students / Finished courses
evelina_sokolova.finished_courses += ['Вводный модуль', 'Основы Python']
sergey_makarov.finished_courses += ['Вводный модуль', 'Основы Python']
# Students / Courses in progress
evelina_sokolova.courses_in_progress += ['Git', 'Python']
sergey_makarov.courses_in_progress += ['Git', 'Python']

# Reviewers
maxim_reviewer = Reviewer('Максим', 'Романов', 'Мужчина')
garik_reviewer = Reviewer('Гарик', 'Добрый', 'Мужчина')
# Reviewers / Courses in progress
maxim_reviewer.courses_attached += ['Python']
garik_reviewer.courses_attached += ['Git']

# Lecturers
oleg_lecturer = Lecturer('Олег', 'Темнов', 'Мужчина')
dima_lecturer = Lecturer('Дмитрий', 'Окунев', 'Мужчина')
# Lecturers / Courses attached
oleg_lecturer.courses_attached += ['Git', 'Python']
dima_lecturer.courses_attached += ['Python']

# The reviewer gives a grade to the student
# (Each element in the list, which is passed as a grade parameter, represents the grade for a
# single lesson)
garik_reviewer.rate_student(evelina_sokolova, 'Git', [8, 7])
maxim_reviewer.rate_student(evelina_sokolova, 'Python', [10, 10, 8])
garik_reviewer.rate_student(sergey_makarov, 'Git', [6, 8])
maxim_reviewer.rate_student(sergey_makarov, 'Python', [9, 10, 7])

# A student gives a grade to the lecture for a course
evelina_sokolova.rate_lecturer(oleg_lecturer, 'Git', 8)
evelina_sokolova.rate_lecturer(oleg_lecturer, 'Python', 10)
evelina_sokolova.rate_lecturer(dima_lecturer, 'Python', 9)
sergey_makarov.rate_lecturer(oleg_lecturer, 'Git', 5)
sergey_makarov.rate_lecturer(oleg_lecturer, 'Python', 7)
sergey_makarov.rate_lecturer(dima_lecturer, 'Python', 8)

print('= TASK 1 and 2 =')
# Displaying the result of the code on the screen for checking
print('[Student] Evelina Sokolova:', evelina_sokolova.grades)
print('[Student] Sergey Makarov:', sergey_makarov.grades)
print('[Lecturer] Oleg Temnov:', oleg_lecturer.grades)

# Print for 3 Task
print('', '= TASK 3 =', '#1 Перезагрузка метода', sep='\n')
print('— Reviewer —', maxim_reviewer, sep='\n')
print('', '— 1 Lecturer —', oleg_lecturer, sep='\n')
print('', '— 2 Lecturer —', dima_lecturer, sep='\n')
print('', '— 1 Student —', evelina_sokolova, sep='\n')
print('', '— 2 Student —', sergey_makarov, sep='\n')

print('', '#2 Реализуйте возможность сравнивать', sep='\n')
print('- Students')
print(evelina_sokolova > sergey_makarov)
print(evelina_sokolova == sergey_makarov)
print('- Lecturers')
print(oleg_lecturer > dima_lecturer)
print(oleg_lecturer == dima_lecturer)


# Counting duplicate keys in different dictionaries
def count_unique_keys(dicts: list[dict]) -> dict:
    """
    Count the number of unique keys in the dictionary.

    Args:
        dicts (list): A list of dictionaries.

    Returns:
        dict: A dictionary with unique keys and their corresponding values.
    """
    keys_number: dict = {}
    for dictionary in dicts:
        for key in dictionary:
            keys_number[key] = keys_number.get(key, 0) + 1
    return keys_number


# Calculating the average grade for homework for all students in a particular course
def average_rating(course_name: str, role: list[dict]) -> float:
    """
    Calculate the average rating for a specific course.

    Args:
        course_name (str): The name of the course to calculate the average rating for.
        role (list): A list of dictionaries containing ratings for different courses.

    Returns:
        float: The average rating for the specified course.
    """
    # The number of keys in the dictionary
    keys: dict = count_unique_keys(role)
    # A list for storing all ratings for future reference.
    combined_grades: list = []
    #
    if keys[course_name] > 1:
        # If there are more than one identical key, we will add the values
        # associated with those keys to a common list.
        for i in range(len(role)):
            combined_grades += role[i][course_name]
    else:
        # If the desired key is found in only one dictionary,
        # we will get its corresponding value
        for dictionary in role:
            if course_name in dictionary:
                combined_grades += dictionary[course_name]
    return round(sum(combined_grades) / len(combined_grades), 1)


average_s_text: str = ('Средняя оценка за домашние задания по всем студентам в рамках конкретного '
                    'курса:')
average_l_text: str = 'Средняя оценка за лекции всех лекторов в рамках конкретного курса:'
average_s_rating: float = average_rating('Python', [evelina_sokolova.grades, sergey_makarov.grades])
average_l_rating: float = average_rating('Git', [oleg_lecturer.grades, dima_lecturer.grades])

print('', '= TASK 4 =', sep='\n')
print(average_s_text, average_s_rating)
print(average_l_text, average_l_rating)
