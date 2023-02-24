from main import Student

mystudents = Student.select()
for students in mystudents:
    print(students.student_name, students.student_id, students.student_class)