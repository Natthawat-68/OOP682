from models.classroom import ClassRoom
my_class = ClassRoom("Math 101")
my_class.add_student("Alice")
my_class.add_student("Bob")
print(len(my_class))
print(my_class[0])
print(my_class[1])