#P.9.4. Implement a class address. An address has a house number, a street, an optional apartment number,
#  a city, a state, and a postal code. Define the constructor such that an object can be created in one 
# of two ways: with an apartment number or without. Supply a print method that print the address with 
# the street on one line and the city, the state, and the postal code on the next line. Supply a method 
# def comesBefore(self, other) that tests whether this address comes before other when compared by postal 
# code.

# class that contains address 
class Address:
    # Define the constructor such that an object can be created in one of two ways: with an apartment number or without
    def __init__(self, houseNumber, street, city, state, postalCode, apartmentNumber = None ):
        self._houseNumber = houseNumber
        self._street = street
        self._apartmentNumber = apartmentNumber
        self._city = city
        self._state = state
        self._postalCode = postalCode

    # prints the address
    def addressDetail(self): 
        print(self._street + '\n' + self._city+ " "+ self._state + " " + str(self._postalCode))

    # compares postal codes for the testing address and the other.
    # method prints " this address comes before the other" 
    # if postal code of this address is less than postal code for the given other object.
    # otherwise, it prints " this address do not come before the other"
    def comesBefore(self, other):
        if self._postalCode <= other._postalCode:
            print("this address comes before the other")
        else:
            print("this adress does not comes before the other")
#Testing
# create instances of class
# without apartment number
thisAddress = Address(102, "Chua lang street", "Ha Noi", "HN", 100000)
# with apartment number
otherAddress = Address(25, "Nguyen Chi Thanh street", "Bac Ninh", "BN", 14246)
# printing
thisAddress.addressDetail()
# compares postal codes of thisAddress and other
print(thisAddress.comesBefore(otherAddress)) 
print("expected output is: this address come before the other")

