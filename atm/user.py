
# class user info
class user():
    def __init__(self,firstname,lastname , balance: float, cardNum, password):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
        self.cardNum = cardNum
        self.password = password


#Getters methode ,get data
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance
    def get_cardNum(self):
        return self.cardNum
    def get_password(self):
        return self.password


#Setters methode , change value
    def  set_firstname(self,newValue):
        self.firstname = newValue
    def  set_lastname(self,newValue):
        self.lastname = newValue
    def  set_balance(self,newValue):
        self.balance = newValue
    def  set_cardNum(self,newValue):
        self.cardNum = newValue
    def  set_password(self,newValue):
        self.password = newValue


#Print out , print values
    def print_out(self):
        print("Firstname - ", self.firstname)
        print("Lastname - ", self.lastname)
        print("Balance - ", self.balance)
        print("Card Number - ", self.cardNum)
        print("Password - ", self.password)

#Print out, print name,lastname , card number
    def print_id(self):
        print("Firstname - ", self.firstname)
        print("Lastname - ", self.lastname)
        print("Card Number - ", self.cardNum)

    def print_name(self):
        print(self.firstname)

    def print_lastname(self):
        print(self.lastname)





