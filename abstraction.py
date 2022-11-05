from abc import ABC, abstractmethod
class breakfastsausage (ABC): #abstract class
    def order(self,number):
        print("Your order of breakfast sausage: ",number)
    @abstractmethod
    def stock(self,number): #function will update stock of breakfast sausage
        pass

class Inventory(breakfastsausage):
    def stock(self,number):
        print("Your purchase of {} boxes of breakfast sausage has been updated.".format(number))


obj = Inventory()
obj.order("13")
obj.stock("13")
    

