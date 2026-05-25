import re


# PART 1: CLASS DEFINITION

class Student:

    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades  # list of integers

    # Add a grade
    def add_grade(self, grade):
        self.grades.append(grade)

    # Average grade
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    # Display student info
    def display_info(self):
        print("\nName:", self.name)
        print("Email:", self.email)
        print("Grades:", self.grades)
        print("Average Grade:", self.average_grade())

    # Return grades as tuple
    def grades_tuple(self):
        return tuple(self.grades)



# PART 2: CREATE OBJECTS

student1 = Student("Alice", "alice@gmail.com", [85, 90])
student2 = Student("Bob", "bob@gmail.com", [70, 75])
student3 = Student("Charlie", "charlie@gmail.com", [95, 88])

students = [student1, student2, student3]

# Add 2 grades to each student
for student in students:
    student.add_grade(100)
    student.add_grade(80)

# Display info
for student in students:
    student.display_info()



# PART 3: DICTIONARY + SET

student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Safe retrieval function
def get_student_by_email(email):
    return student_dict.get(email)


# Get all unique grades
all_grades = set()

for student in students:
    all_grades.update(student.grades)

print("\nUnique Grades:", all_grades)



# PART 4: TUPLE PRACTICE

print("\nTuple Example:")

t = student1.grades_tuple()
print("Grades tuple:", t)

# Demonstrate immutability
try:
    t[0] = 999  # this will cause an error
except TypeError:
    print("Error: Tuples are immutable!")


# PART 5: LIST OPERATIONS

for student in students:

    # Remove last grade
    student.grades.pop()

    # First and last grade
    print("\nStudent:", student.name)
    print("First grade:", student.grades[0])
    print("Last grade:", student.grades[-1])

    # Number of grades
    print("Total grades:", len(student.grades))



# PART 6: BONUS

# Email validation using regex
print("\nEmail Validation:")

for student in students:
    if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", student.email):
        print(student.email, "is valid")
    else:
        print(student.email, "is invalid")


# Count grades above 90
count_above_90 = 0

for student in students:
    for grade in student.grades:
        if grade > 90:
            count_above_90 += 1

print("\nGrades above 90:", count_above_90)