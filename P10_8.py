#Implement a superclass Person. Make two classes, Student and Instructor, 
# that inherit from Person. A person has a name and a year of birth. A student has a major, 
# and an instructor has a salary. Write the class declarations, the constructors, and the _ _repr_ _ method for all classes. 
# Supply a test program that tests these classes and methods.

# Super Class Person 
class Person:
    # Constructor for Person class
    def __init__(self, name, yearOfBirth):
        self._name = name
        self._birthYear = yearOfBirth
    # return name
    def getName(self):
        return self._name
    # return birth year
    def getBirthYear(self):
        return self._birthYear

    # Print the information for class Person
    def __repr__(self):
        return f"Person( name = {self._name}, birth year = {self._birthYear})"
# Subclass student of super class person
class student(Person):
    # Constructor for sub-class student:
    def __init__(self, name, yearOfBirth, major):
        super().__init__(name, yearOfBirth)
        self._major = major
    # return major
    def getMajor(self):
        return self._major

    # Print the information for sub-class student
    def __repr__(self):
        return f"Student( name = {self._name}, birth year = {self._birthYear}, major = {self._major})"
# Sub class instructor of super class Person
class instructor(Person):
    #Constructor for sub-class instructor
    def __init__(self, name, yearOfBirth, salary):
        super().__init__(name, yearOfBirth)
        self._salary = salary 
    # return salary 
    def getSalary(self):
        return self._salary

    # Print the information for sub-class instructor
    def __repr__(self):
        return f"Instructor( name = {self._name}, birth year = {self._birthYear}, salary = {self._salary})"

# Test
Person1 = Person("Joseph", "2001")
print(Person1.__repr__())
print( " Expected: Person( name = Joseph, birth year = 2001)")

Student1 = student("Noon", "1993", "Business Analytics")
print(Student1.__repr__())
print( "Expected: Student( name = Noon, birth year = 1993, major = Business Analytics)")

Instructor1 = instructor("Adam", "1993", "900000")
print(Instructor1.__repr__())
print("Expected: Instructor( name = Adam, birth year = 1993, salary = 900000 ")


