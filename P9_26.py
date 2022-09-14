#Design a Customer class to handle a customer loyalty marketing campaign. After accumulating $100 in purchases, 
#the customer receives a $10 discount on the next purchase. Provide methods
#• def makePurchase(self, amount)
#• def discountReached(self)
#Provide a test program and test a scenario in which a customer has earned a discount and then made over $90, 
# but less than $100 in purchases. This should not result in a second discount. 
# Then add another purchase that results in the second discount.

class Customer:
    #budget is the accumulation amount of money that customers spend on our products.
    def __init__(self, budget):
        self._budget = budget


    #When customers buys our products, their budget is raised with the amount they spend on our products.
    def makePurchase(self, amount):
        self._budget = self._budget + amount


    # If budget is more than $100, customers will get discount for the next purchase and their accumulation
    # for new round is calculated by (budget - 100)
    # If budget is less than $100, customers will not get the discount for the next purchase.
    def discountReached(self):
        if self._budget > 100:
            self._budget = self._budget - 100
            print(f"You will get a discount for the next purchase, your accumulation for new round is {self._budget}")
        else:
            print(f"Your accumulation is {self._budget}, You do not get a discount for the next purchase")
#Testing

customer1 = Customer(120)
print(customer1._budget) # expected 120
customer1.makePurchase(60)
print(customer1._budget) # expected 180
customer1.discountReached()
print(" Expected: You will get a discount for the next purchase, your accumulation for new round is 80")
customer1.makePurchase(12)
customer1.discountReached()
print( "Expected result: Your accumulation is 92, You do not get a discount for the next purchase ")
customer1.makePurchase(70)
customer1.discountReached() 
print("Expected result: You will get a discount for the next purchase, your accumulation for new round is 62p")