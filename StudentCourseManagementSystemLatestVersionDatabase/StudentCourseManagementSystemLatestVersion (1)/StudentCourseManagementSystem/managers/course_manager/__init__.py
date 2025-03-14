from StudentCourseManagementSystem.models.student import Student
from StudentCourseManagementSystem.models.instructor import Instructor
from StudentCourseManagementSystem.models.course import Course
from StudentCourseManagementSystem.models.enrollment import Enrollment
# from test_course_manager import UsedIdException
from StudentCourseManagementSystem.database import DataBase


class RepeatedCourseCreationException(Exception):
    pass


data_base = DataBase()


class CourseManager:

    def __init__(self):

        self.students = []
        self.instructors = []
        self.courses = []
        self.enrollments = []
        data_base.load_from_file()

    def add_student(self, student: Student):
        self.students.append(student)
        data_base.save_to_file()

    def add_instructor(self, instructor: Instructor):
        # if instructor.user_id in self.instructors:
        #      raise UsedIdException("Instructor already exists.")
        self.instructors.append(instructor)
        data_base.save_to_file()

    def add_course(self, course: Course):
        for course in self.courses:
            if course in self.courses:
                raise RepeatedCourseCreationException("You have a course created already!")
        self.courses.append(course)
        data_base.save_to_file()

    def enroll_student(self, student_id: int, course_id: int):
        enrollment = Enrollment(len(self.enrollments) + 1, student_id, course_id)
        self.enrollments.append(enrollment)
        student = self.get_student(student_id)
        student.enroll_course(course_id)
        data_base.save_to_file()
        return enrollment

    def get_student(self, student_id: int):
        for student in self.students:
            if student.user_id == student_id:
                return student
        return None

    def get_course(self, course_id: int):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    # @property
    # def courses(self):
    #      courses_offered = ""
    #      for course in self.courses:
    #          courses_offered += course
    #      return courses_offered

    # @courses.setter
    # def courses(self, courses):
    #     self.courses = courses

    def get_students_in_course(self, course_id: int):
        students = []
        for enrollment in self.enrollments:
            if enrollment.course_id == course_id:
                student = self.get_student(enrollment.student_id)
                students.append(student)
        return students

    @property
    def get_size_of_students(self):
        return len(self.students)

    @property
    def get_size_of_instructor(self):
        return len(self.instructors)

    @property
    def get_size_of_course(self):
        return len(self.courses)

    # def save_to_file(self):
    #         with open('students.txt', 'w') as f:
    #             f.write('Students:\n')
    #             for student in self.students:
    #                 f.write(f"{student.user_id},{student.username},{student.password.decode('utf-8')}\n")
    #
    #         with open('instructors.txt', 'w') as u:
    #             u.write('Instructors:\n')
    #             for instructor in self.instructors:
    #                 u.write(f"{instructor.user_id},{instructor.username},{instructor.password.decode('utf-8')}\n")
    #             u.write('Courses:\n')
    #             for course in self.courses:
    #                 u.write(f"{course.course_id},{course.name},{course.credits}\n")

    # with open('course.txt', 'w') as g:
    #     g.write('Courses:\n')
    #     for course in self.courses:
    #         g.write(f"{course.course_id},{course.name},{course.credits}\n")

    # f.write('Instructors:\n')
    # for instructor in self.instructors:
    #     f.write(f"{instructor.user_id},{instructor.username},{instructor.password.decode('utf-8')}\n")
    # f.write('Courses:\n')
    # for course in self.courses:
    #     f.write(f"{course.course_id},{course.name},{course.credits}\n")

    # def load_from_file(self):
    #     try:
    #         with open('students.txt', 'r') as f:
    #             section = None
    #             for line in f:
    #                 line = line.strip()
    #                 if not line:
    #                     continue
    #                 if line == 'Students:':
    #                     section = 'students'
    #                 elif section == 'students' and line:
    # elif line == 'Instructors:':
    #     section = 'instructors'
    # elif line == 'Courses:':
    #     section = 'courses'
    # elif line == 'Enrollments:':
    #     section = 'enrollments'
    #
    # try:
    #     user_id, username, password_hash = line.split(',')
    #     password_hash = password_hash.encode('utf-8')
    #     self.students.append(Student(int(user_id), username, password_hash))
    # except ValueError:
    #     print(f"Error reading student data: {line}")
    # elif section == 'instructors' and line:
    #     try:
    #         user_id, username, password_hash = line.split(',')
    #         password_hash = password_hash.encode('utf-8')
    #         self.instructors.append(Instructor(int(user_id), username, password_hash))
    #     except ValueError:
    #         print(f"Error reading instructor data: {line}")
    # elif section == 'courses' and line:
    #     try:
    #         course_id, name, instructor_id = line.split(',')
    #         self.courses.append(Course(int(course_id), name, int(instructor_id),credits))
    #     except ValueError:
    #         print(f"Error reading course data: {line}")
    # elif section == 'enrollments' and line:
    #     try:
    #         enrollment_id, student_id, course_id = line.split(',')
    #         self.enrollments.append(Enrollment(int(enrollment_id), int(student_id), int(course_id)))
    #     except ValueError:
    #         print(f"Error reading enrollment data: {line}")
    # with open ('instructors.txt', 'r') as u:
    #     section = None
    #     for line in u:
    #         line = line.strip()
    #         if not line:
    #             continue
    #         if line == 'Instructors:':
    #             section = 'instructors'
    #         elif section == 'instructors' and line:
    #             try:
    #                 user_id, username, password_hash = line.split(',')
    #                 password_hash = password_hash.encode('utf-8')
    #                 self.instructors.append(Instructor(int(user_id), username, password_hash))
    #             except ValueError:
    #                 print(f"Error reading instructor data: {line}")
    #
    #         if line == 'Courses:':
    #             section = 'courses'
    #         elif section == 'courses' and line:
    #             try:
    #                 course_id, name, instructor_id = line.split(',')
    #                 self.courses.append(Course(int(course_id), name, int(instructor_id),credits))
    #             except ValueError:
    #                 print(f"Error reading course data: {line}")

    # with open('courses.txt', 'r') as g:
    #     section = None
    #     for line in g:
    #         line = line.strip()
    #         if not line:
    #             continue
    #         if line == 'Courses:':
    #             section = 'courses'
    #             try:
    #                 course_id, name, instructor_id = line.split(',')
    #                 self.courses.append(Course(int(course_id), name, int(instructor_id),credits))
    #             except ValueError:
    #                 print(f"Error reading course data: {line}")

    # except FileNotFoundError:
    #     print("No previous data found, starting fresh.")
    # except ValueError as e:
    #     print(f"Error reading data from file: {e}")
