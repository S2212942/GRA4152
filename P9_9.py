#Implement a class ComboLock that works like the combination lock in a gym locker, as shown here. 
# The lock is constructed with a combination—three numbers between 0 and 39. The reset method resets the dial so that it points to 0. 
# The turnLeft and turnRight methods turn the dial by a given number of ticks to the left or right. 
# The open method attempts to open the lock. The lock opens if the user first turned it right 
# to the first number in the combination, then left to the second, and then right to the third.
class ComboLock:

    # constructor 
    def __init__(self, secret1, secret2, secret3):
        self._secret1 = secret1
        self._secret2 = secret2
        self._secret3 = secret3 

        # the dial is set equal to 0
        self._dial = 0
        # values is the combination of numbers users use, They are set equal to 0
        self._values = []

        print(f"You set a lock with passwords {self._secret1} {self._secret2} {self._secret3}")

        #Set the instruction to open the lock to users
        print("The lock opens if you first turned it right to the first number in the combination, then left to the second, and then right to the third.")
        
        #Set the instruction when the users use wrong combination
        print("In case you dial to the wrong direction, use reset to restart")
    
    # Reset the lock
    def reset(self):
        self._dial = 0
        self._values = []
        self._sides = []
        print("Now the lock dial is pointed to 0, you can then open it as instruction: 1. turnRight 2.turnLeft 3.turnRight")

    def turnRight(self, ticks):
        self._dial = (self._dial + ticks) % 40
        self._values.append(self._dial)
        print(f"you are dialing {self._values}")


    def turnLeft(self, ticks):
        # using % 40 to  have numbers between 0 and 39 
        self._dial = (self._dial - ticks) % 40
        self._values.append(self._dial)
        print(f"you are dialing {self._values}")


# if number combination is equal to combination among secret1, secret2 and secret3
    # method open() prints "CONGRATULATION, The lock is unlocked!!!"
    # otherwise, prints "Wrong combination [sef._values], you RESET method to restart"
    def open(self):
        if self._values == [self._secret1, self._secret2, self._secret3]:
            return "CONGRATULATION, The lock is unlocked!!!"
        else:
            print (f"Wrong combination {self._values}, you RESET method to restart")

# testing

lock = ComboLock(10, 20, 30)
lock.turnRight(10) # The combination now is [10]
lock.turnLeft(30) # The combination now is [10,20]
lock.turnRight(10) # The combination now is [10,20,30]
lock.open()
print( "Expected: CONGRATULATION, The lock is unlocked!!!")

lock2 = ComboLock(15, 20, 25)
lock2.turnRight(15) # The combination now is [15]
lock2.turnRight(20) # The combination now is  [15,35]
lock2.turnLeft(25) #  The combination now is [15,35,10]
lock2.open()
print ("Expected: Wrong combination [15, 35, 10], you RESET method to restart")

lock2.reset() # The combination now is empty[]
lock2.turnRight(15) # The combination now is [15]
lock2.turnLeft(35) # The combination now is [15,20]
lock2.turnRight(5) # The combination now is [15,20,25]
print(lock2.open())
print("Expected: CONGRATULATION, The lock is unlocked!!!")

lock3 = ComboLock(20, 20, 30)
lock3.turnRight(20) # The combination now is [10]
lock3.turnLeft(40) # The combination now is [10,20]
lock3.turnRight(10) # The combination now is [10,20,30]
lock3.open() # print "CONGRATULATION, The lock is unlocked!!!"
print(lock3.open())
print( "Expected: CONGRATULATION, The lock is unlocked!!!")
