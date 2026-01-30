class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
        
    def info(self):
        return f"{self.name} is {self.age} years old."

def main():
    my_dog = Dog("Fido", 3)
    print(my_dog)
    your_dog = Dog("Buddy", 5)
    print(your_dog)

if __name__ == "__main__":
    main()
