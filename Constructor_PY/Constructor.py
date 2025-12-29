class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)


# main program
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))

s1 = Student(name, roll)
s1.display()
