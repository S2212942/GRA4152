#Improve the appointment book program of Exercises P10.22 and P10.23 by 
# letting the user save the appointment data to a file and reload the data from a file. 
# The saving part is straightforward: Make a method save. Save the type, description, and date to
#a file. The loading part is not so easy. First determine the type of the appointment to be loaded, 
# create an object of that type, and then call a load method to load the data.

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



# Users' experience
done = False

while not done:
    action = input("C)heck the appointment A)dd new appointment Q)uit:")
    action = action.upper()

    if action == "C" or action == "A":
        day = int(input("day: "))
        month = int(input("month: "))
        year = int(input("year: "))

        if action == "C":
            for i in range(len(list1)):
                list1[i].occurOn(day, month, year)
        else:
            description = str(input("description: "))
            typeOfApp = str(input("O)netime: D)aily: M)ontly: "))
            typeOfApp = typeOfApp.upper()
            
            if typeOfApp == "O":
                appointment = OneTime(description, day, month, year)
                list1.append(appointment)
                print(f"You create a new one-time appointment: description: {description}, day: {day}, month: {month}, year: {year} ")

            elif typeOfApp == "D":
                appointment = Daily(description)
                list1.append(appointment)
                print(f"You create a new daily appointment: description: {description}")
            elif typeOfApp == "M":
                appointment = Monthly(description, day)
                list1.append(appointment)
                print(f"You create a new one-time appointment: description: {description}, day: {day} ")
    
    else:
        done = True