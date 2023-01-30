class Student:
    all_students = []
    
    def __init__(self, name, grade):
        self.name = name
        self._grade = grade 
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade not in range(0, 101):
            raise ValueError("New grade not in the accepted range of [0-100].")
        self._grade = grade

    @classmethod
    def get_average_grade(cls):
        return Student.calculate_average_grade(cls.all_students)

    @classmethod
    def get_best_student(cls):
        number_of_students = len(cls.all_students)

        if number_of_students == 0:
            return None
        elif number_of_students == 1:
            return cls.all_students[0]
        else:
            best_student = cls.all_students[0] 

            for student in cls.all_students[1:]:
                if student._grade > best_student._grade:
                    best_student = student 
 
        return best_student

    @staticmethod
    def calculate_average_grade(students):
        students_length = len(students)

        if students_length == 0:
            return -1

        total_students_grades = 0

        for student in students:
            total_students_grades += student._grade

        return total_students_grades / students_length


