# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


class Student:
    def __init__(self):
        self.name = input('Имя: ')
        self.surname = input('Фамилия: ')
        self.gender = input('Пол: ')
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_rate(self):
        course = input('Введите название посещаемого курса: ')
        name = input('Введите имя вашего лектора: ')
        surname = input('Введите фамилию вашего лектора: ')
        grade = int(input('Введите оценку лектору : '))
        if course in self.courses_in_progress and course in lecturers[f'{name} {surname}'].courses_attached \
                and isinstance(lecturers[f'{name} {surname}'], Lecturer) and grade <= 10:
            if course in lecturers[f'{name} {surname}'].grades:
                lecturers[f'{name} {surname}'].grades[course] += [grade]
            else:
                lecturers[f'{name} {surname}'].grades[course] = [grade]
        else:
            print('Ошибка')

    def av_rate(self):
        grade_all = []
        for grade in self.grades.values():
            grade_all += grade
        av_rating = sum(grade_all) / len(grade_all)
        return av_rating

    def __str__(self,):
        text = f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {self.av_rate()} ' \
               f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.av_rate() < other.av_rate()


class Mentor:
    def __init__(self):
        self.name = input('Имя: ')
        self.surname = input('Фамилия: ')
        self.courses_attached = []

    def __str__(self):
        text = f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}'
        return text


class Lecturer(Mentor):
    def __init__(self):
        super().__init__()
        self.grades = {}

    def av_rate(self):
        grade_all = []
        for grade in self.grades.values():
            grade_all += grade
        av_rating = sum(grade_all) / len(grade_all)
        return av_rating

    def __str__(self):
        text = f'Имя: {self.name}' \
               f'\nФамилия: {self.surname}' \
               f'\nСредняя оценка за лекции: {self.av_rate()}'
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.av_rate() < other.av_rate()


class Reviuver(Mentor):
    def __init__(self):
        super().__init__()

    def student_rate(self):
        course = input('Введите название посещаемого курса: ')
        name = input('Введите имя студента: ')
        surname = input('Введите фамилию студента: ')
        grade = int(input('Введите оценку лектору : '))
        if isinstance(students[f'{name} {surname}'], Student) and course in self.courses_attached \
                and course in students[f'{name} {surname}'].courses_in_progress and grade <= 10:
            if course in students[f'{name} {surname}'].grades:
                students[f'{name} {surname}'].grades[course] += [grade]
            else:
                students[f'{name} {surname}'].grades[course] = [grade]
        else:
            print('Ошибка')


students = {}
lecturers = {}
reviuvers = {}


def add_student():
    student = Student()
    a = f'{student.name} {student.surname}'
    students[a] = student
    print(students)


def add_lecturer():
    lecturer = Lecturer()
    a = f'{lecturer.name} {lecturer.surname}'
    lecturers[a] = lecturer
    print(lecturers)


def add_reviuver():
    reviuver = Reviuver()
    a = f'{reviuver.name} {reviuver.surname}'
    reviuvers[a] = reviuver
    print(reviuvers)


def add_course_in_progress():
    name = input('Введите имя студента: ')
    surname = input('Введите фамилию студента: ')
    course = input('Введите название курса')
    students[f'{name} {surname}'].courses_in_progress += [course]


def add_course_attached_lec():
    name = input('Введите имя лектора: ')
    surname = input('Введите фамилию лектора: ')
    course = input('Введите название курса')
    lecturers[f'{name} {surname}'].courses_attached += [course]


def add_course_attached_rev():
    name = input('Введите имя лектора: ')
    surname = input('Введите фамилию лектора: ')
    course = input('Введите название курса')
    reviuvers[f'{name} {surname}'].courses_attached += [course]


def all_lecturer_rate():
    course = input('Введите название преподаваемого курса: ')
    all_grades = []
    for lecturer in lecturers.values():
        all_grades += lecturer.grades.get(course)
    average_rating = sum(all_grades) / len(all_grades)
    return average_rating


def all_students_rate():
    course = input('Введите название изучаемого курса: ')
    all_grades = []
    for student in students.values():
        all_grades += student.grades.get(course)
    average_rating = sum(all_grades) / len(all_grades)
    return average_rating


def commander():
    command = ''
    while command != 'q':
        command = input('Введите команду: ')
        if command == 'as':
            add_student()
        elif command == 'al':
            add_lecturer()
        elif command == 'ar':
            add_reviuver()
        elif command == 'lr':
            name = input('Введите имя оценивающего студента: ')
            surname = input('Введите фамилию оценивающего студента: ')
            if f'{name} {surname}' in students:
                students.get(f'{name} {surname}').lecturer_rate()
            else:
                print('Нет такого студента')
        elif command == 'sr':
            name = input('Введите имя оценивающего лектора: ')
            surname = input('Введите фамилию оценивающего лектора: ')
            if f'{name} {surname}' in lecturers:
                lecturers.get(f'{name} {surname}').student_rate()
            else:
                print('Нет такого лектора')
        elif command == 'pl':
            name = input('Введите имя лектора: ')
            surname = input('Введите фамилию лектора: ')
            print(lecturers[f'{name} {surname}'])
        elif command == 'ps':
            name = input('Введите имя студента: ')
            surname = input('Введите фамилию студента: ')
            print(students[f'{name} {surname}'])
        elif command == 'pr':
            name = input('Введите имя студента: ')
            surname = input('Введите фамилию студента: ')
            print(reviuvers[f'{name} {surname}'])
        elif command == 'acr':
            add_course_attached_rev()
        elif command == 'acl':
            add_course_attached_lec()
        elif command == 'acs':
            add_course_in_progress()
        elif command == 'alr':
            print(all_lecturer_rate())
        elif command == 'asr':
            print(all_students_rate())
        else:
            print('Такой команды нет')


commander()
