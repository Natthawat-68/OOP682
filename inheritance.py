from models.person import Person
from models.student import Student
from models.staff import Staff

person = Person(1122334455667, "John Doe", 30)
student = Student(1234567890123, "Alice", 20, "S123")
staff = Staff(2345678901234, "Bob", 35, "ST456")

print(f"Student: {student.name}, Age: {student.age}, Student ID: {student.student_id}")
print(f"Staff: {staff.name}, Age: {staff.age}, Staff ID: {staff.staff_id}")

def get_person_info(person):
    print(isinstance(person, Person))
    return f"ID: {person.pid}, Name: {person.name}, Age: {person.age}"

get_person_info(student)
get_person_info(staff)