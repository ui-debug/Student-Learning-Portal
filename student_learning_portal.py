# Student Learning Portal
# PROG211 - Object Oriented Programming 1


class Student:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course

    def display_info(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)
        print("Course:", self.course)

    def enroll_course(self, course):
        self.course = course.course_name
        print(self.name, "has enrolled in", course.course_name)

    @classmethod
    def create_student(cls, name, student_id, course):
        return cls(name, student_id, course)


class Course:
    def __init__(self, course_name, course_code, lecturer):
        self.course_name = course_name
        self.course_code = course_code
        self.lecturer = lecturer

    def display_course(self):
        print("Course Name:", self.course_name)
        print("Course Code:", self.course_code)
        print("Lecturer:", self.lecturer)


# List for storing students
students = []


def add_student(student):
    students.append(student)
    print("Student added successfully.")


def display_all_students():
    print("\n--- All Students ---")

    for student in students:
        student.display_info()
        print()


# Create students
student1 = Student(
    "Christian",
    "ST001",
    "Software Engineering"
)

student2 = Student(
    "Abdul",
    "ST002",
    "Computer Science"
)

student3 = Student(
    "Mohamed",
    "ST003",
    "Information Technology"
)


# Create course
course1 = Course(
    "Object Oriented Programming",
    "PROG211",
    "Mr. Kamara"
)


# Add students to list
add_student(student1)
add_student(student2)
add_student(student3)


# Display student information
print("\n--- Student Information ---")

student1.display_info()

print()

student2.display_info()


# Display course information
print("\n--- Course Information ---")

course1.display_course()


# Student interacts with course
print("\n--- Course Enrollment ---")

student1.enroll_course(course1)


# Use class method
student4 = Student.create_student(
    "Fatmata",
    "ST004",
    "Software Engineering"
)

add_student(student4)


# Display all students
display_all_students()