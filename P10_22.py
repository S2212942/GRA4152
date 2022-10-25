###Implement a superclass Appointment and subclasses Onetime, Daily, and Monthly. 
# An appointment has a description (for example, “see the dentist”) and
#a date. Write a method occursOn(year, month, day)
#that checks whether the appointment occurs on
#that date. For example, for a monthly appointment, you must check whether the day of the month matches. 
# Then fill a list of Appointment objects with a mixture of appointments. 
# Have the user enter a date and print out all appointments that occur on that date.

# Solution.
# Super class:
class Appointment:
    # Constructor
    def __init__(self, description):
        self._description = description
    
    # Describe about the date you want to search for information
    def getDescription(self):
        return self._description
    
# Sub class
class OneTime(Appointment):

    #Constructor for subclass
    def __init__(self, description, day, month, year):
        super().__init__(description)
        self._day = day
        self._month = month
        self._year = year
    
    # Check date 
    def occurOn(self, day, month, year):
        if (self._day == day) and (self._month == month) and (self._year == year):
            print(super().getDescription())

# Sub class 
class Daily(Appointment):
    # constructor for subclass:

    def __init__(self, description):
        super().__init__(description)
    
    # Check date
    def occurOn(self, day, month, year):
            print(super().getDescription())

# Sub class
class Monthly(Appointment):
    
    #Constructor for subclass:
    def __init__(self, description, day):
        super().__init__(description)
        self._day = day
    
    # Check month
    def occurOn(self, day, month, year):
        if self._day == day:
            print(super().getDescription())

# Testing 
a1 = OneTime("my birth day", 11, 12, 1999)
a2 = Daily("go to school")
a3 = Monthly("have a rest day", 11)
list1 = [a1,a2,a3]

day = int(input("day: ")) # input 11
month = int(input("month: ")) # input 12
year = int(input("year: ")) # input 1999
for i in range(len(list1)):
    list1[i].occurOn(day, month, year)
print('Expected answer: my birth day')
print('Expected answer: go to school')
print('Expected answer: have a rest day')